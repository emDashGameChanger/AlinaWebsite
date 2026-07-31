# Lab notebook

## 2026-07-29

Built out `biolab/` as a reproducible pipeline: `setup.sh` (fpocket +
AutoDock-Vina-GPU-2.1 build), and the FDA-approved drug library pipeline
(`fetch_drug_library.py` -> `prepare_ligand_library.py` -> `batch_dock.py`,
~1,859 drugs from DrugCentral). Smoke-tested the whole chain end-to-end
against the 3I3R demo receptor (`runs/smoke-test-3I3R/`), which surfaced and
fixed real bugs along the way: a Meeko macrocycle atom-type incompatibility
with Vina-GPU, and Vina-GPU's hard 130-atom-per-ligand limit. No real disease
target chosen yet at this point.

## 2026-07-29 (evening) - 2026-07-30

Ran target research (`target-research` skill) and shortlisted three
disease/target pairs: Chagas disease/cruzain, visceral leishmaniasis/PTR1,
and Chikungunya/nsP2 (`targets/shortlist-2026-07-30.md`). Picked **visceral
leishmaniasis, targeting pteridine reductase 1 (PTR1)** — the unmet-need
case is as strong as Chagas (every current VL treatment is toxic, expensive,
or teratogenic — no option is all three of cheap/safe/easy) and the
FDA-drug-repurposing-vs-PTR1 angle is less picked-over in the published
literature than cruzain. Chagas/cruzain stays the backup and a good
candidate for validating the pipeline against known published results later.

## 2026-07-30

Deepened the PTR1 research (`targets/PTR1.md`): confirmed PDB **1E92**
(*L. major* PTR1, NADP+ + dihydrobiopterin, 2.20 A) as the receptor
structure, over the apo *L. donovani* 2XOX (sulfate in the cofactor site,
not usable for defining the pocket). Found a directly relevant 2024/2025
in-silico benzothiazole-screening paper against this exact target (using PDB
5L4N) that validated the planned approach — keep the NADP+ cofactor in the
receptor, dock into the natural-substrate pocket — and named the key pocket
residues (Ser111, Phe113, Met183, Leu188, Leu226, His241) to check our own
pocket selection against.

Ran fpocket on 1E92 (71 pockets found across the tetramer's 4 equivalent
active sites) and confirmed chain A's **pocket 4** (druggability 0.886) as
the right site — it directly contacts the crystallized dihydrobiopterin
ligand and includes Ser111/Phe113 from the literature. The remaining four
literature residues turned up in two smaller, lower-scored adjacent fpocket
fragments (pocket 36, pocket 8), consistent with fpocket splitting one
continuous cleft into sub-pockets rather than missing the site.

