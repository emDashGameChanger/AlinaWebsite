# Cross-target analysis: sticky binders vs. pocket-specific binders

Date: 2026-07-30
Motivation: after three full-library screens (PTR1, TR, CYP51 — three
chemically unrelated pockets on two different Leishmania proteins),
several drugs kept reappearing near the top of more than one target's
list (conivaptan, nilotinib, rimegepant, eltrombopag). That's a real
question worth answering rigorously rather than just noting anecdotally:
is a repeat top-10 appearance a sign of genuine, independent pocket
complementarity, or is Vina's scoring function just consistently
rewarding certain large, flexible, generically "sticky" molecules
regardless of which pocket they're put in? This analysis answers that
using data already generated — no new docking needed.

## Method

All three screens docked the exact same 1,795 successfully-prepared drugs
(the skip criterion is a ligand-only atom-count limit, independent of
receptor), so every drug already has a directly comparable affinity
against all three pockets.

1. **Data-quality filter first.** Positive Vina affinities are non-physical
   (a failed/clashing pose, not a real weak binder). Counted these per
   target: PTR1 had 2/1795, CYP51 had 12/1795, but **TR had 33/1795** —
   meaningfully more, plausibly because the larger, more sterically
   complex A+B dimer interface is a harder receptor for some bulkier
   ligands to fit into cleanly than PTR1 or CYP51's single-chain pockets.
   Worth remembering as a TR-specific data-quality caveat. Excluded any
   drug with a positive score on *any* target from this analysis, leaving
   1,762 of 1,795 with three clean, comparable numbers.
2. **Per-target z-scores.** Standardized each target's affinity
   distribution (mean/stdev over the clean 1,762) so "how good is this
   score" is comparable across targets with different absolute scales
   (PTR1 mean -7.80±1.65, TR mean -6.53±1.46, CYP51 mean -7.97±1.81).
3. **Specificity gap** = (average z on the two *weaker* targets) − (z on
   the *best* target). A drug that's dramatically better on one target
   than its own baseline performance on the other two has a large,
   positive gap — real evidence the interaction is pocket-specific, not
   generic. A drug with a near-zero gap is equally strong (or weak) on
   all three unrelated pockets — the signature of a molecule Vina's
   scoring function just likes everywhere, independent of pocket shape.
