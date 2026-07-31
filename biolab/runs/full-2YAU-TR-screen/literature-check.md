# Literature check: existing antiparasitic activity of the top 10 TR hits

Date: 2026-07-30
Scope: the top 10 ranked drugs from `results.csv` (the full FDA-approved-drug
screen against trypanothione reductase, PDB 2YAU) — ergotamine,
berotralstat, nilotinib, lomitapide, midostaurin, saquinavir, naldemedine,
rimegepant, conivaptan, bisoctrizole. Same method and rationale as
`../full-1E92-PTR1-screen/literature-check.md` (a physically sane docked
pose and prior published antiparasitic evidence are two independent,
non-substitutable signals — see that file for the full reasoning).

## Method

For each drug: searched `"<drug> Leishmania OR Trypanosoma antiparasitic
activity"` first, and for the top few hits, `"<drug> trypanothione
reductase"` specifically, since that's the actual enzyme this run targets
(a sharper, more mechanism-relevant check than PTR1's general antiparasitic
search). Broadened to drug class / other parasitic diseases where the
direct search came up empty.

## Results

**8 of 10 (berotralstat, lomitapide, midostaurin, naldemedine, rimegepant,
conivaptan, bisoctrizole, and — with one caveat below — ergotamine) have no
published antiparasitic activity found** — the expected/hoped-for outcome
for a repurposing screen, not a red flag.

**Saquinavir** is a real, directly relevant hit: Savoia, Allice & Tovo
(*Int J Antimicrob Agents*, 2005, 26(1):92-4) tested HIV protease
inhibitors indinavir and saquinavir against *Leishmania major* and
*L. infantum* promastigote growth — saquinavir's IC50 against *L. major*
was 7.0 μM, with weaker activity reported against *L. infantum* (the same
species PTR1 and TR are both being screened against in this project).
The mechanism proposed was proteasome inhibition, not TR — so this is a
real but mechanistically independent data point, the same relationship
olaparib had to PTR1 (confirmed activity via an unrelated mechanism), not
a confirmation of the TR docking result specifically. Later work also
found HIV protease inhibitors reduce intracellular survival of
visceral-leishmaniasis-causing *Leishmania* species more broadly, so
saquinavir sits in a small but real cluster of prior repurposing interest,
not an isolated one-off result.

**Nilotinib** has a related but weaker precedent: Juarez-Saldivar et al.
(*Archives of Medical Research*, 2024) ran a structure-based virtual
screen very similar in spirit to this project's own approach, and found
nilotinib more active against *Trypanosoma cruzi* (Chagas disease, via
triosephosphate isomerase) than the reference drugs nifurtimox and
benznidazole — but that same paper's *Leishmania mexicana* hits were
chlorhexidine and protriptyline, not nilotinib. So nilotinib has
antiparasitic precedent, but for a different parasite and a different
enzyme target than either one this project has screened — the same
"real but separate" relationship olaparib had to PTR1.

**Ergotamine**: no published Leishmania/Trypanosoma or trypanothione-
reductase activity found for ergotamine or the ergot-alkaloid class
generally. Given it's also the top hit on two independent TR runs (the
smoke test and the full screen) and its relative dihydroergotamine landed
in the PTR1 top 10, this is the most interesting "no prior literature, but
strong and repeated docking signal" case the project has produced — a
genuinely novel scaffold hypothesis, not a known result being
rediscovered.

## Bottom line

No red flags (nothing found actively contradicting a docking score), one
directly relevant confirmed-active precedent (saquinavir, same target
species, unrelated mechanism), one same-class/different-target precedent
(nilotinib), and a cross-run-consistent, seemingly genuinely novel top
candidate (ergotamine) that's also — unlike almost every other hit on
either target's top-10 list so far — actually cheap. See
`pricing-safety-profile.md` for the cost/safety pass, which is the more
decisive practicality filter for this project's specific goals.

## Scope note

Per project-wide scope rules: none of this is a therapeutic claim. Prior
antiparasitic evidence for a drug's *current* approved form/dose says
nothing about what would happen if it were ever actually tested against
*Leishmania* TR specifically.