Prepared the real receptor (`1E92_receptor.pdbqt`): chain A only, NADP+
kept, dihydrobiopterin/waters/cryoprotectant stripped via PyMOL, converted
with Open Babel. Built a docking box centered on the crystallized ligand
position, sized generously (22x22x22 A) to also cover the adjacent
NADP+-proximal subpocket (`1E92_PTR1_config.txt`). Capped the GPU to 75%
power (337 W of the RTX 3090 Ti's 450 W default) before the full run, per
request — turned out not to matter, since this workload only drew ~212 W at
100% utilization anyway.

Smoke-tested on 24 drugs (`runs/smoke-test-1E92-PTR1/`) — clean run,
affinities -8.4 to -11.0 kcal/mol, top hit ergotamine. Then ran the **full
FDA-approved-drug library (1,808 dockable of 1,840) against PTR1**
(`runs/full-1E92-PTR1-screen/`) — the project's first real screening
campaign. Took ~4h11m. 1,795 drugs docked successfully. Top predicted
binders: alectinib (-12.1), risdiplam (-11.7), eltrombopag (-11.6),
conivaptan (-11.6), entrectinib (-11.5), dihydroergotamine (-11.5 — same
ergot-alkaloid family as the smoke test's top hit, a consistent signal
across two independent runs). None of the top hits match the pterin-mimetic
or benzothiazole chemotypes known from the PTR1-inhibitor literature —
interesting as novel-scaffold candidates rather than a red flag, since
hypothesis-generation doesn't require matching known chemistry.

Wrote this up as the site's first PTR1 tutorial page
(`molecularDocking/PTR1Screen.html`), wired into the index and Molecular
Docking hub cards.

## 2026-07-30 (later)

Ran the visual pose sanity-check that was left open above: rendered the
best docked pose for all top 10 hits in PyMOL from one fixed camera/pocket
view (`molecularDocking/images/ptr1poses/`) so they're directly comparable
side by side. Result: all 10 land in the same pocket, right up against the
NADP+ cofactor, instead of being scattered across the protein surface — a
real physically-grounded plausibility signal on top of the raw affinity
numbers. Added a clickable HTML/CSS grid (each pose links to its own
full-size render) to the PTR1Screen.html write-up; ligand carbons are
rendered magenta for contrast against the gray pocket surface and blue
NADP+.

Added a second render style per candidate: a solid surface/"blob" view of
the ligand (pink, #E03FD8) matching the pocket's own surface style,
alongside the stick view, so the two balance visually. Re-rendered the
stick views with matching pocket-surface parameters for consistency.

## 2026-07-30 (literature check)

Ran the last open item: a literature search for existing antiparasitic
activity on the top 10 hits (`runs/full-1E92-PTR1-screen/literature-check.md`
has the full write-up, method, and citations). Searched each drug against
Leishmania/Trypanosoma/Plasmodium individually, then broadened to drug-class
and known repurposing-screen literature (ReFRAME, kinase-inhibitor-vs-
Leishmania screens) where the direct search came up empty.

Result: 9 of the 10 (alectinib, risdiplam, eltrombopag, conivaptan,
entrectinib, dihydroergotamine, bexarotene, capmatinib, tolvaptan) have no
published antiparasitic activity found — genuinely novel scaffolds, which
is the expected/hoped-for outcome of a repurposing screen, not a red flag.
**Olaparib** is the exception: confirmed potent activity against
*Trypanosoma cruzi* (IC50 3.4 nM against PARP-1, Vilchez Larrea et al.,
PLOS ONE 2012, DOI 10.1371/journal.pone.0046063) — a different parasite,
via a mechanism (PARP/DNA-repair inhibition) unrelated to PTR1's
folate-salvage role, so it's a real but separate data point rather than a
confirmation of the PTR1 docking score.

This closes out the open items from the full screen. Per project scope,
none of this is a therapeutic claim: these are computational hits worth
investigating further, not proof of anything. Not yet added to the public
website write-up — holding for review of the citations first.

## 2026-07-30 (attack-vector research)

The pricing/safety check above landed hard on a real problem: every PTR1 top
hit is an $8,000-19,000+/month specialty drug, which is close to the opposite
of what this project is looking for. Rather than switch diseases, looked for
a **different essential Leishmania target** — a different "attack vector" on
the same parasite (redox/metabolism, membrane biosynthesis, DNA replication)
instead of PTR1's folate-salvage pathway, on the theory that a chemically
different binding pocket might surface a different, hopefully cheaper, class
of hits than PTR1's kinase-inhibitor-heavy result.

Shortlisted and compared three candidates
(`targets/attack-vectors-shortlist-2026-07-30.md`): **trypanothione
reductase** (TR — the parasite-specific redox enzyme that replaces
glutathione reductase, essential, absent in humans entirely; PDB 2JK6/2W0H/
2X50/2YAU/6ER5), **sterol 14-alpha-demethylase** (CYP51 — ergosterol/membrane
biosynthesis; PDB 3L4D, solved with fluconazole already in the pocket), and
**DNA topoisomerase IB** (the literal "reproduction" vector; PDB 2B9S,
heterodimeric — unlike the human enzyme — but deprioritized because
camptothecin-class inhibitors work via a DNA-intercalation mechanism that
doesn't map cleanly onto this pipeline's protein-only Vina-GPU docking setup).

**Decision: run TR next**, with **CYP51 as a near-term follow-up** rather
than a fallback. TR's pocket is chemically nothing like PTR1's pterin site,
so it's the best shot at a genuinely different hit list. CYP51 is the
opposite bet on purpose — azole antifungals are well-documented CYP51
inhibitors with real antileishmanial activity *and* are dirt-cheap generics,
so that run doubles as a pipeline sanity check (do known actives land near
the top?) and a direct test of whether this pipeline can find the
cheap/practical answer when one is known to exist.

Also: this session hit another API false-positive mid-research (same class
of issue as the one recorded 2026-07-30 on the PDB-fetch work, see
`targets/PTR1.md`/scope notes) and had to restart — no change to approach or
scope, still purely public-structure-data + open-source-docking-software
research.

## 2026-07-30 (TR + CYP51 receptor prep)

Prepped both next-up targets from the attack-vector shortlist.

**Trypanothione reductase (TR)**: initially cleaned PDB 2YAU (*L. infantum*)
down to chain A only, following the same recipe as PTR1 — but fpocket on
chain A alone only found a fragment of the real binding cavity (best
druggability 0.461, ~17 Å from the crystallized auranofin ligand). A quick
literature check explained why: TR's main druggable cavity is
**inter-subunit**, formed by the FAD-binding domain of one monomer and the
interface domain of the other — unlike PTR1's tetramer, where each chain
has its own independent active site. Redid the prep keeping the **full A+B
homodimer** (FAD + NADPH kept on both chains, auranofin/Cl/SO4/waters
stripped) and reran fpocket: found a much better pocket spanning both
chains (druggability 0.731, top score on the whole structure), with
residues from chain A and chain B matching the published domain
description almost exactly. Boxed that pocket (the literature "mepacrine
binding site"), *not* the crystallized auranofin position, which turned
out to mark a different, low-druggability catalytic cleft ~17 Å away
(covalent gold-cysteine chemistry, not a normal small-molecule pocket).
Smoke-tested on 20 ligands — clean run, -6.6 to -10.5 kcal/mol
(`runs/smoke-test-2YAU-TR/`).

**CYP51**: cleaned PDB 3L4D (*L. infantum*) to chain A only (correct here —
P450s are monomeric, unlike TR or PTR1). fpocket found an unambiguous best
pocket (druggability 0.993, the top score of anything prepped this
session) right above the heme iron, ~8 Å from the crystallized fluconazole
position. Boxed it with an asymmetric 20x28x28 Å box instead of the usual
22 Å cube, since this pocket is an elongated substrate channel rather than
a compact cavity. Smoke-tested on 20 ligands — clean run, -8.2 to -10.8
kcal/mol (`runs/smoke-test-3L4D-CYP51/`). Both receptors' cofactor rings
(FAD's isoalloxazine, heme's porphyrin) triggered an Open Babel
"failed to kekulize aromatic bonds" warning during PDB->PDBQT conversion —
checked atom counts and AutoDock atom types before/after for both and
confirmed nothing was dropped or mistyped (including the heme iron itself),
so the warning is cosmetic here, not a receptor-quality problem.

Full details and exact box math in `targets/attack-vectors-shortlist-2026-07-30.md`
and both `NOTES.md` files above. Per the earlier decision, **launched the
full 1,808-drug TR screen** (`runs/full-2YAU-TR-screen/`) right after the
TR smoke test passed; CYP51's full screen is prepped and ready to run next
but not yet started.

## 2026-07-30 (full TR screen result)

The full TR screen finished (1,795/1,808 docked successfully;
`runs/full-2YAU-TR-screen/NOTES.md` has the full table). Top hit:
**ergotamine (-10.5 kcal/mol)** — and that's the interesting part. Ergotamine
topped the TR smoke test too, and its close relative dihydroergotamine
landed in the PTR1 screen's top 10. That's now a consistent ergot-alkaloid
signal across **two different targets/pockets and three separate runs**,
and unlike almost every other top hit on either target's list, ergotamine
is a genuinely cheap, decades-generic drug — the first candidate this
project has found that's simultaneously a strong hit *and* actually cheap.
Rest of the TR top 10 (berotralstat, nilotinib, lomitapide, midostaurin,
saquinavir, naldemedine, rimegepant, conivaptan, bisoctrizole) is the same
familiar mix of expensive specialty drugs, with conivaptan notably
reappearing from the PTR1 top 10 on an unrelated pocket (possible generic
"sticky binder" rather than a real signal) and bisoctrizole being a
sunscreen UV filter rather than a real systemic-drug candidate.

## 2026-07-30 (TR follow-up checks + CYP51 full screen launched)

Ran the same follow-up sequence PTR1 got, in parallel with launching
CYP51's full screen (`runs/full-3L4D-CYP51-screen/`, still running).

**Pose check** (`runs/full-2YAU-TR-screen/pose-sanity-check.md`, done
quantitatively rather than with PyMOL renders this time): all 10 top hits'
best poses cluster within 2.8-4.5 Å of the box center rather than
scattering, and ergotamine specifically contacts nearly every
literature-matched pocket-1 residue from both chains at 3.3-4.5 Å —
confirms it's really sitting in the inter-subunit cavity the box was built
around, not just generically inside the box.

**Literature check** (`runs/full-2YAU-TR-screen/literature-check.md`): 8/10
have no prior antiparasitic literature (expected/novel, not a red flag).
**Saquinavir** has a real, directly relevant precedent — Savoia et al. 2005
found it inhibits *L. major* (IC50 7.0 uM) and, more weakly, *L. infantum*
promastigote growth, via proteasome inhibition rather than TR. **Nilotinib**
has a same-class/different-target precedent (active against *T. cruzi* via
triosephosphate isomerase, per a 2024 repositioning-screen paper using this
project's same general approach) but wasn't among that paper's *Leishmania*
hits. **Ergotamine** itself still has no prior antiparasitic literature at
all, despite topping two independent TR runs.

**Pricing/safety** (`runs/full-2YAU-TR-screen/pricing-safety-profile.md`):
same pattern as PTR1 — most of the list is $5,000-300,000+/year
oncology/orphan drugs (nilotinib, lomitapide, midostaurin, berotralstat,
three with black-box warnings), plus non-generic moderate-cost drugs
(saquinavir, naldemedine, rimegepant), conivaptan (already ruled out for
PTR1), and bisoctrizole (a sunscreen UV filter with no US approval or data
for oral/systemic use at all — not a real candidate regardless of score).
**Ergotamine is the exception and the headline result**: in its common
caffeine-combo generic form it's genuinely cheap (~$112-400/20 tablets),
unlike the pure Ergomar brand. Combined with the cross-run docking
consistency and the pose/pocket-contact check, this is the first candidate
in the whole project that's simultaneously a strong, physically plausible
hit *and* actually affordable — flagging it as the most promising practical
lead so far, pending it eventually being tested against a third target or
some other independent check.

## 2026-07-30 (CYP51 full screen result)

CYP51's full screen finished too (`runs/full-3L4D-CYP51-screen/NOTES.md`).
Top 10: digitoxin, dutasteride, irinotecan, rimegepant, vibegron,
conivaptan, nilotinib, ubrogepant, tepotinib, eltrombopag.

The interesting part is the azole result, since CYP51 was picked partly to
test whether the pipeline would correctly re-find the known cheap azole
antifungals. It's a mixed/partial validation: no azole made the top 10, but
itraconazole ranks 42nd of 1795 (top ~2.5%) and the rest of the azole class
clusters together right behind it — a real, class-coherent signal.
**Fluconazole itself — the exact drug crystallized in this receptor
structure — only ranks 854th (roughly median)**, despite its position
literally defining the docking box. That's a known Vina scoring-function
bias (favors bigger molecules with more van der Waals contacts) rather than
a receptor-prep problem, but it's a real limitation worth remembering:
Vina's raw top-10 list systematically favors size over "is this a good real
inhibitor," and fluconazole (the cheapest azole) is exactly the kind of
small, polar molecule that bias underscores.

Also notable: four of the ten top hits (conivaptan, nilotinib, rimegepant,
eltrombopag) have now shown up in a top-10 list on a *different* target's
pocket in this project (PTR1 and/or TR) — a growing sign that these four
specifically may just be large, flexible, generically high-scoring
molecules by Vina's function rather than genuinely pocket-specific binders.
Dutasteride is the most mechanistically interesting new hit, being itself a
steroid-pathway-metabolism drug.

## 2026-07-30 (CYP51 follow-up checks)

Ran the same pose-check/literature-check/pricing-safety sequence on CYP51's
top 10 (`runs/full-3L4D-CYP51-screen/`). Headline result: **digitoxin has
direct, confirmed activity against *Leishmania infantum* itself** —
digitoxigenin (its aglycone) has published IC50 6.9 ug/mL against
*L. infantum* with a 42.8 selectivity index, and a derivative
(beta-acetyl-digitoxin) worked in vivo in infected mice. That's the
strongest literature precedent this project has found, better than PTR1's
or TR's (those matched a different parasite species). Catch: **digitoxin
itself is no longer commercially available in the US** — withdrawn from
market, replaced clinically by digoxin (which wasn't the drug that scored
well here). Irinotecan also has a direct *L. infantum* precedent (it and
its metabolite SN-38 poison *L. infantum* topoisomerase IB, confirmed
in vitro/ex vivo) — a nice callback to Candidate C (topoisomerase IB) from
the attack-vector shortlist, which was deprioritized as a docking target
for exactly the DNA-intercalation-mechanism reason this result illustrates.
Dutasteride (cheap generic, ~$8-40/month, no black box, no prior
antiparasitic literature) is the best practical new candidate on this
list. Pose check: all 10 land within 0.4-2.8 A of the box center and
3.2-5.9 A of the heme iron.

## 2026-07-30 (cross-target specificity analysis — sticky vs. pocket-specific)

With three completed full-library screens (PTR1, TR, CYP51) against three
chemically unrelated pockets, built a rigorous way to tell whether a
repeat top-10 hit (conivaptan, nilotinib, rimegepant, eltrombopag all
showed up more than once) is genuine pocket complementarity or just a
molecule Vina's scoring function likes everywhere. Method and full
25-drug table in `cross-target-specificity-analysis.md`. Short version:
per-target z-scored every drug's affinity (after filtering ~33/1795
non-physical positive-affinity TR results — more clash failures than PTR1
or CYP51 had, likely the dimer receptor being a harder fit for some bulky
ligands), then measured each drug's "specificity gap" (how much better it
is on its best target vs. its own baseline on the other two).

**8 of 25 confirmed generically sticky**: conivaptan, tepotinib,
tolvaptan, nilotinib, eltrombopag, olaparib, dihydroergotamine,
entrectinib — consistently strong on all three unrelated pockets,
essentially flat z-scores. **4 of 25 are genuinely pocket-specific**:
digitoxin and irinotecan (CYP51), alectinib and bexarotene (PTR1) — and
notably, these are also exactly the hits with the strongest independent
literature support found so far, which is a real cross-check on the
metric itself, not just a restatement of the docking scores.

**Important correction**: ergotamine — flagged as the project's best
practical lead after the TR screen — reads as "mixed, leaning sticky"
(specificity gap 0.97, well short of the >1.2 threshold used for the
SPECIFIC group) rather than cleanly pocket-specific. It's a strong binder
on all three targets, just somewhat stronger on TR. In hindsight this
tracks with known ergot-alkaloid pharmacology (notoriously promiscuous
across many unrelated human receptors too) — doesn't disqualify it as a
lead, since it's still the cheapest cross-run-consistent hit found, but
the framing should be "consistently strong, likely non-selective binder"
rather than "novel, pocket-matched scaffold."
