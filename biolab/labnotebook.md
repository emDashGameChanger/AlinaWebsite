# Lab notebook

## 2026-07-29

Built out `biolab/` as a reproducible pipeline: `setup.sh` (fpocket +
AutoDock-Vina-GPU-2.1 build), and the FDA-approved drug library pipeline
(`fetch_drug_library.py` -> `prepare_ligand_library.py` -> `batch_dock.py`,
~1,859 drugs from DrugCentral). Smoke-tested the whole chain end-to-end
against the 3I3R demo receptor (`runs/smoke-test-3I3R/`), which surfaced and
fixed real bugs along the way: a Meeko macrocycle atom-type incompatibility
with Vina-GPU, and Vina-GPU's hard 130-atom-per-ligand limit. No real disease
target chosen yet at this point.

## 2026-07-29 (evening) - 2026-07-30

Ran target research (`target-research` skill) and shortlisted three
disease/target pairs: Chagas disease/cruzain, visceral leishmaniasis/PTR1,
and Chikungunya/nsP2 (`targets/shortlist-2026-07-30.md`). Picked **visceral
leishmaniasis, targeting pteridine reductase 1 (PTR1)** — the unmet-need
case is as strong as Chagas (every current VL treatment is toxic, expensive,
or teratogenic — no option is all three of cheap/safe/easy) and the
FDA-drug-repurposing-vs-PTR1 angle is less picked-over in the published
literature than cruzain. Chagas/cruzain stays the backup and a good
candidate for validating the pipeline against known published results later.

## 2026-07-30

Deepened the PTR1 research (`targets/PTR1.md`): confirmed PDB **1E92**
(*L. major* PTR1, NADP+ + dihydrobiopterin, 2.20 A) as the receptor
structure, over the apo *L. donovani* 2XOX (sulfate in the cofactor site,
not usable for defining the pocket). Found a directly relevant 2024/2025
in-silico benzothiazole-screening paper against this exact target (using PDB
5L4N) that validated the planned approach — keep the NADP+ cofactor in the
receptor, dock into the natural-substrate pocket — and named the key pocket
residues (Ser111, Phe113, Met183, Leu188, Leu226, His241) to check our own
pocket selection against.

Ran fpocket on 1E92 (71 pockets found across the tetramer's 4 equivalent
active sites) and confirmed chain A's **pocket 4** (druggability 0.886) as
the right site — it directly contacts the crystallized dihydrobiopterin
ligand and includes Ser111/Phe113 from the literature. The remaining four
literature residues turned up in two smaller, lower-scored adjacent fpocket
fragments (pocket 36, pocket 8), consistent with fpocket splitting one
continuous cleft into sub-pockets rather than missing the site.

Prepared the real receptor (`1E92_receptor.pdbqt`): chain A only, NADP+
kept, dihydrobiopterin/waters/cryoprotectant stripped via PyMOL, converted
with Open Babel. Built a docking box centered on the crystallized ligand
position, sized generously (22x22x22 A) to also cover the adjacent
NADP+-proximal subpocket (`1E92_PTR1_config.txt`). Capped the GPU to 75%
power (337 W of the RTX 3090 Ti's 450 W default) before the full run, per
request — turned out not to matter, since this workload only drew ~212 W at
100% utilization anyway.

Smoke-tested on 24 drugs (`runs/smoke-test-1E92-PTR1/`) — clean run,
affinities -8.4 to -11.0 kcal/mol, top hit ergotamine. Then ran the **full
FDA-approved-drug library (1,808 dockable of 1,840) against PTR1**
(`runs/full-1E92-PTR1-screen/`) — the project's first real screening
campaign. Took ~4h11m. 1,795 drugs docked successfully. Top predicted
binders: alectinib (-12.1), risdiplam (-11.7), eltrombopag (-11.6),
conivaptan (-11.6), entrectinib (-11.5), dihydroergotamine (-11.5 — same
ergot-alkaloid family as the smoke test's top hit, a consistent signal
across two independent runs). None of the top hits match the pterin-mimetic
or benzothiazole chemotypes known from the PTR1-inhibitor literature —
interesting as novel-scaffold candidates rather than a red flag, since
hypothesis-generation doesn't require matching known chemistry.

Not yet done: a visual sanity-check of a few top binding poses, and a
literature check for any existing antiparasitic activity on the top hits.
Good candidate for the next `website-tutorial-page` once that follow-up
happens — this is the first result substantial enough to be worth writing
up. Per project scope, none of this is a therapeutic claim: these are
computational hits worth investigating further, not proof of anything.
