# Extraction record — 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 2 · Bioassays: 17 · Geno-pheno rows: 0

## Decisions

### Data Extraction Decisions
1. **Surveys**:
   - Created two site-specific surveys (`2016_Dadzie_kome_site_a` and `2016_Dadzie_kome_site_b`) for bioassay data as bioassays were conducted and reported per site.
   - Coordinates for Site B (8°21′0″N, 15°78′0″E) contain a printed value of 78 minutes. Following rule 8 (Values exactly as printed), degrees-minutes-seconds were converted directly (15 + 78/60 = 16.3°E).
   - Created a pooled survey (`2016_Dadzie_kome_pooled`) for genotype data, which were analyzed and reported across the pooled 206 mosquitoes from both sites.
2. **Bioassays**:
   - Bioassay data extracted from Table 1 for 9 insecticides at Site A and 8 at Site B (Propoxur was not tested at Site B).
   - Table 1 reports n_exposed = 100 and percent 24h mortality. Per Rule 2, `dead_alive_printed` is set to false, and `n_dead` and `n_alive` are left null.
3. **Genotypes**:
   - **Ace-1 G280S (Ace-1R)**: Text on pages 6-7 states that 137 individuals across all categories were tested for Ace-1 and all were homozygous susceptible (SS), with complete absence of the mutation. Extracted as n_genotyped = 137, RR = 0, RS = 0, SS = 137, reported_allele_freq = 0.0.
   - **Vgsc L995F (kdr-w)**: Text on page 5 and Abstract states: 'irrespective of susceptibility status, 43 were homozygous for the resistant allele (RR), 19 as heterozygous (RS) and 38 % as homozygous susceptible alleles (SS)'. Recorded as printed (RR = 43, RS = 19, SS = 38, n_genotyped = 206), and the discrepancy (RR+RS+SS = 100 != 206, likely printed percentages without % sign on 43 and 19) is documented in `inconsistency_note` per Rule 8.
4. **Geno-pheno**:
   - The text mentions that about 36% of survivors were heterozygous for kdr-w, but does not report exact counts or full genotype breakdowns for survivors/dead. Thus, no geno_pheno records were extractable.

## Validator warnings

- genotype #2 (2016_Dadzie_kome_pooled, kdr kdr-w): inconsistent in the paper (values kept as printed) — Text states: 'Analysis of a sample of 206 An. gambiae (s.l.) for kdr-w showed that irrespective of susceptibility status, 43 were homozygous for the resistant allele (RR), 19 as heterozygous (RS) and 38 % as homozygous susceptible alleles (SS).' RR (43) + RS (19) + SS (38) = 100, but N = 206. The values 43, 19, and 38% appear to be percentages summing to 100% rather than counts, but 43 and 19 were printed as integers without percent signs.
- genotype #2 (2016_Dadzie_kome_pooled, kdr kdr-w): RR+RS+SS = 43+19+38 = 100 but n_genotyped = 206
