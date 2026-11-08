"""Build the Educational Assessment submission package from manuscript_source_EA.md.

Outputs (output/EA/): EA_manuscript_final.docx (T&F order, figures separate),
EA_manuscript_inline.docx (reading copy, figures/tables after first mention),
EA_manuscript_blinded.docx, EA_manuscript_final.pdf (from inline copy),
EA_tables_editable.docx, EA_figures_editable.pptx, cover_letter_EA.docx,
references_EA.bib, Figure1-3 (.png 600 dpi, .tif 1200 dpi), EA_submission_package_FINAL_QC.zip.
All counts are computed here; nothing is hardcoded.
"""
import glob, json, os, re, shutil, subprocess, sys, zipfile
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from pptx import Presentation
from pptx.util import Inches as PI, Pt as PP

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from docx_math import insert_omml  # noqa: E402

OUT = os.path.join(ROOT, "output", "EA"); FIG = os.path.join(ROOT, "figures", "EA"); TAB = os.path.join(ROOT, "tables", "EA")
os.makedirs(OUT, exist_ok=True)
SRC = open(os.path.join(ROOT, "manuscript_source_EA.md"), encoding="utf-8").read()
REPO_URL = "https://github.com/bougtoir/path-invariant-selection"
MAIN_FIRST, MAIN_LAST = "Introduction", "Conclusion"
BACK = ["Acknowledgments", "Disclosure Statement", "Funding", "Data Availability Statement", "Use of Generative AI"]

# ---------- parse ----------
TITLE = re.search(r"^# (.+)$", SRC, re.M).group(1).strip()
sections, cur = [], None
for line in SRC.splitlines():
    if line.startswith("## "):
        cur = [line[3:].strip(), []]; sections.append(cur)
    elif cur is not None:
        if line.strip():
            if cur[1] and not line.startswith(("- ", "|")) and not cur[1][-1].startswith(("- ", "|")) and cur[1][-1] != "":
                cur[1][-1] += " " + line.strip()  # join hard-wrapped lines
            else:
                cur[1].append(line.strip())
        else:
            cur[1].append("")
sections = [(h, [p for p in ps if p]) for h, ps in sections]
S = dict(sections)
heads = [h for h, _ in sections]
main = heads[heads.index(MAIN_FIRST):heads.index(MAIN_LAST) + 1]
CAPS = {}
for p in S["Figure Captions"]:
    m = re.match(r"(Figure \d+)\. (.+)", p); CAPS[m.group(1)] = m.group(2)
TABLES = {}
for f in sorted(glob.glob(os.path.join(TAB, "Table*.md"))):
    ls = [l.rstrip() for l in open(f, encoding="utf-8") if l.strip()]
    lab, cap = re.match(r"(Table \d+)\. (.+)", ls[0]).groups()
    rows = [[c.strip() for c in l.strip("|").split("|")] for l in ls if l.startswith("|") and not re.match(r"^\|[-| ]+\|$", l)]
    note = [l for l in ls if l.startswith("Note.")][0]
    TABLES[lab] = dict(caption=cap, rows=rows, note=note)


def strip_md(t):
    return re.sub(r"\$([^$]+)\$", r"\1", t.replace("**", "").replace("*", ""))


def words(t):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-–./]*", strip_md(t)))


ABSTRACT_WORDS = words(" ".join(S["Abstract"]))
MAIN_WORDS = sum(words(h) + sum(words(p) for p in S[h]) for h in main)
REF_N = len(S["References"])
assert ABSTRACT_WORDS <= 200, ABSTRACT_WORDS
BRIT = r"\b\w+(?:isation|ise[sd]?|ising|yse[sd]?|ysing)\b|\b(?:behaviour|colour|favour|labour|honour|centre|programme|judgement|defence|licence|modelling|travelled|organisation|whilst|amongst|enrol)\w*"
ALLOW = {"arising", "rising", "otherwise", "advertise", "exercise", "rise", "raise", "wise", "precise", "precisely", "concise", "premise", "promise", "surprise", "comprise", "enterprise", "expertise", "revise", "revised", "arise", "arises", "noise", "franchise", "likewise", "analyse", "paradise", "disguise", "devise", "compromise", "merchandise", "supervise", "supervised", "televised", "improvised", "improvise", "praise", "cruise", "chastise", "excise", "despise", "incise", "apprise", "circumcise", "demise", "poise", "raised", "rises", "arose", "otherwise", "promised", "exercised", "comprised", "comprises", "surprised"}
prose = "\n".join(p for h in ["Abstract"] + main + BACK for p in S[h]) + "\n".join(t["caption"] + t["note"] + " ".join(" ".join(r) for r in t["rows"]) for t in TABLES.values())
brit = sorted({w for w in re.findall(BRIT, prose, re.I) if w.lower() not in ALLOW})
assert not brit, f"British spellings: {brit}"
assert not re.search(r"'[A-Za-z][^']{2,40}'", prose.replace("'s ", " ")), "single quotation marks used as quotes"

