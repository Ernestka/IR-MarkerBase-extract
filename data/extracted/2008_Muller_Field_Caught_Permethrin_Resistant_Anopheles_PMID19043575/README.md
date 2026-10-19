# Extraction record — 2008_Muller_Field_Caught_Permethrin_Resistant_Anopheles_PMID19043575

- Extracted: 2026-10-19
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 0 · Geno-pheno rows: 2

## Decisions

### Survey and Genotype Splitting
- Field collections were conducted in Dodowa, Ghana (05°52.67'N, 000°06.36'W; converted to decimal degrees: 5.877833, -0.106) between October and November 2006. Larvae were collected from natural breeding sites and reared to 3-day old adults.
- Two molecular species were identified among the 333 genotyped females (Table 2): S form (*An. gambiae s.s.*, N = 331) and M form (*An. coluzzii*, N = 2). Separate surveys were created for each.

### Genotype vs Geno-Pheno Assignment
- In Table 2, mosquitoes are reported in two groups: a control group (unexposed, silicone oil carrier only) of 172 individuals (170 S form, 2 M form) and a selected group of 161 individuals (all S form) that survived 0.75% permethrin exposure at the LT50 (122 min).
- Following Rule 6, the control group represents the population baseline and is placed in `genotypes`. The permethrin-selected group represents bioassay survivors and is placed in `geno_pheno` (`phenotype_group: 'alive'`, `insecticide: 'permethrin'`). Dead mosquitoes were not genotyped due to post-mortem RNA degradation concerns, as explained by the authors.

### Multi-Allelic Codon Accounting (Rule 4b)
- In the S form control group (N = 170): 157 RW/RW (1014F/1014F), 10 RW/+ (1014F/L), 3 RW/RE (1014F/1014S), and 0 wild-type (+/+; L/L). For L1014F: RR = 157, RS = 13 (10 + 3), SS = 0. For L1014S: RR = 0, RS = 3, SS = 167 (157 + 10).
- In the M form control group (N = 2): 2 +/+ (L/L). For L1014F: RR = 0, RS = 0, SS = 2. For L1014S: RR = 0, RS = 0, SS = 2.
- In the S form selected group (N = 161 survivors): 153 RW/RW (1014F/1014F), 8 RW/+ (1014F/L), 0 RW/RE, 0 +/+. For L1014F: RR = 153, RS = 8, SS = 0. For L1014S: RR = 0, RS = 0, SS = 161.

### Bioassays
- Bioassays were used to determine an LT50 time-response curve across six exposure durations (12.5 to 200 min) with 'between 98 and 110 individuals per time point and sex' (Figure 1). The 1 h WHO diagnostic mortality (16.8% females, 30.5% males) was predicted from the logistic regression model rather than measured in a dedicated test with printed counts. Because exact exposed and dead/alive counts per exposure time are not printed, no standalone bioassay record was created, and `bioassay_id` in `geno_pheno` is left null.

## Validator warnings

- geno_pheno #1 (permethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #2 (permethrin, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
