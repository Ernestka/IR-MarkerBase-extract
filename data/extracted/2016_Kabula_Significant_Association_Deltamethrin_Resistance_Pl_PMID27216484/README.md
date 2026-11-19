# Extraction record — 2016_Kabula_Significant_Association_Deltamethrin_Resistance_Pl_PMID27216484

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 1 · Bioassays: 1 · Geno-pheno rows: 2

## Decisions

### Survey and Species Stratification
- Collections occurred between November 2012 and May 2013 in Zeneti village (-5.216667, 38.65), Muheza district, northeast Tanzania.
- Three surveys were created:
  1. `..._zeneti_sl`: Anopheles gambiae s.l. for the actual WHO tube susceptibility bioassay performed on 948 wild adult females.
  2. `..._zeneti_ss`: Anopheles gambiae s.s. for the molecularly identified subset of 526 mosquitoes genotyped for Vgsc-L1014S.
  3. `..._zeneti_ara`: Anopheles arabiensis for the molecularly identified subset of 19 mosquitoes genotyped for Vgsc-L1014S.

### Bioassays
- The bioassay was conducted on 948 adult females exposed to 0.05% deltamethrin using WHO tubes, resulting in 77.7% mortality at 24 h. Because exact dead/alive counts were not printed in the paper, `dead_alive_printed` is false and `n_dead` / `n_alive` are left null.
- In accordance with Rule 8b ('Never build a bioassay record from genotyped subsets'), the 526 genotyped An. gambiae s.s. individuals were not used to fabricate a separate bioassay record.

### Genotypes and Geno-Pheno
- An. gambiae s.s. (N=526) mosquitoes were reported broken down by bioassay phenotype (alive/resistant: N=127; dead/susceptible: N=399) in Table 1. As required by Rule 6, these are recorded exclusively in `geno_pheno` to avoid double-counting. `bioassay_id` is set to null because the bioassay was executed at the species complex level (`..._zeneti_sl`) while the genotype-phenotype data are reported specifically for An. gambiae s.s. (`..._zeneti_ss`).
- Serine (Ser) is the mutated resistant allele (RR = Ser/Ser, RS = Ser/Leu, SS = Leu/Leu).
- An. arabiensis (N=19) was not reported split by bioassay outcome. Only its allele frequency (0.32) was printed, so it is recorded in `genotypes` with genotype class counts left null per Rule 2.
- Plasmodium falciparum sporozoite infection and blood meal origin data reported in Table 1 are non-insecticidal phenotypes and were excluded from `geno_pheno`.

## Validator warnings

- genotype #1 (2016_Kabula_Significant_Association_Deltamethrin_Resistance_Pl_PMID27216484_zeneti_ara, Vgsc L1014S): frequency only (no raw counts)
- geno_pheno #1 (deltamethrin, Vgsc L1014S, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, Vgsc L1014S, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
