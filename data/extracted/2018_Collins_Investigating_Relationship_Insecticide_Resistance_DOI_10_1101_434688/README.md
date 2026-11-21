# Extraction record — 2018_Collins_Investigating_Relationship_Insecticide_Resistance_DOI_10_1101_434688

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 23 · Bioassays: 82 · Geno-pheno rows: 0

## Decisions

### Survey and Data Extraction Decisions
1. **Surveys**: Six distinct village collection sites in Forecariah Prefecture, Guinea (Fandie, Madinagbe, Maferinyah Centre I, Moribayah, Senguelen, Yindi) were sampled between June 22 and July 17, 2017. Surveys were created per village.
2. **Markers**: Extracted Vgsc N1575Y (reported as N1575Y), Vgsc I1527T (reported as I1527T), Vgsc L1014F (reported as L1014F under gene kdr), and Ace-1 G119S (reported as G119S under gene Ace-1).
3. **Bioassays**: Extracted all CDC bottle bioassays reported in Table 1 per site, concentration (1X, 2X, 5X, 10X), insecticide, and synergist status (PBO pre-exposure).
4. **Genotype-Phenotype**: Genotypes for alive/dead mosquitoes are discussed in text only via chi-square test stats and p-values; no specific genotype counts split by bioassay outcome were published in tables or text, so `geno_pheno` is left empty.
5. **Inconsistencies**: Table 2 lists the wild type allele frequency S for Seneguelen as 0.05, but genotype counts are SS=82 and RS=8 out of 91, which corresponds to S frequency of 0.945. This printed contradiction was logged in `inconsistency_note`.

## Validator warnings

- genotype #5 (2018_Collins_Investigating_Relationship_Insecticide_Resistance_DOI_10_1101_434688_senguelen, vgsc N1575Y): inconsistent in the paper (values kept as printed) — Table 2 prints wild type frequency (S) as 0.05, which contradicts SS=82 and RS=8 (S allele count = 172/182 = 0.945).
