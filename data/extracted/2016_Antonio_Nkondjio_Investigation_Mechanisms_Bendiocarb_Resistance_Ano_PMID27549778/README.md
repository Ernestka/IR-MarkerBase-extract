# Extraction record — 2016_Antonio_Nkondjio_Investigation_Mechanisms_Bendiocarb_Resistance_Ano_PMID27549778

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 25 · Genotype rows: 1 · Bioassays: 27 · Geno-pheno rows: 0

## Decisions

### Survey and Bioassay Splitting
- **Bendiocarb Bioassays**: Figure 1 presents monthly bendiocarb (0.1%) susceptibility tests for three breeding habitat classifications in Yaoundé: cultivated (13 time points), polluted (5 time points), and non-polluted (4 time points). Following Rule 7, these finest temporal-resolution tests were extracted rather than the habitat-level pooled summaries presented in Table 1, avoiding double counting. Dead counts were not printed on Figure 1, so `dead_alive_printed = false`, `n_dead = null`, and `n_alive = null` with percentages recorded as printed in `reported_mortality_pct`.
- Note on slight count discrepancy: In Figure 1, the sum of sample sizes for cultivated sites is 1476, whereas Table 1 reports 1428 tested for cultivated sites. For polluted (361) and unpolluted (438), Figure 1 totals match Table 1 exactly.
- **Other Insecticide Bioassays**: Table 2 presents susceptibility tests for cultivated mosquitoes from Nkolondom, Yaoundé, against DDT (4%), permethrin (0.75%), deltamethrin (0.05%), and malathion (4%). Tested and dead counts are literally printed in Table 2, so `dead_alive_printed = true`, `n_dead` is recorded, and `n_alive` is left null. The laboratory susceptible strain Kisumu in Table 2 was excluded per Rule 5.
- **Synergist Bioassay**: A synergist test using 4% PBO pre-exposure followed by 0.1% bendiocarb in 2013 cultivated mosquitoes is reported in the text (n=184, 100% mortality).

### Genotyping and Genotype-Phenotype Data
- **Ace-1 G119S**: A total of 392 An. gambiae s.l. specimens including survivors, dead, and unexposed controls were screened for the Ace-1 G119S mutation using TaqMan assays. The paper reports: 'None were detected carrying the Ace-1R mutation.' (0 RR, 0 RS, 392 SS). Because the paper does not break down the sample sizes by bioassay outcome (survivors vs dead vs controls), this result cannot be split into `geno_pheno` rows without guessing sample sizes. Therefore, per extraction guidelines, it is placed in `genotypes` under the Yaoundé collection survey (2010–2013).
- **Other Markers**: The paper investigates metabolic mechanisms using whole-genome microarray expression and qRT-PCR validation (highlighting cyp6z3, cyp6z1, cyp12f2, cyp6m3, cyp6p4, etc.); these are mRNA transcription level measurements rather than DNA target-site mutations, so no other target markers apply.
