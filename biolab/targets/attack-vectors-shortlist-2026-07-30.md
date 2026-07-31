# Additional attack-vector shortlist — 2026-07-30

Follow-up research pass per the `target-research` skill. Same disease (visceral leishmaniasis), but looking for
a **different essential parasite protein/pathway** to dock the FDA-approved drug library against, rather than a
different disease. Motivation: the completed PTR1 screen's top 10 hits
(`runs/full-1E92-PTR1-screen/pricing-safety-profile.md`) were almost entirely $8,000–19,000+/month oncology and
rare-disease specialty drugs — close to the opposite of what this project is looking for. PTR1 sits in the
folate-salvage pathway; this pass looks at other ways to kill the parasite — redox/metabolic vulnerability,
membrane biosynthesis, and DNA replication/reproduction — on the theory that a different binding-pocket chemistry
might surface a different (and hopefully cheaper) class of hits than PTR1's kinase-inhibitor-heavy result.

## Candidate A: Trypanothione reductase (TR) — recommended starting point

**Role.** Trypanosomatids (*Leishmania*, *Trypanosoma*) replace the glutathione/glutathione-reductase redox
system every other eukaryote uses with a parasite-specific trypanothione/trypanothione-reductase system. TR keeps
trypanothione reduced so the parasite's tryparedoxin/tryparedoxin-peroxidase system can neutralize the H2O2
macrophages throw at it during infection. **This system doesn't exist in humans at all** — about as clean a
selectivity argument as a target can have — and TR is essential for parasite survival, not just growth.

- Structure: multiple *L. infantum* TR holo structures exist with different ligands bound in the
  NADPH/trypanothione pocket — PDB **2JK6** (apo-ish reference), **2W0H** (antimony(III) + NADPH, the mechanism of
  antimonial drugs), **2X50** (silver + NADPH), **2YAU** (auranofin), **6ER5** (a synthetic inhibitor). Having
  several independently-solved ligand-bound structures of the same pocket is a good sign for defining the box
  reliably (cross-check pocket residues across structures the way PTR1's fpocket run was cross-checked against
  literature residues).
- Feasibility/novelty signal: TR is a *heavily* validated target with a large inhibitor literature (auranofin — a
  repurposed rheumatoid-arthritis gold compound — and phenothiazine antipsychotics are both known TR inhibitors).
  That cuts the same way cruzain did for PTR1: proven pocket, some risk of "replicating known results" rather than
  pure novelty, but a good pipeline sanity check, and a full 1,859-drug systematic screen specifically may still
  not exist. Chemically, the trypanothione/NADPH pocket is nothing like PTR1's pterin pocket or a kinase ATP
  pocket, so it's likely to surface a genuinely different hit list rather than more kinase inhibitors.

## Candidate B: Sterol 14α-demethylase (CYP51) — strong backup, likely cheap-hit bonus

**Role.** CYP51 performs the 14α-demethylation step of ergosterol biosynthesis — parasite membrane integrity,
not reproduction, but a completely different "kill it" mechanism (membrane biogenesis failure) from either PTR1
or TR.

- Structure: PDB **3L4D**, *L. infantum* CYP51, solved **in complex with fluconazole** — an azole antifungal
  already sitting in the pocket. That's a big advantage for receptor prep (same reason 1E92's dihydrobiopterin
  complex was preferred over the apo 2XOX for PTR1): the real ligand pose defines the box with no guesswork.
- Feasibility/novelty signal: this is the one candidate here where the likely outcome is largely predictable —
  azole antifungals (fluconazole, itraconazole, ketoconazole, posaconazole, voriconazole) are well-documented
  CYP51 inhibitors with real antileishmanial activity already published, and they are also **dirt-cheap generics**
  (fluconazole is a few dollars a month). Running the full library here is less about discovering a totally novel
  scaffold and more about (a) a strong pipeline-validation run — if the known azoles don't land near the top, that's
  a red flag on the receptor prep, the same role Chagas/cruzain played for PTR1 — and (b) directly testing the
  "can we find a genuinely cheap, practical hit" question this whole follow-up pass exists to answer, since azoles
  are exactly the cheap/safe/simple profile VL treatment is missing today.

## Candidate C: DNA topoisomerase IB — noted, deprioritized for now

**Role.** The clearest literal "reproduction" attack vector — Leishmania's topoisomerase IB is required for DNA
replication/transcription, and unusually, it's a **heterodimer** (large subunit TOP1L does DNA binding/catalysis
support, small subunit TOP1S carries the catalytic tyrosine) — a structural feature entirely absent from the
human enzyme, which is normally monomeric. That heterodimer interface is itself a selective-inhibition angle.

- Structure: PDB **2B9S**, *L. donovani* topoisomerase I, solved as a vanadate–DNA transition-state complex.
- Why deprioritized: camptothecin-class topoisomerase-I inhibitors work by intercalating into the
  DNA–enzyme cleavage complex and stabilizing it, not by binding a normal apo protein pocket — the small-molecule
  "site" only exists together with the nicked DNA and the transition-state geometry. That's a poor match for this
  pipeline's normal approach (fpocket + Vina-GPU docking against a protein-only receptor, the same way PTR1 and
  the two candidates above are classic single-chain enzyme-active-site pockets). Would need a materially different
  docking setup (protein+DNA receptor, or accept the docking result only approximates the real mechanism) to do
  properly — worth coming back to later, not a good first pick for a quick second screen.

## Recommendation

**Run Candidate A (trypanothione reductase) next**, with **Candidate B (CYP51) as the near-term follow-up**
rather than a fallback — the two ask different questions (TR: does a fresh chemically-distinct pocket surface
novel cheap candidates; CYP51: does the pipeline correctly re-find the already-known cheap azole answer) and both
are worth actually running, not just one. Topoisomerase IB stays on the list for later, once/if the pipeline is
extended to handle a DNA-bound receptor properly.

Next steps before docking: pick and prep an actual receptor structure (single chain or the minimal biological
unit, strip crystallographic waters/ligands the same way `1E92_receptor.pdbqt` was prepped, keep any structural
cofactor the pocket needs — NADPH for TR, heme for CYP51), run fpocket to confirm/cross-check the pocket against
the literature residues, then smoke-test before committing to a full 1,859-drug run.

Per project scope: this is target/candidate selection for future docking, not a therapeutic claim about any of
these proteins or drugs.
