# Extraction record — 1_s2_0_S0001706X19317632_main

- Extracted: 2026-10-08
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 21 · Bioassays: 19 · Geno-pheno rows: 0

## Decisions

1. **Surveys**: Split into October 2018 and November 2018 cohorts. October 2018 surveys represent the larval collections used for the WHO bioassays. November 2018 surveys represent the molecular genotyping cohorts.
2. **Bissau Split**: Bissau is split into `bissau_oct2018` (Bissau-2) and `bissau_nov2018` (Bissau-1) to avoid duplicate genotype records for Vgsc L1014F in the same survey.
3. **SAB**: SAB stands for Sector Autónomo de Bissau (Autonomous Sector of Bissau). Bioassays and genotypes labeled SAB or Bissau are mapped to the Bissau surveys.
4. **Genotypes**: Table 3 reports mutant allele frequencies from pooled samples (Nov 2018) and individual mosquitoes (Bissau-2, Oct 2018). For pooled samples, `n_genotyped` is derived as half of the reported sample size in alleles (e.g., 100 alleles = 50 individuals) because mosquitoes are diploid.
5. **Bioassays**: Extracted all WHO tube bioassays from Table 1. Standard 1X concentrations are mapped to `diagnostic_dose`, while 5X and 10X are mapped to `intensity`. Synergist assays (PBO + Permethrin) and synergist controls (PBO alone) are also extracted.

## Validator warnings

- genotype #1 (1_s2_0_S0001706X19317632_main_buba_nov2018, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (1_s2_0_S0001706X19317632_main_buba_nov2018, Vgsc L1014S): frequency only (no raw counts)
- genotype #3 (1_s2_0_S0001706X19317632_main_buba_nov2018, Vgsc N1575Y): frequency only (no raw counts)
- genotype #4 (1_s2_0_S0001706X19317632_main_buba_nov2018, Ace-1 G119S): frequency only (no raw counts)
- genotype #5 (1_s2_0_S0001706X19317632_main_gabu_bafata_nov2018, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (1_s2_0_S0001706X19317632_main_gabu_bafata_nov2018, Vgsc L1014S): frequency only (no raw counts)
- genotype #7 (1_s2_0_S0001706X19317632_main_gabu_bafata_nov2018, Vgsc N1575Y): frequency only (no raw counts)
- genotype #8 (1_s2_0_S0001706X19317632_main_gabu_bafata_nov2018, Ace-1 G119S): frequency only (no raw counts)
- genotype #9 (1_s2_0_S0001706X19317632_main_bafata_nov2018, Vgsc L1014F): frequency only (no raw counts)
- genotype #10 (1_s2_0_S0001706X19317632_main_bafata_nov2018, Vgsc L1014S): frequency only (no raw counts)
- genotype #11 (1_s2_0_S0001706X19317632_main_bafata_nov2018, Vgsc N1575Y): frequency only (no raw counts)
- genotype #12 (1_s2_0_S0001706X19317632_main_bafata_nov2018, Ace-1 G119S): frequency only (no raw counts)
- genotype #13 (1_s2_0_S0001706X19317632_main_gabu_nov2018, Vgsc L1014F): frequency only (no raw counts)
- genotype #14 (1_s2_0_S0001706X19317632_main_gabu_nov2018, Vgsc L1014S): frequency only (no raw counts)
- genotype #15 (1_s2_0_S0001706X19317632_main_gabu_nov2018, Vgsc N1575Y): frequency only (no raw counts)
- genotype #16 (1_s2_0_S0001706X19317632_main_gabu_nov2018, Ace-1 G119S): frequency only (no raw counts)
- genotype #17 (1_s2_0_S0001706X19317632_main_bissau_nov2018, Vgsc L1014F): frequency only (no raw counts)
- genotype #18 (1_s2_0_S0001706X19317632_main_bissau_nov2018, Vgsc L1014S): frequency only (no raw counts)
- genotype #19 (1_s2_0_S0001706X19317632_main_bissau_nov2018, Vgsc N1575Y): frequency only (no raw counts)
- genotype #20 (1_s2_0_S0001706X19317632_main_bissau_nov2018, Ace-1 G119S): frequency only (no raw counts)
- genotype #21 (1_s2_0_S0001706X19317632_main_bissau_oct2018, Vgsc L1014F): frequency only (no raw counts)
- bioassay 1_s2_0_S0001706X19317632_main_bafata_oct2018_delta: inconsistent in the paper (values kept as printed) — N = 25 but mortality is 33.3% (which corresponds to 8.3 mosquitoes)
- bioassay 1_s2_0_S0001706X19317632_main_bissau_oct2018_delta: inconsistent in the paper (values kept as printed) — N = 105 but mortality is 44.8% (which corresponds to 47.04 mosquitoes)
