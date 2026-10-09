# Extraction record — s12936_018_2285_6

- Extracted: 2026-10-09
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 24 · Genotype rows: 6 · Bioassays: 75 · Geno-pheno rows: 0

## Decisions

### Key Decisions & Extraction Notes

- **Surveys**: Split by sentinel site and year of collection (2013, 2014, 2015, 2016) to capture the finest temporal and spatial resolution.
- **Genotypes**: Genotype counts for Vgsc L1014F (L995F) in 2014 were read from Figure 2. The exact integer counts (RR, RS, SS) were mathematically resolved based on the printed sample sizes ($N$) and the visual stacked bar heights, yielding perfect integer fits:
  - Kabondo ($N=132$): RR=103, RS=22, SS=7
  - Lodja ($N=86$): RR=0, RS=2, SS=84
  - Kingasani ($N=43$): RR=25, RS=14, SS=4
  - Mikalayi ($N=60$): RR=9, RS=27, SS=24
  - Kapolowe ($N=18$): RR=0, RS=2, SS=16
  - Tshikaji ($N=39$): RR=25, RS=10, SS=4
- **Bioassays**: Extracted from Table 2 (standard susceptibility tests) and Table 3 (synergist bioassays). Since only percentage mortalities were printed, `dead_alive_printed` was set to `false` and the counts (`n_dead`, `n_alive`) were left `null` to avoid back-calculation, while `n_exposed` was set to 100 (or 80 where marked with an asterisk in Table 2).
