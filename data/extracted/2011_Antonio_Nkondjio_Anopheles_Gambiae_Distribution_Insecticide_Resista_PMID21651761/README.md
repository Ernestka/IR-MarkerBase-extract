# Extraction record — 2011_Antonio_Nkondjio_Anopheles_Gambiae_Distribution_Insecticide_Resista_PMID21651761

- Extracted: 2026-11-12
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 8 · Genotype rows: 8 · Bioassays: 30 · Geno-pheno rows: 12

## Decisions

### Data Extraction & Organization Summary
- **Surveys**: Created six surveys corresponding to the three breeding habitat types (cultivated, polluted, non-polluted) in Douala and Yaounde, plus two city-wide surveys (Douala, Yaounde) to anchor city-level pooled geno-pheno data and city-level species totals.
- **Species**: >99% of molecularly identified specimens in Douala (494/495) and Yaounde (379/382) were An. coluzzii (M form). The 3 S form specimens (1 in Douala, 2 in Yaounde) were noted in Table 4.
- **Bioassays**: Extracted 30 WHO diagnostic dose tube bioassays from Figure 5 (% mortality and N exposed per habitat category). Numbers dead and alive were not printed, so `n_dead` and `n_alive` are set to null and `dead_alive_printed` is set to false per extraction rules. Kisumu and OCEAC laboratory reference strains were excluded.
- **Genotypes**: Extracted Vgsc L1014F (kdr-west) counts per habitat category from Table 5. Extracted one carrier of Vgsc L1014S (kdr-east) in Douala (Table 4 / text page 9). Extracted Ace-1 G119S negative screening results (74 tested, 0 positive; page 9).
- **Geno-Pheno**: Extracted 12 genotype-phenotype breakdown records (deaths vs survivors) for DDT 4%, Permethrin 0.75%, and Deltamethrin 0.05% in Douala and Yaounde from Table 5. Because these genotyped subsets were pooled across habitat categories within each city, `bioassay_id` is set to null per Rule 6.

## Validator warnings

- geno_pheno #1 (DDT, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #2 (DDT, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #3 (permethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #4 (permethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #5 (deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #6 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #7 (DDT, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #8 (DDT, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: DDT)
- geno_pheno #9 (permethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #10 (permethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: permethrin)
- geno_pheno #11 (deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #12 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
