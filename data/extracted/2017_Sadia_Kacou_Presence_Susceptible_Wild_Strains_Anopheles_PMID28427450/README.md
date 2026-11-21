# Extraction record — 2017_Sadia_Kacou_Presence_Susceptible_Wild_Strains_Anopheles_PMID28427450

- Extracted: 2026-11-21
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 4 · Bioassays: 10 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - One survey (`2017_Sadia_Kacou_ehania_2013_sl`) covers the WHO tube bioassays performed at the An. gambiae s.l. complex level in Ehania-V1 (June–July 2013).
   - Two separate surveys (`2017_Sadia_Kacou_ehania_2013_gam` and `2017_Sadia_Kacou_ehania_2013_col`) cover the molecular species-specific genotype collections (An. gambiae s.s. and An. coluzzii, respectively).

2. **Coordinates**:
   - Page 2 text states: `longitude: 5°14′N, latitude: 2°46′W`. In geographic reality, 5°14'N corresponds to latitude (5.233333° N) and 2°46'W corresponds to longitude (-2.766667° W). The values were converted directly into decimal degrees.

3. **Genotypes**:
   - Extracted from Table 3 for `kdr L1014F` and `ace-1R G119S` for both species.
   - L1014S was tested by PCR but stated in text as absent/not detected, so only L1014F and G119S count entries are extracted from Table 3.
   - In Table 3 under the `ace-1R G119S` header, the column heading for reported frequency prints `F(1014F)` instead of `F(119S)` (a minor printing typo in the original paper header); the reported numerical frequency matches G119S allele count.

4. **Bioassays & Synergist Bioassays**:
   - Standard 24h mortality bioassay counts (exposed, dead) are extracted from Table 1.
   - Synergist PBO assays are extracted from text/Fig 2 with `reported_mortality_pct` recorded and exposed/dead count fields left null as per Rule 2 (counts not printed).
