"""Write data/raw/ACQUISITION_LEDGER.csv (path, source URL, retrieved UTC, bytes, sha256, terms)."""
import csv, hashlib, os
ROOT = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
SRC = {
    "journal/EA_instructions_wayback_20230531.html": "http://web.archive.org/web/20230531010439/http://www.tandfonline.com/action/authorSubmission?journalCode=heda20&show=instructions",
    "journal/EA_journal_home_wayback_20251217.html": "http://web.archive.org/web/20251217094003/https://www.tandfonline.com/journals/heda20",
    "journal/EA_instructions_live.html": "https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=heda20 (Cloudflare challenge page only)",
    "journal/EA_aims_scope_live.html": "https://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=heda20 (Cloudflare challenge page only)",
    "journal/EA_journal_home_live.html": "https://www.tandfonline.com/journals/heda20 (Cloudflare challenge page only)",
    "journal/TF_AI_policy_live.html": "https://taylorandfrancis.com/our-policies/ai-policy/",
    "journal/tf_APA.pdf": "https://files.taylorandfrancis.com/tf_APA.pdf",
}
rows = []
for dp, _, fns in os.walk(ROOT):
    for fn in sorted(fns):
        p = os.path.join(dp, fn); rel = os.path.relpath(p, ROOT)
        if rel == "ACQUISITION_LEDGER.csv":
            continue
        if rel.startswith("crossref/"):
            url = "https://api.crossref.org/works/" + fn[:-5].replace("_", "/", 1)
        elif rel.startswith("books/"):
            url = "openlibrary.org search / googleapis books (see filename)"
        else:
            url = SRC.get(rel, "")
        h = hashlib.sha256(open(p, "rb").read()).hexdigest()
        rows.append([rel, url, "2026-11-08", os.path.getsize(p), h,
                     "publisher/API public metadata; archived for citation verification only"])
with open(os.path.join(ROOT, "ACQUISITION_LEDGER.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["path", "source_url", "retrieved_utc_date", "bytes", "sha256", "terms_note"]); w.writerows(sorted(rows))
print(len(rows), "ledger rows")
