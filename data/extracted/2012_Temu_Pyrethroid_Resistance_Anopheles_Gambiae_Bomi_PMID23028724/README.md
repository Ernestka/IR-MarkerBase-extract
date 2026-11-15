# Extraction record — 2012_Temu_Pyrethroid_Resistance_Anopheles_Gambiae_Bomi_PMID23028724

- Extracted: 2026-11-15
- Model: gemini:gemini-3.8-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 19 · Geno-pheno rows: 4

## Decisions

### Study and Survey Structure
- Mosquito larvae were collected weekly between July and September 2011 from 4 sites in Bomi County, Liberia (Table 1, Figure 1):
  - Site 3: Klay District (Malema Camp and Gissi Camp)
  - Site 5: Senjeh District / Tubmanburg City (Woman's centre, UNMIL camp, Garage)
  - Site 7: Klay District (Weamoi, Outside Weamoi)
  - Site 10: Suehn Mecca District (Norbor, Outer Norbor)
- Coordinates in Table 1 are reported as UTM X-Y Cartesian coordinates rather than latitude/longitude decimal degrees or DMS. Per instructions, latitude_reported and longitude_reported are left null.
- Reared adults from all 4 sites were identified morphologically as Anopheles gambiae s.l. and tested in standard WHO susceptibility tube bioassays (Table 2).
- Only mosquitoes from Site 3 were tested in WHO cone bioassays on deltamethrin-treated durable wall lining (DL) and indoor residual spraying (IRS) demonstration houses (Tables 3 & 4).
- A subset of 169 mosquitoes tested in the cone bioassays (all from Site 3) were molecularly identified via SINE PCR to species and form: 100% were An. gambiae s.s. (166 M molecular form [An. coluzzii] and 3 S molecular form [An. gambiae s.s.]).

### Bioassays
- Table 2 reports 11 WHO susceptibility tube tests across the 4 sites (deltamethrin 0.05%, fenitrothion 0.05%, and bendiocarb 0.1%; 1 hour exposure, 24-hour mortality).
- Tables 3 & 4 report WHO cone bioassays (30-minute exposure, 24-hour mortality) conducted in 4 test exposures on deltamethrin DL (5 g/kg) and deltamethrin IRS (250 mg/m²). Each exposure is extracted at finest resolution as reported.

### Genotype and Genotype-Phenotype Data
- All genotyped mosquitoes (n=169) were from the cone bioassays and are reported stratified by bioassay outcome (alive vs dead) in Table 5. Therefore, all genotype counts are entered in `geno_pheno`, and the `genotypes` table is left empty (`[]`) to avoid double counting per Rule 6.
- Mosquitoes in Table 5 were sampled across the cone bioassay exposures for IRS and DL; therefore, `bioassay_id` is set to null, and `insecticide` is set to 'deltamethrin'.
- Codon 1014 (L1014F and L1014S) was screened using TaqMan assays. As reported on page 4 and Table 5, the 1014F allele was highly prevalent (homozygote FF and heterozygote LF), and wild-type LL was detected only in 4 dead mosquitoes (2 in IRS, 2 in DL). No 1014S resistant alleles were detected.

## Validator warnings

- geno_pheno #1 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #2 (deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #3 (deltamethrin, Vgsc L1014F, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #4 (deltamethrin, Vgsc L1014F, dead): not linked to a single bioassay (insecticide as reported: deltamethrin)
