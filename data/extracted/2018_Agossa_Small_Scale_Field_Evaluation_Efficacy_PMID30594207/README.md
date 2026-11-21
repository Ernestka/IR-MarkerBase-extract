# Extraction record — 2018_Agossa_Small_Scale_Field_Evaluation_Efficacy_PMID30594207

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 1 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Survey**: One survey representing wild-reared *Anopheles gambiae* s.s. collected as larvae in Dangbo district, Benin.
2. **Genotypes**: The paper reports the Leu-Phe *kdr* mutation (Vgsc L1014F) detected by PCR according to Martinez-Torres et al. (1998). The marker is assigned to gene `Vgsc` and marker `L1014F`. The text states: 'Molecular analysis of the wild Anopheles population from Dangbo showed very high frequency of kdr mutation (0.99) (49/50)'. `n_genotyped` = 50, `n_carriers` = 49, `reported_allele_freq` = 0.99. An inconsistency note records that 49/50 equals 0.98.
3. **Bioassays**: Extracted standard WHO tube susceptibility test results reported in Figure 2 for deltamethrin 0.05%, bendiocarb 0.1%, and pirimiphos-methyl 0.25%. Monthly IRS wall cone bioassay evaluations on treated wall substrates were excluded as they represent substrate persistence tests rather than standard mosquito population susceptibility assays. Reference strain (Kisumu) assays were skipped as controls.
4. **Geno-Pheno**: No genotype breakdowns split by bioassay survivor/dead outcome were presented in the study.

## Validator warnings

- genotype #1 (2018_Agossa_Small_Scale_Field_Evaluation_Efficacy_PMID30594207_dangbo, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Text prints frequency 0.99 along with (49/50). Note that 49/50 = 0.98; the paper prints 0.99.
