# BioMedBound

Alina Ren's science blog/portfolio: molecular docking and drug-repurposing
research (finding novel uses for FDA-approved drugs), plus toy and book
reviews. Written as tutorials, from basic tool setup through fpocket-guided
targeted docking.

- Live site: https://biomedbound.com
- Also mirrored via GitHub Pages: https://emdashgamechanger.github.io/AlinaWebsite/

## Contents

- `index.html`, `MolecularDocking.html`, `books.html`, `toys.html` — site pages
- `molecularDocking/` — docking tutorials (software setup, first docking run,
  fpocket-guided targeted docking)
- `biolab/` — the actual docking tooling: config, example receptor/ligand,
  fpocket output, and a `setup.sh` to reproduce the environment from scratch

## Quickstart

Preview the site locally:
```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

Set up the docking toolchain (fpocket, AutoDock-Vina-GPU-2.1, conda env):
```bash
cd biolab
bash setup.sh
```

See `biolab/README.md` for details, and `CLAUDE.md` for project conventions.

## Contact

alinaren@biomedbound.com
