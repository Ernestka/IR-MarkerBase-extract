# Extraction record — 2015_Wanjala_Insecticidal_Decay_Effects_Long_Lasting_PMID26567915

- Extracted: 2026-11-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 13 · Genotype rows: 13 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Study Overview**: Mosquito larvae were collected from 7 study sites in western Kenya (Ahero, Kisian, Chulaimbo, Emutete, Emakakha, Iguhu, and Bungoma) and reared to adults. Adult mosquitoes were tested in WHO tube susceptibility bioassays, cone bioassays on LLINs of different ages, and cone bioassays on IRS-sprayed mud slabs over time. Sibling species within the *Anopheles gambiae* complex were identified by rDNA-PCR (*An. gambiae* s.s. and *An. arabiensis*).
- **Temporal Information**: Specific collection months and years are not reported in the manuscript; the study was published in 2015.
- **Coordinates**: No geographic coordinates are reported in the text or tables; spatial precision is set to `village`.
- **Surveys and Species Resolution**: Genotyping results in Table 2 are broken down by site and by molecular species (*An. gambiae* s.s. and *An. arabiensis*). Separate surveys were created for each site x species combination with data. At Emutete, 0 *An. arabiensis* were genotyped (Table 2 lists N=0, N/A), so no *An. arabiensis* survey was created for Emutete. This yields 13 surveys in total (7 for *An. gambiae* s.s., 6 for *An. arabiensis*).
- **Genotypes and Mapping**: Table 2 reports counts for "LL", "LS", and "SS", where the table footnote explicitly defines "LL represents wild type" (L1014/L1014, mapped to database `ss`), "LS represents heterozygote mutation" (L1014/1014S, mapped to database `rs`), and "SS represents homozygote mutation" (1014S/1014S, mapped to database `rr`). The mutant allele tested was 1014S (TaqMan real-time PCR assay). Genotype counts perfectly reconcile with sample sizes N and reported allele frequencies.
- **Bioassay Data**: WHO tube bioassay results for the 7 field populations against deltamethrin (0.05%), permethrin (0.75%), and lambda-cyhalothrin (0.05%) are displayed only as a bar graph (Figure 2) without exact mortality counts or numerical percentage values printed in tables or text. In addition, the bioassays were performed on field-reared *An. gambiae* s.l. (mixed species complex) rather than on sorted molecular species. Similarly, LLIN cone bioassays (Figure 3) and IRS mud slab decay bioassays (Figure 5) are shown only as bar graphs. In accordance with the extraction rules prohibiting digitizing/guessing from graphs without printed numbers, no bioassay records were extracted.
- **Genotype-Phenotype**: Genotyping was performed on randomly selected specimens from the populations; mosquitoes were not genotyped separately by bioassay outcome (alive vs dead). Thus, `geno_pheno` is empty.
