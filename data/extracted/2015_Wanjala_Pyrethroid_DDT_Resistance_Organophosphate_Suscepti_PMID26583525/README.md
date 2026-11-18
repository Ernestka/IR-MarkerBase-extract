# Extraction record — 2015_Wanjala_Pyrethroid_DDT_Resistance_Organophosphate_Suscepti_PMID26583525

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 20 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Study Design and Sampling**: Mosquito larvae were collected across 7 sentinel sites in western Kenya (Ahero, Kisian, Chulaimbo, Emutete, Emakakha, Iguhu, Bungoma) between April 2012 and July 2013, reared to adults in the KEMRI Kisumu insectary, and subjected to standard WHO tube bioassays. Species identification was performed by 16S rDNA PCR on 1,002 emerged adults, identifying An. gambiae s.s. and An. arabiensis.
- **Surveys**: Surveys were created at the molecular species level (An. gambiae s.s. and An. arabiensis) for each site where kdr genotyping data were reported in Table 2 (10 site-species pairs total). Site 'Kisan' in Table 2 is a minor typographical error for 'Kisian'.
- **Target Markers**: A subset of 579 mosquitoes was genotyped for kdr codon 1014 using TaqMan PCR. 
  - Vgsc L995S (reported as L1014S): Genotype counts are printed in Table 2 (LL = wild type [SS for marker], LS = heterozygous [RS for marker], SS = homozygous resistant [RR for marker]).
  - Vgsc L995F (reported as L1014F): The paper explicitly reports that L1014F was not detected in An. gambiae s.s. or An. arabiensis at any site (p. 2179). Per multi-allelic codon rule 4b, L1014F is recorded with RR = 0, RS = 0, and SS = n_genotyped.
  - Total mosquitoes in Table 2 sum to 542 (411 An. gambiae s.s. and 131 An. arabiensis); the remaining 37 of 579 examined mosquitoes may represent samples that failed molecular amplification or species verification.
- **Bioassays**: WHO tube bioassay results were reported only as a bar graph (Figure 2) without numerical tables or printed site-specific mortality counts/percentages, and were conducted on pooled An. gambiae s.l. populations prior to molecular species identification. Because exact test-level counts or mortality percentages were not printed, and per Rule 8 values are not guessed/digitized from graphs, bioassays were not extracted into the bioassays table.
- **Geno-Pheno**: Bioassay survivors and dead were not genotyped separately in Table 2; therefore, geno_pheno is empty.
