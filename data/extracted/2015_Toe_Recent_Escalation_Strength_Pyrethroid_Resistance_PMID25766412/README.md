# Extraction record — 2015_Toe_Recent_Escalation_Strength_Pyrethroid_Resistance_PMID25766412

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 12 · Bioassays: 0 · Geno-pheno rows: 16

## Decisions

### Study and Surveys
- Collections were conducted across two sites in south-west Burkina Faso: Vall	ee du Kou 7 (VK7, 11		39'N, 04		41'W) and Tengrela (10		40'N, 4		50'W).
- Longitudinal time windows reported in Table 1 are Jul-11, Oct-11, Jun-12, Jul-13 for VK7, and Jul-12, Jul-13 for Tengrela. Six individual surveys were defined accordingly.
- Species molecularly confirmed via SINE-PCR as Anopheles coluzzii (formerly An. gambiae M molecular form).
- Wild larvae were collected from breeding sites and reared to adults at CNRFP.

### Genotypes and Phenotype-Split Genotyping
- Table 1 reports allele counts (L, F for L1014F; N, Y for N1575Y), total allele counts (n alleles), and allele frequencies for unexposed controls, bioassay dead, and bioassay survivors.
- Control samples are recorded in `genotypes` with resistant_allele_count (count of F or Y alleles) and reported_allele_freq. Diploid genotype classes (RR, RS, SS) and individual mosquito counts were not tabulated (only n alleles), so rr, rs, ss, and n_genotyped are left null in accordance with Rule 2 and Rule 8.
- Bioassay dead and survivor samples are recorded in `geno_pheno` (Rule 6) with phenotype_group 'dead' and 'alive', respectively. Because diploid genotype classes are not reported, rr, rs, ss, and n are left null, and reported_allele_freq is recorded.
- L1014S (Vgsc L995S): The authors state in the text (page 4) that 'The 1014S kdr allele was not found in any sample.' Because individual allele counts or tabulated frequencies per collection/phenotype are not presented in Table 1, 1014S is omitted from the records and documented here.

### Bioassays
- Bioassay mortality percentages and exposed/dead counts are from previous studies (To	e et al. 2014, ref [5]) or not extractable as discrete tests here; therefore `bioassays` is left empty and geno_pheno records have `bioassay_id = null` and `insecticide = 'deltamethrin'` as specified in Rule 6.

## Validator warnings

- geno_pheno #1 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, kdr N1575Y, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #3 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #4 (deltamethrin, kdr N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #5 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #6 (deltamethrin, kdr N1575Y, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #7 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #8 (deltamethrin, kdr N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #9 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #10 (deltamethrin, kdr N1575Y, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #11 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #12 (deltamethrin, kdr N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #13 (deltamethrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #14 (deltamethrin, kdr N1575Y, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #15 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #16 (deltamethrin, kdr N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
