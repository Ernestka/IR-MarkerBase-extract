# Extraction record — 2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 8 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The paper evaluates Anopheles vector adaptation, feeding behavior, parity, and malaria transmission before and after universal LLIN implementation in July 2008 in Dielmo, Senegal (13°43'N, 16°24'W, coordinates converted to decimal 13.7167, -16.4).
- Mosquito collections spanned monthly catches from January 2006 to December 2011. A total of 14,292 Anopheles specimens were sampled by HLC (8,855 An. gambiae s.l. and 5,190 An. funestus). A random monthly subsample of 1,494 An. gambiae s.l. was molecularly identified and genotyped for kdr mutations (L1014F and L1014S).
- In the main text, kdr L1014F allele frequencies are reported across four distinct time periods: 2006–2008 (2.92%), 2009 (9.72%), 2010 (23.16%), and 2011 (30.86%). Consequently, four surveys were created corresponding to these time periods.

### Genotypes Extraction
- Exact counts (RR, RS, SS) by year and species were contained in supplementary File S1 (Table 2), which is external to the main text. Following extraction rules, raw counts were not back-calculated from reported percentages; count fields (rr, rs, ss, n_genotyped) are set to null, and reported proportions are captured in `reported_allele_freq`.
- The authors state: 'No Anopheles specimen with L1014S kdr mutation was identified in the study.' This is captured with `reported_allele_freq` = 0.0 across all survey periods.

### Bioassays and Genotype-Phenotype
- No standard insecticide bioassays (e.g. WHO cylinder tests or CDC bottle bioassays) were performed in this study; the paper focuses on field behavior, parity, human blood index, and CSP sporozoite infection rates. Therefore, `bioassays` and `geno_pheno` arrays are empty.

## Validator warnings

- genotype #1 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2006_2008, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2006_2008, kdr L1014S): frequency only (no raw counts)
- genotype #3 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2009, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2009, kdr L1014S): frequency only (no raw counts)
- genotype #5 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2010, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2010, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2011, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2014_Ndiath_How_Malaria_Vector_Anopheles_Gambiae_PMID24892677_dielmo_2011, kdr L1014S): frequency only (no raw counts)
