# Extraction record — 2005_Asidi_Experimental_Hut_Evaluation_Bednets_Treated_PMID15918909

- Extracted: 2026-11-07
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 0 · Geno-pheno rows: 8

## Decisions

### Data Extraction Summary
- **Survey & Study Details**: Anopheles gambiae mosquitoes collected from experimental huts at Yaokoffikro near Bouaké, Côte d'Ivoire between 15 August 2002 and late September 2002 (33 nights total).
- **Genotypes vs Geno_pheno**: Table 2 on page 6 reports PCR genotyping of 298 A. gambiae for the Ace-1 G119S mutation, categorized by survival (live vs dead) across experimental hut treatments (Untreated Control, Chlorpyrifos-methyl, Lambda-cyhalothrin, Mixture & two-in-one). Per Rule 6, all genotyped specimens are extracted in `geno_pheno` and omitted from `genotypes` to prevent double counting.
- **Bioassay Linking**: The treatment groups in Table 2 combine multiple specific hut treatment arms (e.g. chlorpyrifos-methyl 100 mg/m2 unwashed, washed, 250 mg/m2 unwashed, washed). Because these are pooled across hut arms and no specific bioassay counts are given in main text/tables (detailed counts were placed in Additional File 1), `bioassay_id` is set to `null` and standalone `bioassays` are left empty per Rules 2 & 8b.
- **kdr (L995F)**: Text states that kdr frequency in control huts was >90%, but exact sample counts or exact allele frequencies were not printed, so kdr was omitted.

## Validator warnings

- geno_pheno #1 (no insecticide, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #2 (no insecticide, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: none given)
- geno_pheno #3 (chlorpyrifos-methyl, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: chlorpyrifos-methyl)
- geno_pheno #4 (chlorpyrifos-methyl, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: chlorpyrifos-methyl)
- geno_pheno #5 (lambdacyhalothrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
- geno_pheno #6 (lambdacyhalothrin, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: lambdacyhalothrin)
- geno_pheno #7 (chlorpyrifos-methyl + lambdacyhalothrin, Ace-1 G119S, alive): not linked to a single bioassay (insecticide as reported: chlorpyrifos-methyl + lambdacyhalothrin)
- geno_pheno #8 (chlorpyrifos-methyl + lambdacyhalothrin, Ace-1 G119S, dead): not linked to a single bioassay (insecticide as reported: chlorpyrifos-methyl + lambdacyhalothrin)
