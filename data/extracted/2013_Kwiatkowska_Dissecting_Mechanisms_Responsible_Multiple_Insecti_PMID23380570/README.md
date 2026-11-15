# Extraction record — 2013_Kwiatkowska_Dissecting_Mechanisms_Responsible_Multiple_Insecti_PMID23380570

- Extracted: 2026-11-15
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 7 · Geno-pheno rows: 2

## Decisions

### Data Extraction Decisions
- **Surveys**: Created two surveys: `2013_Kwiatkowska_VK_2010_F0` for field-collected wild female baseline target-site mutation genotyping, and `2013_Kwiatkowska_VK_2010_F1` for F1 progeny tested in WHO susceptibility bioassays.
- **Coordinates**: Converted 11° 23′ 14″ N and 4° 24′ 42″ W to decimal degrees (11.38722, -4.41167) as reported on page 8.
- **Genotypes (F0 Population)**:
  - `Vgsc L1014F`: Exact genotype counts RR=53, RS=43, SS=4, N=100 extracted from explicit percentages for N=100 field F0 females. Reported allele frequency: 0.75.
  - `Vgsc L1014S`: Reported as 0% (N=100); RR=0, RS=0, SS=100, reported allele frequency: 0.0.
  - `Ace-1 G119S`: Reported as 4.2% allele frequency (N=124), always heterozygous; count fields left null per Rule 2.
  - `Rdl A296S`: Reported as 87% allele frequency (N=94) with genotype percentages (77.7% T/T, 19.1% G/T, 3.2% G/G); count fields left null per Rule 2.
- **Bioassays**: Extracted WHO diagnostic concentrations and overall pooled mortalities for 7 insecticides.
- **Geno-Pheno**: Included Ace-1 G119S for bendiocarb alive (4 RS out of 35) and dead (0 RS out of 24) where exact counts were printed. Excluded geno_pheno records for permethrin, DDT, and dieldrin because full genotype breakdowns for alive/dead subsets were only presented as percentages or in supplementary tables (Tables S2 and S4) and exact raw counts or allele frequencies per subset were not printed in the main text.

## Validator warnings

- genotype #3 (2013_Kwiatkowska_VK_2010_F0, Ace-1 G119S): frequency only (no raw counts)
- genotype #4 (2013_Kwiatkowska_VK_2010_F0, Rdl A296S): frequency only (no raw counts)
