#!/usr/bin/env python3
"""
Batch-dock a directory of prepared ligand PDBQTs against a receptor using
AutoDock-Vina-GPU-2.1's native --ligand_directory virtual screening mode,
then collect the results into a ranked CSV (best affinity per ligand).

Example:
  python3 batch_dock.py --run-name smoke-test-3I3R --limit 20
  python3 batch_dock.py --run-name full-3I3R-screen
"""
import argparse
import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BIOLAB_DIR = SCRIPT_DIR.parent
DEFAULT_BINARY = BIOLAB_DIR / "AutoDock-Vina-GPU-2-1"
DEFAULT_RECEPTOR = BIOLAB_DIR / "receptor.pdbqt"
DEFAULT_LIGANDS_DIR = BIOLAB_DIR / "ligands"
DEFAULT_LIBRARY_CSV = BIOLAB_DIR / "data" / "drug_library.csv"
RUNS_DIR = BIOLAB_DIR / "runs"

VINA_RESULT_RE = re.compile(r"REMARK VINA RESULT:\s*(-?\d+\.?\d*)")
MAX_LIGAND_ATOMS = 130  # AutoDock-Vina-GPU-2.1's hard per-ligand atom limit


def load_box_from_config(config_path: Path) -> dict:
    box = {}
    for line in config_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = (p.strip() for p in line.split("=", 1))
        if key in ("center_x", "center_y", "center_z", "size_x", "size_y", "size_z", "search_depth"):
            box[key] = value
    return box


