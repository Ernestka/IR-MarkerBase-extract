# Extraction record — 2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539

- Extracted: 2026-11-10
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 8 · Bioassays: 4 · Geno-pheno rows: 0

## Decisions

### Data Extraction Summary

1. **Surveys**: Split into four distinct collection sites sampled during the dry season (December 2006 – January 2007):
   - **Orogun** (Nigeria, Oyo State, control site)
   - **Ojoo** (Nigeria, Oyo State, oil spillage site)
   - **Akron** (Benin, Ouémé Department / Porto-Novo, agricultural site)
   - **Gbedjromede** (Benin, Littoral Department / Cotonou, urban site)
   All mosquitoes were collected as 4th instar larvae or pupae, reared to F0 adult females, and identified molecularly as the M form of *Anopheles gambiae s.s.* (*An. coluzzii*).

2. **Coordinates**: Recorded directly from Figure 2 (page 7). Akron latitude is printed as 4.4300, which is preserved as printed according to rule 8.

3. **Genotypes**: Extracted from Table 1 for West kdr (L1014F) and East kdr (L1014S) using marker names 'L1014F' and 'L1014S' mapped to Vgsc L995F and Vgsc L995S. Because only sample sizes (N=30) and allele frequencies were reported (without raw RR, RS, SS counts), count fields were left null and frequencies were placed in `reported_allele_freq` per Rule 2.

4. **Bioassays**: Extracted from Table 1 (N=80 per site). Permethrin 0.75% for 1 hour was used for Orogun, Akron, and Ojoo; Olyset net (1 g/m2 permethrin, 10 min exposure) was used for Gbedjromede. Exact dead/alive counts were not printed in Table 1 (only % mortality and N=80), so `dead_alive_printed` is set to false.

5. **Geno-Pheno**: Kdr genotyping was performed on permethrin bioassay survivors for microarray analysis, but genotypes were not reported separately for dead versus alive mosquitoes; thus `geno_pheno` is left empty.

## Validator warnings

- genotype #1 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_orogun, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_orogun, kdr L1014S): frequency only (no raw counts)
- genotype #3 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_akron, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_akron, kdr L1014S): frequency only (no raw counts)
- genotype #5 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_ojoo, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_ojoo, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_gbedjromede, kdr L1014F): inconsistent in the paper (values kept as printed) — Table 1 reports West kdr frequency as 0.83 (N=30), whereas the abstract and page 3 text report f = 0.84.
- genotype #7 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_gbedjromede, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2008_Djouaka_Expression_Cytochrome_P450s_CYP6P3_CYP6M2_PMID19014539_gbedjromede, kdr L1014S): frequency only (no raw counts)
