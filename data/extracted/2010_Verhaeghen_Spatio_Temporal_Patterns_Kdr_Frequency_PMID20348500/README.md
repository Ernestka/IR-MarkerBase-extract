# Extraction record — 2010_Verhaeghen_Spatio_Temporal_Patterns_Kdr_Frequency_PMID20348500

- Extracted: 2026-11-12
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 12 · Genotype rows: 24 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Key Decisions

1. **Surveys**: Split by district and study period as presented in Table 2 for *Anopheles gambiae s.s.*:
   - **2001-2002 Longitudinal Study**: 11 surveys conducted from June 2001 to May 2002 across seven sentinel districts (Apac, Arua, Jinja, Kanungu, Kyenjojo, Mubende, Tororo). Confirmed as *An. gambiae s.s.* S-molecular form.
   - **2004-2006 WHO Bioassay Collections**: Samples genotyped by district (Jinja, Kanungu, Kyenjojo, Mubende, Tororo).

2. **Genotypes (Table 2)**:
   - Extracted from Table 2 for L1014S and L1014F. In accordance with Rule 2, because only the allele frequencies (`reported_allele_freq`) and number tested (`n_genotyped`) are reported (no raw genotype class counts RR, RS, SS are printed), the count fields (`rr`, `rs`, `ss`, `resistant_allele_count`) are left null to prevent back-calculating from percentages.

3. **Genotype-Phenotype Data (Figure 3)**:
   - Figure 3 presents the proportions of RR, RS, and SS genotypes among live and dead mosquitoes exposed to DDT, permethrin, and deltamethrin (pooled nationally across Uganda from 2004 to 2006). Sample sizes (n) are provided, but genotype percentages or counts are only shown as a stacked bar chart without printed numerical counts or values. Following Rule 2 (never back-calculate counts from percentages/figures) and Rule 8 (extract only what is printed), empty records without genotype counts or reported allele frequencies were omitted from `geno_pheno`.

## Validator warnings

- genotype #1 (2010_Verhaeghen_apac_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #2 (2010_Verhaeghen_apac_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #3 (2010_Verhaeghen_arua_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #4 (2010_Verhaeghen_arua_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #5 (2010_Verhaeghen_jinja_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #6 (2010_Verhaeghen_jinja_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #7 (2010_Verhaeghen_kanungu_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #8 (2010_Verhaeghen_kanungu_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #9 (2010_Verhaeghen_kyenjojo_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #10 (2010_Verhaeghen_kyenjojo_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #11 (2010_Verhaeghen_mubende_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #12 (2010_Verhaeghen_mubende_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #13 (2010_Verhaeghen_tororo_2001_2002_gams, kdr L1014S): frequency only (no raw counts)
- genotype #14 (2010_Verhaeghen_tororo_2001_2002_gams, kdr L1014F): frequency only (no raw counts)
- genotype #15 (2010_Verhaeghen_jinja_2004_2006_gams, kdr L1014S): frequency only (no raw counts)
- genotype #16 (2010_Verhaeghen_jinja_2004_2006_gams, kdr L1014F): frequency only (no raw counts)
- genotype #17 (2010_Verhaeghen_kanungu_2004_2006_gams, kdr L1014S): frequency only (no raw counts)
- genotype #18 (2010_Verhaeghen_kanungu_2004_2006_gams, kdr L1014F): frequency only (no raw counts)
- genotype #19 (2010_Verhaeghen_kyenjojo_2004_2006_gams, kdr L1014S): frequency only (no raw counts)
- genotype #20 (2010_Verhaeghen_kyenjojo_2004_2006_gams, kdr L1014F): frequency only (no raw counts)
- genotype #21 (2010_Verhaeghen_mubende_2004_2006_gams, kdr L1014S): frequency only (no raw counts)
- genotype #22 (2010_Verhaeghen_mubende_2004_2006_gams, kdr L1014F): frequency only (no raw counts)
- genotype #23 (2010_Verhaeghen_tororo_2004_2006_gams, kdr L1014S): frequency only (no raw counts)
- genotype #24 (2010_Verhaeghen_tororo_2004_2006_gams, kdr L1014F): frequency only (no raw counts)
