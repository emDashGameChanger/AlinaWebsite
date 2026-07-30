# Target shortlist — 2026-07-30

Research pass per the `target-research` skill: looking for a disease that's rare/neglected or genuinely lacks a
good, affordable cure, with a protein target that has a solved structure and a well-defined small-molecule
binding pocket (i.e. actually tractable for AutoDock Vina-GPU docking, not a protein-protein interface or a
membrane complex that's hard to prep). This is a shortlist for discussion, not a final decision.

## Candidate A: Chagas disease — cruzain (recommended starting point)

**Disease.** Chagas disease (American trypanosomiasis, caused by *Trypanosoma cruzi*) is a WHO-classified
Neglected Tropical Disease. Current burden estimates range from 6–7 million (WHO) to 10.5 million prevalent cases
(Global Burden of Disease Study 2023), with 10,000+ deaths/year and 100+ million people at risk. It's spreading
beyond its traditional Latin American range — cases have now been detected in 44 countries including the US.

**Why it fits "no cheap cure."** The only two approved drugs, benznidazole and nifurtimox, are decades old.
They work reasonably well in the acute phase (~70–80% cure), but most patients are diagnosed in the chronic phase
(the acute phase is often asymptomatic/missed) — and chronic-phase efficacy is only **6–40%** depending on the
study. On top of that, 40–98% of patients on benznidazole have adverse events, and about 15% discontinue
treatment entirely because of them. This is about as clear an "unmet need" case as exists in infectious disease.

**Target: cruzain**, *T. cruzi*'s major cysteine protease — essential for the parasite's survival, a
well-validated drug target, with a clearly defined S1/S2 substrate-binding pocket (a textbook-good docking
target: soluble, single-chain, enzyme active site, not a PPI or membrane complex).
- Structure: PDB **4W5B**, 2.7 Å, solved in complex with an inhibitor (holo structure — good for defining the
  binding site precisely).
- Feasibility signal: **many** existing published studies have already run FDA-approved-drug virtual screens
  against cruzain (e.g. a 3,180-compound structure-based screen; several papers specifically targeting cruzain
  with docking + in vitro follow-up). This cuts both ways — it means our approach is proven to work here, but
  it also means this exact angle is well-trodden; a fresh run would be more "replicate and extend" than novel
  discovery, though comparing our hits against published hits would be a good sanity check on the pipeline.

## Candidate B: Visceral leishmaniasis — pteridine reductase 1 (PTR1)

**Disease.** Visceral leishmaniasis (VL, "kala-azar"), caused by *Leishmania donovani*/*L. infantum*, is fatal if
untreated. WHO-classified NTD, 200,000–400,000 new cases/year.

**Why it fits "no cheap cure."** The effective option, liposomal amphotericin B, is expensive (~$715/patient in
one cost study) and nephrotoxic. The cheap option, meglumine antimoniate (~$168/patient), is older and more
toxic. Miltefosine (the only oral option) is teratogenic and has high discontinuation rates. There is no option
that is simultaneously cheap, safe, and easy to administer — the field explicitly wants "short-course, affordable,
orally bioavailable" alternatives that don't yet exist.

**Target: PTR1**, an NADPH-dependent reductase the parasite uses as a folate-pathway salvage/bypass route,
making it a validated resistance-relevant target (it can compensate when the main folate pathway is blocked).
- Structure: PDB **2XOX** (*L. donovani*, 2.5 Å) — note this specific entry is an apo/blocked structure (a
  sulfate ion occupies the cofactor site rather than a real ligand), so a different, inhibitor- or
  cofactor-bound PTR1 structure (several exist for *L. major*, including NADP+/folic-acid ternary complexes)
  should be used instead when it's time to actually build `receptor.pdbqt` — flagging this now so it isn't
  rediscovered the hard way mid-run.
- Feasibility signal: less saturated than cruzain in the FDA-approved-drug-repurposing-via-docking literature —
  studies exist but the field looks more open than Chagas/cruzain.

## Candidate C: Chikungunya — nsP2 protease (noted, lower priority)

No approved antiviral exists for Chikungunya specifically (only supportive care), and it causes debilitating
chronic arthralgia in a meaningful fraction of patients. nsP2 protease (PDB **4ZTB**, 2.59 Å) is a druggable
enzyme target with existing FDA-drug-repurposing docking studies. Deprioritized mainly because Chikungunya is a
growing/increasingly-studied arbovirus rather than a genuinely neglected one — it fits "no cure" well but "rare
or under-studied" less well than A or B.

## Recommendation

**Start with Candidate B (Leishmaniasis / PTR1).** The unmet-need case is just as strong as Chagas (arguably a
cleaner "everything effective is toxic or expensive" story), it's still a WHO-neglected disease, the target is
docking-tractable, and the specific angle (FDA-approved-drug library vs. PTR1) is less thoroughly picked-over
than cruzain — more room to actually find something interesting rather than mostly reproducing existing papers.
Chagas/cruzain is a strong backup, and specifically a good target to validate the pipeline against, since there's
enough published data to sanity-check whether our docking scores land in a sane range compared to known results.

## Decision (2026-07-30)

**Going with Candidate B: visceral leishmaniasis / PTR1.** Structure question resolved: using PDB **1E92**
(*L. major* PTR1, NADP+ + dihydrobiopterin ternary complex, 2.20 Å) rather than *L. donovani* 2XOX — see
`PTR1.md` for the full deep dive (other PTR1 structures surveyed, inhibitor chemotypes, and a directly relevant
published in-silico benzothiazole screen against LmPTR1 that validates the planned receptor-prep approach:
keep the NADP+ cofactor, dock into the pocket the natural substrate occupies).

- No claims of therapeutic efficacy should be made from any docking score here — this is hypothesis generation,
  per `CLAUDE.md`'s safety/scope note. A strong predicted affinity is a reason to investigate further, not a
  result.
