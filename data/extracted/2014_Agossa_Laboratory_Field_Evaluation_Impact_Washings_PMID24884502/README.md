# Extraction record — 2014_Agossa_Laboratory_Field_Evaluation_Impact_Washings_PMID24884502

- Extracted: 2026-11-01
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 6 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Two survey locations: Akron (southern Benin) and Malanville (northern Benin).
   - Wild-collected larvae/pupae were reared to adult stage (M form An. gambiae s.s.).
   - Collection year is recorded as 2012 based on explicit mention on page 4 ("23.71% mortality rate in 2012 (Table 1)").

2. **Genotypes**:
   - Marker mapping: Map the reported kdr mutation to standard marker `L1014F` (under gene `kdr`).
   - Table 1 reports kdr mutation genotype counts for Akron (RR=21, RS=17, SS=2, total N=40) and Malanville (RR=38, RS=10, SS=0, total N=48).
   - The genotype counts and frequencies are listed repeatedly across all 3 insecticide rows per site in Table 1, representing baseline population characterization. One genotype record per site was extracted to avoid double counting.

3. **Bioassays**:
   - Extracted 6 WHO tube susceptibility bioassays from Table 1 evaluating standard diagnostic doses of Bendiocarb 0.1%, Permethrin 0.75%, and Deltamethrin 0.05% against wild-reared An. gambiae s.s. from Akron and Malanville.
   - Cone bioassays (Figure 3, Table 2) were performed on the susceptible laboratory reference strain Kisumu and excluded according to Rule 5.
   - Experimental hut and tunnel test evaluations of LLIN brand treatments were excluded as LLIN product efficacy evaluations rather than standard insecticide diagnostic bioassays.
