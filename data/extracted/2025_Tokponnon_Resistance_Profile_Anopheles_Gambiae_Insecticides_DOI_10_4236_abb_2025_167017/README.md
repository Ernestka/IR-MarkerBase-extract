# Extraction record — 2025_Tokponnon_Resistance_Profile_Anopheles_Gambiae_Insecticides_DOI_10_4236_abb_2025_167017

- Extracted: 2026-10-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 12 · Genotype rows: 24 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Extraction Notes

1. **Surveys & Species Breakdown:**
   - Surveys were conducted in December 2022 across eight localities in southern Benin (Adjarra, Adjohoun, Sô-Ava, Ouidah, Placodji, Gbégamey, Ayélawadjè, Zogbo).
   - Molecular identification (SINE PCR) detected two species within the *Anopheles gambiae* complex: *An. coluzzii* (predominant/100% at all sites) and *An. gambiae* s.s.
   - Surveys were created at the finest spatial and species resolution available (site x molecular species).

2. **Genotypes:**
   - Target markers extracted from Table 3 (*kdr* L1014F) and Table 4 (*ace-1* G119S).
   - In Table 3 for Ouidah *An. coluzzii*, RR (17) + RS (8) + SS (2) sum to 27, whereas N tested is printed as 28. The printed allele frequency of 0.75 matches N = 28 if SS were 3. This printed mismatch was recorded as an `inconsistency_note` following Rule 8.

3. **Bioassays:**
   - Exact mortality percentages for chlorfenapyr (100 µg) CDC bottle bioassays were explicitly reported in the text (100% across all sites except Adjohoun at 98%) and extracted.
   - WHO tube bioassays with pyrethroids (permethrin, deltamethrin, alpha-cypermethrin) with and without PBO were presented only as bar graphs (Figures 2–4) and as ranges across grouped sites in the text, without site-by-site printed numeric mortality values. To adhere strictly to Rule 8 (avoiding estimation from figures when precise numbers are not printed), pyrethroid bioassays were omitted.

## Validator warnings

- genotype #6 (2025_Tokponnon_ouidah_2022_col, kdr L1014F): inconsistent in the paper (values kept as printed) — RR (17) + RS (8) + SS (2) = 27, which contradicts N = 28. The printed allele frequency of 0.75 matches N = 28 if SS were 3.
- genotype #6 (2025_Tokponnon_ouidah_2022_col, kdr L1014F): RR+RS+SS = 17+8+2 = 27 but n_genotyped = 28
- genotype #6 (2025_Tokponnon_ouidah_2022_col, kdr L1014F): computed allele freq 0.778 differs from reported 0.75
