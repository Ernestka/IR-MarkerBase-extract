# Extraction record — 2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 11 · Genotype rows: 22 · Bioassays: 2 · Geno-pheno rows: 8

## Decisions

### Data Extraction Decisions

1. **Surveys Split**: Eleven distinct survey records were created for the 11 study sites sampled across Kenya between May 2014 and October 2014 (Port Victoria, Homa Bay, Kamkuywa, Kanyawegi, Chulaimbo, Miwani, Marigat, Kabernet, Gazi, Mtwapa, and Malindi).
2. **Species & Identification**: All extracted surveys represent molecularly identified *Anopheles arabiensis* (derived from field-collected *An. gambiae s.l.* larvae identified via ribosomal DNA PCR).
3. **Genotype Data**: Table 1 reports genotype frequencies as percentages (LL, LF, FF, LS, SS). In accordance with Rule 2 (RAW COUNTS ONLY), raw genotype counts (rr, rs, ss) were left null for population samples as back-calculation from percentage columns is forbidden. Allele frequencies explicitly printed in the text and Figure 1 caption for `L1014F` and `L1014S` were recorded in `reported_allele_freq`.
4. **Bioassays**: Extracted standard WHO tube bioassays (0.05% deltamethrin, 60 min exposure, 24 h mortality) reported for Port Victoria (n=516 exposed, 82.8% mortality) and Chulaimbo (n=57 exposed, 73.7% mortality). Dead/alive counts were not explicitly printed as whole numbers, so `n_dead` and `n_alive` were left null and `dead_alive_printed` set to `false`.
5. **Genotype-Phenotype Data**: Subsets of bioassay survivors ('resistant') and dead ('susceptible') genotyped for `L1014F` and `L1014S` at Port Victoria and Chulaimbo are extracted into `geno_pheno` with exact sample sizes `n` and allele frequencies as reported in Figure 2B.

## Validator warnings

- genotype #1 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_port_victoria, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_port_victoria, kdr L1014S): frequency only (no raw counts)
- genotype #3 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_homa_bay, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_homa_bay, kdr L1014S): frequency only (no raw counts)
- genotype #5 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kamkuywa, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kamkuywa, kdr L1014S): frequency only (no raw counts)
- genotype #7 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kanyawegi, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kanyawegi, kdr L1014S): frequency only (no raw counts)
- genotype #9 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_chulaimbo, kdr L1014F): frequency only (no raw counts)
- genotype #10 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_chulaimbo, kdr L1014S): frequency only (no raw counts)
- genotype #11 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_miwani, kdr L1014F): frequency only (no raw counts)
- genotype #12 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_miwani, kdr L1014S): frequency only (no raw counts)
- genotype #13 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_marigat, kdr L1014F): frequency only (no raw counts)
- genotype #14 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_marigat, kdr L1014S): frequency only (no raw counts)
- genotype #15 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kabernet, kdr L1014F): frequency only (no raw counts)
- genotype #16 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_kabernet, kdr L1014S): frequency only (no raw counts)
- genotype #17 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_gazi, kdr L1014F): frequency only (no raw counts)
- genotype #18 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_gazi, kdr L1014S): frequency only (no raw counts)
- genotype #19 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_mtwapa, kdr L1014F): frequency only (no raw counts)
- genotype #20 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_mtwapa, kdr L1014S): frequency only (no raw counts)
- genotype #21 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_malindi, kdr L1014F): frequency only (no raw counts)
- genotype #22 (2018_Hemming_Schroeder_Emerging_Pyrethroid_Resistance_Anopheles_Arabiensi_PMID29363447_malindi, kdr L1014S): frequency only (no raw counts)
