# Extraction record — 2011_Ngufor_Combining_Indoor_Residual_Spraying_Chlorfenapyr_PMID22087506

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 5 · Geno-pheno rows: 8

## Decisions

### Data Extraction Decisions
- **Surveys**: Two surveys were created: one for baseline field-collected larvae reared to adults (Akron, 2010) and one for adult mosquitoes collected in experimental huts (Akron, June-September 2010).
- **Marker Identification**: The paper assesses the kdr locus using Martinez-Torres et al. (1998) PCR assay, which tests for Vgsc L1014F (L995F). `gene` is specified as 'kdr' and `marker` as 'L1014F'.
- **Bioassays**: Extracted from Table 1 for all insecticidal experimental hut treatments against *Anopheles gambiae*. Delayed 72-hour mortality was recorded.
- **Genotype-Phenotype**: Table 3 reports kdr allele counts out of total alleles scored for alive and dead mosquitoes across four experimental hut treatments. Sample sizes (`n`) are derived from total alleles divided by 2. For the 'Alive' group of Chlorfenapyr IRS + LLIN 80 holes, 25 total alleles is printed (yielding a non-integer count of 12.5 mosquitoes, so `n` is set to null).
- **Excluded Non-target Species**: Data for *Culex quinquefasciatus* (Table 2) were excluded as this schema targets African *Anopheles* vectors.

## Validator warnings

- genotype #1 (2011_Ngufor_Benin_Akron_2010_larvae, kdr L1014F): frequency only (no raw counts)
- bioassay 2011_Ngufor_Benin_Akron_2010_hut_cfp_llin_80h: computed mortality 91.5% differs from reported 82.3% (Abbott correction?)
- geno_pheno #3 (2011_Ngufor_Benin_Akron_2010_hut_cfp_llin_80h, kdr L1014F, alive): inconsistent in the paper (values kept as printed) — Total alleles printed as 25 (yielding non-integer 12.5 mosquitoes), so n is set to null.
- geno_pheno #7 (no insecticide, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #8 (no insecticide, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: none given)
