# Extraction record — s12936_025_05562_9

- Extracted: 2026-10-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 6 · Genotype rows: 7 · Bioassays: 24 · Geno-pheno rows: 0

## Decisions

### Study Design and Survey Resolution
- Mosquitoes were collected in July 2023 (start of the rainy season) and October 2023 (end of the rainy season) across three villages in Nanoro Health District, Centre-West Region, Burkina Faso: Seguedin (33 km from the dam), Nazoanga (14 km from the dam), and Soum (dam site).
- Six surveys were established (one for each village x season combination).
- Indoor-collected gravid/semigravid females were brought to the insectary to lay eggs; all bioassays and subsequent molecular tests were performed on F1 progeny (3–5 days old).

### Species Identification
- PCR identification of the An. gambiae complex revealed 100% An. coluzzii among successfully identified mosquitoes in Seguedin and Soum at both time points. Consequently, `molecular_species` is specified as `Anopheles coluzzii` for these two sites.
- In Nazoanga, An. arabiensis comprised 8.5% of identified specimens at the beginning and 5.4% at the end of the season (with An. coluzzii making up the remainder). Since bioassays and genotype counts were reported for An. gambiae s.l. as a whole, `molecular_species` is left as null for Nazoanga.

### Genotypes
- Target markers screened were kdr West (Vgsc L1014F) and kdr East (Vgsc L1014S).
- Genotype counts for kdr West (RR, RS, SS, and N) are extracted directly from Table 1 for all six village x season combinations.
- kdr East was detected only in Nazoanga at the beginning of the rainy season with an allele frequency of 0.03 (page 5 text), but individual genotype counts (RR, RS, SS) were not reported. In accordance with Rule 2, counts are left null and `reported_allele_freq` is recorded as 0.03.

### Bioassays
- Bioassays were standard WHO tube tests on F1 adults with 60 min exposure and 24 h holding period, covering deltamethrin (0.05%), bendiocarb (0.1%), pirimiphos-methyl, and deltamethrin (0.05%) pre-exposed to 4% PBO.
- Exact numbers of mosquitoes exposed, dead, and alive per individual bioassay were not printed in the paper or figures (only 4 replicates of 20–25 mosquitoes were mentioned in the methods protocol, and exact percentages were reported in the text and Figure 2). Therefore, `dead_alive_printed` is set to false, `n_exposed`, `n_dead`, and `n_alive` are left null, and `reported_mortality_pct` is populated from the text.
- Discrepancy noted for pirimiphos-methyl concentration: the Methods section (page 3) specifies pirimiphos-methyl (0.1%), while Figure 2 legend indicates 'Pirimiphosmethyl_0,25%'. This is documented in `inconsistency_note`.

### Genotype-Phenotype
- No genotype-phenotype data (genotypes stratified by bioassay survivors vs dead) were reported in the paper, so `geno_pheno` is empty.

## Validator warnings

- genotype #2 (s12936_025_05562_9_nazoanga_jul2023, kdr L1014S): frequency only (no raw counts)
- bioassay s12936_025_05562_9_seguedin_jul2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
- bioassay s12936_025_05562_9_seguedin_oct2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
- bioassay s12936_025_05562_9_nazoanga_jul2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
- bioassay s12936_025_05562_9_nazoanga_oct2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
- bioassay s12936_025_05562_9_soum_jul2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
- bioassay s12936_025_05562_9_soum_oct2023_pirimiphos_methyl: inconsistent in the paper (values kept as printed) — Methods text on page 3 states pirimiphos-methyl (0.1%), whereas Figure 2 legend specifies Pirimiphosmethyl_0,25%.
