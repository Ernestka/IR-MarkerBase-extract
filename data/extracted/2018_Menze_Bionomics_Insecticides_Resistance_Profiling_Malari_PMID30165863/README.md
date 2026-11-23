# Extraction record — 2018_Menze_Bionomics_Insecticides_Resistance_Profiling_Malari_PMID30165863

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 5 · Bioassays: 17 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling**: Mosquitoes were collected in January 2017 at Mibellon village, Adamawa region, Cameroon. Field collections yielded 584 *An. funestus* group (all confirmed as *An. funestus* s.s.) and 138 *An. gambiae* s.l. (all confirmed as *An. gambiae* s.s., S form). Two separate survey records were established for each molecular species.
2. **Coordinates**: The text reports coordinates as `6°46′N, 11°70′E` on Page 2. Converted 6°46'N to decimal degrees (6.766667 N). Printed longitude `11°70′E` was converted as printed (11 + 70/60 = 12.166667 E).
3. **Genotypes**: Marker names were extracted exactly as printed in text:
   - *An. funestus s.s.*: `GSTe2 L119F` (N=110: 7 RR, 48 RS, 55 SS) and `RDL A296S` (N=92: 3 RR, 12 RS, 75 SS).
   - *An. gambiae s.s.*: `kdr L1014F` (N=72: 22 RR, 48 RS, 2 SS), `kdr L1014S` (N=76: 0 RR, 3 RS, 73 SS), and `ace-1 G119S` (N=50: 0 RR, 0 RS, 50 SS).
4. **Inconsistencies**: For `RDL A296S` in *An. funestus s.s.*, the reported genotype counts (3 RR + 12 RS + 75 SS = 90) sum to 90, whereas total N is reported as 92. The printed SS percentage (83.7%) corresponds to 77/92 (83.695%), indicating that 75 is likely a typographical error for 77. The printed values were retained per Rule 8 and documented in `inconsistency_note`.
5. **Bioassays**: WHO tube bioassays were conducted on F1 adults (females and males reported separately). Bioassays for female mosquitoes were extracted with reported mortality percentages. Because sample sizes for individual bioassay tests were not explicitly printed (only overall totals of 2700 F1 *An. funestus* and 971 F1 *An. gambiae* across all tests), count fields (`n_exposed`, `n_dead`, `n_alive`) were left null per Rule 2. Bed net cone assays were excluded as they test net formulations rather than standard active ingredient concentrations.
6. **Geno-Pheno Data**: No phenotype-split genotype data (genotypes split by survivor/dead status) were reported.

## Validator warnings

- genotype #2 (2018_Menze_mibellon_2017_fun, RDL A296S): inconsistent in the paper (values kept as printed) — RR+RS+SS = 90 (3+12+75) but N = 92; printed percentage for SS (83.7%) corresponds to 77/92, suggesting SS = 75 is a typo for 77.
- genotype #2 (2018_Menze_mibellon_2017_fun, RDL A296S): RR+RS+SS = 3+12+75 = 90 but n_genotyped = 92
