# Extraction record — 2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825

- Extracted: 2026-11-20
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 6 · Bioassays: 15 · Geno-pheno rows: 4

## Decisions

### Study and Surveys Overview
- The paper investigates insecticide resistance and resistance markers in *Anopheles funestus s.s.* from Gounougou, northern Cameroon.
- Collections took place across three timepoints:
  1. December 2006 (F0 wild-collected females described previously in Wondji et al. 2011 [10], reused here for TaqMan genotyping of GSTe2 and RDL).
  2. December 2011 to January 2012 (indoor-resting blood-fed F0 females and reared F1 progeny).
  3. January 2015 (indoor-resting blood-fed F0 females and reared F1 progeny).
- Separate survey IDs were created for F0 wild adults and F1 progeny due to different generations and life stages.

### Target Markers and Genotyping
- Two target markers were genotyped by TaqMan assays:
  1. `GSTe2 L119F`: Genotyped in F0 females from 2006, 2012, and 2015, and in bioassay survivors vs. dead following DDT exposure in 2012 F1 females.
  2. `Rdl A296S`: Genotyped in F0 females from 2006, 2012, and 2015, and in bioassay survivors vs. dead following dieldrin exposure in 2012 F1 females.
- Raw RR/RS/SS genotype counts are not reported in the text (only stacked bar charts in Fig 4A and 4B); therefore, according to extraction rules, allele frequencies are reported in `reported_allele_freq` and count fields are left null without back-calculation.
- VGSC sequencing was performed across intron 19 to exon 20 in 20 mosquitoes (5 alive, 5 dead each for DDT and permethrin). The authors note the absence of codon 1014 mutations and found three novel substitutions (I877L, V881L, A1007S), none of which are target markers; thus, VGSC was not extracted.

### Discrepancies noted in `inconsistency_note`
- For `Rdl A296S` in 2012 F0: Page 9 first paragraph states the frequency was 45%, but the second paragraph states it was 40%.
- For `GSTe2 L119F` DDT bioassay alive group: Page 4 states 30 alive (resistant) F1 females were genotyped, while Page 8 states 35 DDT resistant mosquitoes.
- For `Rdl A296S` dieldrin bioassay alive and dead groups: Page 4-5 states 35 dead and 35 alive F1 females were genotyped, while Page 9 states 30 dead and 30 alive mosquitoes.

### Bioassays
- Bioassay percentages are reported in the text and figures for 2012 and 2015 F1 females. Exact exposure numbers (n_exposed, n_dead, n_alive) per insecticide are not printed (the methods specify 4 replicates of ~20-25 mosquitoes); therefore, counts are left null and `reported_mortality_pct` is extracted with `dead_alive_printed = false`.

## Validator warnings

- genotype #1 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2006, GSTe2 L119F): frequency only (no raw counts)
- genotype #2 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2006, Rdl A296S): frequency only (no raw counts)
- genotype #3 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f0, GSTe2 L119F): frequency only (no raw counts)
- genotype #4 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f0, Rdl A296S): inconsistent in the paper (values kept as printed) — Page 9 first paragraph states the frequency of the resistant 296S allele in Gounougou was 45%, whereas the second paragraph states a reduction from 80% in 2006 to 40% in 2012.
- genotype #4 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f0, Rdl A296S): frequency only (no raw counts)
- genotype #5 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2015_f0, GSTe2 L119F): frequency only (no raw counts)
- genotype #6 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2015_f0, Rdl A296S): frequency only (no raw counts)
- geno_pheno #1 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f1_ddt_4, GSTe2 L119F, alive): inconsistent in the paper (values kept as printed) — Page 4 reports 30 alive (resistant) F1 females genotyped after DDT exposure, whereas page 8 reports 35 DDT resistant mosquitoes with resistant allele frequency of 72.5%.
- geno_pheno #3 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f1_dieldrin_4, Rdl A296S, alive): inconsistent in the paper (values kept as printed) — Page 4-5 reports 35 alive (resistant) F1 female mosquitoes genotyped after dieldrin exposure, whereas page 9 reports 30 dieldrin resistant mosquitoes with 90% resistant allele frequency.
- geno_pheno #4 (2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825_gounougou_2012_f1_dieldrin_4, Rdl A296S, dead): inconsistent in the paper (values kept as printed) — Page 4-5 reports 35 dead (susceptible) F1 female mosquitoes genotyped after dieldrin exposure, whereas page 9 reports 30 susceptible mosquitoes with 40% resistant allele frequency.
