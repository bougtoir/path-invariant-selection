# EA_EQUATION_RENDER_AUDIT

Method: the manuscript source has 4 inline math expressions. `build_outputs_EA.py` converts each to native Word OMML (latex2mathml → docx-equation). Checks: (1) count of `<m:oMath>` objects in each DOCX and absence of `[math ...]` fallback text; (2) visual rendering. LibreOffice was used to convert both the final DOCX and the inline DOCX (the PDF source) to PDF, and the paragraphs containing each expression were rasterized at 150 dpi and inspected. Text extraction was not relied on, because pdftotext omits rendered math.

| # | Expression (source) | OMML in final / inline / blinded DOCX | Rendered in PDF (inline copy, p. 5/7/9) and final-DOCX PDF | Result |
|---|---|---|---|---|
| 1 | `V(E) = V_{\text{intrinsic}} + V_{\text{learning}} + V_{\text{credential}}` | yes / yes / yes | V(E)=V_intrinsic+V_learning+V_credential, upright subscript words | PASS (after fix) |
| 2 | `A \perp P \mid Z` | yes / yes / yes | A ⊥ P \| Z, italic variables, perpendicular and mid symbols visible | PASS |
| 3 | `I(Y; B \mid D)` | yes / yes / yes | I(Y;B\|D) | PASS |
| 4 | `R^2` | yes / yes / yes | R with superscript 2 | PASS |

- OMML objects per DOCX: 4 (final, inline, blinded). Fallback/error strings: 0.
- No blank gaps where equations should be. No corrupted or substituted symbols. PDF meaning matches the DOCX.
- Defect found and fixed: with `\mathrm{...}` the subscripts rendered as letter-spaced italic single characters. The source now uses `\text{...}`, which renders as upright words.
- Greek symbols: none used. Variables named in prose (Z, P, A, B, D, Y) are plain text letters defined where introduced.

Result: PASS.
