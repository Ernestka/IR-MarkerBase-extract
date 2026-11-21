# Extraction record — 2017_Rakotoson_Insecticide_Resistance_Status_Three_Malaria_PMID28835269

- Extracted: 2026-11-21
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 28 · Genotype rows: 30 · Bioassays: 36 · Geno-pheno rows: 0

## Decisions

### Study and Survey Structure
- The study evaluates insecticide resistance across Madagascar in An. gambiae (s.l.), An. funestus, and An. mascarensis.
- Standard bioassays for An. gambiae (s.l.) across 18 sites were reported only in Additional file 1 (Table S1) and graphical summary figures; however, complete numeric bioassay data are reported in Table 2 (CDC bottle bioassays on wild adult An. funestus and An. mascarensis) and Table 3 (synergist CDC bottle bioassays on wild-reared An. gambiae s.l. conducted in 2016).
- Surveys were split into:
  1. Table 4 molecular species surveys (2015/2016 collections from 8 sentinel sites) where individual mosquitoes were identified to species (An. gambiae s.s., An. arabiensis, An. coluzzii, An. merus) and genotyped for Vgsc L1014F and L1014S.
  2. Table 2 surveys for wild-collected adult An. funestus and An. mascarensis tested in CDC bottle bioassays (2015/2016).
  3. Table 3 surveys for wild-reared An. gambiae (s.l.) tested in synergist bioassays (2016).

### Genotype Extractions
- A total of 986 An. gambiae (s.l.) specimens across 8 sites were molecularly identified and tested for both Vgsc L1014F and L1014S by PCR. The paper reports that zero resistant alleles were detected across all 986 specimens (RR = 0, RS = 0, SS = N). Genotypes are extracted per site and per molecular species matching Table 4.
- Ace-1 G119S was tested in 248 mosquitoes from three sites, and all were negative. Because the specific three sites and species breakdowns are not specified in the text or tables, these 248 individuals could not be attributed to specific surveys and were omitted from the genotypes array.

### Genotype-Phenotype Data
- Table 5 reports the species distribution (An. arabiensis vs An. gambiae s.s.) among survivors and dead mosquitoes from bioassays, not target marker genotypes. The molecular tests showed no kdr or ace-1 mutations anywhere in the tested specimens, and no target marker genotype frequencies broken down by dead/alive phenotype were provided. Consequently, `geno_pheno` is empty.

### Bioassays
- All bioassays reported in Table 2 (8 tests) and Table 3 (28 tests) were extracted with their exact reported mortality percentages and sample sizes. Dead/alive counts were not printed as integer counts (only % mortality and total N tested are given in % Mortality (n)), so `dead_alive_printed = false` and `n_dead = null`, `n_alive = null` according to extraction rules.
