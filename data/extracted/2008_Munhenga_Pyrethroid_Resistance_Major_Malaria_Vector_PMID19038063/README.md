# Extraction record — 2008_Munhenga_Pyrethroid_Resistance_Major_Malaria_Vector_PMID19038063

- Extracted: 2026-11-10
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 3 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Surveys**: Two surveys were established based on the two collection periods reported in Gwave village (Gokwe South District, Midlands Province, Zimbabwe): February 2006 and January 2008.
- **Coordinates**: Coordinates for Gwave (17°55' S, 28°41' E) were provided in the text (Page 2) and converted to decimal degrees: latitude -17.916667, longitude 28.683333.
- **Target Markers**: 
  - Vgsc L1014F (Leu-Phe) and L1014S (Leu-Ser): 54 individuals were initially tested by allele-specific PCR, which gave non-specific bands. Direct sequencing of the IIS6 domain in 38 individuals (inclusive of 6 cross-resistant specimens) confirmed the complete absence of both L1014F and L1014S (all 38 were wild-type SS). Corrected target marker names to standard `Vgsc L1014F` and `Vgsc L1014S` per standard schema requirements.
  - Ace-1 G119S: Seven specimens showing altered AChE inhibition profiles were sequenced; all 7 were wild-type (SS) with no G119S mutation detected.
- **Bioassays**: Standard WHO tube bioassays on wild-collected/larval-reared An. arabiensis from Table 2 were extracted for February 2006 and January 2008. Dead and alive counts were not printed in Table 2 (only total tested and mortality percentages were printed), so `dead_alive_printed = false` and `n_dead` / `n_alive` are left null.
- **Isofemale F1 family bioassays (Table 3)**: Table 3 provides family-by-family bioassay results for F1 isofemale lines. In line with extraction rules, these are not extracted as separate survey-level bioassays since the field population bioassays are reported in Table 2.
- **Geno-Pheno**: Although kdr was assayed in bioassay survivors and non-survivors, separate genotype counts for dead vs alive individuals were not reported. Therefore, `geno_pheno` is empty.
