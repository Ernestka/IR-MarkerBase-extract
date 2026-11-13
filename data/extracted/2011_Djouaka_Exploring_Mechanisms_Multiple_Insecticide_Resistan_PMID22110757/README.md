# Extraction record — 2011_Djouaka_Exploring_Mechanisms_Multiple_Insecticide_Resistan_PMID22110757

- Extracted: 2026-11-13
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 3 · Bioassays: 14 · Geno-pheno rows: 4

## Decisions

1. Two surveys created for Pahou: one for wild-collected females (F0) used in pyrosequencing (`2011_Djouaka_pahou_2009_2011_wild`) and one for wild-reared F1 progeny used in WHO bioassays (`2011_Djouaka_pahou_2009_2011_f1`).
2. Target markers evaluated in this paper: Vgsc L1014F (L995F), Vgsc L1014S (L995S), and Ace-1 G119S (G280S). Pyrosequencing of 50 field-collected mosquitoes confirmed 100% wild-type (SS=50) for all three markers.
3. Sanger sequencing of VGSC Exon 20 (containing codon 1014) in 5 permethrin-resistant (alive) and 5 permethrin-susceptible (dead) mosquitoes showed no mutations at codon 1014; these are recorded in `geno_pheno` linked to the female permethrin 0.75% bioassay.
4. Bioassay mortalities and exposed numbers extracted directly from Figure 1 and text for both males and females. Per Rule 2, raw counts (n_dead, n_alive) are left null because only percentages and total exposed numbers were printed.

## Validator warnings

- bioassay 2011_Djouaka_pahou_2009_2011_f1_bendiocarb_01_m: inconsistent in the paper (values kept as printed) — Figure 1 prints 78.3% (46) for males, while page 3 text states 78.1%.
