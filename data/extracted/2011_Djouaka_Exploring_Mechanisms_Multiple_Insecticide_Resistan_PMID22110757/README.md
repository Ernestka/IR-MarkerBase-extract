# Extraction record — 2011_Djouaka_Exploring_Mechanisms_Multiple_Insecticide_Resistan_PMID22110757

- Extracted: 2026-11-13
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 3 · Bioassays: 14 · Geno-pheno rows: 0

## Decisions

1. Two surveys created for Pahou: one for field-collected wild adults (used for target marker SNP genotyping) and one for F1 progeny reared from collected females (used for WHO bioassays).
2. Target markers kdr (L1014F and L1014S) and Ace-1 (G119S) were genotyped in 50 field-collected An. funestus s.s. mosquitoes by pyrosequencing. All 50 were wild-type for all three markers.
3. Bioassays were reported for both females and males separately in Figure 1, so distinct bioassay records were extracted for each sex.
4. Synergist assays with 4% PBO + 4% DDT on females and males were extracted from text (page 3).
5. Minor discrepancies between text and Figure 1 mortality percentages (permethrin females: text 66.7%, Figure 1 66.4%; bendiocarb females: text 65%, Figure 1 64.5%) were recorded in `inconsistency_note` with Figure 1 values retained.
6. Ex20 and Ex27-31 VGSC fragment sequencing in 5 resistant and 5 susceptible mosquitoes identified no amino acid changes/target markers, so no additional genotype records were extracted for those fragments.

## Validator warnings

- bioassay 2011_Djouaka_pahou_2009_2011_f1_permethrin_075_f: inconsistent in the paper (values kept as printed) — Text on page 3 reports mortality of 66.7% for females, whereas Figure 1 reports 66.4% (149). Value from Figure 1 (66.4) extracted.
- bioassay 2011_Djouaka_pahou_2009_2011_f1_bendiocarb_01_f: inconsistent in the paper (values kept as printed) — Text on page 3 reports mortality of 65% for females, whereas Figure 1 reports 64.5% (62). Value from Figure 1 (64.5) extracted.
