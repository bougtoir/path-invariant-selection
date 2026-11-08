# EA_AUTHOR_GUIDE_FINAL_CHECK

## Live-page attempt
- 2026-11-08T01:23:05Z, `curl -A "Mozilla/5.0"`: `https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=heda20` → HTTP 403. `https://www.tandfonline.com/journals/heda20` → HTTP 403 (Cloudflare bot challenge, as in the earlier session-Chrome attempt recorded in EA_AUTHOR_GUIDE.md).
- Guidance used: Instructions for Authors "Updated 17th March 2023" (Wayback capture 2023-05-31); Aims & Scope (Wayback 2025-12-17); live T&F AI Policy; live T&F APA 7 guide. All archived with SHA-256 in `data/raw/ACQUISITION_LEDGER.csv`. The archived instructions are not assumed to be current.

## Submission-critical items

| Item | Archived guidance | Package | Status | Needs human browser confirmation? |
|---|---|---|---|---|
| Article type | Original articles | Original article (theoretical) | OK | Yes (confirm the portal type name) |
| Abstract | Unstructured, 200 words | 195 words, unstructured | OK | Yes (limit may have changed since 2023) |
| Keywords | "Do not include keywords" (checklist), though the generic order lists keywords | None in the manuscript. Suggested list in the handoff | OK under the archived rule | **Yes** (contradictory in the archive) |
| Reference style | T&F Standard APA (APA 7) | APA 7, audited | OK | No |
| Anonymization | Single-anonymous | Full title page in final DOCX. Blinded copy also supplied | OK | Yes (confirm still single-anonymous) |
| Title page | Title, authors, affiliations, corresponding author, ORCID suggested | Placeholders for author completion | Author item | No |
| Tables | Editable, self-contained, on individual pages | Native Word tables on own pages + editable tables DOCX | OK | No |
| Figures | Separate files. 1200 dpi line art / 600 dpi grayscale. TIFF/EPS/JPEG accepted | Separate 1200-dpi grayscale TIFF + 600-dpi PNG. Editable PPTX | OK | No |
| File formats | Word for manuscript (not PDF) | DOCX. PDF is a reading copy only | OK | No |
| AI disclosure | T&F AI Policy: tool name + version, how, why | Placeholder section + EA_AI_DISCLOSURE_DRAFT.txt | Author item | No |
| Data statement | Required where applicable | Accurate statement (no data; figure code public, clean-clone verified) | OK | No |
| Supplemental/code | Supplemental material may be submitted. Data/code via repository encouraged | Public repository linked | OK | No |

Result: compliant with the archived guidance. Items marked "Yes" need a quick check in a normal browser before submission.
