# Extraction record — 2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266

- Extracted: 2026-11-14
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 16 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Survey and Extraction Decisions
- **Sites and Survey Grouping:** The study evaluated 8 cotton cultivation sites representing three pest management regimes: Calendar Control Program (CCP; Parakou, Kandi 1, Banikoara 1), Targeted Intermittent Control Program (TICP; N'dali, Kandi 2, Banikoara 2), and Biological Program (BP; Kandi 3, Banikoara 3). Each site represents a distinct survey.
- **Coordinates:** Precise coordinates are provided in the text (page 3) in decimal degrees written with degree signs in place of decimal points (e.g., 2°62 E, 9°33 N for Parakou = 9.33° N, 2.62° E).
- **Species:** Bioassays were performed on wild-reared adult Anopheles gambiae s.l. reared from larvae collected in breeding sites. PCR showed a predominance of An. gambiae s.s. (70-100%) and sympatric An. arabiensis (0-30%, notably in Parakou and N'dali). The genotypes in Table 2 are given per site across the sampled population (sum of SS+RS+RR equals the total N shown in parentheses for each locality).
- **Target Markers:**
  - Vgsc L995F: Screened as kdr 'Leu-Phe' / 'kdr-west' using allele-specific PCR (Martinez-Torres et al. 1998).
  - Ace-1 G280S: Screened as Ace.1 'G119S' using PCR-RFLP (Weill et al. 2004).
- **Bioassays:** WHO tube bioassays with DDT (4%) and permethrin (0.75%) with 1 h exposure and 24 h holding are reported with exact sample sizes and percent mortalities in Table 1. Number dead/alive are not printed and thus left null with `dead_alive_printed = false`. Deltamethrin (0.05%) and bendiocarb (0.1%) tests gave 100% mortality across all sites as described in the text, but site-specific exposure counts were not reported, so they are omitted as per extraction rules. The laboratory susceptible strain An. gambiae Kisumu control was excluded as per rule 5.
- **Genotype-Phenotype Data:** Mosquitoes were preserved in Carnoy solution after bioassays, but genotypes were not reported separately for alive and dead mosquitoes; hence `geno_pheno` is empty.
- **Inconsistency Notes:**
  - For Ace-1 in Table 2, all heterozygous carrier counts (RS=2, RS=1) have reported frequencies equal to RS / N instead of RS / (2N) (e.g., 2/32 = 0.06 instead of 0.031). These mismatches are flagged in `inconsistency_note`.
  - For Banikoara 1 Kdr mutation, the printed counts (SS=12, RS=36, RR=54, N=102) give an allele frequency of (36 + 108)/(204) = 0.706, whereas the printed F(R) is 0.78 (which would correspond to 72/92). This is also flagged in `inconsistency_note`.

## Validator warnings

- genotype #2 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_parakou_ccp, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Calculated allele frequency from counts is 2/(2*32) = 0.031, but paper reports F(R) = 0.06, which corresponds to 2/32.
- genotype #2 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_parakou_ccp, Ace-1 G119S): computed allele freq 0.031 differs from reported 0.06
- genotype #6 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi1_ccp, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Calculated allele frequency from counts is 2/(2*32) = 0.031, but paper reports F(R) = 0.06 (printed '0,06'), which corresponds to 2/32.
- genotype #6 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi1_ccp, Ace-1 G119S): computed allele freq 0.031 differs from reported 0.06
- genotype #8 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_kandi2_ticp, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Calculated allele frequency from counts is 1/(2*31) = 0.016, but paper reports F(R) = 0.03, which corresponds to 1/31.
- genotype #11 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, kdr kdr-west): inconsistent in the paper (values kept as printed) — Calculated allele frequency from counts (36 + 2*54)/(2*102) = 144/204 = 0.706, but paper reports F(R) = 0.78.
- genotype #11 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, kdr kdr-west): computed allele freq 0.706 differs from reported 0.78
- genotype #12 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, Ace-1 G119S): inconsistent in the paper (values kept as printed) — Calculated allele frequency from counts is 2/(2*32) = 0.031, but paper reports F(R) = 0.06, which corresponds to 2/32.
- genotype #12 (2011_Yadouleton_Cotton_Pest_Management_Practices_Selection_PMID21489266_banikoara1_ccp, Ace-1 G119S): computed allele freq 0.031 differs from reported 0.06
