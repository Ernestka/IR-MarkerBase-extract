# Extraction record — 2014_Kabula_Co_Occurrence_Distribution_East_L1014S_PMID24386946

- Extracted: 2026-11-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 24 · Genotype rows: 38 · Bioassays: 4 · Geno-pheno rows: 4

## Decisions

1. **Surveys & Resolution**: Created 19 site-by-species surveys for genotype records based on Tables 2 and 3, which present genotype counts for *An. gambiae s.s.* and *An. arabiensis* individually across 14 sentinel sites in Tanzania. Also created site-level *An. gambiae s.l.* surveys for bioassays and one countrywide *An. gambiae s.l.* survey (`2014_Kabula_tanzania_2011_sl`) for Table 4 pooled genotype-phenotype data.
2. **Population Type**: Set to `wild_reared` for Tabora/Uyui, Lushoto, and Muleba as larvae were collected and reared to adults per text (page 3); set to `wild_adult` for all other sites (indoor-resting adult catches).
3. **Genotype Data**: Extracted `kdr` gene markers `L1014S` and `L1014F` from Tables 2 and 3 for all 19 site x molecular species combinations. All genotype counts (RR, RS, SS) sum exactly to reported N.
4. **Bioassays**: Bioassays were extracted for the 4 sites (Muheza, Arumeru, Muleba, Dar es Salaam/Ilala) where explicit 24-h mortality percentages were reported in the text. Bioassays for Magu, Babati, Moshi, and Dodoma were excluded because they were adapted from Kabula et al. (2013) as stated in the text and Figure 4 legend.
5. **Geno-Pheno Data**: Table 4 provides genotype counts split by bioassay survivors (resistant, n=85) and dead (susceptible, n=265) pooled across all sites for lambdacyhalothrin. These were extracted into `geno_pheno` with `bioassay_id = null` and `insecticide = 'lambdacyhalothrin'`.

## Validator warnings

- geno_pheno #1 (lambdacyhalothrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
- geno_pheno #2 (lambdacyhalothrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
- geno_pheno #3 (lambdacyhalothrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
- geno_pheno #4 (lambdacyhalothrin, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
