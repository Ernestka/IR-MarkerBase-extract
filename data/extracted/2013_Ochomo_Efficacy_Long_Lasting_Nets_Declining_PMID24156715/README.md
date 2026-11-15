# Extraction record — 2013_Ochomo_Efficacy_Long_Lasting_Nets_Declining_PMID24156715

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 1 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Split by study site (Bungoma District vs Gem District in western Kenya) and mosquito source/population type:
     - `2013_Ochomo_bungoma_2013_nets`: Wild adult *An. gambiae s.s.* resting inside bed nets in Bungoma.
     - `2013_Ochomo_bungoma_2013_f1`: F1 progeny of wild females resting inside nets in Bungoma, used for WHO tube tests and net cone bioassays.
     - `2013_Ochomo_bungoma_2013_larvae`: Wild-reared adults from larval collections in Bungoma.
     - `2013_Ochomo_gem_2013_larvae`: Wild-reared adults from larval collections in Gem.
   - Coordinates provided in text for Gem (0°07′30.06″N, 34°24′32.56″E -> 0.125017, 34.409044) and Bungoma (0°35′20.85″N, 34°29′13.23″E -> 0.589125, 34.487008).

2. **Genotypes**:
   - Target marker: `kdr` / `1014S` (Vgsc L995S). All 343 *An. gambiae s.s.* mosquitoes collected resting inside nets in Bungoma were homozygous for the `1014S` mutation (`rr` = 343, `rs` = 0, `ss` = 0).

3. **Bioassays**:
   - Cone bioassays conducted on field-collected LLINs using the laboratory reference strain *An. gambiae s.s.* Kisumu (Table 4) were excluded per Rule 5 (lab strains are controls, not data).
   - Cone bioassays on new unused LLINs (Olyset and PermaNet 2.0) tested on field F1 progeny from Bungoma nets were extracted.
   - WHO tube bioassays with deltamethrin and permethrin on Bungoma F1 progeny, Bungoma larvae, and Gem larvae were extracted with reported mortality percentages. Exact `n_exposed` was not printed for the tube bioassays, so `n_exposed`, `n_dead`, and `n_alive` were set to `null` per Rule 2.
