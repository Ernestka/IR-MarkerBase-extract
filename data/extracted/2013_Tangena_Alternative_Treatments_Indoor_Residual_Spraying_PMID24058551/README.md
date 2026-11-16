# Extraction record — 2013_Tangena_Alternative_Treatments_Indoor_Residual_Spraying_PMID24058551

- Extracted: 2026-11-16
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 9 · Genotype rows: 12 · Bioassays: 5 · Geno-pheno rows: 0

## Decisions

### Data Extraction Notes

1. **Surveys**:
   - Surveys were split at the finest available spatial resolution (Sare Alpha and Sare Juldeh villages) and molecular species level (*An. arabiensis*, *An. coluzzii* / M form, and *An. gambiae s.s.* / S form) for genotype records from Table 1.
   - Additional site-level and combined-site surveys were created for *An. gambiae s.l.* to accommodate WHO tube bioassay records.

2. **Genotypes**:
   - Table 1 reports wild-caught larval specimen genotypes at codon 1014 (*Vgsc* L995F / L995S) in six genotype classes: LL (wild-type), LS (leucine/serine), LF (leucine/phenylalanine), SF (serine/phenylalanine), FF (phenylalanine/phenylalanine), and SS (serine/serine).
   - Following Rule 4b for multi-allelic codons, 1014F (L995F) and 1014S (L995S) are reported as two separate genotype rows per survey:
     - For 1014F: RR = FF, RS = LF + SF, SS = total N - RR - RS.
     - For 1014S: RR = SS (serine/serine), RS = LS + SF, SS = total N - RR - RS.
   - No SF (serine/phenylalanine) heterozygotes were observed in any sample (SF = 0 across all rows).

3. **Bioassays**:
   - WHO tube bioassays conducted on wild-reared *An. gambiae s.l.* females were extracted for DDT (4%), permethrin (0.75%), bendiocarb (0.1%), and pirimiphos-methyl (0.025%).
   - DDT mortality is reported separately per village (Sare Alpha: 22/44; Sare Juldeh: 11/28).
   - Permethrin, bendiocarb, and pirimiphos-methyl bioassay results are reported pooled across the two villages.
   - Cone bioassays on treated walls were conducted using a sensitive Cameroonian lab colony (*An. gambiae s.s.* M form, Yaoundé strain) and were excluded per Rule 5.

4. **Genotype-Phenotype**:
   - Genotype data split by bioassay outcome (alive vs. dead) was not reported in the paper; therefore `geno_pheno` is empty.
