# Extraction record — 2018_Thiaw_Investigating_Insecticide_Resistance_Knock_Down_PMID29566682

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 6 · Bioassays: 11 · Geno-pheno rows: 8

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Bioassays were performed on wild-reared *Anopheles gambiae* s.l. adult females before molecular identification. Therefore, a generic survey `2018_Thiaw_dielmo_2015_sl` was created for all bioassay records.
   - Genotyping was reported separately per molecular species (*An. arabiensis*, *An. coluzzii*, and *An. gambiae* s.s.). Three species-specific surveys were created: `2018_Thiaw_dielmo_2015_arab`, `2018_Thiaw_dielmo_2015_col`, and `2018_Thiaw_dielmo_2015_gamb`.

2. **Multi-allelic Vgsc Codon 1014 Genotype Mapping**:
   - The paper reports tri-allelic genotypes at codon 1014 (L, F, S) in Table 1 and Table 2 (classifying mosquitoes as LL, LF, LS, FS, FF, SS, where SS in the table refers to S/S homozygotes).
   - Per Rule 4b, L1014F (kdr-w) and L1014S (kdr-e) are recorded as separate rows:
     - **L1014F**: RR = FF count; RS = (LF + FS) count; SS = N - RR - RS = (LL + LS + S/S) count.
     - **L1014S**: RR = S/S count; RS = (LS + FS) count; SS = N - RR - RS = (LL + LF + FF) count.
   - Wild-type (L/L) counts for populations: *An. arabiensis* N=256 (LL=128, FS=19); *An. coluzzii* N=15 (LL=9, FS=2); *An. gambiae* s.s. N=9 (LL=7, FS=0).

3. **Bioassays**:
   - Bioassay mortality rates were reported as percentages for known exposed sample sizes (`n`). Number dead and alive were not printed directly, so `n_dead` and `n_alive` are left null with `dead_alive_printed = false` per Rule 2.
   - Sum of reported bioassay sample sizes in text (91+67+110+101+101+108+74+92+100 = 844) slightly differs from the text total stated as 834; printed values for each test are preserved exactly.
   - Synergist test with etacrynic acid (EA + DDT) and its parallel non-synergist DDT control are extracted as distinct bioassay records.

4. **Genotype-Phenotype Data**:
   - Table 2 reports genotype frequencies for *An. arabiensis* split by bioassay status (Alive vs. Dead) for Pyrethroids (pooled across pyrethroid bioassays) and DDT.
   - `bioassay_id` is set to `null` for these rows because `geno_pheno` records belong to the `2018_Thiaw_dielmo_2015_arab` survey, while bioassays belong to `2018_Thiaw_dielmo_2015_sl` (Rule 6).

## Validator warnings

- geno_pheno #1 (pyrethroids, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #2 (pyrethroids, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #3 (pyrethroids, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #4 (pyrethroids, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: pyrethroids)
- geno_pheno #5 (DDT, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #6 (DDT, kdr L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #7 (DDT, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #8 (DDT, kdr L1014S, dead): not linked to a single bioassay (insecticide as reported: DDT)
