# Extraction record — 2015_Cisse_Characterizing_Insecticide_Resistance_Anopheles_Ga_PMID26296644

- Extracted: 2026-11-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 47 · Genotype rows: 45 · Bioassays: 52 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Resolution:**
   - 13 sites across Mali sampled between November and December 2012.
   - Bioassay testing in Table 3 was reported on unseparated *Anopheles gambiae s.l.* populations for each site. General surveys for bioassays were created at the site level (`<site>_sl`).
   - Molecular species identification (Table 7) and target-site genotype counts (Table 5 & Table 6) were reported per molecular species (*An. coluzzii*, *An. gambiae s.s.*, and *An. arabiensis*). Therefore, individual surveys were created for each identified species per site.

2. **Markers Extracted:**
   - `Vgsc L995F`: Reported in Table 5 as '1014F' / 'Leu-Phe kdr' for *An. coluzzii*, *An. gambiae s.s.*, and *An. arabiensis*. Genotype counts (RR, RS, SS) and reported allele frequencies F(kdr) were extracted directly from Table 5.
   - `Ace-1 G280S`: Reported in Table 6 as 'ace-1R' for four sites (Bla, Kita, Bougouni, Kadiolo) across *An. coluzzii*, *An. gambiae s.s.*, and *An. arabiensis*. Genotype counts (RR, RS, SS) and reported allele frequencies F(ace-1R) were extracted directly from Table 6.

3. **Bioassay Data:**
   - Diagnostic WHO tube tests for DDT 4%, Deltamethrin 0.05%, Lambda-cyhalothrin 0.05%, Bendiocarb 0.01%, and Fenitrothion 1%.
   - Table 3 reports `% Mortality` and sample size `(N)`. As explicit counts for dead or alive mosquitoes were not printed, `dead_alive_printed` is set to `false`, `n_dead` and `n_alive` are set to `null`, and `n_exposed` is set to `N`.
