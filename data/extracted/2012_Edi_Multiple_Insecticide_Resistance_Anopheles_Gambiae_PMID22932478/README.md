# Extraction record — 2012_Edi_Multiple_Insecticide_Resistance_Anopheles_Gambiae_PMID22932478

- Extracted: 2026-10-24
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 1 · Genotype rows: 0 · Bioassays: 5 · Geno-pheno rows: 10

## Decisions

### Extraction Summary
- **Study**: Edi et al. (2012), investigating insecticide resistance in *Anopheles gambiae* s.s. (M form) from Tiassalé, Côte d'Ivoire (collected May–Sept 2011).
- **Bioassays**: Extracted 5 diagnostic WHO bioassays from Table 1 (permethrin, deltamethrin, DDT, fenitrothion, bendiocarb).
- **Genotypes vs Geno-Pheno**: All genotyped mosquitoes reported in the paper are split by bioassay survival status (Alive / Dead) in Table 2 for kdr (L1014F) and Ace-1 (G119S). Therefore, all genotype data are extracted in `geno_pheno` linked to their respective bioassays, and `genotypes` is left empty to prevent double counting per Rule 6.
- **Mapping Ace-1 Genotypes**: In Table 2, Ace-1 alleles are designated G (wild-type, glycine) and S (resistant mutant, serine). Genotype classes GG = wild-type homozygote (`ss`), GS = heterozygote (`rs`), SS = mutant homozygote (`rr`).
- **Mapping kdr Genotypes**: In Table 2, kdr alleles are L (wild-type, leucine) and F (resistant mutant, phenylalanine). Genotype classes LL = wild-type homozygote (`ss`), LF = heterozygote (`rs`), FF = mutant homozygote (`rr`).
- **Coordinates**: Reported in paper as 5°52′47′′N, 4°49′48′′W, converted to decimal degrees (5.879722, -4.83).
