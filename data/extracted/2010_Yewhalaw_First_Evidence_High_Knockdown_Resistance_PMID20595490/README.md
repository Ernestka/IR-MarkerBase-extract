# Extraction record — 2010_Yewhalaw_First_Evidence_High_Knockdown_Resistance_PMID20595490

- Extracted: 2026-10-24
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling Periods:**
   - Genotype testing was conducted on Anopheles arabiensis collected between September and October 2008. Results are provided at the finest spatial resolution available, splitting the 15 study villages into 7 'Low-risk' and 8 'High-risk' villages around the Gilgel-Gibe hydroelectric dam.
   - WHO bioassay testing was performed on mosquitoes collected separately in August 2009. A separate survey record was created for this 2009 collection of wild-caught adult An. gambiae s.l.

2. **Genotypes:**
   - Target markers evaluated: Vgsc L1014F (West African kdr) and Vgsc L1014S (East African kdr).
   - Standard genotype counts (RR, RS, SS) and sample sizes were extracted directly from Table 1 for both low-risk and high-risk village groups. L1014S was confirmed absent across all tested samples (240 total, 117 low-risk, 123 high-risk).
   - Overall summary totals from Table 1 were omitted to avoid double-counting per Rule 7.

3. **Bioassays & Geno-Pheno Linkage:**
   - Diagnostic dose WHO tube bioassays were recorded for DDT 4%, permethrin 0.75%, and deltamethrin 0.05% from Table 2.
   - `dead_alive_printed` was set to `false` and counts left null because only percentage mortalities were reported alongside total exposed numbers.
   - No genotype-phenotype data was available as bioassay survivors/dead were not genotyped.
