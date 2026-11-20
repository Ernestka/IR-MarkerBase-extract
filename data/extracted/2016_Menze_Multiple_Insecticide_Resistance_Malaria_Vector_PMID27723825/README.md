# Extraction record — 2016_Menze_Multiple_Insecticide_Resistance_Malaria_Vector_PMID27723825

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 6 · Bioassays: 15 · Geno-pheno rows: 12

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Three surveys were extracted for Gounougou, northern Cameroon, corresponding to sampling timepoints in 2006 (archival sample reused for temporal analysis), 2011-2012 (primary collection), and 2015 (follow-up monitoring).
   - Mosquitoes were identified as *Anopheles funestus s.s.* via species-specific cocktail PCR (out of 402 F0 collected in 2012, 2 were *An. leesoni* and excluded from further bioassays/genotyping).

2. **Markers Extracted**:
   - `GSTe2 L119F`: Reported in population samples for 2006, 2012, and 2015, and in genotype-phenotype split (alive vs dead) after DDT exposure.
   - `Rdl A296S`: Reported in population samples for 2006, 2012, and 2015, and in genotype-phenotype split (alive vs dead) after dieldrin exposure.
   - `Vgsc L1014F` / `L1014S` (`Vgsc L995F` / `L995S`): Sequenced in 20 individuals (5 dead, 5 alive for permethrin and DDT); no mutations detected at codon 1014 (0 carriers, all wild-type).
   - Novel/non-target mutations mentioned in the text (I877L, V881L, A1007S) were omitted as they are not on the required target markers list.

3. **Bioassays**:
   - Recorded reported 24h mortality percentages for standard WHO susceptibility assays from 2012 and 2015, and PBO synergist assays from 2012.
   - As exact dead/alive counts per individual test were not explicitly printed in text/tables, count fields (`n_exposed`, `n_dead`, `n_alive`) were left null and `dead_alive_printed` was set to false, storing the printed percent in `reported_mortality_pct` per Rule 2.

4. **Inconsistencies Noted**:
   - `GSTe2 L119F` geno-pheno sample size: Methods (p. 4) states 35 dead and 30 alive mosquitoes genotyped for DDT, while Results (p. 8) states 35 dead and 35 alive mosquitoes.
   - `Rdl A296S` geno-pheno sample size: Methods (p. 4) states 35 dead and 35 alive mosquitoes genotyped for dieldrin, while Results (p. 9) states 30 dead and 30 alive mosquitoes.
   - `Rdl A296S` 2012 population frequency: Page 9 first paragraph states 45% allele frequency in Gounougou, while page 9 second paragraph states 40% in 2012.

## Validator warnings

- genotype #1 (2016_Menze_gounougou_2006_fun, GSTe2 L119F): frequency only (no raw counts)
- genotype #2 (2016_Menze_gounougou_2012_fun, GSTe2 L119F): frequency only (no raw counts)
- genotype #3 (2016_Menze_gounougou_2015_fun, GSTe2 L119F): frequency only (no raw counts)
- genotype #4 (2016_Menze_gounougou_2006_fun, Rdl A296S): frequency only (no raw counts)
- genotype #5 (2016_Menze_gounougou_2012_fun, Rdl A296S): inconsistent in the paper (values kept as printed) — Page 9 first paragraph states 296S allele frequency was 45% in Gounougou, but second paragraph states 40% in 2012.
- genotype #5 (2016_Menze_gounougou_2012_fun, Rdl A296S): frequency only (no raw counts)
- genotype #6 (2016_Menze_gounougou_2015_fun, Rdl A296S): frequency only (no raw counts)
- geno_pheno #1 (2016_Menze_gounougou_2012_fun_ddt, GSTe2 L119F, alive): inconsistent in the paper (values kept as printed) — Page 4 states 30 alive (resistant) mosquitoes genotyped after DDT exposure, but page 8 states 35 DDT resistant mosquitoes with 72.5% frequency.
- geno_pheno #3 (2016_Menze_gounougou_2012_fun_dieldrin, Rdl A296S, alive): inconsistent in the paper (values kept as printed) — Page 4 states 35 alive (resistant) F1 female mosquitoes genotyped after dieldrin exposure, but page 9 states 30 dieldrin resistant mosquitoes with 90% frequency.
- geno_pheno #4 (2016_Menze_gounougou_2012_fun_dieldrin, Rdl A296S, dead): inconsistent in the paper (values kept as printed) — Page 4 states 35 dead (susceptible) F1 female mosquitoes genotyped after dieldrin exposure, but page 9 states 30 susceptible mosquitoes with 40% frequency.
