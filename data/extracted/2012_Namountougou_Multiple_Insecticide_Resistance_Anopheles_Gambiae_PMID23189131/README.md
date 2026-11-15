# Extraction record — 2012_Namountougou_Multiple_Insecticide_Resistance_Anopheles_Gambiae_PMID23189131

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 25 · Genotype rows: 38 · Bioassays: 41 · Geno-pheno rows: 0

## Decisions

### Key Decisions
1. **Surveys & Resolution**:
   - Surveys were created at the site x species/form level for target-site mutation genotyping (Tables 1 and 2). At each site, 30 mosquitoes were identified to species/molecular form (An. gambiae S form = An. gambiae s.s., An. gambiae M form = An. coluzzii, and An. arabiensis).
   - For sites where multiple species were detected, bioassays were performed on mixed An. gambiae s.l. (N=100 per test), so separate An. gambiae s.l. surveys were created to link the bioassays. For sites where only the S form was detected (Banfora, Orodara, Soumousso, Tiéfora), bioassays link directly to the species survey.
2. **Target Markers**:
   - `kdr` / `1014F` (Vgsc L995F) from Table 1.
   - `ace-1` / `119S` (Ace-1 G280S) from Table 2.
3. **Bioassays**:
   - Bioassay mortality percentages were read from the bar charts in Figure 2. N=100 exposed per population is explicitly stated in the figure caption (4 batches of 25). Tests marked 'nd' (not determined) were omitted.
4. **Inconsistency Notes**:
   - In Table 2, for Dédougou S form (N=8, RS=3, RR=0), the printed frequency is 0.21, whereas 3/16 = 0.1875. This is flagged in `inconsistency_note`.

## Validator warnings

- genotype #21 (2012_Namountougou_dedougou_2010_gambiae_s, ace-1 119S): inconsistent in the paper (values kept as printed) — Reported allele frequency 0.21 does not match calculated frequency 0.1875 for N=8 (RS=3, RR=0).
- genotype #21 (2012_Namountougou_dedougou_2010_gambiae_s, ace-1 119S): computed allele freq 0.188 differs from reported 0.21
