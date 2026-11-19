# Extraction record — 2016_Etang_When_Intensity_Deltamethrin_Resistance_Anopheles_PMID26951758

- Extracted: 2026-11-19
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 6 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions:

1. **Survey Splitting**:
   - Created four survey records for the Pitoa collection site (August 2011 collection):
     - `2016_Etang_Pitoa_2011_sl`: An. gambiae s.l. (used to link field bioassays performed on unseparated An. gambiae s.l.).
     - `2016_Etang_Pitoa_2011_col`: An. coluzzii (for molecular species-specific genotyping in Table 3).
     - `2016_Etang_Pitoa_2011_gam`: An. gambiae s.s. (for molecular species-specific genotyping in Table 3).
     - `2016_Etang_Pitoa_2011_ara`: An. arabiensis (for molecular species-specific genotyping in Table 3).

2. **Target Markers & Genotypes**:
   - Marker *kdr* L1014F (mapped to Vgsc L995F) and *kdr* L1014S (mapped to Vgsc L995S) were genotyped using HOLA on 154 control (unexposed) mosquitoes.
   - Genotype breakdown in Table 3:
     - *An. coluzzii* (N=19): 6 SS (L/L), 13 RS (L/F), 0 RR (F/F) for L1014F (frequency = 34%). All 19 were SS for L1014S.
     - *An. gambiae s.s.* (N=3): 3 SS (L/L) for both L1014F and L1014S.
     - *An. arabiensis* (N=132): 132 SS (L/L) for both L1014F and L1014S.

3. **Bioassays**:
   - Extracted standard WHO tube susceptibility bioassays (Table 1: DDT 4%, deltamethrin 0.05%, permethrin 0.75%) and intensity tests across deltamethrin working concentrations (Table 2: 0.001%, 0.005%, 0.01%, 0.1%, 0.5%).
   - Excluded Kisumu laboratory susceptible reference strain bioassays per rules.
   - Bioassay mortality percentages were given in Table 1 and text for 0.001%, 0.05%, 0.1%, and 0.5%; raw dead/alive counts were not explicitly printed in tables, so `dead_alive_printed` is set to `false` and counts left `null`.

4. **Geno-Pheno**:
   - No genotype-phenotype data extracted because genotyping was performed exclusively on unexposed control mosquitoes.
