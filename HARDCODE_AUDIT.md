# HARDCODE_AUDIT — manual-insertion / fabrication scan

Scope: `scripts/make_figures.py`, `scripts/build_outputs.py`, `tables/*.md`, `manuscript_source.md`, repository history (`git log -p` on the two content commits).

## Findings

| Item | File | Classification | Notes |
|---|---|---|---|
| Box/arrow x-y coordinates | make_figures.py | PASS | Pure layout constants for conceptual diagrams; no data semantics |
| Gradient band + marker positions (x = 1.9, 5.0, 8.0) | make_figures.py Figure 3 | PASS-WITH-CLARIFICATION | Could be mistaken for measured positions; mitigated by in-figure disclaimer "Positions are conceptual and illustrative; they are not empirically estimated", caption, and Table 1 note. Positions only encode ordinal ordering stated in text — acceptable |
| Colour constants, font sizes, margins | make_figures.py | PASS | visual only |
| Word-count print (`main_words`) | build_outputs.py | PASS | derived from source, category B; printed value used for title-page "approx." count |
| Cover-letter text | build_outputs.py | PASS | no empirical numbers; "six conditional propositions" matches source |
| references.bib generator | build_outputs.py | PASS | mechanical conversion of reference list; no inserted data |
| Table 1 feasibility terms (Low/Moderate/Relatively high) | tables/ | PASS-WITH-CLARIFICATION | qualitative conceptual judgements; footnote marks them illustrative |
| Empirical claims in prose | manuscript_source.md | PASS | all trace to cited sources; magnitude words softened this pass |
| Literal statistics in prose | manuscript_source.md | PASS | none — automated scan finds only citation years, P-labels, "top-1%", "three decades" |
| Earlier-draft values | git history | PASS | finishing-pass commit superseded quantified Figure 3; no residue in current files |
| Commented-out alternative values | all sources | PASS | none present |
| Table 2 "(P7)" label | tables/Table2 | FIXED | inconsistent with "six propositions"; relabelled unnumbered expectation |
| Covay & Carbonaro DOI | references | FIXED | stale/incorrect DOI replaced with verified 10.1177/0038040709356565 |
| 12 uncited references | references | FIXED | removed — no silent citation padding |

## Verdict

No empirically styled hardcoded numbers remain. All flagged items PASS, PASS-WITH-CLARIFICATION, or FIXED. Nothing UNRESOLVED.
