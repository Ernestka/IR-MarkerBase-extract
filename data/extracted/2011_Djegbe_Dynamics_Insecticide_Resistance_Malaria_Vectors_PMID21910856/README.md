# Extraction record — 2011_Djegbe_Dynamics_Insecticide_Resistance_Malaria_Vectors_PMID21910856

- Extracted: 2026-11-13
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 33 · Genotype rows: 35 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Decisions & Extraction Notes

1. **Surveys & Resolution:**
   - Surveys were created at the finest temporal, spatial, and species resolution reported in Table 1 (4 collection periods x 4 sentinel sites x molecular species/forms).
   - Molecular forms of *An. gambiae s.s.* were classified as *An. coluzzii* (M form) and *An. gambiae s.s.* (S form), alongside *An. arabiensis*.

2. **Genotype Data:**
   - Exact genotype counts for *Vgsc* 1014F (L995F) and 1014S (L995S) were extracted from Table 1.
   - Multi-allelic codon rule (Rule 4b) was applied for *An. arabiensis* samples in Bohicon (June 2010) and Malanville (June 2010) where both 1014F and 1014S alleles were present.
   - In Bohicon June 2010 *An. arabiensis* (N=2: 1 Leu-Leu, 1 Ser-Ser), Table 1 printed F(1014F) = 0.5 despite 0 Phe alleles present; this was recorded as printed and flagged in `inconsistency_note`.
   - In Tori-Bossito June 2010 M form (N=31, 16 Phe-Phe, 14 Leu-Phe) and Bohicon June 2010 M form (N=15, 11 Phe-Phe, 1 Leu-Phe), the Leu-Leu cell was printed as '-'; SS counts were derived by subtraction (N - RR - RS).
   - Ace-1 G280S (G119S): The text mentions finding a single Ace-1 G119S heterozygote in an *An. gambiae* M form mosquito from Bohicon (page 6), but no total genotyped denominator per survey is given, so no Ace-1 genotype row was constructed.

3. **Bioassays & Geno-Pheno:**
   - Bioassay results in Figure 2 and Figure 3 are presented only as graphical bar plots without printed numerical tables of mortalities or dead/alive counts; bioassays were therefore omitted to adhere to Rule 2 (no guessing/reading values off charts without exact printed text/tables).
   - Genotyping was performed on unexposed control mosquitoes, so no `geno_pheno` records exist.

## Validator warnings

- genotype #6 (2011_Djegbe_tori_2010_06_m, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Leu-Leu cell printed as '-'; SS derived as N - RR - RS = 1. Printed freq 0.77 fits 46/60 (N=30) rather than 46/62 (N=31).
- genotype #6 (2011_Djegbe_tori_2010_06_m, Vgsc L1014F): computed allele freq 0.742 differs from reported 0.77
- genotype #10 (2011_Djegbe_bohicon_2010_06_m, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Leu-Leu cell printed as '-'; SS derived as N - RR - RS = 3.
- genotype #29 (2011_Djegbe_bohicon_2010_06_arab, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Table 1 reports F(1014F) = 0.5 despite 0 Phe alleles present among N=2 (1 Leu-Leu, 1 Ser-Ser).
- genotype #29 (2011_Djegbe_bohicon_2010_06_arab, Vgsc L1014F): computed allele freq 0.000 differs from reported 0.5
