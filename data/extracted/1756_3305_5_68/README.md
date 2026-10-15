# Extraction record — 1756_3305_5_68

- Extracted: 2026-10-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 2 · Bioassays: 7 · Geno-pheno rows: 0

## Decisions

### Survey and Sampling
- A single survey was created for larval collections in June 2008 at Yaokoffikro, a village near Bouaké, Côte d'Ivoire (7° 11' N = 7.1833°, 5° 1' W = -5.0167°).
- Mosquitoes were identified as Anopheles gambiae s.s. (S molecular form).
- Kisumu laboratory reference strain data were omitted as controls per extraction rules.

### Genotypes
- Vgsc L1014F (L995F) was genotyped in 111 individuals; 108 were reported as carriers, with an allele frequency of 0.94. Homozygote/heterozygote breakdown was not printed, so counts are captured via `n_carriers` and `reported_allele_freq`.
- Ace-1 G119S (G280S) was genotyped in 44 individuals, with an allele frequency of 0.50. Counts of individual genotype classes or carriers were not printed and are left null.

### Bioassays
- Seven diagnostic WHO tube assays were reported for the Yaokoffikro population in Table 1 (carbosulfan 0.4%, propoxur 0.1%, fenitrothion 1%, permethrin 1%, lambdacyhalothrin 0.05%, etofenprox 0.05%, DDT 4%).
- Number exposed (N) and percent mortality were printed, but dead/alive counts were not printed, so `dead_alive_printed` is false and `n_dead` and `n_alive` are null per instructions.

### Genotype-Phenotype Data
- Genotypes were not reported separately by bioassay outcome (alive/dead), so no genotype-phenotype records were extracted.

## Validator warnings

- genotype #2 (1756_3305_5_68_yaokoffikro_2008, Ace-1 G119S): frequency only (no raw counts)
