# Extraction record — s12889_019_7767_0

- Extracted: 2026-10-08
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 18 · Geno-pheno rows: 2

## Decisions

### Extraction Decisions
- **Survey definition**: A single survey record `s12889_019_7767_0_magu_2014` covers the sampling in Magu District, Mwanza Region, Tanzania across January to September 2014.
- **Control strains**: Kisumu reference strain controls were excluded per Rule 5.
- **Bioassays**: 18 WHO tube tests extracted from Table 4, across 3 seasons (long rains, dry season, short rains) for 6 insecticide exposures.
- **Inconsistencies**: Noted minor mismatches between exposed/survived counts and printed mortality percentages for Etofenprox in Table 4 (long rains: 4 survived / 60 exposed printed as 95%; short rains: 2 survived / 60 exposed printed as 100%).
- **Genotypes & Phenotypes**: Genotyping for kdr-west (L995F) and kdr-east (L995S) was performed on 130 mosquitoes that survived insecticide exposures pooled across tests/seasons. Because these are split by phenotype (survivors/alive), they are extracted in `geno_pheno` with `bioassay_id = null` and `insecticide` listed as the combination of exposed insecticides.

## Validator warnings

- bioassay s12889_019_7767_0_magu_2014_lr_etofenprox_05: inconsistent in the paper (values kept as printed) — Table 4 reports 60 exposed and 4 survived (56 dead), but reported mortality is printed as 95% (expected 93.33%).
- bioassay s12889_019_7767_0_magu_2014_sr_etofenprox_05: inconsistent in the paper (values kept as printed) — Table 4 reports 60 exposed and 2 survived (58 dead), but reported mortality is printed as 100% (expected 96.67%).
- bioassay s12889_019_7767_0_magu_2014_sr_etofenprox_05: computed mortality 96.7% differs from reported 100.0% (Abbott correction?)
- bioassay s12889_019_7767_0_magu_2014_sr_cyfluthrin_015: computed mortality 93.3% differs from reported 97.0% (Abbott correction?)
- geno_pheno #1 (permethrin + deltamethrin + lambdacyhalothrin + etofenprox + cyfluthrin + DDT, Vgsc kdr-west, alive): not linked to a single bioassay (insecticide as reported: permethrin + deltamethrin + lambdacyhalothrin + etofenprox + cyfluthrin + DDT)
- geno_pheno #2 (permethrin + deltamethrin + lambdacyhalothrin + etofenprox + cyfluthrin + DDT, Vgsc kdr-east, alive): not linked to a single bioassay (insecticide as reported: permethrin + deltamethrin + lambdacyhalothrin + etofenprox + cyfluthrin + DDT)
