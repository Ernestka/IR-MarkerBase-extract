# Extraction record — 2009_Anto_Insecticide_Resistance_Profiles_Malaria_Vectors_PMID19389257

- Extracted: 2026-11-11
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 15 · Geno-pheno rows: 4

## Decisions

### Data Extraction Decisions

1. **Marker Mapping**: The paper reports genotyping for the kdr gene using primers Agd1-Agd4 from Fanello et al. (2003), which assays the Vgsc L1014F (L995F / kdr-west) mutation. Changed `marker` from 'kdr' to 'L1014F' with `gene` 'Vgsc' to match the standard target marker schema.
2. **Surveys & Spatial Units**: Mosquitoes were collected in Kassena-Nankana District, Ghana. Data are extracted at two levels:
   - District-level An. coluzzii sample (molecular M form of An. gambiae s.s.) used for PCR genotyping of 192 individuals.
   - Three micro-ecological zone surveys (Irrigated, Lowland, Rocky highland) for bioassays extracted from Table 2.
3. **Genotypes vs. Geno-Pheno**: All 192 PCR-genotyped An. gambiae (An. coluzzii) mosquitoes were phenotyped in bioassays (148 survivors split into DDT: 67, deltamethrin: 17, permethrin: 64; and 44 susceptible/dead mosquitoes). Per Rule 6, these are extracted exclusively in `geno_pheno` to avoid double-counting. The `genotypes` array is empty.
4. **Genotype Results**: Zero kdr mutations were detected across all 192 tested individuals (all 192 are wild-type / SS).
5. **Bioassays**: Extracted 24h mortality bioassay data from Table 2 for 3 ecological zones across 5 insecticides (permethrin 0.75%, deltamethrin 0.05%, cyfluthrin 0.15%, lambda-cyhalothrin 0.1%, and DDT 4%). Table 1 (1-hour knockdown percentages) is omitted in favor of Table 2 24h mortality. Numbers of dead/alive were not printed in Table 2 (only total exposed and % mortality), so `dead_alive_printed` is set to `false` and counts left `null` per Rule 2.

## Validator warnings

- geno_pheno #1 (DDT, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #2 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #3 (permethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #4 (no insecticide, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: none given)
