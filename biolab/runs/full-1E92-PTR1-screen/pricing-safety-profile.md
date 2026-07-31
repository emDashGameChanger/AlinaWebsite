# Pricing and safety profile of the top 10 PTR1 hits

Date: 2026-07-30
Scope: same top 10 drugs as `literature-check.md` — alectinib, risdiplam,
eltrombopag, conivaptan, entrectinib, dihydroergotamine, bexarotene,
capmatinib, tolvaptan, olaparib.

## Why this check

A drug can dock well (pose sanity check passed, see `NOTES.md`) and even
have unrelated prior antiparasitic precedent (olaparib, see
`literature-check.md`) and still be a bad practical repurposing candidate.
This project's whole premise for visceral leishmaniasis is that the
existing options all fail on being simultaneously **cheap, safe, and easy
to take** — liposomal amphotericin B is effective but expensive and
nephrotoxic, meglumine antimoniate is cheaper but more toxic, miltefosine
is oral but teratogenic (see `targets/PTR1.md`). So it's worth checking
where each top hit actually lands on that same cost/safety axis, as an
independent practicality filter alongside the docking score and the
literature check.

All prices below are current US list/retail figures pulled via web search
(GoodRx, Drugs.com, manufacturer patient sites, etc.) — they fluctuate and
vary by insurance/country, so treat them as order-of-magnitude, not exact.
Every figure and safety claim below has a source link.

## Summary table

| Drug | Current approved use | Approx. US price | Key safety concerns |
|---|---|---|---|
| Alectinib (Alecensa) | ALK+ non-small-cell lung cancer | ~$12,500–19,000/month brand; ~$70/month via patient assistance | Hepatotoxicity (biweekly LFTs first 3mo), pneumonitis, bradycardia, severe kidney injury |
| Risdiplam (Evrysdi) | Spinal muscular atrophy | Weight-based, up to ~$340,000/year; <$100,000/year for infants | Embryofetal toxicity in animal studies (mortality, malformations), male infertility risk, serious eye/retinal and cardiac symptoms reported |
| Eltrombopag (Promacta) | Immune thrombocytopenia (ITP), aplastic anemia | ~$10,000–18,000/month brand; $195–295/month generic | **Black box**: hepatotoxicity + thrombosis/thromboembolic risk (portal vein thrombosis, PE) |
| Conivaptan (Vaprisol) | Hyponatremia (IV, inpatient only) | ~$450–900/day | Contraindicated in hypovolemic hyponatremia and heart failure; severe interactions with 50+ other drugs |
| Entrectinib (Rozlytrek) | ROS1+/NTRK+ cancers | ~$7,200–8,000/28 days | CHF, CNS effects (confusion, hallucinations, memory problems), bone fracture risk, hepatotoxicity |
| Dihydroergotamine (D.H.E. 45/Migranal) | Migraine | ~$100–335 per dose unit; generics exist | Rare but serious cardiac/vasospasm events (coronary vasospasm, MI, arrhythmia); heavy CYP3A4 drug-interaction risk |
| Bexarotene (Targretin) | Cutaneous T-cell lymphoma | ~$9,469/month average retail; as low as $168 w/ coupon | **Teratogenic** (retinoid class), hyperlipidemia, pancreatitis risk, photosensitivity, requires baseline+ongoing CBC/lipid/LFT/thyroid monitoring |
| Capmatinib (Tabrecta) | MET exon 14-mutant NSCLC | ~$9,469 WAC at launch; ~$11,400–17,950/month retail | Hepatotoxicity, pancreatitis, interstitial lung disease/pneumonitis |
| Tolvaptan (Samsca/Jynarque) | Hyponatremia / ADPKD | ~$3,700 (Samsca, 10 tabs) to ~$16,300/month (Jynarque) | **Black box**: serious/fatal liver injury — Jynarque restricted to a REMS program; risk of osmotic demyelination if sodium corrected too fast |
| Olaparib (Lynparza) | BRCA-mutant ovarian/breast/other cancers | ~$8,700–13,000/month | **Black box**: MDS/AML (~1.5% incidence, ~50% fatal when it occurs); pneumonitis |

## Per-drug sources

