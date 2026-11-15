# Extraction record — 2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 16 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys**: Split into 8 distinct site/program combinations across 4 regions: Parakou (CCP), N'dali (TICP), Kandi 1 (CCP), Kandi 2 (TICP), Kandi 3 (BP), Banikoara 1 (CCP), Banikoara 2 (TICP), Banikoara 3 (BP).
- **Marker Naming**: Corrected `kdr` marker string to `kdr-west` as reported in the text (page 7) and as recognized in the standard target marker aliases list.
- **Coordinates**: Reported coordinates on page 3 use degree symbols as decimal points (e.g. 2°62 E, 9°33 N for Parakou, 2°95 E, 11°16 N for Kandi). These have been recorded as decimal degrees 9.33 N, 2.62 E, etc.
- **Bioassays**: Extracted all WHO tube diagnostic dose bioassays for DDT 4% and Permethrin 0.75% from Table 1 for all 8 surveys. Reference Kisumu strain bioassays were excluded. Tests with deltamethrin and bendiocarb were described in the text as giving 100% mortality across overall programs without site-specific sample sizes and were therefore omitted.
- **Target Markers**: Extracted raw genotype counts (SS, RS, RR) for `kdr` (`kdr-west` / `L995F`) and `Ace.1` (`G119S` / `G280S`) from Table 2. Inconsistency notes were added for Ace-1 entries where printed F(R) matched carrier frequency (RS/N) rather than true allele frequency.
- **Geno-Pheno**: Dead and live mosquitoes from bioassays were preserved but genotype counts were not split by bioassay outcome in the paper.

## Validator warnings

- genotype #2 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_parakou_ccp, Ace.1 G119S): inconsistent in the paper (values kept as printed) — Reported allele frequency 0.06 matches carrier frequency RS/N (2/32 = 0.0625) rather than true allele frequency (2/64 = 0.03125).
- genotype #2 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_parakou_ccp, Ace.1 G119S): computed allele freq 0.031 differs from reported 0.06
- genotype #6 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi1_ccp, Ace.1 G119S): inconsistent in the paper (values kept as printed) — Reported allele frequency 0.06 matches carrier frequency RS/N (2/32 = 0.0625) rather than true allele frequency (2/64 = 0.03125).
- genotype #6 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi1_ccp, Ace.1 G119S): computed allele freq 0.031 differs from reported 0.06
- genotype #8 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi2_ticp, Ace.1 G119S): inconsistent in the paper (values kept as printed) — Reported allele frequency 0.03 matches carrier frequency RS/N (1/31 = 0.03225) rather than true allele frequency (1/62 = 0.0161).
- genotype #11 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, kdr kdr-west): computed allele freq 0.706 differs from reported 0.78
- genotype #12 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, Ace.1 G119S): inconsistent in the paper (values kept as printed) — Reported allele frequency 0.06 matches carrier frequency RS/N (2/32 = 0.0625) rather than true allele frequency (2/64 = 0.03125).
- genotype #12 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, Ace.1 G119S): computed allele freq 0.031 differs from reported 0.06
