# full-2YAU-TR-screen

Second full-library screening campaign — same FDA-approved drug library as
the PTR1 screen, now against trypanothione reductase (TR) instead, per
`../../targets/attack-vectors-shortlist-2026-07-30.md`.

**Receptor**: `2YAU_receptor.pdbqt` — PDB 2YAU (*L. infantum* TR), full A+B
homodimer, FAD + NADPH kept on both chains, auranofin/Cl/SO4/waters
stripped. See `../smoke-test-2YAU-TR/NOTES.md` for why the dimer (not a
single chain) was necessary here.

**Pocket**: fpocket pocket 1 on the A+B dimer (druggability 0.731), the
inter-subunit "mepacrine binding site" cavity, cross-checked against
published TR domain boundaries.

**Box** (`2YAU_TR_config.txt`): centered on (-18.258, -30.263, -2.880),
size 22x22x22 Å, search_depth 100.

**Library**: 1,840 FDA-approved drugs, 32 skipped over Vina-GPU's 130-atom
limit, 1,808 attempted, 1,795 docked successfully.

**Top 10 by predicted affinity (kcal/mol)**:

| Affinity | Drug |
|---|---|
| -10.5 | ergotamine |
| -10.1 | berotralstat |
| -10.0 | nilotinib |
| -10.0 | lomitapide |
| -10.0 | midostaurin |
| -9.9 | saquinavir |
| -9.9 | naldemedine |
| -9.9 | rimegepant |
| -9.9 | conivaptan |
| -9.8 | bisoctrizole |

Full ranked results: `results.csv`.

**Observations**:
- **Ergotamine is the top hit again** — it topped the TR smoke test on a
  20-drug subset, and its close relative dihydroergotamine landed in the
  PTR1 screen's top 10 (`../full-1E92-PTR1-screen/`). That's now a
  consistent ergot-alkaloid signal across two independent targets and
  three separate runs. Unlike almost everything else on either target's
  top-10 list, ergotamine is a genuinely **cheap, decades-generic drug**
  (same practicality profile already documented for dihydroergotamine in
  `../full-1E92-PTR1-screen/pricing-safety-profile.md`) — worth flagging as
  the single most promising practical lead so far across the whole
  project, pending the same literature/pricing checks done for PTR1.
- The rest of the list is a familiar mix: several are expensive
  specialty/orphan drugs (berotralstat for hereditary angioedema, lomitapide
  for homozygous familial hypercholesterolemia, midostaurin for AML — all
  likely in the same $8k+/month range as the PTR1 top hits). Conivaptan
  reappears from the PTR1 top 10 on a completely different target/pocket,
  which is a mild flag that it may just be a generically "sticky"/
  high-affinity molecule (large, flexible, lots of hydrogen-bond donors)
  rather than something specifically complementary to either pocket.
- Saquinavir is an older, largely-generic HIV protease inhibitor — not as
  cheap as ergotamine but meaningfully cheaper than the oncology/orphan
  drugs on this list.
- Bisoctrizole is a UV-filter/sunscreen ingredient in the DrugCentral
  library rather than a systemic medicine — flag for the pricing/safety
  pass to note it's not a realistic oral/systemic repurposing candidate
  regardless of docking score.

**Not yet done** (same follow-up sequence as the PTR1 screen): pose sanity
check, literature check for existing antiparasitic activity, and a
pricing/safety profile — recommended next steps before drawing any
conclusions, especially given how much the ergotamine signal matters here.

**Scope note**: hypothesis-generation only, per project-wide scope rules —
no docking score here is a therapeutic claim.
