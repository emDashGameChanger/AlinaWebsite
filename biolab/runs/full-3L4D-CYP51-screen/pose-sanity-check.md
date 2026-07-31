# Pose sanity check: CYP51 top 10

Date: 2026-07-30
Scope: digitoxin, dutasteride, irinotecan, rimegepant, vibegron,
conivaptan, nilotinib, ubrogepant, tepotinib, eltrombopag. Same
quantitative method as `../full-2YAU-TR-screen/pose-sanity-check.md`.

## Result

All 10 best poses land within 0.4-2.8 Å of the box center (20x28x28 Å),
even tighter clustering than either PTR1 or TR produced — expected, since
this pocket (fpocket druggability 0.993) is the most sharply defined of
the three targets prepped this session.

| Drug | Best-pose centroid | Dist. to box center | Closest atom to heme Fe |
|---|---|---|---|
| digitoxin | (33.6, -24.6, -8.3) | 1.3 Å | 4.45 Å |
| dutasteride | (32.3, -25.9, -5.3) | 2.8 Å | 5.44 Å |
| irinotecan | (33.8, -23.3, -8.3) | 1.5 Å | 5.93 Å |
| rimegepant | (32.3, -23.0, -7.8) | 1.5 Å | 5.67 Å |
| vibegron | (32.8, -25.1, -4.8) | 2.6 Å | 3.17 Å |
| conivaptan | (32.7, -25.2, -5.7) | 2.0 Å | 3.18 Å |
| nilotinib | (32.8, -25.4, -5.8) | 2.0 Å | 4.92 Å |
| ubrogepant | (33.2, -24.2, -7.5) | 0.4 Å | 5.54 Å |
| tepotinib | (32.6, -25.0, -7.1) | 1.1 Å | 5.62 Å |
| eltrombopag | (32.9, -25.5, -4.9) | 2.7 Å | 5.76 Å |

All 10 sit within 3.2-5.9 Å of the heme iron — genuinely occupying the
substrate-access channel above the heme, not just somewhere in the box.
None sit at classic Fe-N coordination distance (~2.0-2.2 Å, the way azole
nitrogens directly coordinate the iron) — expected, since Vina's scoring
function has no dative-bond/coordination term, so it can't specifically
reward that interaction the way a quantum-mechanical or docking method
with metal-coordination scoring could. Worth remembering as a pipeline
limitation specific to this heme-containing target.

## Scope note

Physical plausibility only — says nothing about real inhibition. See
`literature-check.md`.
