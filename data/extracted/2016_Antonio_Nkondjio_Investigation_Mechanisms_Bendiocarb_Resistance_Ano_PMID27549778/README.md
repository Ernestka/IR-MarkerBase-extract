# Extraction record — 2016_Antonio_Nkondjio_Investigation_Mechanisms_Bendiocarb_Resistance_Ano_PMID27549778

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 25 · Genotype rows: 1 · Bioassays: 27 · Geno-pheno rows: 0

## Decisions

### Extraction Decisions

1. **Surveys & Resolution:**
   - Mosquitoes were collected as larvae across three breeding habitat types (cultivated, polluted, non-polluted) in Yaoundé, Cameroon, between October 2010 and December 2013.
   - Bioassay data are reported at monthly resolution per habitat type in Figure 1, and for specific insecticides in cultivated sites (Nkolondom) in Table 2. Individual survey records were defined for each month/habitat combination from Figure 1 and for the Nkolondom study sample in Table 2 to ensure maximum spatiotemporal resolution without double counting.
   - A separate survey record (`2016_antonio_yaounde_2010_2013_genotype`) was created for the 392 specimens genotyped for Ace-1 G119S, as the genotype results are reported pooled across the overall collection period.

2. **Genotyping Data:**
   - Only Ace-1 G119S (G280S) was genotyped in this study (by TaqMan PCR). Among 392 tested mosquitoes (comprising bendiocarb bioassay survivors, dead, and unexposed controls), zero carried the Ace-1R mutation (all 392 were SS).
   - Because subgroup sample sizes for survivors, dead, and controls were not individually specified for the genotyped cohort of 392 mosquitoes, the results are recorded under `genotypes` as a overall population sample rather than split into `geno_pheno`.

3. **Bioassays:**
   - Bioassays from Figure 1 report `% mortality (n_exposed)`. Per rule 2, `dead_alive_printed` is set to `false`, and `n_dead` and `n_alive` are left `null` with `reported_mortality_pct` recorded as printed.
   - Table 2 reports exact numbers tested and dead for DDT 4%, permethrin 0.75%, deltamethrin 0.05%, and malathion 4%. For these, `dead_alive_printed` is set to `true` and `n_alive` is calculated as `n_exposed - n_dead`.
   - PBO pre-exposure bioassay (4% PBO 1h + 0.1% bendiocarb 1h, 100% mortality, n=184) reported on page 4 is included as a synergist bioassay.
   - Laboratory reference strain (Kisumu) bioassays in Table 2 were excluded per rule 5.
