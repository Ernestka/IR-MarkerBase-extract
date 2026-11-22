# Extraction record — 2018_Kristan_Effect_Environmental_Variables_Kdr_Resistance_PMID30367663

- Extracted: 2026-11-22
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 0 · Geno-pheno rows: 2

## Decisions

### Data Extraction Decisions

1. **Surveys**: Mosquitoes were collected as larvae around Butemba, Kyankwanzi District, Uganda between August 2013 and June 2014 and reared to adults. Species identification by PCR of 1,196 An. gambiae (s.l.) yielded 90.4% (1,081) An. gambiae (s.s.) and 9.6% (115) An. arabiensis. Two survey records were created to capture the species breakdown.
2. **Markers Extracted**:
   - `ace-1 G119S`: Tested in 692 An. gambiae (s.s.) samples; 0 carries/mutations were detected (`rr=0, rs=0, ss=692`).
   - `kdr-L1014S` (Vgsc L995S): Extracted into `geno_pheno` because mosquitoes evaluated in the transmission/deltamethrin net exposure experiments were recorded separately by 7-day survival outcome (alive vs dead). Out of 852 survivors, 745 (692 dissected + 53 non-dissected) were homozygous 1014S/1014S. Out of 241 dead mosquitoes, 187 were 1014S/1014S.
3. **Dropped/Unusable Data**:
   - Exact numeric counts for `kdr-L1014F` (homozygotes and L1014S/L1014F heterozygotes) and wild-type L1014 are only shown as percentages in Figure 4 bar charts and not printed as numeric sample counts in text or tables. Following Rule 2 and Rule 9, these were omitted rather than back-calculated.
   - No standard bioassay mortality tables with exact exposed/dead numbers were reported (exposure experiments were evaluated using daily Kaplan-Meier survival curves and mixed-effects logistic regression models).

## Validator warnings

- geno_pheno #1 (deltamethrin, kdr kdr-L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, kdr kdr-L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
