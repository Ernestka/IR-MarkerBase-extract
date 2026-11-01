# Extraction record — 2014_Djegbe_Molecular_Characterization_DDT_Resistance_Anophele_PMID25175167

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 21 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Resolution:**
   - Surveys were split by site (Cotonou, Malanville, Tori-Bossito, Bohicon), collection year (2010, 2011), and molecular form (M-form, S-form) as reported in Table 2.
   - Collections occurred between December 2010 and December 2011 from wild larval collections reared to adult (F0 generation).
   - `n_genotyped` for each target marker record was calculated directly by dividing `N (alleles)` printed in Table 2 by 2.

2. **Target Markers extracted:**
   - `Vgsc L995F` (reported as `1014 F` / `L1014F` in the text and Table 2).
   - `Vgsc N1570Y` (reported as `1575Y` / `N1575Y` in the text and Table 2).
   - `Vgsc L995S` (reported as `1014S` / `L1014S` on page 6 text, detected in 1 specimen of S-form in Bohicon 2011).
   - Candidate metabolic genes (GSTE2, GSTD3, CYP6P3, CYP6M2) analyzed by qPCR differential expression were not target site mutation markers and were not extracted into `genotypes`.

3. **Genotypes vs Allele Frequencies:**
   - Table 2 reports allele frequencies (`reported_allele_freq`) and total alleles (`N (alleles)`), but does not report individual genotype counts (RR, RS, SS). Therefore, RR, RS, and SS counts were left as `null` following Rule 2.
   - For `L1014S`, the text specifies 1 heterozygous specimen (`1014F/1014S`) in Bohicon 2011 S-form, recorded with `n_carriers = 1` and `n_genotyped = 74`.

4. **Bioassays & Geno-Pheno:**
   - 2010 bioassays mentioned in the text (1% and 6% mortality in Malanville and Cotonou) are secondary citations from Djegbe et al. 2011 (reference [18]) and were omitted.
   - 2011 bioassays evaluated DDT 4% across multiple exposure times (30–300 min) and reported 0% mortality in all tests. Exact sample sizes per test point were not printed (described as batches of 20–25), and bioassays were conducted on wild-reared F0 adults prior to molecular species identification. Bioassays were omitted to avoid guessing counts or unseparated species assignments.
   - No phenotype-split genotype data (`geno_pheno`) were reported in the paper.

## Validator warnings

- genotype #1 (2014_Djegbe_cotonou_2010_m, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2014_Djegbe_cotonou_2010_m, kdr N1575Y): frequency only (no raw counts)
- genotype #3 (2014_Djegbe_malanville_2010_m, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2014_Djegbe_malanville_2010_m, kdr N1575Y): frequency only (no raw counts)
- genotype #5 (2014_Djegbe_toribossito_2010_m, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2014_Djegbe_toribossito_2010_m, kdr N1575Y): frequency only (no raw counts)
- genotype #7 (2014_Djegbe_bohicon_2010_m, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2014_Djegbe_bohicon_2010_m, kdr N1575Y): frequency only (no raw counts)
- genotype #9 (2014_Djegbe_cotonou_2011_m, kdr L1014F): frequency only (no raw counts)
- genotype #10 (2014_Djegbe_cotonou_2011_m, kdr N1575Y): frequency only (no raw counts)
- genotype #11 (2014_Djegbe_toribossito_2011_m, kdr L1014F): frequency only (no raw counts)
- genotype #12 (2014_Djegbe_toribossito_2011_m, kdr N1575Y): frequency only (no raw counts)
- genotype #13 (2014_Djegbe_bohicon_2010_s, kdr L1014F): frequency only (no raw counts)
- genotype #14 (2014_Djegbe_bohicon_2010_s, kdr N1575Y): frequency only (no raw counts)
- genotype #15 (2014_Djegbe_toribossito_2010_s, kdr L1014F): frequency only (no raw counts)
- genotype #16 (2014_Djegbe_toribossito_2010_s, kdr N1575Y): frequency only (no raw counts)
- genotype #17 (2014_Djegbe_bohicon_2011_s, kdr L1014F): frequency only (no raw counts)
- genotype #18 (2014_Djegbe_bohicon_2011_s, kdr N1575Y): frequency only (no raw counts)
- genotype #20 (2014_Djegbe_toribossito_2011_s, kdr L1014F): frequency only (no raw counts)
- genotype #21 (2014_Djegbe_toribossito_2011_s, kdr N1575Y): frequency only (no raw counts)
