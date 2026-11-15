# Extraction record — 2013_Okia_Bioefficacy_Long_Lasting_Insecticidal_Nets_PMID23634798

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 10 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Summary

1. **Surveys**: Mosquito collections took place in April and October 2011 in four districts of Uganda (Kanungu, Lira, Tororo, Wakiso). Mosquitoes were extracted at the finest spatial and species level available: four site-level surveys for *Anopheles gambiae s.s.* and one pooled country-level survey for *Anopheles arabiensis* (14 individuals genotyped total across sites).
2. **Markers**: Gene and marker names were extracted exactly as written (`kdr` / `L1014S` and `L1014F`).
   - For `L1014S`, Table 1 reports allele frequencies per site for *An. gambiae s.s.* without printing complete individual RR/RS/SS counts (except for Kanungu where text specifies 1 RR). Genotype frequencies were entered as reported allele frequencies without back-calculating genotype counts.
   - For `L1014F`, text states no L1014F mutations were observed in any species, so RR=0, RS=0, SS=N, reported_allele_freq=0.0.
3. **Bioassays**: Standard WHO tube susceptibility tests (permethrin 0.75% and deltamethrin 0.05%) from Table 2 were extracted. `dead_alive_printed` was set to `false` because only number exposed (100) and 24 h mortality (%) are printed in the table. Kisumu laboratory reference strain bioassays were excluded as controls per Rule 5. Net bioefficacy tests (cone and wireball assays on manufactured LLIN products) were not included as standard susceptibility bioassays.
4. **Geno-Pheno**: No phenotype-split genotyping (survivors vs dead) was reported in the paper.

## Validator warnings

- genotype #3 (2013_Okia_Bioefficacy_Long_Lasting_Insecticidal_Nets_PMID23634798_lira_gambiae, kdr L1014S): frequency only (no raw counts)
- genotype #5 (2013_Okia_Bioefficacy_Long_Lasting_Insecticidal_Nets_PMID23634798_tororo_gambiae, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2013_Okia_Bioefficacy_Long_Lasting_Insecticidal_Nets_PMID23634798_wakiso_gambiae, kdr L1014S): frequency only (no raw counts)
