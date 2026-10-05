# Extraction record — s13071_021_04706_5

- Extracted: 2026-10-05
- Model: gemini:gemini-3.1-flash-lite
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 1 · Bioassays: 1 · Geno-pheno rows: 2

## Decisions

1. Genotype data: Table 3 provides counts for L1014S (L995S) for resistant (alive) and susceptible (dead) mosquitoes. The total genotyped An. gambiae (s.s.) is 49 (15 resistant + 34 susceptible). 2. Marker names: The paper uses L1014S, which maps to L995S. 3. Bioassays: The paper reports bioassay results for multiple insecticides across eight sites, but does not provide the raw n_exposed/n_dead/n_alive counts per site/insecticide, only mortality percentages in Figure 2. Therefore, no site-specific bioassay records were created. However, Table 3 provides the aggregate phenotype counts for the genotyped subset exposed to pyrethroids, which I have used to create a single bioassay record to link the geno_pheno data. 4. Geno-pheno: The geno_pheno data is linked to the bioassay ID 's13071_021_04706_5_pyrethroid_bioassay'. 5. SS count for dead: The paper reports 34 dead, 2 RR, 1 RS. Thus, SS = 34 - 2 - 1 = 31.
