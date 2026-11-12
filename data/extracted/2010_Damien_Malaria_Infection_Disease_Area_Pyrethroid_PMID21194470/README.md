# Extraction record — 2010_Damien_Malaria_Infection_Disease_Area_Pyrethroid_PMID21194470

- Extracted: 2026-11-12
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

- **Surveys & Resolution**: The study collected mosquitoes across 7 villages in the Ouidah-Kpomassè-Tori Bossito health district in southern Benin. Entomological and molecular data (Vgsc 1014F *kdr* frequency) are reported pooled across the district, broken down by molecular forms (M form = *An. coluzzii*, S form = *An. gambiae s.s.*). Therefore, two surveys were created at the district level.
- **Genotype Data**: The paper reports only point estimates and 95% CIs for the 1014F allele frequency in M form (0.47) and S form (0.61). It does not report raw genotype counts (RR, RS, SS) or exact sample sizes genotyped per molecular form. Per Rule 2, counts are left `null` and frequencies recorded directly in `reported_allele_freq`.
- **Spatial Coordinates**: Although Table 1 provides coordinates for each of the 7 individual villages, latitude/longitude are left `null` for the survey records because the *kdr* allele frequencies are aggregated across all 7 villages at the district level (`spatial_precision` = 'admin2').
- **Bioassays & Geno-Pheno**: No susceptibility bioassays or genotype-phenotype association testing were conducted in this study.

## Validator warnings

- genotype #1 (2010_Damien_Ouidah_2007_2008_m_form, Vgsc L1014F): frequency only (no raw counts)
- genotype #2 (2010_Damien_Ouidah_2007_2008_s_form, Vgsc L1014F): frequency only (no raw counts)
