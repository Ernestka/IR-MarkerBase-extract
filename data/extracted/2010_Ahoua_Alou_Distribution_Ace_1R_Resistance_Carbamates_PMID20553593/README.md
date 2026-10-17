# Extraction record — 2010_Ahoua_Alou_Distribution_Ace_1R_Resistance_Carbamates_PMID20553593

- Extracted: 2026-10-17
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 10 · Genotype rows: 8 · Bioassays: 23 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions

1. **Surveys & Molecular Species Mapping**:
   - In 4 of the 6 collection sites (Yamoussoukro, Tiassalé, Nieky, Abidjan), 100% of genotyped mosquitoes belonged to the M form. For these 4 sites, bioassays and genotypes share a single survey record with `molecular_species = 'Anopheles coluzzii'` (M form).
   - In 2 sympatric sites (Toumbokro: 58.1% M, 41.9% S; Toumodi: 98.7% M, 1.3% S), bioassays were performed on the field-collected, unseparated *Anopheles gambiae s.s.* population. Thus, separate general surveys (`_gen`) were created for bioassays, while M form (`_m`) and S form (`_s`) surveys were created for genotype records.
   - M form is mapped to `Anopheles coluzzii` and S form to `Anopheles gambiae s.s.` per current taxomony.

2. **Bioassays**:
   - 23 WHO tube diagnostic bioassays were extracted from Table 1.
   - Mortality rates are reported as percentages with sample size in parentheses. Per Rule 2, `dead_alive_printed` is set to `false`, and `n_dead`/`n_alive` are set to `null`.
   - Chlorpyrifos-methyl bioassay was 'NT' (not tested) for Yamoussoukro and is excluded.
   - Kisumu laboratory reference strain controls were omitted per Rule 5.

3. **Genotypes**:
   - Ace-1 G119S genotype counts (S, RS, R) and allele frequencies were extracted directly from Table 2 for a total of 328 genotyped mosquitoes across 8 species x location combinations.
   - No homozygous resistant (RR) individuals were found in any population.
