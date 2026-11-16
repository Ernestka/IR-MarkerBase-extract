# Extraction record — 2014_Abdalla_Insecticide_Resistance_Anopheles_Arabiensis_Sudan_PMID24886129

- Extracted: 2026-11-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 6

## Decisions

### Summary of Decisions

1. **Survey Definition**:
   - Genotype data in Table 4 are pooled across four sentinel sites in Gezira state (Wad Medani, Elmanagil, Wad Elhadad, Rufaa) and across all six biannual collection rounds (2008–2011).
   - A single aggregated survey `2014_Abdalla_gezira_2008_2011` was created to represent these pooled collections.

2. **Genotype Data**:
   - Genotypes for `kdr` / `L1014F` are reported separately for survivors (alive) and dead specimens from WHO bioassays with permethrin, deltamethrin, and DDT in Table 4.
   - These were extracted into `geno_pheno` with `bioassay_id` set to `null` because the mosquitoes were pooled across multiple bioassays and collection rounds.
   - Screening for `L1014S` was reported as negative across all specimens ('The L1014S mutation was not detected in any specimens'), but exact genotype counts were not separately tabulated for this negative finding.

3. **Bioassays**:
   - Bioassay results are depicted in Figure 2 as bar graphs showing % mortality per round per site, but printed numerical counts (n_exposed, n_dead) per individual bioassay test are not provided in the paper text or main tables.
   - To adhere strictly to rules against back-calculating bioassay counts from figures or incomplete text estimates, individual bioassay records were omitted.

4. **Target Loci**:
   - Microarray analysis results (differentially expressed detoxification genes such as CYP6P3, CYP6M2, GSTe4, CYP6Z3) were not extracted as they are transcriptomic measurements rather than target SNP/CNV/SV marker counts.

## Validator warnings

- geno_pheno #1 (permethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #2 (permethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #3 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #4 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #5 (DDT, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #6 (DDT, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: DDT)
