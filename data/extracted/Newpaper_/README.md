# Extraction record — Newpaper_

- Extracted: 2026-10-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 13 · Geno-pheno rows: 4

## Decisions

### Survey and Site Decisions
- Larval collections were conducted weekly from July to September 2011 in 4 sites across different administrative districts of Bomi County, Liberia (Table 1, Figure 1).
- Table 1 reports UTM X-Y coordinates (without zone specification), so `latitude_reported` and `longitude_reported` are kept null per extraction guidelines.
- All genotyped mosquitoes (n = 169) were from Site 3 (Klay District, Malema and Gissi camps) where cone bioassays were performed. All 169 were identified as Anopheles gambiae s.s. (98% M form [166 mosquitoes] and 3 S form, all of which survived).

### Genotypes vs. Geno-Pheno
- All 169 genotyped mosquitoes are reported with phenotype status (cone bioassay survivors vs. dead) in Table 5. Following Rule 6, they are extracted under `geno_pheno` and not duplicated in `genotypes`.
- L1014S was also screened via TaqMan but only L and F alleles are reported in Table 5 (LL, LF, FF account for 100% of tested individuals), meaning no 1014S alleles were found.

### Bioassays
- 11 WHO tube bioassays from Table 2 across the 4 sites are extracted. For these, `# tested` and `# dead 24 h` are literally printed in Table 2, so `dead_alive_printed = true`, `n_dead` is recorded, and `n_alive` is left null as it was not explicitly reported as a count.
- 2 WHO cone bioassays (one on durable lining [DL] and one on indoor residual spraying [IRS], both deltamethrin) conducted with Site 3 mosquitoes are extracted from Tables 3 and 4 to link with the genotype-phenotype data.
