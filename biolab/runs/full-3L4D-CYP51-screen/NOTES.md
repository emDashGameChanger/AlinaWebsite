# full-3L4D-CYP51-screen

Third full-library screening campaign — same FDA-approved drug library,
now against sterol 14-alpha-demethylase (CYP51), per
`../../targets/attack-vectors-shortlist-2026-07-30.md`.

**Receptor**: `3L4D_receptor.pdbqt` — PDB 3L4D (*L. infantum* CYP51), chain
A only, heme (HEM) kept, fluconazole (TPF)/waters stripped. See
`../smoke-test-3L4D-CYP51/NOTES.md`.

**Pocket**: fpocket pocket 1 on chain A (druggability 0.993), directly
above the heme iron.

**Box** (`3L4D_CYP51_config.txt`): centered on (33.192, -24.058, -7.177),
size 20x28x28 Å (asymmetric — elongated substrate channel), search_depth
100.

**Library**: 1,840 FDA-approved drugs, 32 skipped over Vina-GPU's 130-atom
limit, 1,808 attempted, 1,795 docked successfully.

**Top 10 by predicted affinity (kcal/mol)**:

| Affinity | Drug |
|---|---|
| -13.0 | digitoxin |
| -12.6 | dutasteride |
| -12.5 | irinotecan |
| -12.2 | rimegepant |
| -12.1 | vibegron |
| -12.1 | conivaptan |
| -12.0 | nilotinib |
| -12.0 | ubrogepant |
| -12.0 | tepotinib |
| -11.9 | eltrombopag |

Full ranked results: `results.csv`.

**The azole question (this is the important part)**: CYP51 was picked
partly as a pipeline sanity check, since azole antifungals are
well-documented CYP51 inhibitors with real antileishmanial activity *and*
are dirt-cheap generics — the expectation was that they'd show up as
strong, plausible hits. They did, but with a real nuance:

- **No azole broke into the top 10.** The best, itraconazole, ranks
  **42nd of 1795** (-11.1 kcal/mol) — comfortably in the top 2.5%, a real
  positive signal, just not a #1 crown.
- The rest of the azole class clusters together right behind it:
  posaconazole (-10.5), terconazole (-10.4), ketoconazole (-10.0),
  oxiconazole (-9.5), sertaconazole/voriconazole (-9.4), down through
  miconazole (-8.5) and fluconazole (-8.2) — a coherent class signal,
  not scattered randomly through the rankings.
- **Fluconazole itself — the exact drug crystallized in this receptor
  structure — ranks only 854th of 1795 (roughly median)**, despite being
  the known, confirmed-bound ligand whose position literally defined the
  docking box. This is the one result worth being upfront about: it's a
  known, well-documented limitation of Vina's scoring function, not
  evidence the receptor prep is wrong — Vina's score correlates
  substantially with ligand size (more atoms means more favorable
  van der Waals contacts), and fluconazole is one of the smallest, most
  polar molecules in the azole class, exactly the profile Vina's function
  tends to underscore regardless of whether the binding mode is real.
  It's also, not coincidentally, the *cheapest* azole (~$4-20/month) — so
  the specific drug this project would most want to rank well is the one
  the scoring function is least kind to.
- Bottom line: this is a **partial pipeline validation** — real, class-
  coherent signal for azoles as a group, itraconazole specifically
  landing convincingly in the strong-hit range — but not the clean "cheap
  drug reaches the very top" result that would have been the ideal
  outcome. Worth keeping in mind when interpreting any future screen's
  absolute top-10 list: Vina's raw affinity ranking has a real bias
  toward bigger molecules, independent of whether they're good real
  inhibitors.

**Observations on the actual top 10**: several repeat "sticky binder"
molecules across all three screens run so far — **conivaptan** (3rd
appearance: PTR1 top 10, and now #6 here), **nilotinib** (2nd: TR top 10,
now #7 here), **rimegepant** (2nd: TR top 10, now #4 here), **eltrombopag**
(2nd: PTR1 top 10, now #10 here). Four of ten repeat hits across
chemically distinct pockets is a stronger signal that these are large,
flexible, generically high-affinity molecules by Vina's scoring function
(consistent with the same molecular-size bias noted above) rather than
genuinely CYP51-specific binders. Digitoxin (a cardiac glycoside, large
and rigid) and dutasteride (a steroid-pathway drug, chemically related to
CYP51's actual sterol substrates) are the two new top hits most worth a
closer look — dutasteride in particular is mechanistically plausible
given it's itself a steroid-metabolism-pathway inhibitor.

**Not yet done**: pose sanity check, literature check, and pricing/safety
profile for the top 10 — same sequence run for PTR1 and TR.

**Scope note**: hypothesis-generation only, per project-wide scope rules.
