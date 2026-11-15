# Extraction record — 2012_Dabire_Population_Dynamics_Anopheles_Gambiae_Bobo_PMID22721002

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 11 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys**: Separate surveys were established for bioassays (An. gambiae s.l. at two time windows: September 2008 and November 2008, for Kodéni and Dioulassoba) and for population genotype frequencies (per site and molecular species across the May-December 2008 collection period).
- **Genotypes**: Genotype counts for `kdr L1014F` (Table 4) and `ace-1R` (G119S, Table 5) were reported pooled across insecticide-exposed specimens (survivors and dead). Thus, they were extracted into `genotypes` with `pooled = true` to avoid double-counting.
- **Bioassays**: Extracted from Table 2 for four insecticides (4% DDT, 0.75% permethrin, 0.05% deltamethrin, 0.1% bendiocarb) tested at two time points (September and November 2008). Mortality percentages were recorded; `dead_alive_printed` set to false as exact dead/alive counts were not explicitly printed in Table 2.
- **Exclusions**: Kisumu lab reference strain control bioassays were excluded as per Rule 5.
