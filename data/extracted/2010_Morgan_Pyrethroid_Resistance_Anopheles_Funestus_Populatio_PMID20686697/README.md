# Extraction record — 2010_Morgan_Pyrethroid_Resistance_Anopheles_Funestus_Populatio_PMID20686697

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 7 · Geno-pheno rows: 4

## Decisions

### Data Extraction Notes

1. **Survey Pooling**: Indoor-resting blood-fed female *An. funestus s.s.* were collected in April and November 2009 in Tororo District, Uganda. F1 progeny from both collection periods were pooled together and reared for bioassays and molecular analyses. A single survey record was created for Tororo covering April-November 2009.
2. **Bioassays**: Extracted from Table 2 for total sample size (combined males and females) across 7 WHO bioassay tests (permethrin 0.75%, deltamethrin 0.05%, DDT 4%, bendiocarb 0.01%, dieldrin 4%, malathion 5%, and PBO + permethrin 0.75%). Exact counts of dead/alive were not printed (only n_exposed and % mortality), so `dead_alive_printed` is set to false.
3. **Genotype Data**: Sequencing of exon 20 spanning codon 1014 of the VGSC gene was conducted on 19 mosquitoes (13 resistant: 5 DDT resistant + 8 permethrin resistant, and 6 susceptible). No mutations were detected at codon 1014 (100% 1014L wild-type). Per Rule 6, because all genotyped mosquitoes were split by phenotype (alive vs dead), they are extracted into `geno_pheno` (13 alive, 6 dead), and `genotypes` is left empty to avoid double-counting.
4. **Expression Data**: RT-PCR profiling for P450 genes (CYP6P9b, etc.) and biochemical assays were reported in the paper but do not include DNA target marker genotypes, so they are excluded per extraction schema.

## Validator warnings

- geno_pheno #1 (DDT + permethrin, VGSC L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin)
- geno_pheno #2 (DDT + permethrin, VGSC L1014S, alive): not linked to a single bioassay (insecticide as reported: DDT + permethrin)
- geno_pheno #3 (no insecticide, VGSC L1014F, dead): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #4 (no insecticide, VGSC L1014S, dead): not linked to a single bioassay (insecticide as reported: none given)
