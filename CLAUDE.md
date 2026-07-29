# BioMedBound / AlinaWebsite

## Project purpose & audience

BioMedBound is Alina Ren's personal science blog/portfolio (high school
student, aspiring doctor). It documents a molecular docking / drug-repurposing
research project: using AutoDock-Vina-GPU-2.1 (GPU-accelerated docking) and
fpocket (binding-pocket detection) to search for novel (repurposed) uses of
existing FDA-approved drugs, with a focus on rare or under-studied diseases
that don't get much research attention. The site is written as tutorials for
fellow students, teachers, and anyone learning docking basics — audience is
smart but not necessarily expert, so explain jargon rather than assuming it.

The site also has non-docking sections (toy reviews, book reviews) — same
voice, lower priority than the docking content.

## Repo layout

```
index.html, MolecularDocking.html, books.html, toys.html   # top-level pages
styles.css                                                   # shared stylesheet
images/, books/, toys/, molecularDocking/                    # page assets + subsections
biolab/                                                       # docking tooling, config, example run
  setup.sh, environment.yml, README.md
  config.txt, receptor.pdbqt, ligand.*, 3I3R.pdb, 3I3R_out/, ...
  runs/            # (created as needed) per-experiment logs, see docking-run skill
  targets/         # (created as needed) candidate disease-target research, see target-research skill
  labnotebook.md   # (created as needed) dated project log, see lab-notebook skill
```

The website lives **at the repo root**, not in a subfolder — this is
intentional so the same files serve correctly from GitHub Pages
(`emdashgamechanger.github.io/AlinaWebsite/`), the Namecheap host (served from
domain root), and local testing.

## Environment & build setup

- Docking tooling env: conda env `biolab` (`biolab/environment.yml`:
  `pymol-open-source`, `openbabel`). Activate with `conda activate biolab`.
- AutoDock-Vina-GPU-2.1 and fpocket are built from source via
  `biolab/setup.sh` (idempotent — safe to re-run, `--force` to rebuild).
  These build outputs (`AutoDock-Vina-GPU-2-1` binary, `OpenCL` symlink,
  `Kernel*_Opt.bin` kernel caches, `vendor/` source clones) are
  machine/GPU-specific and gitignored — never commit them, just make sure
  `setup.sh` stays accurate if the build steps change.

## Available hardware

- Primary: RTX 3090 Ti (CUDA/OpenCL) — used for docking runs by default.
- An older Radeon GPU is also available on this machine via ROCm
  (`rocm-smi`) if a second/parallel compute target is useful.
- A remote server (up to 80 cores, 300+GB RAM, Nvidia Tesla GPU) is
  available for heavier compute later — e.g. batch-screening a full
  FDA-approved-drug library against a target, which won't be practical on
  the local machine alone. Not wired up yet; ask before assuming access.

## Docking workflow conventions

Every docking run should be reproducible and traceable. Record, per run:
- The exact `config.txt` used (receptor/ligand paths, box center/size,
  search_depth).
- Full Vina stdout/log.
- Receptor identity (PDB ID) and ligand identity (PubChem CID, SMILES, or
  other clear source).
- Which fpocket pocket ID was targeted, if pocket-guided, and why.
- Resulting best affinity score(s).

This isn't just bookkeeping — this project's tutorials are literally built
from these records (see `molecularDocking/Hello2.html`'s -5.1 → -7.8 kcal/mol
before/after comparison as the pattern to follow). Use the `docking-run` and
`lab-notebook` skills for this.

## Website update conventions

- **Relative paths only.** Never use a leading `/` in `href`/`src` — it
  breaks on GitHub Pages' subpath URL. Root pages use `styles.css`,
  `index.html`, etc.; pages one level deep (`toys/`, `molecularDocking/`) use
  `../styles.css`, `../index.html`, etc., and same-folder assets stay
  unprefixed (`images/foo.png`).
- Reuse existing structure/classes rather than inventing new markup: a page
  is built from `mainDiv` > `titleDiv` + `topLinksDiv` (nav) + `topSplashDiv`
  (intro) + content (`pageBodyDiv`, `.code` for command blocks, `.pageImage`
  for images, `reviewCardDiv`/`indexCard` for card layouts) + `.footer`
  (contact mailto).
- The `topLinksDiv` nav block is duplicated across every page — if you add a
  new top-level page, update the nav in *all* existing pages to keep them in
  sync. (Note: as of this writing, several pages' "Science Book Reviews" nav
  link incorrectly points at `index.html` instead of `books.html` — worth
  fixing site-wide next time nav is touched.)
- Contact footer always uses `alinaren@biomedbound.com`.

## House style / tone

First-person, high-school-science-blog voice — plainspoken, tutorial-style,
mild humor is fine, but don't skip past jargon without a quick explanation.
Match the tone already in `molecularDocking/softwareInstall.html`,
`Hello1.html`, `Hello2.html`.

## Skills

Claude Code skills for this project live at `~/.claude/skills/` (cloned from
`emDashGameChanger/AlinaSkills`, applies globally on this machine):
`docking-run`, `website-tutorial-page`, `target-research`, `lab-notebook`.
Use them for the workflows they cover instead of improvising each time.

## Safety / scope

This is **computational drug-repurposing research only** — in-silico docking
scores are predictions/hypotheses, not proof of efficacy or safety. Tutorial
and results content should never present docking scores as clinical claims,
treatment recommendations, or medical advice.
