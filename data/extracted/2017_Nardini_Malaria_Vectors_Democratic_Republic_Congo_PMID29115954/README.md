# Extraction record — 2017_Nardini_Malaria_Vectors_Democratic_Republic_Congo_PMID29115954

- Extracted: 2026-11-21
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 2 · Bioassays: 34 · Geno-pheno rows: 4

## Decisions

### Decisions and Derivations Summary

1. **Surveys**:
   - Four surveys were defined based on site (Kibali Gold Mine, Moto goldfields, DRC), year (2011 vs 2012), and molecular species (*An. gambiae s.s.* vs *An. funestus s.s.*).
   - 2011 collections used wild adults (F0), whereas 2012 bioassays and target site molecular assays were conducted using F1 progeny.
   - Site coordinates were provided in text on page 3 (`N03°08.846′ E29°36.548′`) and converted to decimal degrees: 3.147433°N, 29.609133°E.

2. **Markers and Target-Site Genotypes**:
   - **Vgsc 1014 codon (L1014S / L1014F)**: Tested in *An. gambiae s.s.* exposed to DDT (2012 cohort). Out of 55 specimens tested, 50 amplified successfully (5 failed). Genotype counts from Figure 2b/caption: RR (east) = 29, RS (east) = 3, RR (west) = 5, compound heterozygous (S/F) = 13.
     - Per Rule 4b for multi-allelic VGSC 995/1014:
       - **L1014S (Vgsc L995S)**: RR = 29 (S/S), RS = 3 (L/S) + 13 (S/F) = 16, SS = 50 - 29 - 16 = 5 (F/F homozygotes). True wild-type L/L count is 0 (all 50 genotyped carried at least one mutation).
       - **L1014F (Vgsc L995F)**: RR = 5 (F/F), RS = 0 (L/F) + 13 (S/F) = 13, SS = 50 - 5 - 13 = 32 (29 S/S + 3 L/S).
   - **Rdl A296G**: Genotyped separately in dieldrin bioassay survivors (1 alive, heterozygous RS) and mortalities (32 dead, homozygous SS), recorded under `geno_pheno`.
   - **Ace-1 G119S**: Genotyped in bendiocarb bioassay cohort (22 alive, 25 dead). All 47 were wild-type SS (0 mutants detected), recorded under `geno_pheno`.

3. **Bioassays & Synergists**:
   - Diagnostic bioassays from Table 3 (*An. gambiae*) and Table 4 (*An. funestus*) for 2011 and 2012 were extracted.
   - Synergist assays (deltamethrin with PBO and TPP) from Table 5 were extracted.
   - Inconsistencies noted: Table 3 reports 2012 dieldrin N = 32 (97% mortality), whereas page 4 text reports 1 survivor + 32 mortalities (N = 33 total).

## Validator warnings

- bioassay 2017_Nardini_DRC_kibali_2012_gambiae_dieldrin_04: inconsistent in the paper (values kept as printed) — Table 3 reports N = 32 with 97% mortality, whereas text on page 4 reports 1 survivor and 32 mortalities (N = 33 total).
- bioassay 2017_Nardini_DRC_kibali_2012_gambiae_dieldrin_04: n_dead + n_alive = 33 but n_exposed = 32
- bioassay 2017_Nardini_DRC_kibali_2012_gambiae_dieldrin_04: computed mortality 100.0% differs from reported 97.0% (Abbott correction?)
