# Extraction record — 2017_Abeku_Insecticide_Resistance_Patterns_Uganda_Effect_PMID28427415

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 18 · Bioassays: 29 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Survey Breakdown**: Surveys were split by district and molecularly identified species (`Anopheles gambiae s.s.` and `Anopheles arabiensis`) as reported in Table 1 and Table 2.
2. **Target Markers Extracted**: 
   - `kdr L1014S` (target marker `Vgsc L995S`): Complete genotype counts (SS, RS, RR) were extracted from Table 2 for 9 districts for both species.
3. **Markers Excluded / Not Extracted**: 
   - `kdr L1014F`: Text on page 6 states 56 *An. arabiensis* from Bugiri, Mayuge, and Soroti were all SS, and 21 *An. gambiae s.s.* from other districts had 2 RR, 1 RS, rest SS. These were not extracted into individual genotype records because they are aggregated across multiple districts.
   - `ace-1 G119S`: Text on page 7 states 449 *An. gambiae s.s.* and 154 *An. arabiensis* were all SS. These are pooled countrywide/across districts and thus excluded per Rule 7.
4. **Bioassays**: Extracted from Table 1 for all tests with N >= 20. Bioassays report n exposed and % mortality, so `dead_alive_printed` is set to `false` and `n_dead` and `n_alive` are left null per Rule 2.
5. **Geno-Pheno Data**: The paper discusses regression analysis comparing indoor adult vs larval collections for *kdr* homozygosity, but does not report raw genotype counts separated by bioassay survivors vs dead mosquitoes for individual bioassays. Thus, `geno_pheno` is left empty.
