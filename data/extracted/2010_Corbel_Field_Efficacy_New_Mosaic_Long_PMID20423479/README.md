# Extraction record — 2010_Corbel_Field_Efficacy_New_Mosaic_Long_PMID20423479

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 1 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Surveys & Locations**:
   - Three experimental stations were evaluated: Malanville (Benin), Pitoa (Cameroon), and VK7 in Vallée du Kou (Burkina Faso).
   - Collection dates per site: September to November 2007 for Vallée du Kou; July to September 2008 for Malanville and Pitoa.
   - Coordinates reported in text: Malanville (11°87N, 03°38E), Pitoa (9°21N, 13°31E), and VK7 (11°24N, 4°24E). Coordinates were converted to decimal degrees where applicable; '11°87N' for Malanville was recorded as 11.87 as printed.

2. **Genotypes & Target Markers**:
   - Pre-trial baseline collections genotyped a sub-sample of 30 mosquitoes per locality for molecular species identification and the Vgsc L1014F (L995F) kdr mutation.
   - Table 1 reports kdr frequencies: 16% in Malanville (0.16 proportion), '<5%' in Pitoa, and '>80% %M' / '>80% %S' in Vallée du Kou.
   - Genotype records for Pitoa ('<5%') and Vallée du Kou ('>80%') were omitted because the paper reported kdr frequencies as inequality ranges rather than exact numeric values or genotype counts, which would otherwise result in empty/unparseable genotype records.

3. **Bioassays**:
   - Pre-trial WHO cylinder susceptibility tests (0.05% deltamethrin, 1 h exposure, 24 h holding period) were conducted on four batches of 25 unfed females (total 100 exposed per site).
   - Mortality percentages printed in Table 1: Malanville (85%), Pitoa (70%), Vallée du Kou (23%). `dead_alive_printed` is set to `false` and integer dead/alive counts are left null as they were not printed in the paper.
   - WHO cone bioassays in Table 2 were excluded as they were conducted on the laboratory reference strain (Kisumu).

## Validator warnings

- genotype #1 (2010_Corbel_Field_Efficacy_New_Mosaic_Long_PMID20423479_malanville_2008, kdr L1014F): frequency only (no raw counts)
