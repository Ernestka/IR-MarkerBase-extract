# Extraction record — 2014_Tokponnon_Impact_Long_Lasting_Insecticidal_Nets_PMID24581394

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 25 · Genotype rows: 25 · Bioassays: 25 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Study Overview**: The study evaluated LLIN effectiveness alongside vector resistance (deltamethrin susceptibility) and *kdr* mutation frequencies across 25 villages in Plateau Department, south-western Benin, between May and August 2012. 32 villages were initially selected (Table 1), but 7 villages were dropped due to unproductive larval collections, leaving 25 villages.
- **Spatial Allocation**: The 25 villages belong to 4 districts:
  - Ifangni (13 villages): Banigbé, Kokoumolou, Araromi, Ko-Dogba, Tchaada, Kétougbékon, Lokossa, Itakpako, Ita-soumba, Ko-Aïdjedo, Zihan, Gblo-Gblo, Daagbe.
  - Sakete (5 villages): Igbo-Abikou, Alabansa, Iwaï, Djohounkolé, Igbola.
  - Pobe (1 village): Agbarou.
  - Ketou (6 villages): Mowodani, Idena3, Adjozoume, Okéola, Idena2, Kpankoun.
- **Species**: 100% of mosquitoes tested were *Anopheles gambiae s.s.* (page 6). Molecular form identification revealed both M and S forms (Figure 2), but *kdr* frequencies and bioassay results are reported pooled at the village level in Table 2.
- **Bioassays**: WHO cylinder tube tests using deltamethrin 0.05% with 60-min exposure and 24-h mortality observation. Both `n_exposed` and `No killed 24 hours after 1-hr exposure` (`n_dead`) are explicitly printed in Table 2, so `dead_alive_printed = true`.
- **Target Marker & Genotyping**: Corrected gene/marker naming to `kdr` / `L1014F` to match standard schema target marker definitions for Vgsc L995F (historically L1014F). Detected using HOLA technique (Lynd et al. 2005). Sample size `n_genotyped` (= 2n / 2) is explicitly confirmed in Figure 2. Genotype classes (RR, RS, SS) are not reported in the text or tables and are left null in accordance with Rule 2.
- **Geno-Pheno**: Bioassay dead and alive mosquitoes were not genotyped separately; DNA for PCR was extracted from control (non-exposed) mosquitoes (page 4). Thus, `geno_pheno` is empty.

## Validator warnings

- genotype #1 (2014_Tokponnon_banigbe, kdr L1014F): frequency only (no raw counts)
- genotype #2 (2014_Tokponnon_kokoumolou, kdr L1014F): frequency only (no raw counts)
- genotype #3 (2014_Tokponnon_agbarou, kdr L1014F): frequency only (no raw counts)
- genotype #4 (2014_Tokponnon_araromi, kdr L1014F): frequency only (no raw counts)
- genotype #5 (2014_Tokponnon_ko_dogba, kdr L1014F): frequency only (no raw counts)
- genotype #6 (2014_Tokponnon_mowodani, kdr L1014F): frequency only (no raw counts)
- genotype #7 (2014_Tokponnon_igbo_abikou, kdr L1014F): frequency only (no raw counts)
- genotype #8 (2014_Tokponnon_idena3, kdr L1014F): frequency only (no raw counts)
- genotype #9 (2014_Tokponnon_alabansa, kdr L1014F): frequency only (no raw counts)
- genotype #10 (2014_Tokponnon_tchaada, kdr L1014F): frequency only (no raw counts)
- genotype #11 (2014_Tokponnon_adjozoume, kdr L1014F): frequency only (no raw counts)
- genotype #12 (2014_Tokponnon_iwai, kdr L1014F): frequency only (no raw counts)
- genotype #13 (2014_Tokponnon_djohounkole, kdr L1014F): frequency only (no raw counts)
- genotype #14 (2014_Tokponnon_ketougbekon, kdr L1014F): frequency only (no raw counts)
- genotype #15 (2014_Tokponnon_lokossa, kdr L1014F): frequency only (no raw counts)
- genotype #16 (2014_Tokponnon_itakpako, kdr L1014F): frequency only (no raw counts)
- genotype #17 (2014_Tokponnon_igbola, kdr L1014F): frequency only (no raw counts)
- genotype #18 (2014_Tokponnon_ita_soumba, kdr L1014F): frequency only (no raw counts)
- genotype #19 (2014_Tokponnon_ko_aidjedo, kdr L1014F): frequency only (no raw counts)
- genotype #20 (2014_Tokponnon_zihan, kdr L1014F): frequency only (no raw counts)
- genotype #21 (2014_Tokponnon_gblo_gblo, kdr L1014F): frequency only (no raw counts)
- genotype #22 (2014_Tokponnon_okeola, kdr L1014F): frequency only (no raw counts)
- genotype #23 (2014_Tokponnon_idena2, kdr L1014F): frequency only (no raw counts)
- genotype #24 (2014_Tokponnon_kpankoun, kdr L1014F): frequency only (no raw counts)
- genotype #25 (2014_Tokponnon_daagbe, kdr L1014F): frequency only (no raw counts)
