# Extraction record — 2013_Nwane_Multiple_Insecticide_Resistance_Mechanisms_Anophel_PMID23433176

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 48

## Decisions

### Data Extraction Decisions

1. **Surveys & Resolution:**
   - Samples were collected between October 2008 and May 2009 from 6 localities in Cameroon: Nkolondom, Nkolbikon, Bonanloka, Campo, Makoutchietoum, and Pitoa.
   - Surveys were split at the finest resolution by locality and molecular species/form (An. gambiae S form, An. gambiae M form, and An. arabiensis).
   - Geographic coordinates printed on page 2 were converted from DMS to decimal degrees.

2. **Target Markers:**
   - Genotyping was conducted at the Vgsc 1014 locus (kdr-west 1014F / L995F and kdr-east 1014S / L995S).
   - In accordance with rule 4b, 1014F and 1014S are recorded as separate entries.
   - Gene name is given as `kdr` and markers as `1014F` and `1014S` as printed in Table 2 and Figure 3.

3. **Bioassays Array:**
   - Table 1 reports exposed sample sizes (N), knockdown times (kdT50, kdT95), and % suppression of knockdown (%kdts), but does NOT print numerical 24-hour post-exposure mortality counts (dead/alive) or printed mortality percentages (mortality is presented as a bar chart in Figure 2 without printed numeric values).
   - Per rule 8b, bioassays reporting only knockdown times without printed mortality numbers were skipped.

4. **Genotypes & Geno_Pheno Arrays:**
   - All genotyped specimens in this study were bioassay-tested and segregated into survivors (alive) and dead. Therefore, all genotype records are placed in `geno_pheno` and `genotypes` is left empty.
   - Table 2 prints sample size (N) and reported allele frequencies (f(1014L), f(1014F), f(1014S)) for survivors of DDT, permethrin, and deltamethrin. Raw counts were not back-calculated from percentages and `reported_allele_freq` is stored.
   - In cases where a group is 100% wild-type 1014L/1014L (e.g. An. arabiensis from Pitoa, and Campo M form permethrin survivors and dead), exact counts (rr=0, rs=0, ss=N) were explicitly stated in text.

## Validator warnings

- geno_pheno #1 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #2 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #3 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #4 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #5 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #6 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #7 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #8 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #9 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #10 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #11 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #12 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #13 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #14 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #15 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #16 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #17 (DDT, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #18 (DDT, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #19 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #20 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #21 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #22 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #23 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #24 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #25 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #26 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #27 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #28 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #29 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #30 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #31 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #32 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #33 (permethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #34 (permethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #35 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #36 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #37 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #38 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #39 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #40 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #41 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #42 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #43 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #44 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #45 (deltamethrin, kdr 1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #46 (deltamethrin, kdr 1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #47 (permethrin, kdr 1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #48 (permethrin, kdr 1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
