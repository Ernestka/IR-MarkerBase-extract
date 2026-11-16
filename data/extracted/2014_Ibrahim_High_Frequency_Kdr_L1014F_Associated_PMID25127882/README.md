# Extraction record — 2014_Ibrahim_High_Frequency_Kdr_L1014F_Associated_PMID25127882

- Extracted: 2026-11-16
- Model: gemini:gemini-3.7-flash
- Confidence (model's own): high
- Surveys: 5 · Genotype rows: 2 · Bioassays: 6 · Geno-pheno rows: 5

## Decisions

### Data Extraction Decisions

1. **Surveys & Species Splitting**:
   - Larval collections were carried out in Auyo (Jigawa State) in June 2009 (rainy season) and February 2011 (harmattan, for malathion), and in Bunkure (Kano State) in August 2010.
   - Bioassays were run on mixed F0 adult female *An. gambiae s.l.* from both sites.
   - Molecular identification of Auyo mosquitoes exposed to lambda-cyhalothrin revealed *An. coluzzii* (88 genotyped: 81 alive, 7 dead), *An. arabiensis* (26 genotyped: 13 alive, 13 dead), and 1 hybrid (alive, heterozygous A/T for L1014F, not included in species counts).
   - Separate surveys are created for *An. coluzzii* and *An. arabiensis* from Auyo 2009 to record species-level genotyping, as well as surveys for *An. gambiae s.l.* pools tested in bioassays.

2. **Genotype-Phenotype Data & Resolution of Dead Mosquito Counts**:
   - For *An. coluzzii* exposed to lambda-cyhalothrin:
     - Alive (n=81): counts are explicitly printed on page 4 (rr=60, rs=16, ss=5).
     - Dead (n=7): Table 2 reports allele counts of 5 R (TTT) and 9 S (TTA). Combined with Figure 4A (which plots frequencies of T/T, A/T, and A/A in susceptible mosquitoes), the only integer combination matching 5 R and 9 S alleles is rr=2 (28.6%), rs=1 (14.3%), and ss=4 (57.1%).
   - For *An. arabiensis* exposed to lambda-cyhalothrin:
     - Alive (n=13): counts are explicitly printed on pages 4–5 (rr=1, rs=3, ss=9).
     - Dead (n=13): Table 2 reports allele counts of 2 R (TTT) and 24 S (TTA). Combined with Figure 4B (which shows 0 T/T, ~15% A/T, and ~85% A/A), the only integer combination is rr=0, rs=2 (15.4%), and ss=11 (84.6%).
   - For *ace-1* G119S:
     - All 100 mosquitoes tested in the malathion bioassay died (100% mortality) and were 100% wild-type G/G (rr=0, rs=0, ss=100).

3. **Genotypes Table**:
   - *kdr* L1014S was screened simultaneously on all 115 mosquitoes from Auyo. One single *An. arabiensis* was heterozygous (rs=1, ss=25), and zero *An. coluzzii* carried the mutation (rr=0, rs=0, ss=88). Because L1014S was not reported split by phenotype, these rows are placed in `genotypes`.

4. **Bioassays**:
   - All bioassay sample sizes (n_exposed) and mortality percentages at 24 hours are extracted from text and Figure 3. Exact counts of dead and alive are not printed as integer counts in text/tables, so `dead_alive_printed` is set to false.

## Validator warnings

- geno_pheno #1 (lambda-cyhalothrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: lambda-cyhalothrin)
- geno_pheno #2 (lambda-cyhalothrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: lambda-cyhalothrin)
- geno_pheno #3 (lambda-cyhalothrin, kdr L1014F, alive): not linked to a single bioassay (insecticide as reported: lambda-cyhalothrin)
- geno_pheno #4 (lambda-cyhalothrin, kdr L1014F, dead): not linked to a single bioassay (insecticide as reported: lambda-cyhalothrin)
