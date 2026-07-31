# Literature check: existing antiparasitic activity of the top 10 PTR1 hits

Date: 2026-07-30
Scope: the top 10 ranked drugs from `results.csv` (the full FDA-approved-drug
screen against PTR1, PDB 1E92) — alectinib, risdiplam, eltrombopag,
conivaptan, entrectinib, dihydroergotamine, bexarotene, capmatinib,
tolvaptan, olaparib.

## Why this check, and why it's a separate question from the pose check

The docked-pose sanity check (see `NOTES.md` and the PTR1Screen.html
write-up) answered one question: *is the docking geometry physically
plausible?* All 10 hits land in the same pocket next to NADP+, which says
the scoring function and box are behaving sensibly. It says nothing about
whether any of these drugs have ever actually been shown to do anything to
a parasite in a lab.

This check asks that second, independent question: **has anyone already
published evidence of antiparasitic activity for any of these 10 drugs,
against anything?** The two checks can't substitute for each other:

- A drug with a physically sane pose *and* no prior antiparasitic
  literature is exactly what a repurposing screen is supposed to turn up —
  a genuinely novel candidate worth a closer look, not a red flag.
- A drug with a physically sane pose *and* independently confirmed prior
  antiparasitic activity (even against an unrelated species) is a small
  amount of real corroborating evidence — two independent methods (docking
  geometry, and someone else's wet-lab result) pointing the same direction.
- Prior evidence that a drug is *inactive* against related parasites would
  also be useful to know (a reason for skepticism about the docking score)
  — none turned up here, but it was one of the things being watched for.

## Method

For each of the 10 drugs:

1. Searched `"<drug> Leishmania antiparasitic OR antitrypanosomal activity"`
   as the primary query.
2. Where that came back empty (all 10, on the first pass), broadened to the
   drug's pharmacological class and other parasitic diseases —
   Chagas/*Trypanosoma cruzi*, malaria/*Plasmodium* — since a drug's
   off-target antiparasitic activity is sometimes published under a
   different disease than the one this project cares about, and a search
   scoped only to "Leishmania" would miss it.
3. Cross-checked against known drug-repurposing *screening campaigns* run
   against Leishmania/trypanosomatids as a class — the ReFRAME library
   screens, and recent kinase-inhibitor-vs-*Leishmania*-MAP-kinase
   repurposing papers — since 3 of the 10 hits (alectinib, entrectinib,
   capmatinib) are kinase inhibitors, and it's plausible one of these
   mega-screens already tested them even without a dedicated single-drug
   paper existing.
4. Every claim below is backed by a URL/DOI so it can be checked
   independently — nothing here is asserted from memory alone.

This was web search, not a systematic query against a structured bioactivity
database (ChEMBL, PubChem BioAssay). See **Limitations** below.

## Findings

### Olaparib — confirmed antiparasitic activity, but against a different parasite

**Vilchez Larrea SC, Haikarainen T, Narwal M, Schlesinger M, Venkannagari H,
Flawiá MM, Fernández Villamil SH, Lehtiö L. "Inhibition of poly(ADP-ribose)
Polymerase Interferes with *Trypanosoma cruzi* Infection and Proliferation
of the Parasite." *PLOS ONE* 7(9): e46063, 2012.**
DOI: [10.1371/journal.pone.0046063](https://doi.org/10.1371/journal.pone.0046063)
Full text: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0046063

- Screened a 32-compound in-house library of PARP inhibitors against
  *Trypanosoma cruzi* (the Chagas disease parasite — same trypanosomatid
  family as *Leishmania*, and this project's documented backup/pipeline-
  validation target, but not the disease actually being screened against
  here).
- **Olaparib was the most potent compound in the panel**: IC50 = 3.4 nM
  against human PARP-1; significantly reduced epimastigote growth and
  intracellular amastigote counts at 25 nM. No significant effect on
  trypomastigote counts was reported.
- Two caveats:
  - Published in **2012**, before olaparib's FDA approval (December 2014).
    At the time it was tested as a research PARP-inhibitor tool compound
    (sometimes listed under its development code AZD2281), not yet as an
    approved drug — but it is the same molecule now sitting in our top 10.
  - This is *T. cruzi*, not *Leishmania*/PTR1. Mechanistically it's also a
    different story: PARP inhibition targets DNA-repair machinery, which
    has nothing obviously to do with PTR1's role in folate/pterin salvage.
    If olaparib really does bind PTR1 the way Vina predicts, that would be
    a second, independent (and mechanistically unrelated) mode of
    antiparasitic action — a "moonlighting" possibility, not something the
    PARP result explains on its own.

### The other 9 — no antiparasitic literature found

Despite the broadened searches described above, no published antiparasitic
activity (Leishmania, Trypanosoma, or Plasmodium) turned up for:
**alectinib, risdiplam, eltrombopag, conivaptan, entrectinib,
dihydroergotamine, bexarotene, capmatinib, tolvaptan.**

One partial lead followed up and ruled inconclusive rather than negative:
a 2024 *Life Sciences* paper (Bhattacharjee et al., "Repurposing approved
protein kinase inhibitors as potent anti-leishmanials targeting *Leishmania*
MAP kinases," DOI: [10.1016/j.lfs.2024.122844](https://pubmed.ncbi.nlm.nih.gov/38897344/))
screened 12 FDA-approved kinase inhibitors against *Leishmania* MAP
kinases. Its abstract names only sorafenib and imatinib as leads. The full
text is paywalled, so I could not confirm whether alectinib, entrectinib,
or capmatinib were even among the 12 screened — this is an **unconfirmed
gap**, not a checked negative, for those three specifically.

## Limitations

- This was iterative web search (via search-engine results and paper
  abstracts), not a systematic query against a structured bioactivity
  database like ChEMBL or PubChem BioAssay. A compound could have deposited
  but unpublished screening data that a web search wouldn't surface.
- Several potentially relevant papers were paywalled past the abstract
  (e.g. the 2024 kinase-inhibitor paper above, and the 2014 *J Antimicrob
  Chemother* kinase-inhibitor-vs-*Leishmania* paper) — "not found" in those
  cases means "not confirmable from what's publicly readable," not a
  verified negative.
- **Absence of evidence is not evidence of absence.** For 9 of the 10
  drugs, "no antiparasitic literature found" should be read as "nothing
  published that this search could locate," not "proven inactive."

## Bottom line

Nine of the ten top-ranked drugs from the screen appear to be genuinely
novel with respect to antiparasitic activity — no prior published evidence
either way. That's the expected, hoped-for outcome of a repurposing screen
and is consistent with what was already written on the site (novel
scaffolds vs. the known pterin-mimetic/benzothiazole PTR1-inhibitor
chemotypes). Olaparib is the one exception: it has real, citable, prior
antiparasitic activity — just against a different trypanosomatid (*T.
cruzi*) via a different, unrelated mechanism (PARP inhibition) than the one
being screened for here (PTR1 binding). That's an interesting data point
to read directly and think about, not a confirmation of the PTR1 docking
result for olaparib.

## Scope note

Per project-wide scope rules (`CLAUDE.md`): none of this is a therapeutic
claim. A docking score plus an unrelated prior antiparasitic result is
still just two independent reasons to investigate olaparib further
computationally — not evidence that it treats visceral leishmaniasis.
