#!/usr/bin/env python3
"""
Convert biolab/data/drug_library.csv (SMILES per FDA-approved drug) into
docking-ready PDBQT files under biolab/ligands/, one per drug:

  SMILES -> RDKit 3D embed (ETKDGv3, fixed seed) -> MMFF94 optimize
          -> Meeko PDBQT write

Resumable: skips ligands that already have a .pdbqt file, unless --force.
Molecules that fail 3D embedding or PDBQT writing are logged (not fatal)
to biolab/data/ligand_prep_failures.csv.
"""
import argparse
import csv
import sys
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDLogger
from meeko import MoleculePreparation, PDBQTWriterLegacy

SCRIPT_DIR = Path(__file__).resolve().parent
BIOLAB_DIR = SCRIPT_DIR.parent
LIBRARY_CSV = BIOLAB_DIR / "data" / "drug_library.csv"
LIGANDS_DIR = BIOLAB_DIR / "ligands"
FAILURES_CSV = BIOLAB_DIR / "data" / "ligand_prep_failures.csv"

RANDOM_SEED = 42  # fixed for reproducible 3D conformers


def prepare_one(smiles: str):
    """Returns (pdbqt_string, None) on success, or (None, error_message)."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, "RDKit could not parse SMILES"

    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = RANDOM_SEED
    if AllChem.EmbedMolecule(mol, params) != 0:
        # retry once with random coords fallback, some molecules need it
        params.useRandomCoords = True
        if AllChem.EmbedMolecule(mol, params) != 0:
            return None, "3D embedding failed"

    try:
        AllChem.MMFFOptimizeMolecule(mol)
    except Exception as e:
        return None, f"MMFF optimization failed: {e}"

    try:
        # rigid_macrocycles=True: Vina-GPU-2.1's atom-type table doesn't
        # include Meeko's macrocycle "glue" pseudo-atom types (e.g. CG0),
        # so ring-breaking flexibility for macrocycles isn't usable here --
        # treat macrocyclic rings as rigid instead.
        preparator = MoleculePreparation(rigid_macrocycles=True)
        mol_setups = preparator.prepare(mol)
        if not mol_setups:
            return None, "Meeko produced no molecule setups"
        pdbqt_string, is_ok, err = PDBQTWriterLegacy.write_string(mol_setups[0])
        if not is_ok:
            return None, f"Meeko PDBQT write failed: {err}"
        return pdbqt_string, None
    except Exception as e:
        return None, f"Meeko exception: {e}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="regenerate ligands that already have a .pdbqt file")
    parser.add_argument("--limit", type=int, default=None, help="only process the first N drugs (for testing)")
    args = parser.parse_args()

    RDLogger.DisableLog("rdApp.*")  # RDKit is very chatty about minor warnings

    if not LIBRARY_CSV.exists():
        sys.exit(f"{LIBRARY_CSV} not found -- run fetch_drug_library.py first")

    LIGANDS_DIR.mkdir(parents=True, exist_ok=True)

    with LIBRARY_CSV.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if args.limit:
        rows = rows[: args.limit]

    n_total = len(rows)
    n_skipped = 0
    n_ok = 0
    n_failed = 0
    failures = []

    for i, row in enumerate(rows, 1):
        drug_id = row["drugcentral_id"]
        out_path = LIGANDS_DIR / f"{drug_id}.pdbqt"

        if out_path.exists() and not args.force:
            n_skipped += 1
            continue

        pdbqt_string, err = prepare_one(row["smiles"])
        if pdbqt_string is None:
            n_failed += 1
            failures.append({"drugcentral_id": drug_id, "name": row["name"], "smiles": row["smiles"], "error": err})
        else:
            out_path.write_text(pdbqt_string)
            n_ok += 1

        if i % 100 == 0 or i == n_total:
            print(f"  [{i}/{n_total}] ok={n_ok} failed={n_failed} skipped={n_skipped}")

    if failures:
        with FAILURES_CSV.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["drugcentral_id", "name", "smiles", "error"])
            writer.writeheader()
            writer.writerows(failures)
        print(f"\n{len(failures)} failures logged to {FAILURES_CSV}")

    print(f"\nDone. {n_ok} new PDBQT files written, {n_skipped} already present, {n_failed} failed.")
    print(f"Total ligands available in {LIGANDS_DIR}: {len(list(LIGANDS_DIR.glob('*.pdbqt')))}")


if __name__ == "__main__":
    sys.exit(main())
