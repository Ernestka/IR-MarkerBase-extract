# Extraction record — 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245

- Extracted: 2026-11-19
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 3 · Genotype rows: 1 · Bioassays: 17 · Geno-pheno rows: 0

## Decisions

# Data Extraction Decisions: Dadzie et al. (2016)

## Study & Survey Design
- **Sites**: Larval sampling was carried out from 15 October to 7 November 2013 across two sites in Kome, Logone Oriental region, southern Chad: Site A (8°36′0″N, 16°26′0″E = 8.6°N, 16.433333°E) and Site B (8°21′0″N, 15°78′0″E = 8.35°N, 16.3°E; 78 arcminutes converted to 1.3°). Larvae were reared to adults in the laboratory.
- **Surveys**: Separate survey records were created for Site A (`..._site_a`) and Site B (`..._site_b`) to host their respective bioassays from Table 1. A pooled survey (`..._kome_pooled`) was created for the N = 206 mosquitoes molecularly analyzed across both sites (107 from Site A and 99 from Site B).

## Bioassays
- Bioassay results are extracted from Table 1 for 9 insecticides at Site A and 8 insecticides at Site B (Propoxur was not evaluated at Site B).
- **Exposure numbers**: Table 1 gives 'No. tested: 100' for every test, while Methods states that each insecticide test comprised 'four replicates of 20 mosquitoes per test and a control setup of 20 mosquitoes'. Therefore, 80 mosquitoes were exposed to insecticide and 20 were controls. We recorded `n_exposed = 80` (with `inconsistency_note` documenting the Table 1 value of 100).
- Only percentage mortalities at 24 h (with 95% CIs) are printed; no raw dead/alive counts are provided (`dead_alive_printed = false`, `n_dead = null`, `n_alive = null`).

## Genotypes
- **Target markers**: Knockdown resistance (kdr-w / Vgsc L995F, L1014F) and acetylcholinesterase-1 (Ace-1 G280S / G119S).
- **kdr-w (Vgsc L995F)**: Page 5 states: 'irrespective of susceptibility status, 43 were homozygous for the resistant allele (RR), 19 as heterozygous (RS) and 38 % as homozygous susceptible alleles (SS)'. Because 43 + 19 + 38 = 100, these numbers clearly represent percentages of the population with '%' omitted from 43 and 19. Per Rule 8, we record `rr = 43` and `rs = 19` as printed, leave `ss = null` (since printed as '38 %'), and record the arithmetic discrepancy with N = 206 in `inconsistency_note`.
- **Species-specific kdr-w**: In text and Fig 4, genotype frequencies per sibling species/molecular form are reported as decimal fractions/percentages of the entire pooled population (e.g., An. coluzzii: 37.4% RR, 17.5% RS, 8.3% SS; An. gambiae s.s.: 1% or 5% RR). Because these are decimals/percentages and raw integer counts are not reported, they cannot be extracted into integer count fields under the non-derivation rules.
- **Ace-1**: 137 mosquitoes were evaluated. The text provides contradictory qualitative statements ('homozygous susceptible Ace-1R allele was the most predominant', 'frequency of the Ace-1R homozygote resistance allele (RR) was low', and 'complete absence of Ace-1R gene mutation') but provides no raw counts or allele frequencies. Thus, no Ace-1 genotype row could be extracted.

## Genotype-Phenotype Associations
- Page 6 mentions 'about 36 % heterozygous kdr-w in the individuals that survived the WHO susceptibility tests' and notes that killed mosquitoes 'mostly had susceptible genes'. Because neither sample sizes nor full genotype counts are reported per phenotype group or per specific insecticide, no records could be formed for `geno_pheno`.

## Validator warnings

- genotype #1 (2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_kome_pooled, kdr-w L1014F): inconsistent in the paper (values kept as printed) — Text states '43 were homozygous for the resistant allele (RR), 19 as heterozygous (RS) and 38 % as homozygous susceptible alleles (SS)'. 43 + 19 + 38 = 100, which indicates these numbers are population genotype percentages with '%' omitted on 43 and 19. If read as raw counts, RR (43) + RS (19) != 206.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_permethrin_075: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_lambdacyhalothrin_005: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_deltamethrin_005: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_ddt_4: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_fenitrothion_1: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_malathion_5: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_pirimiphos_methyl_09: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_propoxur_01: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_a_bendiocarb_01: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_permethrin_075: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_lambdacyhalothrin_005: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_deltamethrin_005: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_ddt_4: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_fenitrothion_1: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_malathion_5: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_pirimiphos_methyl_09: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
- bioassay 2016_Dadzie_Species_Composition_Insecticide_Resistance_Status_PMID27553245_site_b_bendiocarb_01: inconsistent in the paper (values kept as printed) — Table 1 prints 'No. tested: 100', but Methods states each test comprised four replicates of 20 mosquitoes (80 exposed to insecticide) and a control setup of 20 mosquitoes.
