# Extraction record — 2025_02_14_637727v2_full

- Extracted: 2026-10-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 7 · Genotype rows: 26 · Bioassays: 1 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The paper evaluates the Ag-vampIR panel on 4 cohorts:
  1. Obuasi, Ghana (2017 field collection, Prokopak indoor aspiration, molecularly confirmed An. gambiae s.s.).
  2. Siaya colony, Kenya (established in 2023 from wild mosquitoes in Siaya County, An. gambiae s.s.).
  3. VK7 colony, Burkina Faso (established in 2014 from Valle de Kou, An. coluzzii).
  4. Upper River Region, The Gambia (2011 field collection, CDC light traps). Molecular identification delineated this cohort into An. arabiensis (n=45), An. coluzzii (n=17), and An. gambiae (n=4).
- Because Vgsc 995F and 995S frequencies in The Gambia are reported explicitly per molecular species in the text, separate species-specific surveys were created for An. arabiensis, An. coluzzii, and An. gambiae in The Gambia. Meanwhile, for other resistance markers shown in Figure 3B, frequencies are reported only for the pooled Gambian cohort, so an An. gambiae s.l. survey (`gambia_urr_2011_sl`) was created to hold those records without double-counting.

### Marker Extraction
- Only target markers listed in the prompt instructions were extracted:
  - Vgsc 995F (L995F)
  - Vgsc 995S (L995S)
  - Ace1 G280S
  - Cyp6p4 I236M
  - Rdl A296S
  - Rdl A296G
  - Cyp4j5 L43F
- Other markers reported in Figure 3B and text (Cyp6p3-I88T, Cyp6p1-L374M, Gste2-I114T, Gste2-L119V, TEP1, and selective sweep tag SNPs) are non-target markers and were ignored.
- Allele frequencies printed in Figure 3B and verbatim in the text (pages 8-10) were extracted into `reported_allele_freq`. Where resistant allele counts were explicitly printed in the text (e.g. Ace1 G280S: 1 in Gambia, 6 in Siaya, 0 in VK7), they were recorded in `resistant_allele_count`.

### Bioassays and Genotype-Phenotype Associations
- The Siaya colony underwent an extended WHO cone bioassay on PermaNet 2.0 (deltamethrin) with 40-minute exposure (n=252 exposed; 48.8% dead, 51.2% alive). Counts of dead and alive are not printed in the paper, so `dead_alive_printed = false`, and `n_dead` and `n_alive` are left null.
- In the genotype-phenotype association study (Figure 3C and text on page 11), results are reported as odds ratios and p-values from a GLM (e.g. Vgsc 995F OR=1.78; 995S OR=0.56; Cyp4j5 L43F OR=2.25; Cyp6p4 I236M OR=3.16-3.65) and machine learning model metrics, but genotype classes (RR/RS/SS) or carrier counts split by alive and dead phenotypes are not printed in the text or figures. Therefore, no `geno_pheno` records could be extracted.

## Validator warnings

- survey 2025_02_14_637727v2_full_kenya_siaya_2023: laboratory population — normally excluded
- survey 2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014: laboratory population — normally excluded
- genotype #1 (2025_02_14_637727v2_full_ghana_obuasi_2017, Ace1 G280S): frequency only (no raw counts)
- genotype #2 (2025_02_14_637727v2_full_ghana_obuasi_2017, Cyp6p4 I236M): frequency only (no raw counts)
- genotype #3 (2025_02_14_637727v2_full_ghana_obuasi_2017, Rdl A296S): frequency only (no raw counts)
- genotype #4 (2025_02_14_637727v2_full_ghana_obuasi_2017, Rdl A296G): frequency only (no raw counts)
- genotype #5 (2025_02_14_637727v2_full_ghana_obuasi_2017, Cyp4j5 L43F): frequency only (no raw counts)
- genotype #6 (2025_02_14_637727v2_full_kenya_siaya_2023, Vgsc 995F): frequency only (no raw counts)
- genotype #7 (2025_02_14_637727v2_full_kenya_siaya_2023, Vgsc 995S): frequency only (no raw counts)
- genotype #9 (2025_02_14_637727v2_full_kenya_siaya_2023, Cyp6p4 I236M): frequency only (no raw counts)
- genotype #10 (2025_02_14_637727v2_full_kenya_siaya_2023, Rdl A296S): frequency only (no raw counts)
- genotype #11 (2025_02_14_637727v2_full_kenya_siaya_2023, Rdl A296G): frequency only (no raw counts)
- genotype #12 (2025_02_14_637727v2_full_kenya_siaya_2023, Cyp4j5 L43F): frequency only (no raw counts)
- genotype #13 (2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014, Vgsc 995F): frequency only (no raw counts)
- genotype #15 (2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014, Cyp6p4 I236M): frequency only (no raw counts)
- genotype #16 (2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014, Rdl A296S): frequency only (no raw counts)
- genotype #17 (2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014, Rdl A296G): frequency only (no raw counts)
- genotype #18 (2025_02_14_637727v2_full_burkina_faso_valle_de_kou_2014, Cyp4j5 L43F): frequency only (no raw counts)
- genotype #20 (2025_02_14_637727v2_full_gambia_urr_2011_sl, Cyp6p4 I236M): frequency only (no raw counts)
- genotype #21 (2025_02_14_637727v2_full_gambia_urr_2011_sl, Rdl A296S): frequency only (no raw counts)
- genotype #22 (2025_02_14_637727v2_full_gambia_urr_2011_sl, Rdl A296G): frequency only (no raw counts)
- genotype #23 (2025_02_14_637727v2_full_gambia_urr_2011_sl, Cyp4j5 L43F): frequency only (no raw counts)
- genotype #24 (2025_02_14_637727v2_full_gambia_urr_2011_ara, Vgsc 995S): frequency only (no raw counts)
- genotype #25 (2025_02_14_637727v2_full_gambia_urr_2011_gam, Vgsc 995F): frequency only (no raw counts)
- genotype #26 (2025_02_14_637727v2_full_gambia_urr_2011_col, Vgsc 995F): frequency only (no raw counts)
