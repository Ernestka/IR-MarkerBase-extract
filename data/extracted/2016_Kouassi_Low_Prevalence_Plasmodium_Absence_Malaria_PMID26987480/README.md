# Extraction record — 2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480

- Extracted: 2026-10-18
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 7 · Genotype rows: 7 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Study and Survey Overview
- The study investigated mosquito bio-ecology and insecticide resistance kdr mutations in Conakry, Guinea, using exit traps (ETC) and pyrethrum spray catches (PSC) between December 2012 and November 2013 (stated as November 2012 to October 2013 in the abstract).
- Adult Anopheles gambiae s.l. were identified to molecular species via PCR-RFLP (Favia et al. 1997). Out of 112 tested, 89 were An. coluzzii (M form), 13 An. gambiae s.s. (S form), and 10 An. melas. 
- 102 mosquitoes (An. coluzzii and An. gambiae s.s.) were assayed for the Leu-Phe kdr (L1014F/L995F) mutation using the PCR method of Martinez-Torres et al. (1998).
- Data are extracted at the finest reported resolution: by district (Matoto, Matam, Kaloum, Ratoma) and molecular species (An. coluzzii and An. gambiae s.s.) according to Table 4. Per extraction rules, pooled Conakry totals are omitted to avoid double counting.
- No bioassays were conducted in this study due to lack of larval numbers/equipment; hence bioassays and geno_pheno tables are empty.

### Table 4 Inconsistencies
Table 4 contains several printed internal inconsistencies which are retained verbatim and noted in `inconsistency_note`:
1. Matam An. coluzzii: RR=0, RS=0, SS=1, Total=1, but the resistant percentage column states '1 (50)'.
2. Kaloum An. coluzzii: RR=0, RS=0, SS=1, Total=1, but the resistant percentage column states '1 (100)'.
3. Kaloum An. gambiae s.s.: RR=2, RS=0, SS=0 (sum=2), while Total is reported as 4.
4. Ratoma An. coluzzii: RR=28, RS=28, SS=25 (sum=81), while Total is reported as 84; resistant percentage is printed as 60.2% for 56 carriers (56/84 would be 66.7%).
5. Ratoma An. gambiae s.s.: RR=2, RS=2, SS=1 (sum=5), while Total is reported as 7 (4/7 = 57.1%).

## Validator warnings

- genotype #2 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_matam_coluzzii, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 reports Total = 1, RR = 0, RS = 0, SS = 1, but reports '(%) of resistant (R and RS)' as '1 (50)'.
- genotype #4 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_kaloum_coluzzii, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 reports Total = 1, RR = 0, RS = 0, SS = 1, but reports '(%) of resistant (R and RS)' as '1 (100)'.
- genotype #5 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_kaloum_gambiae, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 reports Total = 4, but RR = 2, RS = 0, SS = 0 (sum = 2).
- genotype #5 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_kaloum_gambiae, kdr 1014F): RR+RS+SS = 2+0+0 = 2 but n_genotyped = 4
- genotype #6 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_ratoma_coluzzii, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 reports Total = 84, but RR = 28, RS = 28, SS = 25 (sum = 81); printed resistant percentage is 60.2% for 56 carriers.
- genotype #6 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_ratoma_coluzzii, kdr 1014F): RR+RS+SS = 28+28+25 = 81 but n_genotyped = 84
- genotype #7 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_ratoma_gambiae, kdr 1014F): inconsistent in the paper (values kept as printed) — Table 4 reports Total = 7, but RR = 2, RS = 2, SS = 1 (sum = 5).
- genotype #7 (2016_Kouassi_Low_Prevalence_Plasmodium_Absence_Malaria_PMID26987480_ratoma_gambiae, kdr 1014F): RR+RS+SS = 2+2+1 = 5 but n_genotyped = 7
