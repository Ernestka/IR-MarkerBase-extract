# Extraction record — 2012_Jones_Footprints_Positive_Selection_Associated_Mutation_PMID22493253

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 15 · Genotype rows: 29 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Data Extraction Decisions

### Markers Extracted
- `L1014F` (Vgsc L995F): reported in Table 1 for all annual field collections.
- `N1575Y` (Vgsc N1570Y): reported in Table 1 for all annual field collections.
- `I1532T` (Vgsc I1527T): reported in text for Goundry M form (3 of 40 heterozygotes, frequency 0.038).

### Surveys & Population Structure
- Surveys are grouped by country/site, year, and molecular form/species matching Table 1 (Burkina Faso annual collections 2008-2010 for M form, S form, and An. arabiensis; Benin 2011; Yaoundé, Cameroon 2006; Accra, Ghana 2006; Goundry village M form for I1532T).
- In 2012 taxonomy, M form = *Anopheles coluzzii*, S form = *Anopheles gambiae* s.s.

### Genotype vs Allele Frequency Counts
- Table 1 reports allele frequencies (`(f)`) and number of alleles (`n (alleles)`), but not raw diploid genotype counts (RR, RS, SS). Following Rule 2, allele frequencies are placed in `reported_allele_freq`, and diploid genotype count fields are left `null` (no back-calculation from frequencies).
- For `I1532T` in Goundry M form, raw counts are explicitly given in text (3 of 40 C/T heterozygotes -> `n_genotyped` = 40, `rr` = 0, `rs` = 3, `ss` = 37).

### Bioassays & Geno-Pheno
- Detailed population mortality numbers for WHO bioassays were provided in Table S3 (supplementary file), which is not part of the main text/figures OCR. Therefore, no `bioassays` records were generated.
- Figure 5 reports haplotypic association test odds ratios (ORs) between 1014-1575 haplotypes across phenotyped mosquitoes, but does not print raw genotype/allele counts or frequencies per phenotype group (alive vs dead). Thus, no `geno_pheno` records were created.

## Validator warnings

- genotype #1 (2012_Jones_bf_2008_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #2 (2012_Jones_bf_2008_m, VGSC L1014F): frequency only (no raw counts)
- genotype #3 (2012_Jones_bf_2009_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #4 (2012_Jones_bf_2009_m, VGSC L1014F): frequency only (no raw counts)
- genotype #5 (2012_Jones_bf_2010_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #6 (2012_Jones_bf_2010_m, VGSC L1014F): frequency only (no raw counts)
- genotype #7 (2012_Jones_benin_2011_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #8 (2012_Jones_benin_2011_m, VGSC L1014F): frequency only (no raw counts)
- genotype #9 (2012_Jones_cameroon_2006_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #10 (2012_Jones_cameroon_2006_m, VGSC L1014F): frequency only (no raw counts)
- genotype #11 (2012_Jones_ghana_2006_m, VGSC N1575Y): frequency only (no raw counts)
- genotype #12 (2012_Jones_ghana_2006_m, VGSC L1014F): frequency only (no raw counts)
- genotype #13 (2012_Jones_bf_2008_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #14 (2012_Jones_bf_2008_s, VGSC L1014F): frequency only (no raw counts)
- genotype #15 (2012_Jones_bf_2009_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #16 (2012_Jones_bf_2009_s, VGSC L1014F): frequency only (no raw counts)
- genotype #17 (2012_Jones_bf_2010_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #18 (2012_Jones_bf_2010_s, VGSC L1014F): frequency only (no raw counts)
- genotype #19 (2012_Jones_benin_2011_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #20 (2012_Jones_benin_2011_s, VGSC L1014F): frequency only (no raw counts)
- genotype #21 (2012_Jones_cameroon_2006_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #22 (2012_Jones_cameroon_2006_s, VGSC L1014F): frequency only (no raw counts)
- genotype #23 (2012_Jones_ghana_2006_s, VGSC N1575Y): frequency only (no raw counts)
- genotype #24 (2012_Jones_ghana_2006_s, VGSC L1014F): frequency only (no raw counts)
- genotype #25 (2012_Jones_bf_2009_arab, VGSC N1575Y): frequency only (no raw counts)
- genotype #26 (2012_Jones_bf_2009_arab, VGSC L1014F): frequency only (no raw counts)
- genotype #27 (2012_Jones_bf_2010_arab, VGSC N1575Y): frequency only (no raw counts)
- genotype #28 (2012_Jones_bf_2010_arab, VGSC L1014F): frequency only (no raw counts)
