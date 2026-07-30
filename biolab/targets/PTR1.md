# Target: Pteridine reductase 1 (PTR1) — visceral leishmaniasis

Chosen 2026-07-30 over Chagas/cruzain (backup candidate) — see
`shortlist-2026-07-30.md` for the full disease-level comparison. This doc is
the deep dive on the target itself: known structures, binding-site
literature, and inhibitor chemotypes, gathered before committing to a
docking box.

## Disease and target recap

Visceral leishmaniasis (*Leishmania donovani*/*L. infantum*), fatal if
untreated, ~200,000–400,000 cases/year. No option is simultaneously cheap,
safe, and easy to administer (liposomal amphotericin B is expensive and
nephrotoxic; meglumine antimoniate is cheaper but more toxic; miltefosine,
the only oral option, is teratogenic). PTR1 is an NADPH-dependent pteridine/
folate-salvage reductase that lets the parasite bypass the main folate
pathway — validated as a drug-resistance-relevant target.

## Structure chosen: PDB 1E92

*L. major* PTR1, 2.20 Å, X-ray, homotetramer (chains A–D, D2 symmetry, each
subunit an independent active site). Each chain has its own bound **NAP**
(NADP+) and **HBI** (7,8-dihydrobiopterin, the natural substrate — this is
what occupies the site we want to dock our drug library into). Also present:
EDO (ethylene glycol, cryoprotectant) and waters — both discardable.
Downloaded and confirmed locally at `biolab/1E92.pdb`.

Chosen over *L. donovani* 2XOX, which is an apo/blocked structure (sulfate
ion in the cofactor site rather than a real ligand) — unsuitable for
defining the binding pocket.

## Other PTR1/PTR1-family structures surveyed (for context, not used directly)

- **1W0C** — LmPTR1 + NADPH + 2,4,6-triaminoquinazoline (TAQ), 2.6 Å.
- **5L4N** / **5L42** — LmPTR1 in complex with flavanone-derived inhibitors
  (compounds 1 and 3). **5L4N is the receptor used by the closest published
  precedent for this exact project** (see below).
- **6RXC** — LmPTR1 + NADPH + inhibitor NMT-C0026 (a
  2,4-diaminopteridine/piperidine-carboxylate), 2.10 Å, IC50 220 nM vs
  LmPTR1 (from a fragment-based design campaign, 2020).
- **2QHX** — LmPTR1 + inhibitor (Ki 100 nM parent compound, 37 nM optimized
  analog), 2007 SAR series.
- **1P33** — *L. tarentolae* PTR1 + NADPH + methotrexate (cross-species
  reference; antifolate).
- **3BMQ**, **3JQA** — *T. brucei* PTR1 (different trypanosomatid, useful
  for cross-species SAR only, not used here).
- A 2022 paper solved a high-resolution LmPTR1 + NADP+/NADPH + folic acid
  ternary complex (PMC8996148) — folic acid is the other natural substrate
  besides dihydrobiopterin, confirming the same subsite is used by multiple
  physiological ligands.

## Directly relevant precedent: in-silico benzothiazole screen against LmPTR1

Found a close methodological match — an in-silico study screening
benzothiazole-core compounds against LmPTR1 (Bittencourt-Cunha et al.-style
virtual screening/QSAR paper, PMC11740253, 2024/2025):

- **Receptor**: PDB **5L4N** (LmPTR1 apo-ish structure), prepared in UCSF
  Chimera (solvent deletion, added hydrogens/charges, incomplete side chains
  rebuilt).
- **Cofactor handling**: kept **NADP+ in the receptor** as an essential part
  of the binding site — direct support for our plan to keep NAP in 1E92
  rather than stripping it.
- **Grid box**: 20 Å³ centered on the co-crystallized inhibitor's position
  (i.e. pocket-centered, not blind docking).
- **Key pocket residues**: **Phe113, His241, Leu188, Met183, Leu226, Ser111**
  — Phe113 in particular does π-stacking with both the ligand and NADP+.
  These residue numbers should carry over to 1E92 since it's the same
  protein (LmPTR1) — worth cross-checking against fpocket's chosen pocket
  for 1E92 as a sanity check that we've got the right site.
- **Docking engine**: AutoDock Vina 1.1.2 (same lineage as our
  AutoDock-Vina-GPU-2.1). Validated by redocking the co-crystallized ligand
  (RMSD 0.55 Å, well under the 2 Å acceptance bar) and by ROC/BEDROC
  discrimination (AUC 0.913) between known actives/inactives.
- **Top hit**: 2-aminobenzothiazole scaffold, predicted pIC50 competitive
  with known low-nanomolar LmPTR1 inhibitors.

**Why this matters for us**: this is close to a worked answer key for our
own screen — same target, same general docking approach (Vina family, box
centered on the known pocket, cofactor retained), just a smaller focused
library instead of the full FDA-approved set. It validates our planned
receptor-prep approach (keep chain, keep NADP+, strip water/cryoprotectant)
and gives us named residues to check our fpocket pocket selection against.

## Inhibitor chemotypes seen across the literature

- Pteridine/pterin-mimetic scaffolds (TAQ, NMT-C0026 class) — closest
  chemically to the natural dihydrobiopterin/folate substrates.
- 2-aminobenzothiazole derivatives — newer, non-pterin scaffold, strong
  in-silico hits.
- Flavanone-derived inhibitors (5L4N/5L42 series).
- Antifolates (methotrexate, cross-reactive with related pterin reductases).

None of these chemotypes were checked yet against whether they (or close
analogs) appear in our FDA-approved drug library — worth a quick post-hoc
check once results.csv exists, as a sanity/plausibility signal (finding a
known-adjacent scaffold scoring well would be reassuring; finding nothing
familiar isn't disqualifying, just less validated).

## Open items before docking

- Run fpocket on 1E92 chain A and confirm the top pocket includes/borders
  Phe113, His241, Leu188, Met183, Leu226, Ser111 (or their 1E92-numbering
  equivalents) before trusting the box.
- Confirm receptor prep choice: single chain (A) + its NAP, HBI removed
  (that's the site we're docking into), waters/EDO stripped. Matches the
  PMC11740253 precedent's cofactor-retained approach.

## Scope note

Hypothesis-generation only, per project-wide scope rules — no docking score
here should be read as a therapeutic claim, only as "worth investigating
further computationally."
