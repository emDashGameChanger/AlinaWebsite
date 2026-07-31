# Pose sanity check: TR top 10

Date: 2026-07-30
Scope: same top 10 as the run's `results.csv` — ergotamine, berotralstat,
nilotinib, lomitapide, midostaurin, saquinavir, naldemedine, rimegepant,
conivaptan, bisoctrizole.

## Method

Did this quantitatively rather than with PyMOL renders this time (see the
PTR1 screen's approach for the visual version) — extracted the best/top-
ranked pose (first `MODEL` block) from each hit's `docked/<id>_out.pdbqt`,
computed its centroid, and checked two things:

1. Distance from the docking box center (-18.258, -30.263, -2.880) — do all
   10 land in the same region, or are some scattered elsewhere in the box
   or clipped against a wall?
2. For the top hit specifically, minimum distance from each pocket-1
   lining residue (the literature-matched interfacial residues listed in
   `../smoke-test-2YAU-TR/NOTES.md`) to any ligand atom — does it actually
   contact the residues the pocket was chosen for, not just sit somewhere
   generically inside the box?

## Result

**All 10** best poses land within 2.8-4.5 Å of the box center (22 Å cube),
tightly clustered rather than scattered — the same physically-grounded
signal the PTR1 screen's visual pose check found: the scoring function and
box are behaving sensibly, not just returning noise.

| Drug | Best-pose centroid | Distance to box center |
|---|---|---|
| ergotamine | (-19.3, -31.7, 0.4) | 3.7 Å |
| berotralstat | (-19.4, -32.5, -0.6) | 3.4 Å |
| nilotinib | (-18.7, -31.7, -0.5) | 2.8 Å |
| lomitapide | (-19.3, -31.0, 0.3) | 3.4 Å |
| midostaurin | (-18.7, -30.2, 1.3) | 4.2 Å |
| saquinavir | (-19.8, -32.5, -1.4) | 3.1 Å |
| naldemedine | (-18.3, -30.9, 1.3) | 4.3 Å |
| rimegepant | (-19.6, -33.3, -1.0) | 3.8 Å |
| conivaptan | (-20.6, -31.4, 0.8) | 4.5 Å |
| bisoctrizole | (-19.4, -31.4, 1.2) | 4.4 Å |

**Ergotamine (the top hit) vs. the literature-matched pocket-1 residues**:
contacts (< 5 Å) essentially every residue the pocket was originally
chosen for, from *both* chains — B432 (3.30 Å), B436 (3.33), B371 (3.37),
B367 (3.37), B68 (3.45), B72 (3.47), B433 (3.50), A72 (3.54), B400 (3.61),
B61 (3.62), A433 (3.77), A61 (3.82), A400 (3.93), B401 (4.24), B75 (4.38),
A436 (4.50) — confirming it's genuinely occupying the inter-subunit
"mepacrine binding site" cavity the box was built around, not just
floating nearby.

## Scope note

Physical plausibility of the docking geometry only — says nothing about
whether ergotamine or any other hit actually inhibits TR or kills the
parasite. See `literature-check.md` for the separate question of prior
published evidence.
