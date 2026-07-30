# smoke-test-1E92-PTR1

**Receptor**: `1E92_receptor.pdbqt` — PDB 1E92 (*L. major* PTR1), chain A only,
NADP+ (NAP) cofactor kept, dihydrobiopterin (HBI)/waters/EDO stripped.

**Pocket**: fpocket pocket 4 on chain A (druggability 0.886, directly
contacts the crystallized HBI ligand, includes Ser111/Phe113 from the
published binding-site literature) — see `../../targets/PTR1.md`.

**Box** (`1E92_PTR1_config.txt`): centered on the crystallized HBI position
(-4.650, 32.833, 64.336), size 22x22x22 Å, search_depth 100. Sized to also
reach the adjacent NADP+-proximal subpocket (fpocket pocket 36).

**Ligands**: first 25 alphabetically from the FDA drug library, 24 dockable
(1 skipped, 130-atom limit).

**Result**: clean run, no errors. Best affinities ranged -8.4 to -11.0
kcal/mol. Top hit: ergotamine (-11.0). Used to validate the receptor/box
before committing to the full library — see
`../full-1E92-PTR1-screen/NOTES.md` for that run.
