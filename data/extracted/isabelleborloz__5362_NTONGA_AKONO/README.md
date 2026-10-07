# Extraction record — isabelleborloz__5362_NTONGA_AKONO

- Extracted: 2026-10-07
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 0 · Bioassays: 12 · Geno-pheno rows: 4

## Decisions

### Key Decisions and Extraction Notes

1. **Surveys**: Split into two surveys: `isabelleborloz__5362_NTONGA_AKONO_rural` and `isabelleborloz__5362_NTONGA_AKONO_urban` based on the distinct collection sites (Kribi rural and Kribi urbain) and their respective coordinates.
2. **Bioassays**: 
   - Reared F0 adults were tested using standard WHO tube bioassays.
   - Footnote of Table III states: `%mort. : moyenne de 4 répliques en raison de 20 moustiques par réplique`, which yields `n_exposed = 80` for each test. This matches the reported percentages perfectly (e.g., 36.25% of 80 is exactly 29 dead).
   - Permethrin concentration is listed as '75%' in Table III (likely a typo for 0.75% or 3.75% as mentioned in the text on page 7). We extracted it exactly as printed ('75%').
   - Laboratory reference strain (Kisumu) was excluded as per Rule 5.
3. **Genotypes / Genotype-Phenotype**:
   - Page 7 states: "Un total de 350 moustiques ayant survécu aux tests de sensibilité a été utilisé..." indicating that the genotyped individuals are survivors of the bioassays. Therefore, they are extracted in `geno_pheno` with `phenotype_group = 'alive'`.
   - The total of 350 in Table IV is the sum of the N column (100 + 100 + 75 + 75 = 350), which means 175 unique mosquitoes were genotyped for both Kdr West and Kdr East.
   - Since only allele frequencies (R and S) are reported without raw genotype counts (RR, RS, SS), the count fields are left null and the resistant allele frequency is recorded in `reported_allele_freq`.
   - Genotyping method: Abstract mentions HOLA, Table IV header says Taqman, and text on page 5 mentions Martinez-Torres (1998). We recorded 'HOLA' as it is the primary method highlighted in the abstract and methodology.

## Validator warnings

- geno_pheno #1 (DDT, permethrin, deltamethrin, Vgsc Kdr West, alive): not linked to a single bioassay (insecticide as reported: DDT, permethrin, deltamethrin)
- geno_pheno #2 (DDT, permethrin, deltamethrin, Vgsc Kdr East, alive): not linked to a single bioassay (insecticide as reported: DDT, permethrin, deltamethrin)
- geno_pheno #3 (DDT, permethrin, deltamethrin, Vgsc Kdr West, alive): not linked to a single bioassay (insecticide as reported: DDT, permethrin, deltamethrin)
- geno_pheno #4 (DDT, permethrin, deltamethrin, Vgsc Kdr East, alive): not linked to a single bioassay (insecticide as reported: DDT, permethrin, deltamethrin)
