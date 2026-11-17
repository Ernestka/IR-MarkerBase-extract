# Extraction record — 2014_Kabula_Co_Occurrence_Distribution_East_L1014S_PMID24386946

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 19 · Genotype rows: 38 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Key Decisions
1. **Surveys**: 14 sentinel districts in Tanzania were sampled in June–July 2011. For each site, 25 mosquitoes (total 350) were molecularly identified to species using PCR (Collins et al. 1987; Scott et al. 1993). In five sites (Handeni, Ilala/Dar es Salaam, Babati, Muheza, Muleba), both *An. gambiae s.s.* and *An. arabiensis* were found, yielding two surveys per site. In the remaining nine sites, only one molecular species was detected (25 specimens each). Thus, exactly 19 surveys were created at the finest spatial and molecular species level.
2. **Collection method & population type**: Text on page 3 specifies that adult female mosquitoes were collected by indoor-resting catch in most sites, except in Tabora (Uyui), Lushoto, and Muleba where larval collections were reared to adults due to insufficient adult density. These three sites are coded as `wild_reared` (generation `F0`, collection method `larval collection`); all others are coded as `wild_adult` (collection method `indoor resting catch`).
3. **Genotype extraction**: Genotype counts for `kdr` `L1014S` and `L1014F` are extracted from Table 2 and Table 3 directly at the site and molecular species resolution (38 genotype records across the 19 surveys). In Muleba *An. gambiae s.s.*, 5 individuals carried L1014S homozygous resistant (RR) and 3 carried L1014F heterozygous (RS), with 16 wild-type for L1014S and 18 wild-type for L1014F.
4. **Bioassay and geno_pheno exclusion**:
   - Bioassay results in Figure 4 were performed on unseparated *An. gambiae s.l.* field populations, not by molecular species. In four sites (Magu, Babati, Moshi, Dodoma rural), mortality results were explicitly adapted from Kabula et al. 2013 (secondary data). For six sites, mortalities are only reported as an aggregated range '98–100%' without exact counts. Only four sites had mortality percentages printed in text, but dead/alive counts were not printed. Because bioassays were conducted at the *An. gambiae s.l.* level and cannot be linked to the species-specific surveys, no bioassay records were extracted.
   - Table 4 presents L1014S and L1014F counts split by bioassay survivors vs dead mosquitoes, but only pooled across all 14 sites and both species. Table 5 presents totals pooled across all sites per species. Following extraction rule 7 (extracting at finest resolution, avoiding double-counting pooled totals) and rule 6, these national pooled summaries are not additionally extracted.