# ---------- docx helpers ----------
TOKEN = re.compile(r"(\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*)")


def add_rich(p, text, size=None, bold=False, italic=False):
    for tok in TOKEN.split(text):
        if not tok:
            continue
        if tok.startswith("$"):
            insert_omml(p, tok[1:-1]); continue
        b, i, t = bold, italic, tok
        if tok.startswith("**"):
            b, t = True, tok[2:-2]
        elif tok.startswith("*"):
            i, t = True, tok[1:-1]
        r = p.add_run(t); r.bold = b; r.italic = i
        if size:
            r.font.size = Pt(size)
    return p


def base_doc(spacing=2.0):
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(12)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    st.paragraph_format.line_spacing = spacing; st.paragraph_format.space_after = Pt(0)
    for s in d.sections:
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(1)
        fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run(); f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
        it = OxmlElement("w:instrText"); it.text = "PAGE"; f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
        r._r.append(f1); r._r.append(it); r._r.append(f2)
    return d


def heading(d, text, level=1):
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER if level == 1 else WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text); r.bold = True
    p.paragraph_format.space_before = Pt(12); p.paragraph_format.keep_with_next = True
    return p


def body_para(d, text, indent=True):
    if text.startswith("- "):
        p = d.add_paragraph(); p.paragraph_format.left_indent = Inches(0.5); p.paragraph_format.first_line_indent = Inches(-0.25)
        p.add_run("\u2022\t"); add_rich(p, text[2:]); return p
    p = d.add_paragraph()
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)
    add_rich(p, text); return p


def page_break(d):
    d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def add_table(d, lab, size=9):
    t = TABLES[lab]
    p = d.add_paragraph(); p.add_run(lab).bold = True; p.paragraph_format.keep_with_next = True
    p = d.add_paragraph(); add_rich(p, t["caption"], italic=True); p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_after = Pt(6)
    tb = d.add_table(rows=len(t["rows"]), cols=len(t["rows"][0])); tb.style = "Table Grid"
    for i, row in enumerate(t["rows"]):
        for j, c in enumerate(row):
            cell = tb.cell(i, j); cell.text = ""
            cp = cell.paragraphs[0]; cp.paragraph_format.line_spacing = 1.0
            add_rich(cp, c, size=size, bold=(i == 0))
    p = d.add_paragraph(); p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_before = Pt(6)
    note = t["note"]; r = p.add_run("Note."); r.italic = True; r.font.size = Pt(size)
    add_rich(p, note[len("Note."):], size=size)
    sp = d.add_paragraph(); sp.paragraph_format.space_after = Pt(12)


def add_figure(d, lab):
    n = lab.split()[1]
    d.add_picture(os.path.join(FIG, f"Figure{n}.png"), width=Inches(6.3))
    d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = d.add_paragraph(); p.paragraph_format.line_spacing = 1.0; p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(18)
    p.add_run(f"{lab}. ").bold = True; add_rich(p, CAPS[lab], size=11)


def title_page(d, blinded):
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; r = p.add_run(TITLE); r.bold = True; r.font.size = Pt(14)
    d.add_paragraph()
    if not blinded:
        for t in ["[Author full name: to be completed by the author]", "[Affiliation, city, country: to be completed by the author]",
                  "[ORCID: to be completed by the author]", "Corresponding author: [name, postal address, email: to be completed by the author]"]:
            q = d.add_paragraph(t); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        d.add_paragraph()
    q = d.add_paragraph(f"Word count: {MAIN_WORDS:,} (main text, excluding abstract, references, tables, figure captions, and back matter)")
    q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    q = d.add_paragraph(f"Abstract: {ABSTRACT_WORDS} words | Tables: {len(TABLES)} | Figures: {len(CAPS)} | References: {REF_N}")
    q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    page_break(d)


