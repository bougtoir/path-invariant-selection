# NUMERIC_AUDIT — numeric / quasi-numeric statements, gate H1–H8

Categories: A verified source, B derived, C structural, D explicitly illustrative.
Automated scan of `manuscript_source.md`: the only numeral strings in body text are citation years, proposition labels P1–P6, "top-1%", and "three decades" — no invented statistics. Reference-list numerals (volumes, issues, pages, DOIs, in-title counts such as "60,000" and "85 Years") belong to source titles.

## Itemised audit (body text)

| Location | Value / phrase | Cat. | Support | Action |
|---|---|---|---|---|
| Introduction | "Over the past three decades … widened the evidentiary basis" | A | Marginson 2016; Karabel 2005; Stevens 2007 trend literature | none |
| Introduction | "increasingly stratified by class" (was "grown sharply more stratified") | A | Snellman et al. 2015 | softened — FIXED |
| Introduction | "correlate with household income at least as strongly as test scores do" (was "more strongly") | A | Alvero et al. 2021 (title claim: essay content/style strongly related to household income and SAT) | softened — FIXED |
| Introduction | "substantial share of the admissions advantage … richest families" | A | Chetty, Deming & Friedman 2026 (QJE 141(1)) | none — qualitative, source-backed |
| Two roles | V(E) = V_intrinsic + V_learning + V_credential | D | definitional decomposition, no numbers | none |
| Path invariance | A ⊥ P | Z; K_i = K_j ⇒ A_i = A_j | C | schematic notation | none |
| Primary case | "top-1% income applicants … Ivy-Plus" | A | Chetty et al. 2026 | "most detailed microdata yet analysed" → "large-scale admissions microdata" — FIXED |
| Primary case | "large-scale admissions microdata" | A | Chetty et al. 2026 | as above |
| Paradox | "tests correlate with socioeconomic status" | A | Sackett et al. 2009 | none |
| Paradox | "improved perceived selectivity more reliably than diversity" | A | Belasco et al. 2015 abstract | none — kept conditional |
| RBV | I(Y ; B | D); R²(D+B) − R²(D) | D | labelled "illustrative rather than a proposed statistic" | none |
| RBV | "employment … relatively high … admissions intermediate … political lowest" | D | conceptual ordering, repeated as illustrative in Fig 3 + Table 1 note | none |
| RBV | "work samples and simulations are established and strongly predictive" | A | Schmidt & Hunter 1998 | none |
| RBV | blind auditions "altered selection outcomes" | A | Goldin & Rouse 2000 | none |
| Employment | "raised productivity without reducing minority hiring in a naturalistic field study" (was "best naturalistic study available") | A | Autor & Scarborough 2008 | softened — FIXED |
| Politics | "debates measure … verbal fluency, preparation, media skill" | A | Popkin 1991 | none — qualitative |
| Propositions | "six propositions, three normative and three empirical" | C | P1–P6 labels; verified consistent after P3 fix | none |
| Agenda | designs (i)–(iii) | C | structural enumeration | none |
| Abstract | "six propositions"; 123 words | C | verified | none |
| Title page | "approx. {main_words}" | B | computed by build_outputs.py from source | none |
| Cover letter | "six conditional propositions" | C | matches | none |

## Gate H2 — figures

- Figure 1: arrows R→E→K→D→A (developmental) and E→credential signal→A (credential) match final theory incl. Y and dotted Y→A. PASS.
- Figure 2: two panels, no magnitudes, directions match caption. PASS.
- Figure 3: regenerated finishing-pass version — gradient band, three labelled positions, directional arrows only; no axes, ticks, coordinates, or fitted lines; disclaimer text inside figure and caption. PASS.

## Gate H3 — tables

- Table 1 uses "Moderate / Relatively high / Low / Large residual role" in feasibility columns; footnote states positions are conceptual and illustrative, not empirically estimated — Gate satisfied. PASS-WITH-CLARIFICATION already in place; no further change.
- Table 2 "(P7)" relabelled — FIXED.

## Gate H4 — claim–source match

All headline empirical claims re-verified against REFERENCE_AUDIT (finishing pass) plus this pass's wording softening. No claim exceeds source strength after fixes.

## Gate H5 — magnitude phrases

"sharply", "most detailed", "best naturalistic study" removed/softened. "strongly predictive" retained with Schmidt & Hunter support. "substantial share" retained — qualitative and directly the paper's finding.

## Gate H6 — citation integrity

- Covay & Carbonaro 2010 DOI corrected (10.1177/0038040710385547 → 10.1177/0038040709356565) — FIXED.
- Collins 2011 IJSE DOI resolves via doi.org (302 → journal page; not in Crossref index) — PASS.
- All other DOIs verified 200 via Crossref API (16 checked).
- 12 uncited bibliography entries removed — FIXED.
- No year/text mismatches; Chetty consistently 2026 QJE published version.

## Gate H7 — cross-version contamination

`git log` shows only two content commits (initial package + finishing pass); current files all post-finishing-pass state. No stale figures/tables/captions present. PASS.

## Gate H8 — single source of truth

Title, proposition count (6 + unnumbered seventh expectation), figure count (3), table count (2), abstract wording, target journal are consistent across manuscript_source.md, cover letter, docx builder, audit docs. PASS after Table 2 relabel.
