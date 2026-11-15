# Extraction record — 2013_Koffi_Re_Visiting_Insecticide_Resistance_Status_PMID24358177

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 26 · Genotype rows: 51 · Bioassays: 61 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys & Resolution**: Surveys are partitioned per site and molecular species (M form / *An. coluzzii* vs S form / *An. gambiae s.s.*) for genotype data as reported in Table 2 and Table 3. Bioassays performed on unseparated field-reared *An. gambiae s.s.* populations are linked to site-level overall surveys.
- **Target Markers Extracted**:
  - `Vgsc L1014F` (extracted from Table 2 with genotype counts SS, RS, RR and allele frequencies per molecular form).
  - `Ace-1 G119S` (extracted from Table 3 as allele frequencies per molecular form).
  - `Ace-1 DUP` (extracted from Table 3 as duplicated allele 'D' frequencies per molecular form).
- **Bioassays**: Diagnostic concentration bioassays and PBO synergist bioassays were extracted from Figures 2 and 3 and relevant main text descriptions. Mortalities were read from bar graphs and text. Control strains (Kisumu) were omitted per Rule 5.
- **Inconsistency Note**: Table 2 lists Yamoussoukro M molecular form genotype counts as SS=4, RS=17, RR=3 (summing to 24), but prints n1=26. The printed frequency 0.479 matches 23/48 (N=24).

## Validator warnings

- genotype #2 (2013_Koffi_bingerville_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #3 (2013_Koffi_bingerville_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #5 (2013_Koffi_bingerville_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #6 (2013_Koffi_bingerville_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #8 (2013_Koffi_port_bouet_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #9 (2013_Koffi_port_bouet_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #11 (2013_Koffi_yopougon_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #12 (2013_Koffi_yopougon_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #13 (2013_Koffi_yamoussoukro_m, Vgsc L1014F): inconsistent in the paper (values kept as printed) — Printed RR+RS+SS = 24 (3+17+4), but n1 is printed as 26. The printed frequency 0.479 matches 23/48 (where N=24).
- genotype #13 (2013_Koffi_yamoussoukro_m, Vgsc L1014F): RR+RS+SS = 3+17+4 = 24 but n_genotyped = 26
- genotype #14 (2013_Koffi_yamoussoukro_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #15 (2013_Koffi_yamoussoukro_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #17 (2013_Koffi_yamoussoukro_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #18 (2013_Koffi_yamoussoukro_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #20 (2013_Koffi_korhogo_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #21 (2013_Koffi_korhogo_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #23 (2013_Koffi_korhogo_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #24 (2013_Koffi_korhogo_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #26 (2013_Koffi_kaforo_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #27 (2013_Koffi_kaforo_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #29 (2013_Koffi_kaforo_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #30 (2013_Koffi_kaforo_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #32 (2013_Koffi_man_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #33 (2013_Koffi_man_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #35 (2013_Koffi_man_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #36 (2013_Koffi_man_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #38 (2013_Koffi_zele_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #39 (2013_Koffi_zele_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #41 (2013_Koffi_zele_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #42 (2013_Koffi_zele_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #44 (2013_Koffi_san_pedro_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #45 (2013_Koffi_san_pedro_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #47 (2013_Koffi_abengourou_m, Ace-1 G119S): frequency only (no raw counts)
- genotype #48 (2013_Koffi_abengourou_m, Ace-1 Ace-1 DUP): frequency only (no raw counts)
- genotype #50 (2013_Koffi_abengourou_s, Ace-1 G119S): frequency only (no raw counts)
- genotype #51 (2013_Koffi_abengourou_s, Ace-1 Ace-1 DUP): frequency only (no raw counts)
