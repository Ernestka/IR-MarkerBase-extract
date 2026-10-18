# Extraction record — 2007_Djouaka_Does_Spillage_Petroleum_Products_Anopheles_PMID18053173

- Extracted: 2026-10-18
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 15 · Genotype rows: 6 · Bioassays: 15 · Geno-pheno rows: 0

## Decisions

### Study and Surveys
- Djouaka et al. (2007) investigated the relationship between petroleum spillage in breeding sites and pyrethroid resistance in South Western Nigeria.
- Larvae were collected from 15 localities across five states (Oyo, Osun, Ondo, Ekiti, Ogun) and reared to adults. Larvae from a 16th site (Lagos) died in transit and were not tested (0 tested in Table 1 and Table 4), so no survey was created for Lagos.
- In each locality, a subset of 20-30 bio-assayed mosquitoes underwent PCR species identification. In 6 localities (Ojoo, Bashorun, UI, Challenge, Lagere, Modakeke), all tested individuals were identified as An. gambiae s.s. molecular form M (now recognized as Anopheles coluzzii). In the remaining 9 localities, all tested individuals were identified as Anopheles arabiensis.
- Coordinates were recorded with GPS according to the text, but numerical coordinates are not reported anywhere in the paper, so latitude_reported and longitude_reported are null.
- Collection dates/years are not explicitly stated in the text. Map creation is credited to CREC 2005 and the paper was accepted in December 2007; dates are left null with an explanation in temporal_notes.

### Bioassays
- Standard WHO tube bioassays with 0.75% permethrin (1-hour exposure, 24-hour mortality) were performed on adult females emerging from field collections across 15 localities (Table 1).
- Table 1 reports the total number tested (n_exposed) and percentage mortality (reported_mortality_pct) without raw dead/alive counts. Accordingly, per Rule 2, dead_alive_printed is false, and n_dead and n_alive are null.

### Genotypes
- PCR-kdr screening was performed according to Martinez-Torres et al. (1998) (targeting Vgsc L1014F / L995F) on 30 An. gambiae s.s. specimens per site from 6 localities (Table 4).
- In all 6 sites, 'No Kdr' was detected (all 30 genotyped were wild-type homozygous susceptible: RR = 0, RS = 0, SS = 30, n_carriers = 0, resistant_allele_count = 0).
- The target marker is recorded as gene: 'Vgsc', marker: 'L995F' (with amino_acid_change 'L1014F').
- PCR-kdr was not performed on An. arabiensis specimens.
- Mosquitoes were genotyped from the bioassay pool without reporting genotype classes separately by alive/dead phenotype, so these counts are recorded in genotypes, and geno_pheno is empty.
