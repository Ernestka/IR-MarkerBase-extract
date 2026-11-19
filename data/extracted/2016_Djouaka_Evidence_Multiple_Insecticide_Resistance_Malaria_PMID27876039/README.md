# Extraction record — 2016_Djouaka_Evidence_Multiple_Insecticide_Resistance_Malaria_PMID27876039

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 2 · Bioassays: 15 · Geno-pheno rows: 4

## Decisions

# Decisions and Extraction Notes

- **Surveys Split**: Split into three surveys: (1) `akakaremo_f0` representing the indoor-resting wild-caught adult females (F0), which were molecularly identified to An. funestus s.s. and genotyped directly; (2) `akakaremo_f1_female` representing the F1 adult females reared from 96 ovipositing mothers (total F1 females = 679) used for WHO susceptibility bioassays, PBO synergist assays, and genotype-phenotype analysis; and (3) `akakaremo_f1_male` representing the F1 adult males (total F1 males = 590) tested in parallel in the standard WHO susceptibility bioassays.
- **Target Markers**: Only two target markers from the required list were genotyped in this study:
  1. `GSTe2 L119F` (reported as `L119F-GSTe2`)
  2. `Rdl A296S` (reported as `A296S-RDL`)
- **Genotypes (F0)**: Counts of RR, RS, and SS classes were literally reported in the text (page 5) for F0 wild females:
  - GSTe2 L119F: N = 88 (52 RR, 31 RS, 5 SS; reported allele frequency = 0.77).
  - Rdl A296S: N = 92 (50 RR, 40 RS, 2 SS; reported allele frequency = 0.76).
- **Bioassays**: The study exposed 1269 F1 adults (679 females and 590 males) to six insecticides (permethrin 0.75%, deltamethrin 0.05%, DDT 4%, dieldrin 4%, bendiocarb 0.1%, malathion 5%). Specific per-insecticide sample sizes were not reported for the baseline diagnostic bioassays, so `n_exposed`, `n_dead`, and `n_alive` are left null and `dead_alive_printed = false` while `reported_mortality_pct` is extracted. For PBO synergist assays, sample sizes are reported in the text (n = 70 for permethrin + PBO, n = 48 for dieldrin + PBO, n = 45 for DDT + PBO) and extracted accordingly.
- **Geno-Pheno**: Tested on F1 females post-bioassay for DDT (25 resistant/alive, 25 susceptible/dead) and dieldrin (15 alive, 5 dead). Genotype classes were reported only as percentages in the text and figures (Figs 4b and 5b). Per Rule 2, genotype count classes (RR, RS, SS) are left null, and the reported allele frequencies are entered. An inconsistency in the dieldrin-susceptible class (5 dead mosquitoes reported with 10% RS frequency) is documented in `inconsistency_note`.

## Validator warnings

- geno_pheno #4 (2016_Djouaka_Evidence_Multiple_Insecticide_Resistance_Malaria_PMID27876039_akakaremo_f1_female_dieldrin, RDL A296S, dead): inconsistent in the paper (values kept as printed) — The paper reports 5 dead mosquitoes tested, 'genotypic frequency of 10% RS' and Fig 5b shows 90% SS and 10% RS with 10% allele frequency. For N = 5 diploid mosquitoes (10 alleles), 10% RS corresponds to 0.5 individuals; 1 RS mosquito out of 5 would represent 20% genotype frequency and 10% allele frequency.
