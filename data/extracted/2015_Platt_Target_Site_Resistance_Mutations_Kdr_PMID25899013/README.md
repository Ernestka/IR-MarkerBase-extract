# Extraction record — 2015_Platt_Target_Site_Resistance_Mutations_Kdr_PMID25899013

- Extracted: 2026-11-17
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 10 · Bioassays: 3 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The study investigated mating competitiveness of Anopheles coluzzii (formerly An. gambiae M molecular form) collected in April 2010 in VK3 village, Vallée du Kou, Burkina Faso.
- Mosquitoes were divided into distinct sample groups:
  1. Mated males captured in copula from swarms (sweep net).
  2. Uncoupled males captured from swarms after coupling ceased (sweep net).
  3. Mated females captured in copula from swarms (sweep net).
  4. F1 virgin males reared from indoor-resting blood-fed females.
  5. F1 females reared from indoor-resting blood-fed females used for WHO bioassays.
- Each of these five cohorts is represented as a separate survey record to avoid confounding different sampling methods, generations, sexes, and mating phenotypes.

### Coordinates
- Coordinates printed on page 244 under Study site: 'The Vallée du Kou (VK) (4° 25’ W, 11° 25’ N)'. Note that the OCR had an artifact reading '40° 25’ W', but inspection of the original PDF page 244 confirms 4° 25’ W. Converted: 11° 25' N = 11.4167, 4° 25' W = -4.4167.

### Target Resistance Markers
- Target markers genotyped by pyrosequencing:
  - `kdr` `L1014F`: genotype counts and frequencies extracted directly from Table 1 for mated males, uncoupled males, F1 virgin males, and mated females.
  - `RDL` `A296S`: genotype counts and frequencies extracted directly from Table 3 for all four groups.
  - `Ace-1` `G119S`: the main text (page 246) reports allele frequencies only for coupled males (5.9%) and F1 virgin males (1.6%), and notes that no homozygotes were detected. Because exact counts were only provided in Supplementary Figure S1, the allele frequencies are reported with count fields left null per Rule 2.
- Pooled totals across all sample groups (bottom rows of Table 1 and Table 3) were omitted per Rule 7.

### Bioassays and Genotype-Phenotype
- WHO tube bioassay mortalities for permethrin 0.75% (12%), DDT 4% (6%), and bendiocarb 0.1% (91%) on 2-5 day old F1 adult females are reported in the text (page 244-245). Total numbers exposed per insecticide are in Supplementary Table S4 (not printed in main text), so `n_exposed`, `n_dead`, and `n_alive` are left null, with `reported_mortality_pct` recorded.
- Dieldrin 4% bioassay was conducted according to methods, but results are not printed in the main text.
- `geno_pheno` is empty because genotypes were analyzed in relation to mating success (coupled vs uncoupled males), not for bioassay survivors vs dead.

## Validator warnings

- genotype #9 (2015_platt_vk3_2010_mated_males, Ace-1 G119S): frequency only (no raw counts)
- genotype #10 (2015_platt_vk3_2010_f1_virgin_males, Ace-1 G119S): frequency only (no raw counts)
