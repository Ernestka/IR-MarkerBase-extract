# Extraction record — s12936_018_2285_6

- Extracted: 2026-10-10
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 6 · Bioassays: 12 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The study reports entomological monitoring across 8 sentinel sites in the Democratic Republic of the Congo (DRC) between 2013 and 2016.
- Target resistance marker genotyping for Vgsc L1014F was performed only on 2014 samples from six sites (Kabondo, Lodja, Kingasani, Mikalayi, Kapolowe, and Tshikaji). Kalemie and Katana were added in 2015 and not tested in 2014.
- Six surveys are created for the 2014 collections at these six sentinel sites.

### Genotype Class Counts Read from Figure 2
- Genotype data for Vgsc L1014F are presented in Figure 2 as a stacked bar chart of genotype frequencies (RR, RS, SS) with total sample sizes printed below each site: Kabondo (n=132), Lodja (n=86), Kingasani (n=43), Mikalayi (n=60), Kapolowe (n=18), and Tshikaji (n=39), totaling N=378.
- Genotype class counts (RR, RS, SS) were determined from the stacked bar proportions and integer constraints matching N and reported qualitative frequencies (>70% in Kabondo, Kingasani, Tshikaji; <20% in Lodja, Kapolowe):
  - Kabondo (n=132): RR=95, RS=32, SS=5 (sum=132; allele freq = 84.1%)
  - Lodja (n=86): RR=2, RS=13, SS=71 (sum=86; allele freq = 9.9%)
  - Kingasani (n=43): RR=31, RS=7, SS=5 (sum=43; allele freq = 80.2%)
  - Mikalayi (n=60): RR=10, RS=20, SS=30 (sum=60; allele freq = 33.3%)
  - Kapolowe (n=18): RR=1, RS=3, SS=14 (sum=18; allele freq = 13.9%)
  - Tshikaji (n=39): RR=28, RS=8, SS=3 (sum=39; allele freq = 82.1%)

### Bioassays
- Bioassays conducted during 2014 for these six sentinel sites (deltamethrin 0.05% and DDT 4%) are extracted from Table 2. Tests used 100 mosquitoes per assay, except DDT in Kapolowe which tested 80 mosquitoes.
- Exact numbers of dead/alive mosquitoes were not printed in Table 2, so `dead_alive_printed` is set to false and `n_dead`/`n_alive` are left null with `reported_mortality_pct` recorded.

### Genotype-Phenotype
- No genotype data split by bioassay outcome (alive vs. dead) are reported; `geno_pheno` is empty.
