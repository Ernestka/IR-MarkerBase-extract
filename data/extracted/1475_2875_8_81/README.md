# Extraction record — 1475_2875_8_81

- Extracted: 2026-10-15
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 2 · Geno-pheno rows: 4

## Decisions

### Survey and Species Resolution
- Mosquitoes were collected as indoor resting gravid/blood-fed females across three ecological zones in Kassena-Nankana District, Upper East Region, Ghana between November 2006 and October 2007 (dry and wet seasons). F1 progeny were reared and tested.
- Sibling species determination on 192 Anopheles gambiae s.l. identified all 192 as the molecular M form (now An. coluzzii).
- Two surveys are created: one for An. gambiae (molecular M form / An. coluzzii, N = 5676 total tested) and one for An. funestus (N = 4073 total tested).
- Precise point coordinates are not provided; the paper states a bounding box (10°30' to 11°00'N, 1°00' to 1°30'W), so latitude and longitude are left null with precision set to admin2.

### Bioassays
- Table 1 reports '% knock-down after 1 hour exposure' for pyrethroids and DDT, not 24-hour mortality. Per Rule 8b, knockdown-only assays are skipped.
- 24-hour mortality percentages are explicitly printed in the text for DDT 4% by species: An. gambiae (1068 exposed, 79.1% mortality) and An. funestus (569 exposed, 83.5% mortality). These two bioassays were extracted.
- Pyrethroid 24-hour mortalities are shown only in Figure 3 as a bar chart without printed values, and in Table 2 pooled across An. gambiae and An. funestus. To avoid guessing unprinted values from Figure 3 and to avoid multi-taxa pooled records, these are not extracted as bioassays.

### Genotypes and Geno-Pheno
- A subsample of 192 An. gambiae (all molecular M form) were genotyped for the kdr mutation (Vgsc L995F, L1014F) using the Fanello et al. (2003) PCR assay with primers Agd1, Agd2, Agd3, Agd4. No kdr mutation was detected in any mosquito (all 192 were homozygous susceptible SS / wild-type).
- All 192 genotyped mosquitoes originated from bioassay outcomes: 148 survivors (67 DDT, 17 deltamethrin, 64 permethrin) and 44 susceptible (dead) mosquitoes. In accordance with Rule 6, all 192 are recorded in `geno_pheno` and none in `genotypes` to avoid double counting.
- The 67 DDT survivors link directly to the extracted DDT bioassay (`1475_2875_8_81_kassena_gambiae_ddt`). The deltamethrin and permethrin survivors have bioassay_id set to null because those bioassays lack 24h mortality data in the text/tables. The 44 susceptible mosquitoes have bioassay_id and insecticide set to null as their specific bioassay exposure was not specified individually.
- The marker was updated from 'kdr' to 'L1014F' (gene: 'kdr', marker: 'L1014F', mapping to target marker Vgsc L995F).

## Validator warnings

- geno_pheno #2 (deltamethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #3 (permethrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #4 (no insecticide, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: none given)
