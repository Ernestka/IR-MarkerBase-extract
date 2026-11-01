# Extraction record — 2014_Riveron_Highly_Polymorphic_CYP6M7_Cytochrome_P450_PMID25261072

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 9 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Markers**: The main gene investigated in this study is CYP6M7, which is not in the schema's target marker list. CYP6P9a, CYP6P9b, and GSTe2 are target marker genes, but no target diagnostic SNP/CNV genotype class counts (RR/RS/SS) or carrier counts were reported in this paper (only expression profiling and full-gene/cDNA sequencing for haplotype diversity/phylogenetics in small clone sets). The GSTe2 L119F mutation was mentioned as absent in Zambia, but no individual genotype counts were reported. Consequently, `genotypes` and `geno_pheno` arrays are empty.
2. **Surveys & Bioassays**:
   - Bioassays were performed specifically for the F1 progeny of *An. funestus s.s.* collected in Mbinga (Katete District, Zambia) in October 2010.
   - Bioassay data from Malawi and Mozambique referenced in the text were conducted in previous studies (Riveron et al. 2013, Wondji et al. 2012, Cuamba et al. 2010) and are omitted here per Rule 5.
   - Female WHO bioassay results are extracted per standard WHO vector monitoring procedures. Male bioassay results shown in Figure 1 are omitted to avoid duplicate insecticide entries since the schema lacks a sex field.
   - Percent mortality values were taken from the main text (pages 5-6), and sample sizes ($n_{exposed}$) for female tests were read from Figure 1.
   - Recombinant *E. coli* metabolism assays and transgenic *Drosophila melanogaster* contact bioassays were excluded as non-mosquito lab assays.
