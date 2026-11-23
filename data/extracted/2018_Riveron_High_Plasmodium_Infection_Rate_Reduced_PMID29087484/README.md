# Extraction record — 2018_Riveron_High_Plasmodium_Infection_Rate_Reduced_PMID29087484

- Extracted: 2026-11-23
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 26 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Sampling**:
   - Mosquitoes were collected in May 2015 in Ndjili-Brasserie, Kinshasa, DRC (4°19′39″S, 15°18′48″E).
   - Two separate surveys created for the sympatric vector species: *Anopheles gambiae* s.l. and *Anopheles funestus* s.s.
   - Molecular species identification of *An. gambiae* s.l. (subsample of 100) revealed 95% *An. gambiae* s.s. and 5% *An. coluzzii*. Genotyping and bioassay data are reported for *An. gambiae* s.l.
   - All 81 *An. funestus* group mosquitoes tested were confirmed as *An. funestus* s.s.

2. **Genotypes**:
   - *An. gambiae* s.l.: Genotyped 111 F0 females for Vgsc L1014F and L1014S. Exact allele counts are printed: 195/222 alleles (87.8%) for 1014F and 24/222 (10.8%) for 1014S. Per Rule 4b (multi-allelic codon 1014), separate rows created for L1014F and L1014S with `resistant_allele_count` populated and `reported_allele_freq` formatted as a proportion (0.878 and 0.108).
   - *An. funestus* s.s.: Genotyped 66 F0 females. GSTe2 L119F resistant allele frequency reported as 66.7% (43.1% RR, 47.1% RS). RDL A296S resistant allele frequency reported as 10%. Per Rule 2, count fields (RR/RS/SS) left null as only percentages were printed.

3. **Bioassays**:
   - Extracted standard WHO tube bioassays (60 min exposure as well as extended exposure durations of 30, 90, 180, 360 min where reported) and PBO synergist tube bioassays.
   - Mosquitoes were F1 generation adult offspring reared from F0 females.
   - Bioassay mortalities were reported as percentages (mean ± standard error); exact numbers of dead/alive per tube test were not explicitly printed, so `n_exposed`, `n_dead`, and `n_alive` are left null with `dead_alive_printed = false`.
   - Net cone bioassays with commercially produced nets (Olyset, PermaNet) were excluded from standard WHO tube bioassays as per guidelines.

4. **Geno-Pheno**:
   - No genotype-phenotype data (genotypes split by bioassay survivors vs dead) were reported. F0 females were genotyped directly from field collections.

## Validator warnings

- genotype #3 (2018_Riveron_High_Plasmodium_Infection_Rate_Reduced_PMID29087484_kinshasa_2015_funestus, GSTe2 L119F): frequency only (no raw counts)
- genotype #4 (2018_Riveron_High_Plasmodium_Infection_Rate_Reduced_PMID29087484_kinshasa_2015_funestus, RDL A296S): frequency only (no raw counts)
