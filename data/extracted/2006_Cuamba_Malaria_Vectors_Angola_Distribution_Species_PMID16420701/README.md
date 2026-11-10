# Extraction record — 2006_Cuamba_Malaria_Vectors_Angola_Distribution_Species_PMID16420701

- Extracted: 2026-11-10
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 9 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Marker Naming Correction**:
   - In the previous output, `gene` and `marker` were both set to `kdr`. Corrected `marker` to `L1014F` (the West African kdr mutation assayed via the Martínez-Torres et al. 1998 protocol) so that it matches the target marker definition Vgsc L995F / L1014F.

2. **Surveys & Genotypes Breakdown**:
   - Genotype data for the West African *kdr* mutation (Vgsc L1014F) assayed via PCR (Martínez-Torres et al. 1998) were reported in Table 3 for 218 total *An. gambiae* s.s. mosquitoes across 5 sites (Cawango, Bela Vista, São Pedro, São Jose, Cazenga).
   - Data were separated into 9 distinct surveys representing site × molecular form (M-form/*An. coluzzii* and S-form/*An. gambiae s.s.*).
   - All 218 genotyped mosquitoes were homozygous susceptible (+/+). Thus, for each subgroup: `rr` = 0, `rs` = 0, `ss` = `n_genotyped`, and `reported_allele_freq` = 0.0.
   - Samples from Cacuaco (13 specimens) were not genotyped for *kdr* (Table 3 footnote) and are omitted from genotype records.

3. **Coordinates**:
   - Coordinates for all sites were explicitly stated in the text on Page 2 and converted from DMS to decimal degrees:
     - Funda: 08°51' S, 13°34' E -> -8.850000, 13.566667
     - Samba: 08°59' S, 13°15' E -> -8.983333, 13.250000
     - São Pedro: 12°20' S, 13°34' E -> -12.333333, 13.566667
     - Cawango & Bela Vista: 12°34' S, 13°24' E -> -12.566667, 13.400000
     - São Jose & Cazenga: 12°47' S, 15°44' E -> -12.783333, 15.733333

4. **Bioassays and Phenotype Data**:
   - No bioassays or genotype-phenotype links were conducted or reported in this study.
