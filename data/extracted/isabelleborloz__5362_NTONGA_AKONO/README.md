# Extraction record — isabelleborloz__5362_NTONGA_AKONO

- Extracted: 2026-10-05
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 2 · Genotype rows: 4 · Bioassays: 12 · Geno-pheno rows: 0

## Decisions

- Split surveys into "Kribi rural" and "Kribi urbain" based on the two distinct collection sites.
- Collection dates are June and October 2020, and January and April 2021.
- Bioassay sample sizes were determined to be exactly 80 mosquitoes per test based on the footnote in Table III ("moyenne de 4 répliques en raison de 20 moustiques par réplique") and the fact that all reported mortality percentages yield exact integers when multiplied by 80.
- Genotype data are from survivors of the bioassays, pooled across different bioassays. Since they cannot be linked to a single bioassay, they are recorded in the `genotypes` table rather than `geno_pheno` to avoid losing the data.
- Genotype counts (RR, RS, SS) were not reported, only allele frequencies. Thus, genotype counts are left null and frequencies are recorded in `reported_allele_freq`.
- Genotyping method is listed as "TaqMan" in Table IV, although the abstract mentions "HOLA" and the methods mention Martinez-Torres (1998). We recorded "TaqMan" as it is explicitly written in the table.

## Validator warnings

- genotype #1 (isabelleborloz__5362_NTONGA_AKONO_urban, kdr Kdr West): frequency only (no raw counts)
- genotype #2 (isabelleborloz__5362_NTONGA_AKONO_urban, kdr Kdr East): frequency only (no raw counts)
- genotype #3 (isabelleborloz__5362_NTONGA_AKONO_rural, kdr Kdr West): frequency only (no raw counts)
- genotype #4 (isabelleborloz__5362_NTONGA_AKONO_rural, kdr Kdr East): frequency only (no raw counts)
