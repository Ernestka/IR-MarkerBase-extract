# Extraction record — 2010_Weetman_Association_Mapping_Insecticide_Resistance_Wild_PMID20976111

- Extracted: 2026-11-12
- Model: gemini:gemini-3.6-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 3 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys**:
   - Split by collection site (Yaoundé, Cameroon vs Dodowa, Ghana) and molecular form (*An. coluzzii* / M form vs *An. gambiae s.s.* / S form).
   - Sample sizes per molecular form were derived from cluster/tree sizes reported in Figure 2a and the text (Cameroon M: 673, Cameroon S: 62; Ghana S: 770).

2. **Genotypes**:
   - Extracted Vgsc L995F (reported as `kdr L1014F` / SNP 2L 2422652) minor allele frequencies (MAF) for Cameroon M, Cameroon S, and Ghana S from Table 2.
   - Vgsc L995S (`kdr L1014S`) was noted in text (page 6) as present in Cameroon M and S forms (sequenced in N=29 S forms and N=16 M forms), but no genotype counts, carrier counts, or allele frequencies were printed. Per extraction schema rules, it is omitted from the genotype table.
   - No other target markers were found in Table 2 or main text.

3. **Bioassays & Geno-Pheno**:
   - Bioassays were used for establishing LT50 thresholds (16.8 min for Cameroon, 122 min for Ghana) to phenotypically partition mosquitoes for association mapping. Standard WHO bioassay tables (reporting exact numbers exposed, dead, and alive for fixed exposures) were not printed.
   - Individual SNP genotypes/counts split by alive/dead status were not printed as raw counts or single-SNP tables (only overall MAFs, odds ratios, and haplotype block frequencies in Figure 7), so `geno_pheno` is left empty per Rule 2 and Rule 6.

## Validator warnings

- genotype #1 (2010_Weetman_Association_Mapping_Insecticide_Resistance_Wild_PMID20976111_cameroon_yaounde_2006_m, Na channel L1014F): frequency only (no raw counts)
- genotype #2 (2010_Weetman_Association_Mapping_Insecticide_Resistance_Wild_PMID20976111_cameroon_yaounde_2006_s, Na channel L1014F): frequency only (no raw counts)
- genotype #3 (2010_Weetman_Association_Mapping_Insecticide_Resistance_Wild_PMID20976111_ghana_dodowa_2006_s, Na channel L1014F): frequency only (no raw counts)
