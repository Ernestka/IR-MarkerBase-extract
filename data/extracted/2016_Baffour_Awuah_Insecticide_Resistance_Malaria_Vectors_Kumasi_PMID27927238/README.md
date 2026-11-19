# Extraction record — 2016_Baffour_Awuah_Insecticide_Resistance_Malaria_Vectors_Kumasi_PMID27927238

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 3 · Bioassays: 10 · Geno-pheno rows: 0

## Decisions

### Survey and Sampling Structure
- Collections were conducted across six major open-spaced irrigated vegetable farms in the Asokwa submetropolis, Kumasi Metropolis, Ashanti Region, Ghana. Larvae and pupae were reared to adults in an insectary and pooled for WHO tube bioassays.
- Exact sampling dates were not reported in the text; ethics approval was obtained in 2014 (CHRPE/AP/343/14) and the manuscript was received in April 2016.
- Three surveys were configured:
  1. `..._asokwa_gasl`: Represents the pooled Anopheles gambiae s.l. population used for WHO tube susceptibility tests (N = 1,069) and the subset tested for ace-1 G119S (N = 450).
  2. `..._asokwa_gambiae_ss`: Molecularly identified An. gambiae s.s. (537 of 619 genotyped from pyrethroid and organochlorine exposures).
  3. `..._asokwa_coluzzii`: Molecularly identified An. coluzzii (82 of 619 genotyped from pyrethroid and organochlorine exposures).

### Bioassays
- Ten WHO diagnostic tube bioassays on field-collected mosquitoes are reported in Table 1 across four chemical classes: organophosphates (malathion 5%, pirimiphos-methyl 0.25%), carbamates (propoxur 0.1%, bendiocarb 0.1%), pyrethroids (cyfluthrin 0.15%, deltamethrin 0.05%, lambda-cyhalothrin 0.05%, permethrin 0.75%), and organochlorines (DDT 4%, dieldrin 4%).
- Susceptible Kisumu laboratory strain control assays in Table 1 were excluded per Rule 5.

### Genotype Data and Handling of Table 3
- Target markers assayed were Vgsc L1014F (West African kdr) by AS-PCR (Martinez-Torres et al. 1998) and ace-1 G119S by PCR-RFLP (Weill et al. 2003).
- kdr results are reported as 'kdr-resistant' and 'kdr-sensitive' without splitting into RR and RS classes. Therefore, resistant counts were assigned to `n_carriers`, sensitive counts to `ss`, and reported percentages to `reported_allele_freq`.
- Ace-1 G119S was negative in all 450 mosquitoes tested from carbamate and organophosphate assays (Page 5: 'Ace-1 mutation on the other hand was not detected among the female Anopheles mosquitoes subjected to organophosphates and carbamates.'). Thus, ss = 450, rr = 0, rs = 0, reported_allele_freq = 0.0.
- Table 3 breaks down kdr-resistant mosquitoes into alive and dead groups for each insecticide, but reports kdr-sensitive mosquitoes in a single column without phenotypic segregation. As a result, complete genotype counts or sample sizes per phenotype class cannot be obtained without back-calculating/subtracting from bioassay mortality totals (which is explicitly forbidden by Rule 2 and Rule 4b). Furthermore, the percentage columns printed in Table 3 represent complex, garbled cross-tabulation percentages rather than allele frequencies. Consequently, population-level genotype counts are extracted from Table 2 into `genotypes` to preserve complete, reconciled counts for each species, and Table 3 is omitted to prevent partial double counting and ungrounded derivation.
