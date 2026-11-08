# Educational Assessment (Taylor & Francis / Routledge) — author-guideline record

Verified 2026-11-08. The live tandfonline.com pages return a Cloudflare bot-challenge to both curl and the session Chrome (archived as `data/raw/journal/*_live.*`, challenge text only). Authoritative copies used instead (all archived with SHA-256 in `data/raw/ACQUISITION_LEDGER.csv`):

| Source | Snapshot | File |
|---|---|---|
| Journal home page incl. Aims & Scope | Wayback 2025-12-17 | `EA_journal_home_wayback_20251217.html/.txt` |
| Instructions for Authors ("Updated 17th March 2023") | Wayback 2023-05-31 (latest 200 capture) | `EA_instructions_wayback_20230531.html/.txt` |
| T&F Standard APA 7 reference guide v3.1 | live PDF | `tf_APA.pdf` |
| T&F AI Policy | live | `TF_AI_policy_live.html/.txt` |

Limitation: the Instructions snapshot is from 2023; the 2025-12 home page confirms the same Aims & Scope wording. The author should glance at the live Instructions page in a normal browser before upload.

## Requirements and how the package meets them

| Item | Official wording (abridged) | Package |
|---|---|---|
| Aims & scope | "original research on the design, analysis and use of assessment to deepen understanding of the performance and quality of individuals, groups, and programs in educational settings. It welcomes rigorous theoretical pieces ... that can inform important national and international discussions in educational policy and practice." Interests include "use and consequences ... to support educational decision-making", "novel approaches to validation". | Paper framed as a theoretical piece on the design and use of evidence in educational selection; validity-argument and consequences sections; policy/practice section. |
| Article types | "original articles" | Original article (theoretical). |
| Language / spelling | English; "American spelling style consistently"; double quotation marks | American spelling throughout (checked by builder); double quotes. |
| Peer review | "single anonymous peer reviewed by two independent, anonymous expert referees" | Blinding not required; an optional anonymized copy is supplied anyway in case the live policy has changed. |
| Order | title page; abstract; keywords; main text; acknowledgments; declaration of interest statement; references; appendices; tables (on individual pages); figures; figure captions (as a list) | Builder emits this order (keywords omitted — see next row). |
| Abstract | "unstructured abstract of 200 words" | ≤ 200 words (builder asserts). |
| Keywords | "Do not include keywords" (journal-specific checklist line, contradicts the generic order line) | Not in manuscript; suggested keywords listed in FINAL_HANDOFF_EA for the portal metadata form if requested. |
| Word limit | "Please include a word count ... There are no word limits" | Word count on title page (computed). |
| Reference style | T&F Standard APA (APA 7) | References and in-text citations converted to APA 7 (`&`, "et al." for ≥3 authors, https://doi.org/ DOIs). |
| Format | Word, not PDF; figures saved separately | docx + separate 600-dpi PNG figures; PDF only as reading copy. |
| Figures | 1200 dpi line art / 600 dpi grayscale / 300 dpi color; EPS, PS, JPEG, TIFF, Word | Figures are grayscale-safe line art; exported as 1200-dpi TIFF (preferred) plus 600-dpi PNG. |
| Tables | "editable files"; "interpret ... without reference to the text"; on individual pages | Native Word tables, each on its own page, self-contained notes; also a separate editable tables docx. |
| Equations | "ensure that equations are editable" | Native Word OMML equations. |
| Disclosure | "If there are no relevant competing interests ... The authors report there are no competing interests to declare." | Disclosure statement present (author to confirm). |
| Funding | Funding agency/grant wording | Placeholder for author. |
| Data availability | Statement where a data set is associated; Basic Data Sharing Policy | Statement: no data generated/analyzed; figure code at public repository. |
| AI | T&F AI Policy: "Authors must clearly acknowledge within the article ... any use of Generative AI tools through a statement that includes: the full name of the tool used (with version number), how it was used and the reason for use." | AI-use disclosure section drafted; version field left for author to confirm. |
| Charges | "There are no submission fees, publication fees or page charges"; Open Select APC optional; color print charge | No mandatory fee. Figures are grayscale, so no print color charge. |
| Submission | Routledge Submission Portal; Crossref originality screening | Noted in handoff. |
