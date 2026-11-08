# Path-invariant selection

Code and materials for the conceptual manuscript *When Should Experience Matter? Path-Invariant Evaluation in Educational Selection*.

The manuscript is theoretical: no new data were generated or analyzed. Its three figures are conceptual diagrams drawn by code; they contain no data, and Figure 3 is an explicitly illustrative (non-empirical) placement.

## Reproduce the figures

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/make_figures_EA.py
```

Outputs `figures/EA/Figure1.png`, `Figure2.png`, `Figure3.png` (600 dpi, grayscale) and the corresponding `.tif` files (1200 dpi, grayscale, LZW). Tested with Python 3.10 and the pinned versions in `requirements.txt`.

## Layout

- `manuscript_source_EA.md`: manuscript source; `tables/EA/`: table sources; `figures/EA/`: generated figures.
- `scripts/make_figures_EA.py`: figure generation (the only code needed for the figures).
- `scripts/build_outputs_EA.py`: optional rebuild of DOCX/PDF/PPTX files (additionally needs python-docx, python-pptx, latex2mathml, docx-equation==0.3.0, and LibreOffice).
- `scripts/audit_references_EA.py`, `scripts/audit_consistency_EA.py`: reference and consistency audits.
- `data/raw/crossref/`: archived Crossref metadata for the cited works; `data/raw/ACQUISITION_LEDGER.csv`: acquisition ledger. Third-party journal guideline pages listed in the ledger are kept privately and are not redistributed here.
- Files for an earlier version of the manuscript (`manuscript_source.md`, `scripts/make_figures.py`, `scripts/build_outputs.py`) are retained for provenance.