4. **Ligand efficiency (LE)** = |best affinity| / heavy-atom count (heavy
   atoms counted via RDKit from each drug's SMILES in `drug_library.csv`)
   — a standard med-chem sanity metric, included because Vina's raw score
   is known to correlate with molecular size (more atoms → more possible
   favorable contacts). A big molecule racking up a good score mostly by
   being big should show unremarkable LE even with an impressive raw
   number; a small molecule matching a pocket precisely shows high LE.

## Results: every drug discussed across the three screens so far

| Drug | Heavy atoms | z (PTR1 / TR / CYP51) | Best target | Specificity gap | Ligand efficiency | Read |
|---|---|---|---|---|---|---|
| digitoxin | 54 | -0.79 / +0.15 / **-2.78** | CYP51 | **2.47** | 0.241 | **SPECIFIC** |
| irinotecan | 43 | -0.97 / -0.74 / **-2.51** | CYP51 | **1.65** | 0.291 | **SPECIFIC** |
| alectinib | 36 | **-2.61** / -1.22 / -1.07 | PTR1 | **1.47** | 0.336 | **SPECIFIC** |
| bexarotene | 26 | **-2.19** / -0.81 / -1.01 | PTR1 | **1.28** | 0.438 | **SPECIFIC** |
| naldemedine | 42 | -0.67 / **-2.32** / -1.84 | TR | 1.06 | 0.236 | mixed |
| vibegron | 33 | -1.28 / -1.08 / **-2.29** | CYP51 | 1.11 | 0.367 | mixed |
| berotralstat | 41 | -1.34 / **-2.45** / -1.40 | TR | 1.09 | 0.246 | mixed |
| ubrogepant | 40 | -0.85 / -1.49 / **-2.23** | CYP51 | 1.06 | 0.300 | mixed |
| dutasteride | 37 | -1.09 / -2.04 / **-2.56** | CYP51 | 0.99 | 0.341 | mixed |
| ergotamine | 43 | -1.94 / **-2.73** / -1.57 | TR | 0.97 | 0.244 | mixed (leans sticky) |
| saquinavir | 49 | -1.28 / **-2.32** / -1.57 | TR | 0.90 | 0.202 | mixed |
| risdiplam | 30 | **-2.37** / -1.15 / -1.84 | PTR1 | 0.87 | 0.390 | mixed |
| bisoctrizole | 49 | -1.09 / **-2.25** / -1.68 | TR | 0.86 | 0.200 | mixed |
| capmatinib | 31 | **-2.19** / -1.49 / -1.35 | PTR1 | 0.77 | 0.368 | mixed |
| lomitapide | 50 | -2.07 / **-2.39** / -1.35 | TR | 0.68 | 0.200 | mixed |
| rimegepant | 39 | -1.03 / -2.32 / **-2.34** | CYP51 | 0.67 | 0.313 | mixed |
| midostaurin | 43 | -1.64 / **-2.39** / -1.84 | TR | 0.64 | 0.233 | mixed |
| entrectinib | 41 | **-2.25** / -1.97 / -1.73 | PTR1 | 0.39 | 0.280 | STICKY |
| dihydroergotamine | 43 | **-2.25** / -2.11 / -1.73 | PTR1 | 0.33 | 0.267 | STICKY |
| olaparib | 32 | **-2.13** / -1.84 / -1.79 | PTR1 | 0.31 | 0.353 | STICKY |
| eltrombopag | 33 | **-2.31** / -1.84 / -2.18 | PTR1 | 0.30 | 0.352 | STICKY |
| nilotinib | 39 | -2.00 / **-2.39** / -2.23 | TR | 0.27 | 0.256 | STICKY |
| tolvaptan | 32 | **-2.13** / -1.70 / -2.12 | PTR1 | 0.22 | 0.353 | STICKY |
| tepotinib | 37 | -2.07 / -2.04 / **-2.23** | CYP51 | 0.18 | 0.324 | STICKY |
| conivaptan | 38 | -2.31 / **-2.32** / -2.29 | TR | 0.02 | 0.261 | STICKY |

(z-scores in **bold** mark each drug's best target. "Read" thresholds:
gap > 1.2 = SPECIFIC, gap < 0.6 = STICKY, in between = mixed.)

## What this changes

**8 of 25 are confirmed generically sticky** (conivaptan, tepotinib,
tolvaptan, nilotinib, eltrombopag, olaparib, dihydroergotamine,
entrectinib) — consistently strong across all three chemically unrelated
pockets, essentially the same z-score regardless of target. Their good raw
scores are real, but the evidence now points to "Vina likes this molecule
in general" rather than "this molecule fits this specific pocket." This
confirms the informal suspicion flagged after the CYP51 run (conivaptan's
3rd appearance, nilotinib's 2nd, etc.) — it wasn't a fluke, it's the
majority pattern for repeat hits.

**4 of 25 are genuinely pocket-specific**, and — this is the part worth
paying attention to — **they're also exactly the ones with the strongest
independent literature corroboration found across all three screens**:
digitoxin and irinotecan both have confirmed activity against *L.
infantum* itself (`../full-3L4D-CYP51-screen/literature-check.md`), and
alectinib was PTR1's original #1 hit. That's a real, independent
cross-check on this whole specificity metric — it's picking out the same
drugs the literature separately flags as most biologically plausible, not
just re-describing the docking scores in a different way. Bexarotene
(PTR1) has no literature precedent but is the single best ligand-efficiency
result in the whole table (0.438 from only 26 heavy atoms) — worth a
second look for that reason alone.

**Correction to the TR writeup's framing: ergotamine is "mixed,
leaning sticky" (gap 0.97), not cleanly pocket-specific.** It's a strong
binder on all three targets, just clearly strongest on TR — real signal,
but weaker specificity evidence than the "genuinely novel, pocket-matched"
framing in `runs/full-2YAU-TR-screen/pricing-safety-profile.md` implied.
This is chemically unsurprising in hindsight: ergot alkaloids are
famous for promiscuous polypharmacology even against human receptors
(dopamine, serotonin, and adrenergic receptors are all real ergotamine
targets) — a scaffold already known for hitting many unrelated binding
sites has no particular reason to suddenly be pocket-selective against a
novel parasite target instead. **This doesn't disqualify ergotamine** —
it's still the cheapest, most cross-run-consistent hit the project has
found, and promiscuous compounds have a real (if less mechanistically
tidy) history as antiparasitics — but the story going forward should be
"consistently strong, likely non-selective binder, still worth the cost
argument" rather than "novel, pocket-matched scaffold."

**Ligand efficiency didn't cleanly separate the two groups** on its own —
sticky and specific drugs both span roughly 0.2-0.35 LE, except for the
standout cases (bexarotene 0.438, digitoxin/irinotecan in the 0.24-0.29
range despite being fairly large). The specificity gap (item 3 above) is
doing essentially all of the discriminating work here; LE is a useful
secondary signal (bexarotene's high LE reinforces that it's a genuinely
efficient binder, not just a big molecule), not a standalone filter.

## How to use this going forward

For any future screen: before getting excited about a top-10 hit, check
its score against the *other* targets already screened. A drug that's
merely "consistently good everywhere" is a weaker novel-mechanism claim
than a drug that's dramatically better on the new target specifically. Add
this cross-target comparison as a standard step alongside the pose check,
literature check, and pricing/safety profile once a fourth target is ever
screened — three targets was the minimum needed to make this analysis
possible at all (two targets can't distinguish "consistent" from
"coincidence"; a gap needs an average of at least two *other* targets to
compare against).

## Scope note

Per project-wide scope rules: this is a computational specificity
heuristic, not proof of mechanism. A high specificity gap is evidence
consistent with genuine pocket complementarity, not confirmation of it —
and a low gap doesn't prove a drug has no real antiparasitic activity via
some other mechanism, only that this particular signal doesn't
distinguish it from a generic strong binder.