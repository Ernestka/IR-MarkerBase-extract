# Extraction record — 2012_Dabire_Population_Dynamics_Anopheles_Gambiae_Bobo_PMID22721002

- Extracted: 2026-11-14
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 11 · Bioassays: 16 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions

- **Study Overview**: The paper describes mosquito surveys in Bobo-Dioulasso, Burkina Faso, conducted between May and December 2008 in two districts: Kodéni (outskirts) and Dioulassoba (center of the city). Larvae were collected from breeding sites and reared to adults for insecticide resistance bioassays (WHO tube assays in September and November 2008) and genotyping.
- **Survey Splitting**:
  - Genotype data in Tables 4 and 5 are broken down by molecular species: An. arabiensis, An. gambiae M form (An. coluzzii), and An. gambiae S form (An. gambiae s.s.). Following extraction rules, 6 surveys are created for the genotype data (2 sites × 3 molecular species).
  - Insecticide susceptibility tests (Table 2) were conducted on wild-reared An. gambiae s.l. at two time points: September 2008 and November 2008. Therefore, 4 surveys are created for these bioassays (2 sites × 2 time points).
- **Bioassays vs Genotyped Subsets (Rule 8b)**:
  - Table 2 reports the actual WHO tube bioassays performed on An. gambiae s.l. populations (N exposed and % mortality ± SE). These 16 bioassays are extracted. Since dead and alive counts are not printed, `dead_alive_printed` is set to `false`, and `n_dead` and `n_alive` are left null.
  - Table 3 reports species identification of subsets of survivors and dead mosquitoes from the bioassays. Per Rule 8b ("Never build a bioassay record from genotyped subsets"), Table 3 is not extracted as bioassays.
- **Genotypes vs Geno-Pheno (Rule 6)**:
  - As stated by the authors on pages 3 and 4: "As the sample size was sometimes too low to give reliable estimates of kdr and ace-1R frequency for each species or molecular form, we pooled all specimens (resistant and susceptible to DDT, pyrethroids and bendiocarb) prior to allele frequency determination." Table 4 (kdr L1014F) and Table 5 (ace-1R G119S) report genotype counts for the pooled bioassay mosquitoes by site and species. They are therefore recorded in `genotypes`.
  - In Table 5, for Dioulassoba An. gambiae M form, N = 0, so no genotype entry is generated.
  - Text mentions partial carrier counts among survivors for ace-1, but complete separate genotype distributions for alive and dead are not reported in the tables; thus `geno_pheno` is empty.
