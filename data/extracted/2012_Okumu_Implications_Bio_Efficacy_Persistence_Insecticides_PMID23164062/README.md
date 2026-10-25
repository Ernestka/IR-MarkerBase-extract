# Extraction record — 2012_Okumu_Implications_Bio_Efficacy_Persistence_Insecticides_PMID23164062

- Extracted: 2026-10-25
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 6 · Bioassays: 5 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Splitting
- Field collections in Lupiro village (Ulanga District, Tanzania; 8.385°S, 36.670°E) were divided into three groups:
  1. `2012_Okumu_Lupiro_exp_huts`: Wild An. gambiae s.l. (96% molecularly confirmed An. arabiensis) collected using interception exit traps in unsprayed experimental huts. This population provided mosquitoes for the WHO tube susceptibility assays (Table 1) and kdr screening (383 molecularly confirmed An. arabiensis, all kdr-negative).
  2. `2012_Okumu_Lupiro_houses`: Wild An. gambiae s.l. caught using CDC light traps inside local houses near occupied bed nets (15 confirmed An. arabiensis genotyped, all kdr-negative).
  3. `2012_Okumu_Lupiro_colony`: Insectary colony established from blood-fed An. arabiensis collected resting indoors in local houses (122 genotyped, all kdr-negative).
- Both L1014F and L1014S mutations were tested using the Martinez-Torres AS-PCR protocol and were 100% absent across all groups.

### Bioassays
- Standard WHO susceptibility tube assays against DDT 4%, permethrin 0.75%, lambda-cyhalothrin 0.05%, deltamethrin 0.05%, and dieldrin 0.4% are extracted from Table 1 for the experimental hut wild population. Total dead counts are literally printed in Table 1 (`dead_alive_printed = true`).
- Monthly cone and wire ball residual efficacy assays testing IRS and LLIN decay over 6 months were performed using colony mosquitoes, and raw counts are presented only as graphs in Figures 1-3 (and detailed in Additional File 1, not provided), so they were not extracted.

### Genotype-Phenotype Data
- The authors noted that the colony mosquitoes screened for kdr included individuals that survived the IRS/LLIN bioassays, but no separate counts or breakdowns between alive and dead mosquitoes were given. Hence, `geno_pheno` is empty.

## Validator warnings

- survey 2012_Okumu_Lupiro_colony: laboratory population — normally excluded
