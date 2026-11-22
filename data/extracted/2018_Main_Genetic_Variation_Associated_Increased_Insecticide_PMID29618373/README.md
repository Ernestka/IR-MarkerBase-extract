# Extraction record — 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373

- Extracted: 2026-11-22
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 2 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Target Markers & Gene Mapping**:
   - Renamed marker to `L1014F` under gene `Vgsc` as per target marker specifications for the kdr mutation in Malian An. coluzzii populations.
   - Genotype counts for kdr (wt/wt = SS, wt/kdr = RS, kdr/kdr = RR) were calculated directly from Figure 2 bar numbers across female and male F2 cross groups: females (38 SS, 16 RS, 1 RR under cyp-2; 38 SS, 21 RS, 4 RR under cyp-1/2) and males (42 SS, 33 RS, 7 RR under cyp-2; 33 SS, 13 RS under cyp-1). Summed totals across categories yield 151 SS, 83 RS, 12 RR out of 246 genotyped F2 mosquitoes.

2. **Surveys & Bioassays**:
   - Laboratory reference strains (1995 An. coluzzii MOPTI / MRA-763 and An. gambiae Pimperena / MRA-861) were excluded as reference controls per Rule 5.
   - Bioassays conducted on the 2014 An. coluzzii Selenkenyi colony (permethrin alone and PBO + permethrin) were extracted under survey `2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_selenkenyi_2014_col`.
   - Bioassays on individual F2 cross mosquitoes evaluated 60-minute knockdown/mobility status without 24-hour mortality counts by genotype class, so no `geno_pheno` records were created per Rule 8b.

## Validator warnings

- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_selenkenyi_2014_col: laboratory population — normally excluded
- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_f2_cross: laboratory population — normally excluded
- bioassay 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_selenkenyi_2014_col_permethrin: inconsistent in the paper (values kept as printed) — Page 4 paragraph 1 states 68% mortality after 24 h for 2014 An. coluzzii, while paragraph 2 states mortality increased from 67% (n = 43) to 98% (n = 53) in the PBO-treated group.
