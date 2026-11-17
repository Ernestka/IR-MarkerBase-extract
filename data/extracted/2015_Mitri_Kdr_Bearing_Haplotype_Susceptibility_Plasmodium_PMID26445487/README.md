# Extraction record — 2015_Mitri_Kdr_Bearing_Haplotype_Susceptibility_Plasmodium_PMID26445487

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 1 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Decisions
- **Site and sampling**: Mosquitoes were collected as larvae in Goundry, Burkina Faso (12°30′N, 1°20′W) in 2007 and 2008 and reared to adults. The sample of 363 individuals comprised 46 An. gambiae, 53 An. coluzzii, and 264 Goundry form mosquitoes.
- **Marker reporting**: The study investigates the ~3.3 Mb Pfin6 haplotype containing the *para* (*Vgsc*) gene. Haplotype allele HapA carries the *kdr* L1014F mutation. For the Goundry form (n=264), the paper explicitly reports 84 mosquitoes homozygous for HapA (HapA/HapA = RR) and 180 mosquitoes with all other haplotypes (HapA/HapB and HapB/HapB pooled together). Consequently, `rr` is set to 84, `n_genotyped` to 264, and `rs` and `ss` are left null as they cannot be distinguished from the pooled count of 180.
- **Other taxa**: For An. gambiae, *kdr* is reported as 'essentially fixed' without raw counts; for An. coluzzii, the sample size was noted as insufficient for association testing and no counts are reported. Thus, no genotype rows could be extracted for these two groups.
- **Phenotype assays**: The phenotypic assays in this paper evaluate *Plasmodium falciparum* oocyst susceptibility (natural gametocyte membrane feeding), not insecticide susceptibility. There are no insecticide bioassays conducted in this study; hence `bioassays` and `geno_pheno` are empty arrays.
