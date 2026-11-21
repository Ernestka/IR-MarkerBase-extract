# Extraction record — 2018_Ketoh_Efficacy_Two_PBO_Long_Lasting_PMID29995894

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 2 · Bioassays: 11 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Surveys**:
   - Mosquitoes were collected as larvae around Kolokopé, Togo (07°47'59"N, 01°18'00"E) between June and December 2013 and reared to adults in the field laboratory.
   - Three surveys were defined to match the resolution of species reported:
     - `..._kolokope_2013_sl` for WHO susceptibility tube tests performed on *An. gambiae s.l.*.
     - `..._kolokope_2013_col` for *An. coluzzii* kdr genotype counts.
     - `..._kolokope_2013_gam` for *An. gambiae s.s.* kdr genotype counts.

2. **Genotypes**:
   - *kdr* L1014F (target marker Vgsc L995F) exact genotype counts (RR, RS, SS) were extracted from Table 2 for *An. coluzzii* (RR=83, RS=1, SS=49, Total=133) and *An. gambiae s.s.* (RR=131, RS=1, SS=5, Total=137).
   - Genotype frequencies reported in Table 2 (0.62 for *An. coluzzii* and 0.96 for *An. gambiae s.s.*) match the raw count proportions.

3. **Bioassays**:
   - 11 WHO susceptibility tube assays (including PBO synergist assays) from Table 1 were extracted.
   - `dead_alive_printed` is set to `false` because Table 1 reports total exposed `N` and `Mortality 24hrs (%)` rather than exact counts of dead/alive mosquitoes.
   - Bioassays on Kisumu (laboratory reference strain) were excluded per guidelines.
   - WHO cone bioassays on experimental hut net pieces (Table 4) were excluded as they represent bed net bioefficacy evaluations rather than standard discriminating-dose susceptibility bioassays.

4. **Geno-Pheno**:
   - No bioassay survivor/dead genotype breakdowns were presented in the text or tables.