def best_affinity(pdbqt_path: Path):
    text = pdbqt_path.read_text(errors="ignore")
    matches = VINA_RESULT_RE.findall(text)
    if not matches:
        return None
    return min(float(m) for m in matches)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-name", required=True, help="subfolder under biolab/runs/ for this screen's config/log/results")
    parser.add_argument("--receptor", default=str(DEFAULT_RECEPTOR))
    parser.add_argument("--ligand-dir", default=str(DEFAULT_LIGANDS_DIR))
    parser.add_argument("--library-csv", default=str(DEFAULT_LIBRARY_CSV), help="drug_library.csv, used to attach drug names to results")
    parser.add_argument("--config", default=str(BIOLAB_DIR / "config.txt"), help="existing config.txt to pull box center/size/search_depth from")
    parser.add_argument("--binary", default=str(DEFAULT_BINARY))
    parser.add_argument("--limit", type=int, default=None, help="only dock the first N ligands (alphabetical) -- for smoke testing")
    parser.add_argument("--search-depth", type=int, default=None, help="override search_depth from --config")
    parser.add_argument("--thread", type=int, default=8000, help="Vina-GPU compute lanes (8000 is the tool's recommended default)")
    args = parser.parse_args()

    receptor = Path(args.receptor).resolve()
    ligand_dir = Path(args.ligand_dir).resolve()
    binary = Path(args.binary).resolve()
    library_csv = Path(args.library_csv).resolve()
    run_dir = (RUNS_DIR / args.run_name).resolve()

    if not receptor.exists():
        sys.exit(f"receptor not found: {receptor}")
    if not binary.exists():
        sys.exit(f"Vina-GPU binary not found: {binary} -- run biolab/setup.sh first")

    box = load_box_from_config(Path(args.config)) if Path(args.config).exists() else {}
    if args.search_depth:
        box["search_depth"] = str(args.search_depth)
    required = ("center_x", "center_y", "center_z", "size_x", "size_y", "size_z")
    missing = [k for k in required if k not in box]
    if missing:
        sys.exit(f"Missing box parameters {missing} -- pass --config pointing at a config.txt with a defined search box")

    run_dir.mkdir(parents=True, exist_ok=True)
    output_dir = run_dir / "docked"
    output_dir.mkdir(exist_ok=True)

    # Optionally build a subset dir (symlinks, no copying) for smoke testing
    if args.limit:
        subset_dir = run_dir / "ligands_subset"
        if subset_dir.exists():
            shutil.rmtree(subset_dir)
        subset_dir.mkdir()
        all_ligands = sorted(ligand_dir.glob("*.pdbqt"))[: args.limit]
        for lig in all_ligands:
            (subset_dir / lig.name).symlink_to(lig)
        ligand_dir = subset_dir
        print(f"Smoke-test subset: {len(all_ligands)} ligands linked into {subset_dir}")

    n_ligands = len(list(ligand_dir.glob("*.pdbqt")))
    if n_ligands == 0:
        sys.exit(f"no .pdbqt files found in {ligand_dir} -- run prepare_ligand_library.py first")

    # Vina-GPU-2.1 has a hard 130-atom-per-ligand limit and aborts that
    # ligand (wasting a slot in the run) rather than skipping gracefully --
    # so pre-filter oversized ligands ourselves and report them separately.
    filtered_dir = run_dir / "ligands_filtered"
    if filtered_dir.exists():
        shutil.rmtree(filtered_dir)
    filtered_dir.mkdir()
    skipped_too_large = []
    for lig in sorted(ligand_dir.glob("*.pdbqt")):
        n_atoms = sum(1 for line in lig.read_text().splitlines() if line.startswith("ATOM"))
        if n_atoms > MAX_LIGAND_ATOMS:
            skipped_too_large.append((lig.stem, n_atoms))
        else:
            (filtered_dir / lig.name).symlink_to(lig.resolve())
    ligand_dir = filtered_dir

    if skipped_too_large:
        skipped_csv = run_dir / "skipped_too_large.csv"
        with skipped_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["drugcentral_id", "num_atoms"])
            writer.writerows(skipped_too_large)
        print(f"Skipped {len(skipped_too_large)} ligands over the {MAX_LIGAND_ATOMS}-atom Vina-GPU limit -> {skipped_csv}")

    n_ligands = len(list(ligand_dir.glob("*.pdbqt")))
    if n_ligands == 0:
        sys.exit("all ligands were filtered out (too large) -- nothing to dock")

    config_path = run_dir / "vina_config.txt"
    config_path.write_text(
        f"receptor = {receptor}\n"
        f"ligand_directory = {ligand_dir}\n"
        f"output_directory = {output_dir}\n"
        f"center_x = {box['center_x']}\n"
        f"center_y = {box['center_y']}\n"
        f"center_z = {box['center_z']}\n"
        f"size_x = {box['size_x']}\n"
        f"size_y = {box['size_y']}\n"
        f"size_z = {box['size_z']}\n"
        f"search_depth = {box.get('search_depth', 100)}\n"
        f"thread = {args.thread}\n"
    )
    print(f"Wrote {config_path}")
    print(f"Docking {n_ligands} ligands from {ligand_dir} against {receptor.name} ...")

    log_path = run_dir / "vina_run.log"
    # Vina-GPU looks for its opencl kernel binaries relative to cwd by default,
    # so run with cwd=biolab/ where Kernel1_Opt.bin / Kernel2_Opt.bin live.
    with log_path.open("w") as log_f:
        result = subprocess.run(
            [str(binary), "--config", str(config_path)],
            cwd=str(BIOLAB_DIR),
            stdout=log_f,
            stderr=subprocess.STDOUT,
        )
    print(f"Vina-GPU exited with code {result.returncode}, full log at {log_path}")
    if result.returncode != 0:
        sys.exit(f"Docking run failed -- see {log_path}")

    # Collect results
    names_by_id = {}
    if library_csv.exists():
        with library_csv.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                names_by_id[row["drugcentral_id"]] = row["name"]

    results = []
    for out_pdbqt in sorted(output_dir.glob("*.pdbqt")):
        drug_id = out_pdbqt.stem.replace("_out", "")
        affinity = best_affinity(out_pdbqt)
        if affinity is None:
            continue
        results.append({
            "drugcentral_id": drug_id,
            "name": names_by_id.get(drug_id, ""),
            "best_affinity_kcal_mol": affinity,
            "output_pdbqt": str(out_pdbqt.relative_to(BIOLAB_DIR)),
        })

    results.sort(key=lambda r: r["best_affinity_kcal_mol"])
    results_csv = run_dir / "results.csv"
    with results_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["drugcentral_id", "name", "best_affinity_kcal_mol", "output_pdbqt"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n{len(results)} ligands docked successfully. Results: {results_csv}")
    print("\nTop 10 by predicted affinity:")
    for r in results[:10]:
        print(f"  {r['best_affinity_kcal_mol']:>7.2f} kcal/mol  {r['name']} ({r['drugcentral_id']})")


if __name__ == "__main__":
    sys.exit(main())
