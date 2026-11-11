# Extraction record — 2008_Pages_Malaria_Transmission_Dakar_Two_Year_PMID18796138

- Extracted: 2026-11-11
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 2 · Bioassays: 0 · Geno-pheno rows: 0

## Decisions

# Decisions and Extraction Notes

- **Surveys**: Split by the two sampling districts in Dakar (French military camps of Bel-air and Ouakam). Coordinates given in the paper (14°40'20" N, 17°25'22" W) are for the city of Dakar as a whole, hence `spatial_precision` is set to `town`.
- **Temporal range**: Entomological monitoring was conducted between May 2005 and October 2006, but the samples tested for kdr genotype classes in Table 3 explicitly cover May 2005 to May 2006.
- **Kdr-w (Vgsc L995F / L1014F)**: Full genotype counts (RR, RS, SS, Total) for *An. arabiensis* are reported in Table 3 on page 7. Frequencies reported in the table cells are genotype frequencies (e.g. 11/109 = 0.10, 4/109 = 0.04, 94/109 = 0.86), while allele frequencies are reported in the text as 12% (0.12) for Bel-air and 9% (0.09) for Ouakam.
- **Ace-1**: The authors state: "Ace 1 mutations were not identified in any members of the An. gambiae complex either in Ouakam or in Bel-air" and tested "All CSP-positive mosquitoes per site and a random sample of 100 PCR-identified mosquitoes". However, exact genotype counts or sample sizes per species/site were not reported in Table 3, so Ace-1 is not extracted to avoid guessing unprinted species-specific sample sizes.
- **Bioassays / Geno-pheno**: No susceptibility bioassays were conducted in this study.
