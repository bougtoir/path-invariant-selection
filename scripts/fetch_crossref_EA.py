"""Fetch Crossref metadata for every DOI in manuscript_source_EA.md that is not yet archived."""
import os, re, json, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
RAW = os.path.join(ROOT, "data", "raw", "crossref")
src = open(os.path.join(ROOT, "manuscript_source_EA.md"), encoding="utf-8").read()
for doi in sorted(set(re.findall(r"https://doi\.org/(\S+)", src))):
    fn = os.path.join(RAW, doi.lower().replace("/", "_") + ".json")
    if any(f.lower() == os.path.basename(fn) for f in os.listdir(RAW)):
        continue
    req = urllib.request.Request("https://api.crossref.org/works/" + doi, headers={"User-Agent": "path-invariant-selection (mailto:bougtoir@gmail.com)"})
    data = urllib.request.urlopen(req, timeout=60).read()
    open(fn, "wb").write(data); print("fetched", doi); time.sleep(0.5)
