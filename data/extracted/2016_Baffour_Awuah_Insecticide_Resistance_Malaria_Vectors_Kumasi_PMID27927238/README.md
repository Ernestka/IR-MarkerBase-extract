# Extraction record — 2016_Baffour_Awuah_Insecticide_Resistance_Malaria_Vectors_Kumasi_PMID27927238

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 2 · Bioassays: 10 · Geno-pheno rows: 0

## Decisions

### Survey and Study Design
- **Surveys:** 1,069 wild An. gambiae (s.l.) reared from larvae collected across irrigated vegetable farms in Asokwa submetropolis, Kumasi, Ghana were tested in 10 WHO tube bioassays. A subset of 619 mosquitoes exposed to pyrethroids and organochlorines was subsequently identified to species via PCR (537 An. gambiae s.s. and 82 An. coluzzii) and genotyped for kdr L1014F. Therefore, three surveys were defined: `2016_baffour_awuah_asokwa_sl` for the bioassays (which were conducted on An. gambiae s.l. before molecular identification), and two species-specific surveys (`2016_baffour_awuah_asokwa_gambiae_ss` and `2016_baffour_awuah_asokwa_coluzzii`) for target-site resistance marker genotyping.
- **Collection Dates:** The manuscript does not report collection dates; ethics approval reference is CHRPE/AP/343/14 (2014) and the manuscript was received in April 2016.

### Genotypes and Markers
- **Vgsc L1014F (L995F):** AS-PCR was performed to detect L1014F. Table 2 reports total mosquitoes tested and counts classified as 'kdr-resistant' and 'kdr-sensitive'. Because distinct homozygous resistant (RR) and heterozygous (RS) counts were not separated, counts are placed in `n_carriers` (329 for An. gambiae s.s., 75 for An. coluzzii) with total tested in `n_genotyped` (537 and 82, respectively), and rr/rs/ss set to null.
- **Ace-1 G119S (G280S):** PCR-RFLP was conducted on mosquitoes exposed to carbamates and organophosphates. The authors reported that the ace-1 mutation was not detected ('Ace-1 mutation on the other hand was not detected among the female Anopheles mosquitoes subjected to organophosphates and carbamates'). However, no exact genotyped count was printed, nor were these mosquitoes identified to species; thus no raw count could be extracted.

### Bioassays
- All 10 bioassays from Table 1 were extracted under the An. gambiae (s.l.) survey with printed counts for exposed, dead, and survived (alive). Reference strain (Kisumu) bioassays were excluded as controls.

### Genotype-Phenotype Data
- Table 3 provides counts of 'kdr-resistant' alive and dead mosquitoes, but reports 'kdr-sensitive' mosquitoes only as an unsegregated pooled total column across both alive and dead outcomes. Furthermore, the species-specific denominators (number of alive or dead mosquitoes genotyped per species) are neither reported nor uniquely determinable. Because the sensitive mosquitoes cannot be allocated to alive or dead and denominators are missing, Table 3 cannot be represented as valid geno_pheno records. The complete population-level genotype counts from Table 2 are extracted in `genotypes` without duplication.
