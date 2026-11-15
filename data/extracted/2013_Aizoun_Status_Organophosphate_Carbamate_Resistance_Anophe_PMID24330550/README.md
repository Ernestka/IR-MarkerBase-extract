# Extraction record — 2013_Aizoun_Status_Organophosphate_Carbamate_Resistance_Anophe_PMID24330550

- Extracted: 2026-11-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 2 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Study Overview**: The study examined susceptibility to fenitrothion (organophosphate) and bendiocarb (carbamate) using CDC bottle bioassays in *Anopheles gambiae s.l.* field collections from four districts in Benin in 2012 (Seme, Tanguieta, Kandi, Malanville). Species-specific PCR confirmed 100% of tested specimens were *Anopheles gambiae s.s.*
- **Ace-1 Genotyping**: Only mosquitoes from Kandi and Malanville were genotyped for the Ace-1 G119S mutation (Table 2). Tanguieta and Seme were not genotyped in this study (explicitly noted on Page 5: 'Although this mechanism was not investigated in Anopheles gambiae Tanguieta populations in the current study...').
- **Genotypes vs. Geno-Pheno**: Table 2 lists Ace-1 genotypes for Kandi and Malanville ('issue from performing CDC bioassays tests') without splitting the counts into bioassay survivors and non-survivors (dead vs. alive). Consequently, per rule 6, these records are placed in `genotypes`, and `geno_pheno` is left empty.
- **Bioassay Exposure Duration**: While the title of Table 1 refers to 'after 2 hours exposure', the text (Pages 3 and 4) explicitly explains that mosquitoes were monitored up to 120 minutes, but the diagnostic threshold mortality was recorded at 30 minutes (e.g., 'A percentage mortality of 57.14% of An. gambiae from Malanville and 76.72% of An. gambiae from Tanguieta were recorded after 30 minutes of exposure to CDC bottles treated with fenitrothion'). Thus, `exposure_duration_min` is recorded as 30.0.
- **Bioassay Counts**: Table 1 gives `Number tested` and `% Mortality`, but does not print the explicit count of dead or alive mosquitoes. Per Rule 2, `dead_alive_printed` is set to `false`, `n_dead` and `n_alive` are left `null`, and `% Mortality` is recorded in `reported_mortality_pct`.
- **Control Strain**: The Kisumu laboratory reference strain reported in Table 1 was omitted per Rule 5.
