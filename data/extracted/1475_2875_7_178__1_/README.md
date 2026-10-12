# Extraction record — 1475_2875_7_178__1_

- Extracted: 2026-10-12
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Survey and Genotype Extraction Decisions
- **Surveys**: Split into two distinct surveys representing the two study sites in Dakar, Senegal: Bel-air and Ouakam. Mosquitoes were collected by human landing catches between May 2005 and May 2006 for the cohorts evaluated for resistance mutations.
- **Coordinates**: The paper provides coordinates for Dakar as a whole (14°40'20" N, 17°25'22" W; converted to 14.6722, -17.4228). Spatial precision is set to 'town'.
- **Markers**: 
  - Vgsc L995F: Reported as 'Kdr-w' in An. arabiensis. Full genotype counts (RR, RS, SS, and Total) are extracted directly from Table 3. Allele frequencies of 12% (0.12) for Bel-air and 9% (0.09) for Ouakam are recorded in `reported_allele_freq` as reported in the text.
  - Ace-1 G280S: Tested via PCR-RFLP (Weill et al. 2004). The text states 'Ace 1 mutations were not identified in any members of the An. gambiae complex either in Ouakam or in Bel-air'. Because no numeric sample sizes or class counts were broken down by species or site for Ace-1, it cannot be quantified into the genotypes table and is noted here.
- **Bioassays & Geno-Pheno**: No bioassays or genotype-phenotype tests were conducted in this study.
