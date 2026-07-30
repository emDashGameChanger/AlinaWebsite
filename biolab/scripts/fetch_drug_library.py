#!/usr/bin/env python3
"""
Download the DrugCentral "FDA Approved Drugs" list and join it against
DrugCentral's structures file to produce biolab/data/drug_library.csv:
one row per FDA-approved drug with a usable SMILES string.

Source: https://drugcentral.org/download (CC BY-SA 4.0 -- cite DrugCentral
if this data is used in any published/shared results).
"""
import argparse
import csv
import datetime
import sys
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
BIOLAB_DIR = SCRIPT_DIR.parent
RAW_DIR = BIOLAB_DIR / "data" / "drugcentral_raw"
OUT_CSV = BIOLAB_DIR / "data" / "drug_library.csv"

FDA_APPROVED_URL = "https://drugcentral.org/static/FDA_Approved.csv"
STRUCTURES_URL = "https://unmtid-dbs.net/download/DrugCentral/2021_09_01/structures.smiles.tsv"


def download(url: str, dest: Path, force: bool) -> Path:
    if dest.exists() and not force:
        print(f"  {dest.name} already present, skipping download")
        return dest
    print(f"  downloading {url}")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    print(f"  wrote {dest} ({len(resp.content):,} bytes)")
    return dest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="re-download even if raw files already exist")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("Fetching DrugCentral source files...")
    fda_csv = download(FDA_APPROVED_URL, RAW_DIR / "FDA_Approved.csv", args.force)
    structures_tsv = download(STRUCTURES_URL, RAW_DIR / "structures.smiles.tsv", args.force)

    # FDA_Approved.csv has no header: drugcentral_id,name
    approved = {}
    with fda_csv.open(newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) < 2:
                continue
            drugcentral_id, name = row[0].strip(), row[1].strip()
            approved[drugcentral_id] = name

    print(f"  {len(approved):,} FDA-approved drug entries")

    # structures.smiles.tsv header: SMILES, InChI, InChIKey, ID, INN, CAS_RN
    structures_by_id = {}
    with structures_tsv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            structures_by_id[row["ID"].strip()] = row

    print(f"  {len(structures_by_id):,} structure records available")

    date_pulled = datetime.date.today().isoformat()
    rows_out = []
    missing_structure = 0
    for drugcentral_id, name in approved.items():
        struct = structures_by_id.get(drugcentral_id)
        if not struct or not struct.get("SMILES"):
            missing_structure += 1
            continue
        rows_out.append({
            "drugcentral_id": drugcentral_id,
            "name": name,
            "smiles": struct["SMILES"].strip(),
            "inchikey": struct.get("InChIKey", "").strip(),
            "cas_rn": struct.get("CAS_RN", "").strip(),
            "source": "DrugCentral",
            "source_version": "FDA_Approved.csv (current) + structures.smiles.tsv (2021_09_01)",
            "date_pulled": date_pulled,
        })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "drugcentral_id", "name", "smiles", "inchikey", "cas_rn",
            "source", "source_version", "date_pulled",
        ])
        writer.writeheader()
        writer.writerows(rows_out)

    print(f"\nWrote {len(rows_out):,} drugs with SMILES to {OUT_CSV}")
    if missing_structure:
        print(f"({missing_structure:,} approved entries had no matching structure record, skipped)")


if __name__ == "__main__":
    sys.exit(main())
