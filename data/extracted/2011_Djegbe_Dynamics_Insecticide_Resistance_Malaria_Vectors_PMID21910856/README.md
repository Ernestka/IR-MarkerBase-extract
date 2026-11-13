# Extraction record — 2011_Djegbe_Dynamics_Insecticide_Resistance_Malaria_Vectors_PMID21910856

- Extracted: 2026-11-13
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 33 · Genotype rows: 35 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Resolution**:
   - Surveys are defined at the finest available resolution: site x collection round (October 2008, June 2009, October 2009, June 2010) x molecular species/form (An. coluzzii / M form, An. gambiae s.s. / S form, An. arabiensis).
   - Four sentinel sites in Benin were sampled: Asecna (Cotonou), Tori-Bossito, Bohicon, and Malanville.

2. **Target Markers Extracted**:
   - `Vgsc L1014F` and `Vgsc L1014S` (codon 995/1014) from Table 1.
   - `Ace-1 G119S` (G280S) was reported in text as found in a single heterozygous specimen of An. gambiae M form in Bohicon, but full genotype counts across surveys are not systematically tabulated; therefore, Ace-1 was not added as complete survey-level genotype records.

3. **Multi-allelic Codon 1014 (Rule 4b)**:
   - For multi-allelic Vgsc 1014 (carrying L, F, and S alleles), separate records were created for L1014F and L1014S.
   - SS is computed as mosquitoes without that specific mutation (which includes wild-type L/L and carriers of the alternative mutation).
   - For Bohicon June 2010 An. arabiensis (N=2: 1 Leu-Leu, 1 Ser-Ser):
     - L1014F: RR=0, RS=0, SS=2, F(1014F)=0.50.
     - L1014S: RR=1, RS=0, SS=1, F(1014S)=0.50.
   - For Malanville June 2010 An. arabiensis (N=3: 1 Leu-Phe, 2 Leu-Ser):
     - L1014F: RR=0, RS=1, SS=2, F(1014F)=0.16.
     - L1014S: RR=0, RS=2, SS=1, F(1014S)=0.33.

4. **Inconsistencies Noted**:
   - Bohicon June 2010 M form: Table 1 prints N=15, Leu-Phe=1, Phe-Phe=11, leaving 3 specimens unaccounted for among printed genotype classes. Recorded in `inconsistency_note` with SS=3 by subtraction.

5. **Unidentified Specimens Excluded**:
   - Footnote in Table 1 mentions 2 additional 1014S specimens (1 homozygote, 1 heterozygote) detected in Bohicon and Malanville whose species could not be identified; excluded per Rule 8.

6. **Bioassays & Phenotype-split Genotypes**:
   - WHO cylinder bioassays were performed on unseparated wild-reared An. gambiae s.l. populations. Percent mortality values are presented graphically in Figures 2 and 3 without printed exact numerical values in tables/text, so bioassays are omitted to avoid digitising approximations.
   - No phenotype-split genotype data (alive vs dead) are reported in the paper.

## Validator warnings

- genotype #6 (2011_Djegbe_tori_2010-06_M, Vgsc L1014F): computed allele freq 0.742 differs from reported 0.77
- genotype #10 (2011_Djegbe_bohicon_2010-06_M, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Table 1 lists N=15, Leu-Phe=1, Phe-Phe=11, leaving 3 specimens unaccounted for among genotype classes in the table.
- genotype #29 (2011_Djegbe_bohicon_2010-06_arab, Vgsc L1014F): computed allele freq 0.000 differs from reported 0.5
