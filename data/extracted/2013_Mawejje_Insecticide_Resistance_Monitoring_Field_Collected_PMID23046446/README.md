# Extraction record — 2013_Mawejje_Insecticide_Resistance_Monitoring_Field_Collected_PMID23046446

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 20 · Geno-pheno rows: 25

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Two distinct surveys were created for the two molecular species identified in Jinja, Uganda (Walukuba sub-county): `2013_Mawejje_jinja_2011_gam` for *Anopheles gambiae s.s.* and `2013_Mawejje_jinja_2011_arab` for *Anopheles arabiensis*.
   - Collection took place between July and October 2011.

2. **Target Markers & Mapping**:
   - Vgsc 1014S (maps to Vgsc L995S) and Vgsc 1014F (maps to Vgsc L995F) were extracted.
   - In Table 1, genotype categories LL, LS, SS, FS represent: LL = L/L (susceptible homozygote), LS = L/S (heterozygote), SS = S/S (resistant homozygote for 1014S), and FS = F/S (heterozygote for 1014F and 1014S).
   - Per Rule 4b, L995S and L995F are extracted separately. For L995S, SS (wild-type L/L) = LL, RS = LS + FS, RR = SS. For L995F, 1 F/S carrier in Table 1 (Permethrin female alive) is recorded as RS=1, RR=0, SS=167.

3. **Population Genotypes**:
   - Extracted baseline/overall population frequencies from text for 1014S in *An. arabiensis* (4 L/S in 2988 tested) and *An. gambiae s.s.* (95.04%), as well as 1014F screening (1 S/F in 150 *An. gambiae s.s.*, 0 in 126 *An. arabiensis*).

4. **Bioassays**:
   - Diagnostic 1h WHO tube bioassays reported in Figure 2 and text were extracted with exact `n_exposed` and `reported_mortality_pct`. Dead/alive counts were left null as per Rule 2 since only mortality percentages and exposed counts were printed.

5. **Geno-Pheno Linkage**:
   - Table 1 genotype counts were extracted into `geno_pheno`. Since mosquitoes in Table 1 represent pooled exposure times across standard bioassays and time-response LT50 tests, `bioassay_id` is set to null per Rule 6.

## Validator warnings

- genotype #2 (2013_Mawejje_jinja_2011_gam, Vgsc 1014S): frequency only (no raw counts)
- geno_pheno #1 (permethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #2 (permethrin, Vgsc 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #3 (permethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #4 (permethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #5 (permethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #6 (DDT, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #7 (DDT, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #8 (DDT, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #9 (DDT, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #10 (deltamethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #11 (deltamethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #12 (deltamethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #13 (deltamethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #14 (permethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #15 (permethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #16 (permethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #17 (permethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #18 (DDT, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #19 (DDT, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #20 (DDT, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #21 (DDT, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #22 (deltamethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #23 (deltamethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #24 (deltamethrin, Vgsc 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #25 (deltamethrin, Vgsc 1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
