# Extraction record — 2017_Edi_First_Detection_N1575Y_Mutation_Pyrethroid_PMID29018842

- Extracted: 2026-11-20
- Model: gemini:gemini-3.5-flash
- Confidence (model's own): high
- Surveys: 4 · Genotype rows: 0 · Bioassays: 2 · Geno-pheno rows: 5

## Decisions

### Data Extraction Decisions & Notes

1. **Surveys & Species Breakdown**:
   - Mosquitoes were collected as larvae between April and November 2016 at two sites: Tiassalé and Elibou in Southern Côte d'Ivoire.
   - In Tiassalé, 100% of tested individuals were *An. coluzzii*. A survey `tiassale_col` was created.
   - In Elibou, bioassays were performed on *An. gambiae s.l.* prior to species identification (`elibou_sl`), while Table 1 reports N1575Y genotypes separately for bioassay survivors of *An. coluzzii* (`elibou_col`) and *An. gambiae s.s.* (`elibou_gam`).

2. **Genotype vs. Geno-Pheno Placement**:
   - All genotyped samples in Table 1 are explicitly designated with phenotype `Alive` (survivors of deltamethrin WHO bioassay).
   - Per Rule 6, all genotype counts (NN=SS, NY=RS, YY=RR) are recorded in `geno_pheno` to prevent double counting.
   - Tiassalé entries are linked directly to `bioassay_id` `..._tiassale_col_delta`.
   - Elibou `geno_pheno` entries are assigned per molecular species (`elibou_col` and `elibou_gam`) with `bioassay_id` left `null` and `insecticide` set to `deltamethrin`, as the bioassay was conducted on un-typed *An. gambiae s.l.*.

3. **Bioassay Counts**:
   - Bioassay mortalities are given as percentages only (25% for Tiassalé, 4.4% for Elibou) without explicit counts of dead/alive printed. Per Rule 2, `n_exposed` is recorded while `n_dead` and `n_alive` are left `null` with `dead_alive_printed = false`.

4. **Markers Extracted**:
   - `Vgsc N1575Y`: Genotype counts in Table 1 (NN = SS, NY = RS, YY = RR).
   - `Vgsc L1014F`: Frequency reported as 79.3% in Tiassalé survivors (`reported_allele_freq = 0.793`). Genotype counts were not reported for Elibou.
   - `Vgsc L1014S`: Explicitly reported as absent in Tiassalé (`rr=0, rs=0, ss=92, reported_allele_freq=0.0`).

## Validator warnings

- geno_pheno #4 (deltamethrin, Vgsc N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
- geno_pheno #5 (deltamethrin, Vgsc N1575Y, alive): not linked to a single bioassay (insecticide as reported: deltamethrin)
