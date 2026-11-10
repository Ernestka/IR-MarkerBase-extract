# Extraction record — 2008_Kamau_Status_Insecticide_Susceptibility_Anopheles_Gambia_PMID20345290

- Extracted: 2026-11-10
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 11 · Genotype rows: 8 · Bioassays: 15 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
- **Surveys**: Created 11 distinct surveys based on site and species breakdown as presented in the paper (Rota, Kisii, Kwale, Ahero, Mwea). For Rota, bioassays were performed on morphological *An. gambiae s.l.* and *An. funestus*, while genotyping was conducted on molecularly identified *An. gambiae s.s.* and *An. arabiensis*.
- **Bioassays**: Extracted bioassay results from Table 1 for field populations from Rota and Ahero. Laboratory reference strain (Kisumu strain) bioassay controls were excluded per Rule 5. In Table 1, `n` represents total mosquito families assayed; exact counts of dead/alive mosquitoes were not printed, so `dead_alive_printed` is `false` and counts are left `null` with `reported_mortality_pct` recorded as printed.
- **Genotypes**: Extracted genotype counts (SS, SR, RR) for the East African *kdr* mutation (L1014S, Vgsc L995S) from Table 2. The West African *kdr* mutation (L1014F, Vgsc L995F) was reported on page 5 as absent across 674 sampled alleles (Rota: 238 alleles, Kisii: 80, Kwale: 100, Mwea: 154, Ahero: 102), but without species breakdown for the tested subset, so it is noted here rather than added as separate species genotype rows.
- **Geno-Pheno**: Empty array as genotypes were not reported separately for bioassay survivors and dead mosquitoes.