def build_manuscript(path, blinded=False, inline=False):
    d = base_doc()
    title_page(d, blinded)
    heading(d, TITLE); heading(d, "Abstract")
    for p in S["Abstract"]:
        body_para(d, p, indent=False)
    page_break(d)
    done = set()
    for h in main:
        heading(d, h, 1 if h in (MAIN_FIRST,) else 1)
        for i, ptxt in enumerate(S[h]):
            body_para(d, ptxt, indent=True)
            if inline:
                for lab in re.findall(r"(Figure \d|Table \d)", ptxt):
                    if lab not in done:
                        done.add(lab)
                        add_figure(d, lab) if lab.startswith("Figure") else add_table(d, lab)
    for h in BACK:
        if blinded and h in ("Acknowledgments", "Funding"):
            continue
        heading(d, h, 2)
        for ptxt in S[h]:
            if blinded:
                ptxt = ptxt.replace(REPO_URL, "[repository link withheld for review]")
            body_para(d, ptxt, indent=False)
    page_break(d)
    heading(d, "References")
    for r in S["References"]:
        p = d.add_paragraph(); p.paragraph_format.left_indent = Inches(0.5); p.paragraph_format.first_line_indent = Inches(-0.5)
        add_rich(p, r)
    if not inline:
        for lab in sorted(TABLES):
            page_break(d); add_table(d, lab)
        page_break(d); heading(d, "Figure Captions")
        for lab in sorted(CAPS):
            p = d.add_paragraph(); p.add_run(f"{lab}. ").bold = True; add_rich(p, CAPS[lab])
    d.core_properties.title = TITLE
    d.core_properties.author = "" if blinded else "[Author]"
    d.save(path)
    bad = [p.text for p in Document(path).paragraphs if "\n" in p.text or "\r" in p.text]
    assert not bad, bad[:2]
    if inline:
        assert done == set(CAPS) | set(TABLES), done


# ---------- tables docx ----------
def build_tables(path):
    d = base_doc(1.0)
    sec = d.sections[0]; sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = sec.page_height, sec.page_width
    for i, lab in enumerate(sorted(TABLES)):
        if i:
            page_break(d)
        add_table(d, lab, size=10)
    d.save(path)


# ---------- pptx (13.333 x 7.5 in, title, centered image, caption) ----------
def build_pptx(path):
    from PIL import Image
    prs = Presentation(); prs.slide_width, prs.slide_height = PI(13.333), PI(7.5)
    for lab in sorted(CAPS):
        n = lab.split()[1]; s = prs.slides.add_slide(prs.slide_layouts[6])
        tb = s.shapes.add_textbox(PI(0.5), PI(0.25), PI(12.333), PI(0.6)); tb.text_frame.text = lab
        tb.text_frame.paragraphs[0].runs[0].font.size = PP(24); tb.text_frame.paragraphs[0].runs[0].font.bold = True
        img = os.path.join(FIG, f"Figure{n}.png"); w, h = Image.open(img).size
        maxw, maxh = 12.0, 5.0; sc = min(maxw / (w / 600), maxh / (h / 600)); iw, ih = w / 600 * sc, h / 600 * sc
        s.shapes.add_picture(img, PI((13.333 - iw) / 2), PI(0.95 + (maxh - ih) / 2), PI(iw), PI(ih))
        cb = s.shapes.add_textbox(PI(0.6), PI(6.05), PI(12.133), PI(1.3)); cb.text_frame.word_wrap = True
        cb.text_frame.text = f"{lab}. {strip_md(CAPS[lab])}"
        for r in cb.text_frame.paragraphs[0].runs:
            r.font.size = PP(12)
    prs.save(path)


# ---------- references_EA.bib ----------
def build_bib(path):
    out = []
    for r in S["References"]:
        m = re.match(r"(.+?) \((\d{4})\)\. (.+)", r); auth, year, rest = m.groups()
        doi = re.search(r"https://doi\.org/(\S+)$", r)
        key = re.sub(r"[^A-Za-z]", "", auth.split(",")[0]) + year
        title = re.split(r"\. (?=\*)|\. In ", rest)[0].strip("*")
        if doi:
            cr = {os.path.basename(x)[:-5].lower(): x for x in glob.glob(os.path.join(ROOT, "data", "raw", "crossref", "*.json"))}
            f = cr[doi.group(1).lower().replace("/", "_")]
            msg = json.load(open(f))["message"]
            ppl = msg.get("author") or msg.get("editor") or []
            authors = " and ".join(f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in ppl)
            jt = (msg.get("container-title") or [""])[0]
            typ = "article" if msg.get("type") == "journal-article" else "book"
            fields = dict(author=authors, title=msg["title"][0], journal=jt, year=year, volume=msg.get("volume", ""),
                          number=msg.get("issue", ""), pages=(msg.get("page") or msg.get("article-number") or "").replace("-", "--"),
                          publisher=msg.get("publisher", "") if typ == "book" else "", doi=doi.group(1))
        else:
            typ = "incollection" if " In " in rest else "book"
            fields = dict(author=auth.replace(", &", " and").replace(" & ", " and "), title=title, year=year, note=strip_md(rest))
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
        out.append(f"@{typ}{{{key},\n{body}\n}}")
    open(path, "w", encoding="utf-8").write("\n\n".join(out) + "\n")
    return len(out)


