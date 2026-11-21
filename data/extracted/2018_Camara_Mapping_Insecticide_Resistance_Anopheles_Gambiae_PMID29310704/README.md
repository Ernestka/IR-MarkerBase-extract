# Extraction record — 2018_Camara_Mapping_Insecticide_Resistance_Anopheles_Gambiae_PMID29310704

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 18 · Genotype rows: 24 · Bioassays: 12 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Primary Data Selection**: Extracted primary field survey data collected across 35 sentinel sites in Côte d'Ivoire (2013–2015). Excluded secondary literature review sites referenced in Tables 1–3 (e.g., Ref [24], [54], [55], [56]).
- **Surveys & Resolution**: Created surveys at the molecular species level (An. coluzzii, An. gambiae s.s.) where reported in Table 3, and at the An. gambiae s.l. level for bioassays in Tables 1 and 2. Followed Rule 7 to avoid double counting species breakdown vs total population.
- **Genotypes**: Marker names extracted as printed ('kdr L1014F' for Vgsc L995F, 'ace-1R G119S' for Ace-1 G280S). Genotyping was performed on unexposed control mosquitoes, so no geno_pheno records apply. As Table 3 reports sample sizes ($n$) and allele frequencies ($F$) rather than genotype counts, count fields (RR/RS/SS) were left null per Rule 2.

## Validator warnings

- genotype #1 (2018_Camara_Abengourou_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2018_Camara_Abengourou_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #3 (2018_Camara_Abengourou_gam, Vgsc L1014F): frequency only (no raw counts)
- genotype #4 (2018_Camara_Abengourou_gam, Ace-1 G119S): frequency only (no raw counts)
- genotype #5 (2018_Camara_Bondoukou_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #6 (2018_Camara_Bondoukou_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #7 (2018_Camara_Bondoukou_gam, Vgsc L1014F): frequency only (no raw counts)
- genotype #8 (2018_Camara_Bondoukou_gam, Ace-1 G119S): frequency only (no raw counts)
- genotype #9 (2018_Camara_GrandBassam_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #10 (2018_Camara_GrandBassam_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #11 (2018_Camara_GrandBassam_gam, Vgsc L1014F): frequency only (no raw counts)
- genotype #12 (2018_Camara_GrandBassam_gam, Ace-1 G119S): frequency only (no raw counts)
- genotype #13 (2018_Camara_Korhogo_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #14 (2018_Camara_Korhogo_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #15 (2018_Camara_Korhogo_gam, Vgsc L1014F): frequency only (no raw counts)
- genotype #16 (2018_Camara_Korhogo_gam, Ace-1 G119S): frequency only (no raw counts)
- genotype #17 (2018_Camara_Mbe_sl, Vgsc L1014F): frequency only (no raw counts)
- genotype #18 (2018_Camara_Mbe_sl, Ace-1 G119S): frequency only (no raw counts)
- genotype #19 (2018_Camara_PortBouet_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #20 (2018_Camara_PortBouet_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #21 (2018_Camara_Yamoussoukro_col, Vgsc L1014F): frequency only (no raw counts)
- genotype #22 (2018_Camara_Yamoussoukro_col, Ace-1 G119S): frequency only (no raw counts)
- genotype #23 (2018_Camara_Yamoussoukro_gam, Vgsc L1014F): frequency only (no raw counts)
- genotype #24 (2018_Camara_Yamoussoukro_gam, Ace-1 G119S): frequency only (no raw counts)
