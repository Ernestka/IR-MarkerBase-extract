# Extraction record — 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 1 · Bioassays: 4 · Geno-pheno rows: 0

## Decisions

### Data Extraction Summary

1. **Surveys Defined**:
   - `mopti_1995`: An. coluzzii laboratory colony established in 1995 from Mopti, Mali.
   - `selenkenyi_2014`: An. coluzzii laboratory colony established in 2014 from Selenkenyi, Mali.
   - `pimperena`: An. gambiae laboratory colony from Pimperena, Mali.
   - `f2_recombinants`: F2 recombinant cross between 1995 An. coluzzii (cyp-2 females) and 2014 An. coluzzii (cyp-1 males).

2. **Target Markers Extracted**:
   - **Vgsc L1014F (kdr)**: Mapped to target marker `Vgsc L1014F` / `Vgsc L995F`. Extracted genotype counts for the F2 recombinants from Figure 2. The paper genotyped `kdr` (wt = SS, wt/kdr = RS, kdr = RR) across F2 females and males. Summing the subgroup counts printed on Figure 2 bars gives RR = 12 (5 females, 7 males), RS = 83 (37 females, 46 males), SS = 151 (76 females, 75 males), with total n_genotyped = 246.
   - CYP9K1 cyp-1/cyp-2 haplotypes are multi-gene X-chromosome selective sweep haplotypes rather than the target SNP Cyp9k1 G454A, so they were excluded from target marker extraction.

3. **Bioassays & Geno-Pheno**:
   - CDC bottle bioassay mortality rates for permethrin (21.5 μg) alone and with PBO pre-treatment were extracted from text (page 4) and Figure 1a.
   - Figure 2 reports proportion resistant (Y-axis) per genotype class rather than raw counts of dead and alive mosquitoes. Per extraction rules, counts were not back-calculated from percentages/bar charts, so overall F2 genotype counts were placed in `genotypes` and `geno_pheno` was left empty.

## Validator warnings

- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_mopti_1995: laboratory population — normally excluded
- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_selenkenyi_2014: laboratory population — normally excluded
- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_pimperena: laboratory population — normally excluded
- survey 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_f2_recombinants: laboratory population — normally excluded
- genotype #1 (2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_f2_recombinants, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Text states 122 females and 141 males (263 total) were tested, but subgroup sample sizes printed on bars in Figure 2 sum to 118 females and 128 males (246 total).
- bioassay 2018_Main_Genetic_Variation_Associated_Increased_Insecticide_PMID29618373_selenkenyi_2014_permethrin: inconsistent in the paper (values kept as printed) — Page 4 text states 68% mortality in one sentence and 67% (n = 43) in another.
