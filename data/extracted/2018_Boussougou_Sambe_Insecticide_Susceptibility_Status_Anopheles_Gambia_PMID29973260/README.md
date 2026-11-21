# Extraction record — 2018_Boussougou_Sambe_Insecticide_Susceptibility_Status_Anopheles_Gambia_PMID29973260

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 12 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Created 3 site-level surveys for *An. gambiae (s.l.)* to link WHO bioassays performed on field-reared adult mosquitoes.
   - Created 6 species-specific surveys (*An. coluzzii* and *An. gambiae s.s.* for each of Limbe, Tiko, Buea) to link target marker genotype counts.
   - Collection window: November to December 2015.
   - Coordinates were extracted directly as reported in Methods (Page 2) and converted from DMS to decimal degrees.

2. **Target Markers**:
   - Extracted Vgsc L1014F and L1014S (reported as `kdr` / `L1014F` and `L1014S`).
   - Genotype counts for L1014F (SS, SR, RR) and sample sizes were extracted directly from Table 3.
   - For L1014S, the text explicitly reports no L1014S allele was detected in any analyzed sample; all genotyped specimens were therefore homozygous susceptible (SS).

3. **Bioassays**:
   - Extracted 8 WHO susceptibility bioassays (deltamethrin 0.05%, permethrin 0.75%, malathion 5%) across the three sites.
   - Sample sizes `n` were taken from Table 1, and 24h mortality percentages were taken from Fig 1 / text.
   - Because exact raw counts for dead/alive were not explicitly printed for pyrethroids, `dead_alive_printed` is set to `false` and `n_dead` / `n_alive` are left `null` per rule 2.
   - For malathion in Limbe and Buea, 100% mortality was reported with a combined sample size of 228 across both sites; individual site sample sizes were not split, so `n_exposed` is left `null` for the individual malathion bioassays.

4. **Genotype-Phenotype Data (`geno_pheno`)**:
   - Genotype counts in Table 3 represent population samples not split by bioassay outcome.
   - Pooled allele frequencies mentioned in text (85.38% in resistant vs 80.26% in susceptible) were not broken down by site or species in the main text (detailed only in Additional File 1, which is not provided). Therefore, per rule 7, no pooled phenotype-genotype rows were recorded in `geno_pheno`.
