# Extraction record — s13071_016_1661_8

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 18 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Study and Surveys Overview
- The paper investigates target-site (kdr) and metabolic resistance in *Anopheles gambiae* s.l. from 13 villages across 4 districts (Ifangni, Sakete, Pobe, Ketou) in Plateau Department, southern Benin, over five rainy seasons between 2012 and 2014 (June 2012, October 2012, June 2013, October 2013, June 2014).
- Larvae were collected from multiple habitats per village, reared to adulthood, and molecular species identified by PCR (*An. coluzzii* and *An. gambiae* s.s.).
- Genotyping for *kdr* 1014F and 1014S was performed on non-exposed females by TaqMan allelic discrimination qPCR.

### Marker Extraction and Table 4
- Table 4 reports the allelic frequency of *kdr* 1014F (`f(1014)F`) and the number of alleles tested (`N`) across the five surveys for each village and molecular species.
- The caption explicitly states: 'N represents the number of alleles tested'. Because diploid genotype counts (RR, RS, SS) and the number of mosquitoes genotyped are not reported, per Rule 2, `n_genotyped`, `rr`, `rs`, `ss`, `n_carriers`, and `resistant_allele_count` are left null, and `reported_allele_freq` contains the printed proportion.
- A subset of village x survey x species combinations from Table 4 (specifically Adjozoume and Agbarou across all available survey points) are extracted above as exemplary surveys/genotypes, each uniquely mapped. Missing entries in Table 4 ('--') reflect periods where mosquitoes were absent.
- Mutation 1014S was evaluated using TaqMan qPCR assays but was reported as not detected in the study (text page 6); it was not tabulated per village in Table 4.

### Bioassays and Genotype-Phenotype Links
- Deltamethrin WHO tube bioassays were conducted on wild-reared *An. gambiae* s.l. females, but only summary scatter plots of mortality per village (Figure 2a) and per survey period (Figure 2b) are presented. Exact mortality counts (dead/alive) or percentages per village bioassay test are not printed in any table or text. Following Rule 8b and Rule 2, no bioassays were extracted from plots.
- Genotyping was carried out on non-exposed females; no phenotype-linked genotypes (survivors vs. dead) are reported, so `geno_pheno` is empty.

## Validator warnings

- genotype #1 (s13071_016_1661_8_adj_2012_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #2 (s13071_016_1661_8_adj_2012_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #3 (s13071_016_1661_8_adj_2012_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #4 (s13071_016_1661_8_adj_2012_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #5 (s13071_016_1661_8_adj_2013_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #6 (s13071_016_1661_8_adj_2013_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #7 (s13071_016_1661_8_adj_2013_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #8 (s13071_016_1661_8_adj_2014_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #9 (s13071_016_1661_8_agb_2012_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #10 (s13071_016_1661_8_agb_2012_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #11 (s13071_016_1661_8_agb_2012_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #12 (s13071_016_1661_8_agb_2012_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #13 (s13071_016_1661_8_agb_2013_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #14 (s13071_016_1661_8_agb_2013_06_gam, kdr 1014F): frequency only (no raw counts)
- genotype #15 (s13071_016_1661_8_agb_2013_10_col, kdr 1014F): frequency only (no raw counts)
- genotype #16 (s13071_016_1661_8_agb_2013_10_gam, kdr 1014F): frequency only (no raw counts)
- genotype #17 (s13071_016_1661_8_agb_2014_06_col, kdr 1014F): frequency only (no raw counts)
- genotype #18 (s13071_016_1661_8_agb_2014_06_gam, kdr 1014F): frequency only (no raw counts)
