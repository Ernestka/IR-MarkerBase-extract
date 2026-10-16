# Extraction record — 2023_Boussougou_Sambe_Anopheles_Gambiae_Resistance_Pyrethroids_DDT_PMID38110952

- Extracted: 2026-10-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

1. Study split into two surveys based on site: Lambaréné (semi-urban) and Zilé (rural village), sampled from November 2017 to February 2018.
2. SINE200 PCR identified 100% of successfully amplified mosquitoes as Anopheles gambiae s.s.
3. Vgsc 1014 codon carries two mutations: L1014F and L1014S. Following rule 4b, L1014F and L1014S are recorded as separate rows per survey. For Lambaréné (N=60): 46 1014F/1014F, 12 1014F/1014S, 2 1014S/1014S (no 1014L wild-type allele was found). For Zilé (N=56): 32 1014F/1014F, 18 1014F/1014S, 6 1014S/1014S. Combined totals from Table 2 were excluded to avoid double counting per Rule 7.
4. Genotyping was performed on randomly selected control mosquitoes, not split by bioassay outcome; therefore, geno_pheno is empty.
5. Bioassays were extracted for deltamethrin (0.05%), permethrin (0.75%), and DDT (4%) for both sites. Exact mortality percentages were printed for deltamethrin (51% Lambaréné, 76% Zilé), permethrin in Zilé (6%), and DDT in Zilé (2%). Permethrin and DDT in Lambaréné were reported as '<3%' in text without exact percentage, so reported_mortality_pct is left null.
