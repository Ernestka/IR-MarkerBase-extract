# Extraction record — 2015_Ngufor_Insecticide_Resistance_Profile_Anopheles_Gambiae_PMID26581678

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 4 · Bioassays: 8 · Geno-pheno rows: 0

## Decisions

# Extraction Decisions for Ngufor et al. (2015)

## Survey and Species Resolution
- The study evaluates the Anopheles gambiae s.l. population from the Phase II experimental hut station in Cové, southern Benin (7°14'N, 2°18'E).
- Species PCR and SINE-PCR identified the population as a mixture of Anopheles coluzzii (100% in rainy season; 77% in dry season) and Anopheles gambiae s.s. (23% in dry season only). However, target site resistance genotypes were not reported separately by molecular species or season, but only as a pooled total for the site (Table 2). Therefore, a single survey record was created for Anopheles gambiae s.l.
- Sample collection spanned late 2013 to late 2014, including both dry (October 2013 / September-October 2014) and rainy seasons (March 2014).

## Target Site Genotypes
- Target markers genotyped via TaqMan assays (Table 2) include Vgsc L1014F (L995F), Ace-1 119S (G280S), and Vgsc N1575Y (N1570Y).
- For Vgsc codon 995/1014, the text explicitly reports that "No 1014S alleles were found" across the tested cohort (n = 247). As per Rule 4b for multi-allelic codons, L1014S is extracted as a separate row with RR = 0, RS = 0, and SS = 247 (all individuals wild-type for this allele). The true wild-type L/L count is 6, and there are no F/S heterozygotes.

## Bioassays
- WHO cylinder susceptibility tests: Approximately 100 mosquitoes (4 replicates of 25) were exposed to diagnostic doses. Full susceptibility (100% mortality) is reported in the text for bendiocarb 0.1%, malathion 5%, and fenitrothion (1% in Fig. 4, noted as 4% in methods). Mortalities for DDT 4% (~9%), deltamethrin 0.05% (~11.5%), and permethrin 0.75% (~9%) were read from Figure 4 (text states mortality was < 15%).
- Synergist assays in CDC bottles: 150 adult females were tested with permethrin alone (32% mortality reported in text) and permethrin with 1-hour PBO pre-exposure (50% mortality reported in text).
- Experimental hut trial data (Figure 6) evaluate net and IRS product performance pooled across 4 trials and are not extracted as standard susceptibility bioassays.
- Laboratory susceptible controls (Kisumu) were excluded.
- No genotypes were split by bioassay outcome (alive vs dead), so `geno_pheno` is empty.

## Validator warnings

- bioassay 2015_Ngufor_Cove_who_fenitrothion: inconsistent in the paper (values kept as printed) — Page 3 methods states '4 % fenithrothion', but Figure 4 labels the test as 'Fenitrothion 1%'.
