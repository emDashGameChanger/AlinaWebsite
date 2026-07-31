# Literature check: existing antiparasitic activity of the top 10 CYP51 hits

Date: 2026-07-30
Scope: digitoxin, dutasteride, irinotecan, rimegepant, vibegron, conivaptan,
nilotinib, ubrogepant, tepotinib, eltrombopag. Same method as the PTR1 and
TR literature checks. Four of these (rimegepant, conivaptan, nilotinib,
eltrombopag) already have a writeup in the TR or PTR1 literature-check
files as repeat hits — only re-checked here for anything CYP51/sterol-
pathway-specific, which turned up nothing new for any of the four.

## Results — this is the best literature hit the project has found

**Digitoxin has direct, confirmed activity against *Leishmania infantum*
itself** — the exact species this whole project targets. Two independent
lines of evidence:
- Digitoxigenin (digitoxin's aglycone, i.e. digitoxin with its sugars
  removed) showed antileishmanial IC50 = 6.9 ± 1.5 μg/mL against
  *L. infantum*, with a selectivity index of 42.8 (good separation from
  host-cell toxicity).
- β-acetyl-digitoxin (a digitoxin derivative) showed activity against
  infected macrophages *and* reduced parasite load in vivo in mice.

This is a stronger, more direct hit than anything either PTR1 or TR
produced (those checks found precedent against a *different* species —
olaparib vs. *T. cruzi*, saquinavir vs. *L. major*, nilotinib vs. *T.
cruzi* — never the exact *L. infantum* target itself). See
`pricing-safety-profile.md` for a major caveat: digitoxin itself isn't
commercially available in the US anymore.

**Irinotecan** also has a real, specific *L. infantum* precedent: it and
its active metabolite SN-38 act as DNA topoisomerase IB poisons in
*L. infantum* promastigotes, confirmed both in vitro and ex vivo on
infected splenocytes. This is the same "real but mechanistically separate"
relationship as digitoxin-vs-CYP51 — irinotecan's confirmed activity is via
topoisomerase IB, not sterol biosynthesis, so it doesn't validate the
CYP51 docking score specifically. It is a direct, interesting callback to
**Candidate C (DNA topoisomerase IB)** from
`../../targets/attack-vectors-shortlist-2026-07-30.md`, which was
deprioritized as a docking target because camptothecin-class drugs (which
irinotecan is) work via DNA intercalation rather than a normal small-
molecule pocket — this result is a real-world illustration of exactly that
mechanism, appearing here as a side effect of screening a different
target.

**Dutasteride, vibegron, ubrogepant, tepotinib**: no published
antiparasitic activity found for any of them — the expected novel-scaffold
outcome, not a red flag. Dutasteride is the most mechanistically plausible
of the four on priors alone (it's itself a steroid-pathway enzyme
inhibitor, chemically closer to CYP51's substrate class than any of the
others).

## Bottom line

This screen produced the single strongest literature precedent the whole
project has found — digitoxin/digitoxigenin confirmed active against the
project's actual target species, *L. infantum*, in vivo — but it comes
with the sharpest practicality catch to match: see
`pricing-safety-profile.md`.

## Scope note

Per project-wide scope rules: none of this is a therapeutic claim. Confirmed
activity of digitoxigenin (an aglycone/derivative) doesn't automatically
transfer to digitoxin itself at approved cardiac doses, and none of this
says anything about CYP51 specifically as the mechanism for any hit here.
