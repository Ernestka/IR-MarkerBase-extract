# Extraction record — 2018_Salako_Insecticide_Resistance_Status_Frequency_L1014F_PMID30509288

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 24 · Bioassays: 30 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions for Salako et al. (2018)

1. **Surveys & Sampling**: Mosquitoes were collected as larvae/pupae by dipping in 6 districts of northern Benin (Kandi, Gogounou, Segbana in Alibori region; Djougou, Copargo, Ouake in Donga region) during the rainy season (June–October 2016).
2. **Species & Bioassays**: Bioassays were conducted using standard WHO tube bioassays on reared adult females (unidentified *An. gambiae (s.l.)*). Separate s.l. survey records were created for bioassays per district. Subsets of bioassay mosquitoes were subsequently identified by PCR to *An. gambiae* s.s. and *An. coluzzii*, and genotyped for target markers.
3. **Genotypes**: Tables 3 and 4 present raw genotype counts for *kdr* L1014F (Vgsc L995F) and *Ace-1* G119S (Ace-1 G280S) split by molecular species (*An. gambiae* s.s. and *An. coluzzii*) for each district. Twelve species-specific survey records were created to hold these genotype data.
4. **Genotype-Phenotype**: Table 2 provides molecular species identification split by dead and live status after bioassays, but does not provide target marker genotype counts split by bioassay outcome. Thus, no target marker entries were added to `geno_pheno`.
5. **Omitted Data**: Biochemical assay results and laboratory reference strains (Kisumu) were excluded per instructions. Bounding coordinate ranges given in the text were not converted to point coordinates; spatial precision was set to 'admin2'.