**Alectinib (Alecensa)**
- Price: [Prescription Hope](https://prescriptionhope.com/medication/alecensa-alectinib/), [Drugs.com price guide](https://www.drugs.com/price-guide/alecensa), [GoodRx](https://www.goodrx.com/alecensa)
- Side effects: [Alecensa official patient site](https://www.alecensa.com/patient/metastatic/side-effects/possible-side-effects.html), [WebMD](https://www.webmd.com/drugs/2/drug-170687/alecensa-oral/details), [RxList](https://www.rxlist.com/alecensa-drug.htm)

**Risdiplam (Evrysdi)**
- Price: [GoodRx](https://www.goodrx.com/evrysdi), [Drugs.com price guide](https://www.drugs.com/price-guide/evrysdi), [pharmaphorum](https://pharmaphorum.com/news/roche-takes-on-pricey-rivals-as-fda-approves-sma-drug)
- Side effects: [Drugs.com side effects](https://www.drugs.com/sfx/evrysdi-side-effects.html), [Drugs.com MTM](https://www.drugs.com/mtm/risdiplam.html), [Medscape](https://reference.medscape.com/drug/evrysdi-risdiplam-4000042)

**Eltrombopag (Promacta)**
- Price: [GoodRx](https://www.goodrx.com/promacta), [Drugs.com price guide](https://www.drugs.com/price-guide/promacta), [MedsPartner generic guide](https://medspartner.com/blogs/resources/promacta-alternatives-a-guide-to-affordable-global-access-to-generic-eltrombopag)
- Side effects/black box: [Healthline](https://www.healthline.com/health/drugs/eltrombopag-oral-tablet), [RxList](https://www.rxlist.com/promacta-drug.htm), [Drugs.com side effects](https://www.drugs.com/sfx/promacta-side-effects.html)

**Conivaptan (Vaprisol)**
- Price + side effects: [American Family Physician](https://www.aafp.org/pubs/afp/issues/2008/1015/p984.html), [RxList](https://www.rxlist.com/vaprisol-drug.htm), [Medscape](https://reference.medscape.com/drug/vaprisol-conivaptan-342808)

**Entrectinib (Rozlytrek)**
- Price: [NCBI pharmacoeconomic review](https://www.ncbi.nlm.nih.gov/books/NBK601789/), [Drugs.com price guide](https://www.drugs.com/price-guide/rozlytrek)
- Side effects: [RxList](https://www.rxlist.com/rozlytrek-drug.htm), [GoodRx](https://www.goodrx.com/rozlytrek/what-is)

**Dihydroergotamine (D.H.E. 45 / Migranal)**
- Price + side effects: [Drugs.com price guide](https://www.drugs.com/price-guide/dihydroergotamine), [RxList (D.H.E. 45)](https://www.rxlist.com/dhe-45-drug.htm), [RxList (Migranal)](https://www.rxlist.com/migranal-drug.htm), [GoodRx](https://www.goodrx.com/dihydroergotamine-mesylate/what-is)

**Bexarotene (Targretin)**
- Price + side effects: [GoodRx](https://www.goodrx.com/bexarotene), [WebMD](https://www.webmd.com/drugs/2/drug-17979/targretin-oral/details), [RxList](https://www.rxlist.com/targretin-drug.htm), [official prescribing info (PDF)](https://pi.bauschhealth.com/globalassets/BHC/PI/TargretinCapsules-PI.pdf)

**Capmatinib (Tabrecta)**
- Price: [Drugs.com price guide](https://www.drugs.com/price-guide/tabrecta), [Medical Letter](https://secure.medicalletter.org/TML-article-1674d), [tandfonline budget-impact analysis](https://www.tandfonline.com/doi/full/10.1080/13696998.2020.1867470)
- Side effects: [MedicalNewsToday](https://www.medicalnewstoday.com/articles/drugs-tabrecta), [RxList](https://www.rxlist.com/tabrecta-drug.htm), [Healthline](https://www.healthline.com/health/drugs/tabrecta-side-effects)

**Tolvaptan (Samsca / Jynarque)**
- Price: [Drugs.com price guide](https://www.drugs.com/price-guide/tolvaptan), [Jynarque copay assistance](https://www.jynarque.com/copay-assistance.html)
- Black box + side effects: [Jynarque safety info](https://www.jynarque.com/important-safety-information), [Mayo Clinic](https://www.mayoclinic.org/drugs-supplements/tolvaptan-oral-route/description/drg-20073109), [Medscape](https://reference.medscape.com/drug/samsca-jynarque-tolvaptan-999103)

**Olaparib (Lynparza)**
- Price: [Drugs.com price guide](https://www.drugs.com/price-guide/lynparza), [GoodRx](https://www.goodrx.com/lynparza/what-is)
- Black box + side effects: [Lynparza official side-effects page](https://www.lynparza.com/side-effects.html), [WebMD](https://www.webmd.com/drugs/2/drug-167493-1856/lynparza-oral/olaparib-tablet-oral/details), [MedicalNewsToday](https://www.medicalnewstoday.com/articles/lynparza)

## Bottom line

Every one of the top 10 hits is an expensive specialty, oncology, or
rare-disease drug — the cheapest (dihydroergotamine, generic, per-dose
pricing in the low hundreds of dollars) is still an outlier against a
field where most others run **$8,000–19,000+ per month** in the US, and
two carry FDA black-box warnings (tolvaptan: fatal liver injury, REMS-
restricted; olaparib: MDS/AML). That's close to the opposite of what this
project is looking for — the entire case for investigating visceral
leishmaniasis in the first place was that *no existing option* is cheap,
safe, **and** easy to administer all at once, and most of this list would
fail that bar even before asking whether it works.

**Dihydroergotamine is the one partial exception**: real generics exist,
per-dose cost is far below the rest of the list, and it has decades of
real-world safety data with a well-characterized (if serious in rare
cases) risk profile, rather than a monitoring-heavy oncology-drug
profile. It's also the drug with the most cross-run consistency signal so
far (top hit in the smoke test as ergotamine; dihydroergotamine landed in
the top 10 of the full screen) — worth flagging as the most *practically*
interesting candidate on this list, independent of the fact that no prior
antiparasitic literature exists for it either way (see
`literature-check.md`).

## Scope note

Per project-wide scope rules: none of this is a treatment recommendation.
Pricing and safety data describe these drugs' *current, approved* uses —
none of it says anything about what dose, formulation, or safety profile
they would have if ever actually tested against *Leishmania* or PTR1. This
is context for judging practical repurposing feasibility, not a clinical
claim.
