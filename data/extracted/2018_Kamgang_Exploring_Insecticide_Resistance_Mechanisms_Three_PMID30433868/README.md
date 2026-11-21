# Extraction record — 2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 8 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Summary of Decisions
- **Surveys**: Created separate surveys per species and generation stage:
  1. `bangui_2016_col`: F0 wild adult female *An. coluzzii* oviposited mothers (N=21).
  2. `bangui_2016_gam`: F0 wild adult female *An. gambiae s.s.* oviposited mothers (N=16).
  3. `bangui_2016_fun`: Non-exposed F1 progeny of wild *An. funestus s.s.* females (N=51).
  4. `bangui_2016_gaml_f2`: F2 generation of *An. gambiae s.l.* used in WHO bioassays (total 241 tested).
- **Genotypes**:
  - *An. coluzzii*: Table 1 lists kdr-w (RR=2, RS=18, SS=1). For kdr-e and Ace-1, Table 1 reports SS=20 (100%) for total N=21, noted in `inconsistency_note`.
  - *An. gambiae s.s.*: Table 1 lists kdr-w (RR=6, RS=9, SS=0, total=15 for column N=16). Text confirms 15 mosquitoes genotyped. Ace-1 lists SS=10 (100%) for N=16, noted in `inconsistency_note`.
  - *An. funestus s.s.*: GSTe2 L119F genotyped in 43 F1 mosquitoes (RR=13, RS=21; SS left null as count not printed). Rdl A296S genotyped in 51 F1 mosquitoes (RR=0, RS=1; SS left null).
- **Bioassays**: Extracted WHO tube bioassays on F2 *An. gambiae s.l.* for permethrin (0.75%), deltamethrin (0.05%), and DDT (4%). Section 2.2 states assays were conducted using 4 replicates of 20 mosquitoes per test (n_exposed = 80 per bioassay). Permethrin and deltamethrin mortality reported as 0%; DDT reported as '< 3%' (so reported_mortality_pct set to null).
- **Geno_Pheno**: No post-bioassay genotype-phenotype data reported.

## Validator warnings

- genotype #2 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_col, kdr kdr-e): inconsistent in the paper (values kept as printed) — Table 1 lists N = 21 for An. coluzzii, but kdre-SS = 20 (100%), leaving 1 specimen ungenotyped or typo in table.
- genotype #2 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_col, kdr kdr-e): RR+RS+SS = 0+0+20 = 20 but n_genotyped = 21
- genotype #3 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_col, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Table 1 lists N = 21 for An. coluzzii, but Ace 1-SS = 20 (100%), leaving 1 specimen ungenotyped or typo in table.
- genotype #3 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_col, Ace-1 G119S): RR+RS+SS = 0+0+20 = 20 but n_genotyped = 21
- genotype #4 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_gam, kdr kdr-w): inconsistent in the paper (values kept as printed) — Table column N = 16, but RR + RS + SS = 15; text on page 4 states 15 mosquitoes were genotyped for kdr-w.
- genotype #4 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_gam, kdr kdr-w): RR+RS+SS = 6+9+0 = 15 but n_genotyped = 16
- genotype #6 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_gam, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Table 1 column N = 16, but Ace 1-SS = 10 (100%), leaving 6 mosquitoes ungenotyped or typo in table.
- genotype #6 (2018_Kamgang_Exploring_Insecticide_Resistance_Mechanisms_Three_PMID30433868_bangui_2016_gam, Ace-1 G119S): RR+RS+SS = 0+0+10 = 10 but n_genotyped = 16
