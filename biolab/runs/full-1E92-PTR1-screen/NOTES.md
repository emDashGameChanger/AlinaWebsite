# full-1E92-PTR1-screen

First real screening campaign for the project: the full FDA-approved-drug
library against a chosen disease target.

**Receptor**: `1E92_receptor.pdbqt` — PDB 1E92 (*L. major* PTR1), chain A
only, NADP+ (NAP) cofactor kept, dihydrobiopterin (HBI)/waters/EDO stripped.
Same receptor/box as the `smoke-test-1E92-PTR1` run that validated this
setup first.

**Pocket**: fpocket pocket 4 on chain A (druggability 0.886) — see
`../../targets/PTR1.md` for the full pocket-selection reasoning and the
published-literature cross-check (Ser111, Phe113, Met183, Leu188, Leu226,
His241).

**Box** (`1E92_PTR1_config.txt`): centered on the crystallized HBI position
(-4.650, 32.833, 64.336), size 22x22x22 Å, search_depth 100.

**Run conditions**: GPU power-capped to 337 W (75% of the RTX 3090 Ti's
450 W default) before this run. GPU utilization sat at 100% but power draw
stayed around 212 W, well under the cap — the cap didn't actually throttle
this workload.

**Library**: 1,840 FDA-approved drugs, 32 skipped over Vina-GPU's 130-atom
ligand limit, 1,808 attempted, 1,795 docked successfully (13 failed
AutoDock's atom-type parsing, e.g. Si/B atoms Vina-GPU doesn't support).

**Wall time**: ~4h11m (00:36 -> 04:47, 2026-07-30).

**Top 10 by predicted affinity (kcal/mol)**:

| Affinity | Drug |
|---|---|
| -12.1 | alectinib |
| -11.7 | risdiplam |
| -11.6 | eltrombopag |
| -11.6 | conivaptan |
| -11.5 | entrectinib |
| -11.5 | dihydroergotamine |
| -11.4 | bexarotene |
| -11.4 | capmatinib |
| -11.3 | tolvaptan |
| -11.3 | olaparib |

Full ranked results: `results.csv`.

**Observations**: dihydroergotamine shares the ergot-alkaloid family with
ergotamine, the smoke test's top hit on a different 25-drug subset — a
consistent signal across two independent runs. Several top hits
(alectinib, entrectinib, capmatinib) are kinase inhibitors, chemically
unrelated to the pterin-mimetic/benzothiazole chemotypes known from the
published PTR1-inhibitor literature (see `../../targets/PTR1.md`) — novel
scaffolds if they hold up, not a red flag on their own.

**Not yet done** (follow-ups worth doing before writing this up further):
visually sanity-check a few top binding poses (physically plausible
orientation vs. junk pose), and a literature check for any existing
antiparasitic/PTR1 activity on the top hits.

**Scope note**: hypothesis-generation only — no docking score here is a
therapeutic claim, per project-wide scope rules.
