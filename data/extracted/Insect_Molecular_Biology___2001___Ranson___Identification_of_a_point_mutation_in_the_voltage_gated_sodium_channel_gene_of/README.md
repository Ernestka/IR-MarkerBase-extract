# Extraction record — Insect_Molecular_Biology___2001___Ranson___Identification_of_a_point_mutation_in_the_voltage_gated_sodium_channel_gene_of

- Extracted: 2026-10-15
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 1 · Bioassays: 0 · Geno-pheno rows: 2

## Decisions

### Survey and Genotype Extraction Decisions
- **Marker naming**: Standardized marker name to `Vgsc` / `L1014S` matching the target list for Vgsc L995S (Leu1014Ser).
- **Field population (1999)**: 42 An. gambiae s.l. collected in 1999 from four villages ~50 km NW of Kisumu, Kenya, were screened using an allele-specific PCR adapted to detect Leu1014Ser (Vgsc L1014S). 3 heterozygotes were identified (RS=3), and all remaining mosquitoes were homozygous susceptible (SS=39), with RR=0. The 3 heterozygotes were confirmed as An. gambiae s.s. by PCR.
- **1986 field collection**: Mentioned on page 4 as containing individuals with the Leu1014Ser mutation, but no counts, sample sizes, or frequencies were reported, so no record could be extracted.
- **Laboratory F2 Cross (Table 2)**: F2 progeny from single-pair crosses between resistant Kenyan RSP-ST females and susceptible FAST males were tested for permethrin resistance linkage. Genotypes split by phenotype (dead vs. alive) are extracted into `geno_pheno` under a laboratory survey. Exposure duration varied (60-90 min empirically determined per family to achieve ~50% mortality), so the bioassay itself was not extracted as a standardized WHO bioassay, leaving `bioassay_id` as null in `geno_pheno` as permitted under Rule 6.
- **Colony strain sequencing (Table 1)**: 4 individuals each from Bobo, Kisumu, Kou, Tola, FAST, ZAN/U, and RSP-ST colonies were sequenced to discover the Leu1014Ser substitution; these are laboratory strain characterizations and are omitted from field genotypes.

## Validator warnings

- survey Insect_Molecular_Biology___2001___Ranson___Identification_of_a_point_mutation_in_the_voltage_gated_sodium_channel_gene_of_rsp_st_fast_f2: laboratory population — normally excluded
- geno_pheno #1 (permethrin, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #2 (permethrin, Vgsc L1014S, alive): not linked to a single bioassay (insecticide as reported: permethrin)
