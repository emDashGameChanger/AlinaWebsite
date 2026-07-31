# Pricing and safety profile of the top 10 CYP51 hits

Date: 2026-07-30
Scope: same top 10 as `literature-check.md`. Conivaptan, nilotinib,
rimegepant, and eltrombopag are repeat hits already profiled in
`../full-1E92-PTR1-screen/pricing-safety-profile.md` and
`../full-2YAU-TR-screen/pricing-safety-profile.md` — not re-priced here,
see those files.

## Summary table (new drugs only)

| Drug | Current approved use | Approx. US price | Key safety concerns |
|---|---|---|---|
| Digitoxin | Heart failure, arrhythmia (historically) | **Not commercially available in the US** — withdrawn from the market; digoxin (its still-marketed cousin) runs ~$24+/month generic | Narrow therapeutic index, cardiac glycoside toxicity; N/A for current US prescribing |
| Dutasteride (Avodart) | Benign prostatic hyperplasia | ~$8-40/month generic; $350-450 brand | Sexual dysfunction, gynecomastia — no black box, comparatively mild |
| Irinotecan (Camptosar) | Colorectal/pancreatic cancer chemotherapy | ~$11/2 mL vial, generic available | Severe diarrhea, bone-marrow suppression/infection risk — IV chemo, requires infusion-center administration |
| Vibegron (Gemtesa) | Overactive bladder | ~$500-700/month, no generic; ~$95/month w/ copay card | Urinary retention (rare); mostly mild GI/UTI-type side effects |
| Ubrogepant (Ubrelvy) | Acute migraine | ~$1,100-1,450/10 tablets, no generic | Hypersensitivity reactions; capped at 8 uses/month |
| Tepotinib (Tepmetko) | MET exon 14-mutant NSCLC | ~$9,340-12,900/month | Interstitial lung disease/pneumonitis, hepatotoxicity, pancreatitis |

## Per-drug sources

**Digitoxin**
- Availability: [Davis's Drug Guide](https://www.drugguide.com/ddo/view/Davis-Drug-Guide/109117/all/digitoxin), [ScienceDirect overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/digitoxin)
- Digoxin price (as the practical modern proxy): [GoodRx](https://www.goodrx.com/digoxin)

**Dutasteride (Avodart)**
- Price: [GoodRx](https://www.goodrx.com/dutasteride), [MedicalNewsToday](https://www.medicalnewstoday.com/articles/drugs-dutasteride-cost)
- Safety: [GoodRx](https://www.goodrx.com/dutasteride/what-is)

**Irinotecan (Camptosar)**
- Price: [GoodRx](https://www.goodrx.com/irinotecan), [Drugs.com price guide](https://www.drugs.com/price-guide/camptosar)
- Safety: [WebMD](https://www.webmd.com/drugs/2/drug-13700/irinotecan-intravenous/details)

**Vibegron (Gemtesa)**
- Price: [GoodRx](https://www.goodrx.com/gemtesa/gemtesa-cost-without-insurance), [Northwest Pharmacy](https://www.northwestpharmacy.com/special-features/speciality-medications/why-is-gemtesa-vibegron-so-expensive)
- Safety: [Gemtesa official safety info](https://www.gemtesa.com/overactive-bladder-treatment-safety/)

**Ubrogepant (Ubrelvy)**
- Price: [GoodRx](https://www.goodrx.com/ubrelvy/what-is), [SingleCare](https://www.singlecare.com/blog/ubrelvy-without-insurance/)
- Safety: [MedicalNewsToday](https://www.medicalnewstoday.com/articles/ubrelvy)

**Tepotinib (Tepmetko)**
- Price: [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK603316/), [Drugs.com price guide](https://www.drugs.com/price-guide/tepmetko)
- Safety: [RxList](https://www.rxlist.com/tepmetko-drug.htm), [WebMD](https://www.webmd.com/drugs/2/drug-180798/tepmetko-oral/details)

## Bottom line

**Digitoxin is a real letdown on the practicality axis, despite being both
the single best docking score of the whole project (-13.0 kcal/mol) and
the strongest literature precedent found so far** (confirmed *L. infantum*
activity, see `literature-check.md`) — it's simply not something that can
be prescribed in the US today. Its still-marketed cousin digoxin is cheap
and widely available, but digoxin wasn't the drug that scored well here or
the drug tested in the antileishmanial literature — it would need its own
independent check (docking + literature) before leaning on it as a
substitute, not an assumption that it inherits digitoxin's results.

**Dutasteride is the best practical candidate on this list**: cheap
generic (~$8-40/month), no black box, decades of real-world safety data,
and — unlike almost everything else across all three screens so far — a
comparatively mild side-effect profile (sexual/hormonal effects, not organ
toxicity). No prior antiparasitic literature, so it's a genuinely novel
hypothesis rather than a rediscovery, and it's mechanistically the most
plausible novel hit here given it's itself a steroid-pathway inhibitor.

Irinotecan is inexpensive per unit but is IV chemotherapy requiring
infusion-center administration and carries real hematologic/GI toxicity at
approved doses — "cheap" doesn't translate to "easy to administer" here.
The rest (vibegron, ubrogepant, tepotinib) follow the now-familiar
pattern: real but non-trivial-to-large expense, none catastrophically
unsafe except tepotinib (organ toxicity warnings consistent with the
oncology drugs seen throughout this project).

## Scope note

Per project-wide scope rules: none of this is a treatment recommendation.