# ---------- cover letter ----------
def build_cover(path):
    d = base_doc(1.15)
    for t in ["[Author full name]", "[Affiliation]", "[Email]", "", "[Date]", "", "The Editor", "Educational Assessment", ""]:
        d.add_paragraph(t)
    paras = [
        "Dear Editor,",
        f"I am pleased to submit the manuscript \u201c{TITLE}\u201d for consideration as an original article in Educational Assessment.",
        "The manuscript is a theoretical contribution on the design and use of evidence in high-stakes educational selection. Selection decisions combine relatively direct evidence of the attributes an institution targets, such as examinations, grades, and structured performance tasks, with distal biographical evidence such as activity records and personal statements, usually without stating what each source is evidence of. The article develops a path-invariance principle as a warrant within argument-based validation: when different pathways can produce the same target attribute, the pathway by which an applicant acquired it should not independently affect the decision once the attribute is adequately evidenced, unless the pathway is part of the target, adds incremental information, or informs the interpretation of other evidence.",
        "I believe the manuscript fits the journal\u2019s aims, which welcome rigorous theoretical pieces on the design, analysis, and use of assessment, including the use and consequences of assessment for educational decision-making and novel approaches to validation. The article distinguishes the principle from incremental validity, construct-irrelevant variance, measurement invariance, differential prediction, and consequential validity; separates contextual interpretation from credit for possessing an experience; and derives six normative, empirical, and consequential propositions with designs that could disconfirm them. University admissions is the primary case. The practical implication is an evidence-role audit for admissions offices and assessment designers rather than advocacy for any testing technology.",
        f"The main text is approximately {MAIN_WORDS:,} words, with a {ABSTRACT_WORDS}-word abstract, {len(TABLES)} tables, and {len(CAPS)} conceptual figures. No new data were analyzed; the code that generates the figures is openly available, and I have verified that it reproduces them from a clean copy of the public repository.",
        "This manuscript is original, has not been published previously, and is not under consideration elsewhere. I have no competing interests to declare. [Author: add funding and generative-AI statements if applicable.]",
        "Thank you for your consideration.",
        "Sincerely,", "", "[Author full name]"]
    for t in paras:
        p = d.add_paragraph(); add_rich(p, t); p.paragraph_format.space_after = Pt(8)
    d.save(path)


if __name__ == "__main__":
    for f in glob.glob(os.path.join(OUT, "*")):
        os.remove(f)
    fin, inl, bl = (os.path.join(OUT, n) for n in ("EA_manuscript_final.docx", "EA_manuscript_inline.docx", "EA_manuscript_blinded.docx"))
    build_manuscript(fin); build_manuscript(inl, inline=True); build_manuscript(bl, blinded=True)
    build_tables(os.path.join(OUT, "EA_tables_editable.docx")); build_pptx(os.path.join(OUT, "EA_figures_editable.pptx"))
    build_cover(os.path.join(OUT, "cover_letter_EA.docx"))
    nbib = build_bib(os.path.join(ROOT, "references_EA.bib")); shutil.copy(os.path.join(ROOT, "references_EA.bib"), OUT)
    shutil.copy(os.path.join(ROOT, "manuscript_source_EA.md"), OUT)
    for f in glob.glob(os.path.join(FIG, "Figure*")):
        shutil.copy(f, OUT)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", OUT, inl], check=True, capture_output=True)
    os.replace(os.path.join(OUT, "EA_manuscript_inline.pdf"), os.path.join(OUT, "EA_manuscript_final.pdf"))
    for n in sorted(sum((glob.glob(os.path.join(ROOT, g)) for g in ("EA_*_FINAL.md", "EA_*_FINAL_CHECK.md", "EA_EQUATION_RENDER_AUDIT.md", "EA_PUBLIC_REPRODUCIBILITY_AUDIT.md", "EA_AI_DISCLOSURE_DRAFT.txt", "FINAL_HANDOFF_EA_FINAL.md")), [])):
        if os.path.exists(n):
            shutil.copy(n, OUT)
    z = os.path.join(OUT, "EA_submission_package_FINAL_QC.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(os.listdir(OUT)):
            if f != os.path.basename(z):
                zf.write(os.path.join(OUT, f), arcname=f)
    names = zipfile.ZipFile(z).namelist()
    assert all("/" not in n and not n.startswith(".") for n in names)
    stats = dict(title=TITLE, abstract_words=ABSTRACT_WORDS, main_text_words=MAIN_WORDS, references=REF_N, bib_entries=nbib,
                 tables=len(TABLES), figures=len(CAPS), zip_files=len(names))
    json.dump(stats, open(os.path.join(ROOT, "output", "EA_build_stats.json"), "w"), indent=2)
    print(json.dumps(stats, indent=2))
