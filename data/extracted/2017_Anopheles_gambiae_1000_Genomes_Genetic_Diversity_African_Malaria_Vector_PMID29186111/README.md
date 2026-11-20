# Extraction record — 2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 9 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Study Scope**: This is Phase 1 of the Anopheles gambiae 1000 Genomes Project (Ag1000G), reporting whole-genome Illumina sequencing of 765 wild-caught An. gambiae and An. coluzzii specimens across 8 African countries.
- **Target Markers**: Allele frequencies for two target markers in the voltage-gated sodium channel gene (*Vgsc*), L995F (L1014F / kdr-west) and L995S (L1014S / kdr-east), are explicitly reported on Page 7.
- **Genotype Counts**: The paper prints allele frequencies as percentages in the text (e.g., Guinea 100%, Burkina Faso 93%, Cameroon 53%, Gabon 36%, Angola 86% for L995F; Cameroon 15%, Gabon 65%, Uganda 100%, Kenya 76% for L995S). Per Schema Rule 2, genotype count fields (`rr`, `rs`, `ss`, `n_carriers`, `resistant_allele_count`) are left null and back-calculation from percentages is avoided. Frequencies are converted to 0-1 proportions and stored in `reported_allele_freq`.
- **Surveys**: Surveys are created for each country population sample using the collection years and sample sizes detailed in Extended Data Figure 1. Guinea-Bissau is included as a survey matching Extended Data Figure 1, though no text allele frequency for L995F/S was explicitly reported for it on Page 7.
- **Other Markers**: The paper mentions N1570Y and Gste2 I114T (note: I114T is not in the target marker list), but does not report explicit numerical allele frequencies or genotype counts for them in text.

## Validator warnings

- genotype #1 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_guinea_2012, Vgsc L995F): frequency only (no raw counts)
- genotype #2 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_burkina_faso_2012, Vgsc L995F): frequency only (no raw counts)
- genotype #3 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_cameroon_2009, Vgsc L995F): frequency only (no raw counts)
- genotype #4 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_cameroon_2009, Vgsc L995S): frequency only (no raw counts)
- genotype #5 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_gabon_2000, Vgsc L995F): frequency only (no raw counts)
- genotype #6 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_gabon_2000, Vgsc L995S): frequency only (no raw counts)
- genotype #7 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_angola_2009, Vgsc L995F): frequency only (no raw counts)
- genotype #8 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_uganda_2012, Vgsc L995S): frequency only (no raw counts)
- genotype #9 (2017_Anopheles_gambiae_1000_Genomes_Genetic_Diversity_African_Malaria_Vector_PMID29186111_kenya_2012, Vgsc L995S): frequency only (no raw counts)
