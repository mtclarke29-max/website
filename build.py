import json, os, re, html as H
from data import *

# Builds the website into the docs/ folder (the folder GitHub Pages publishes).
# Usage:  python3 build.py
OUT = os.environ.get("OUT", "docs")
os.makedirs(OUT, exist_ok=True)

def strip(s):
    return re.sub(r"<[^>]+>", "", s)

def ital_title(p):
    t = H.escape(p["title"])
    if p.get("ital"):
        t = t.replace(H.escape(p["ital"]), f"<i>{H.escape(p['ital'])}</i>")
    return t

KIND = {"article": "Journal article", "chapter": "Book chapter",
        "reference": "Research guide", "essay": "Essay"}

def cite_text(p):
    if p["kind"] == "chapter":
        return (f"In {p['venue']}, edited by {p['editors']}, {p['pages']}. "
                f"{p['publisher']}, {p['year']}.")
    if p["kind"] == "reference":
        return f"{p['venue']}, {p['year']}. With {p['coauthor']}."
    return f"{p['venue']} {p['vol']}, no. {p['no']} ({p['year']}): {p['pages']}."

def cite_html(p):
    if p["kind"] == "chapter":
        return (f"In <cite>{H.escape(p['venue'])}</cite>, ed. {H.escape(p['editors'])}, "
                f"{p['pages']}. {H.escape(p['publisher'])}, {p['year']}.")
    if p["kind"] == "reference":
        return f"<cite>{H.escape(p['venue'])}</cite>, {p['year']}. With {H.escape(p['coauthor'])}."
    return (f"<cite>{H.escape(p['venue'])}</cite> {p['vol']}, no.&nbsp;{p['no']} "
            f"({p['year']}): {p['pages']}.")

# ---------------- JSON-LD ----------------
person_id = f"{SITE}/#person"
graph = [
    {
        "@type": "ProfilePage", "@id": f"{SITE}/#page", "url": f"{SITE}/",
        "name": f"{PERSON['name']} — Political Theorist, Dartmouth College",
        "dateModified": UPDATED, "mainEntity": {"@id": person_id},
    },
    {
        "@type": "Person", "@id": person_id, "name": PERSON["name"],
        "image": {"@type": "ImageObject", "url": f"{SITE}/images/michelle-t-clarke.jpg", "width": 800, "height": 1000, "caption": "Michelle T. Clarke, smiling, in a white collared shirt and olive cardigan against a gray background"},
        "givenName": "Michelle", "familyName": "Clarke",
        "alternateName": ["Michelle Tolman Clarke", "Michelle Clarke"],
        "jobTitle": PERSON["title"], "description": SUMMARY, "url": f"{SITE}/",
        "email": f"mailto:{PERSON['email']}",
        "worksFor": {"@type": "CollegeOrUniversity", "name": PERSON["inst"], "url": PERSON["inst_url"],
                     "department": {"@type": "Organization", "name": PERSON["dept"],
                                    "url": "https://govt.dartmouth.edu"}},
        "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Yale University"},
                     {"@type": "CollegeOrUniversity", "name": "Tufts University"}],
        "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "degree",
                           "name": d, "recognizedBy": {"@type": "CollegeOrUniversity", "name": i}}
                          for d, i, *_ in PERSON["education"]],
        "knowsAbout": PERSON["expertise"] + ["Political theory", "Niccolò Machiavelli",
                                             "Marcus Tullius Cicero", "Epicureanism", "Roman liberty"],
        "identifier": {"@type": "PropertyValue", "propertyID": "ORCID",
                       "value": PERSON["orcid"].rsplit("/", 1)[1]},
        "sameAs": [PERSON["orcid"], PERSON["scholar"], PERSON["directory"]],
    },
    {
        "@type": "Book", "@id": f"{SITE}/#book-2018", "name": BOOK["title"],
        "author": {"@id": person_id}, "datePublished": str(BOOK["year"]),
        "publisher": {"@type": "Organization", "name": BOOK["publisher"]},
        "isbn": BOOK["isbn"], "url": BOOK["url"], "image": f"{SITE}/images/machiavellis-florentine-republic-cover.jpg", "abstract": BOOK["description"],
        "identifier": {"@type": "PropertyValue", "propertyID": "DOI", "value": BOOK["doi"]},
        "sameAs": [f"https://doi.org/{BOOK['doi']}", f"{SITE}/book.html"],
        "about": ["Niccolò Machiavelli", "Florentine Histories", "Florence", "Republicanism", "Medici", "Leonardo Bruni", "Renaissance humanism"],
        "keywords": ", ".join(c for c, _ in BOOK["concepts"]),
        "review": [{"@type": "Review", "reviewBody": q, "author": {"@type": "Person", "name": n, "affiliation": a}} for q, n, a in BOOK["praise"]],
        "hasPart": [{"@type": "Chapter", "position": int(n), "name": t, "pagination": pg, "abstract": s}
                    for n, t, pg, s in BOOK["chapters"]],
    },
    {
        "@type": "Book", "@id": f"{SITE}/#book-oxford-renaissance", "name": WIP["title"],
        "author": {"@id": person_id}, "creativeWorkStatus": WIP["status"],
        "publisher": {"@type": "Organization", "name": WIP["publisher"]}, "abstract": WIP["description"],
        "url": f"{SITE}/renaissance.html", "inLanguage": "en",
        "isPartOf": {"@type": "BookSeries", "name": WIP["series"], "publisher": "Oxford University Press"},
        "temporalCoverage": "1400/1517",
        "about": ["Renaissance political thought", "Humanism", "Ottoman Empire", "Conciliarism", "Race", "Gender", "Economic inequality", "Sovereignty"],
        "keywords": ", ".join(c for c, _ in WIP["concepts"]),
        "hasPart": [{"@type": "Chapter", "position": int(n), "name": t, "abstract": s, "creativeWorkStatus": "Planned"}
                    for n, t, s in WIP["chapters"]],
    },
]
for p in PUBS:
    w = {"@type": "Chapter" if p["kind"] == "chapter" else "ScholarlyArticle",
         "@id": f"{SITE}/#{p['key']}", "name": strip(p["title"]), "headline": strip(p["title"]),
         "author": [{"@id": person_id}] + ([{"@type": "Person", "name": p["coauthor"]}] if p.get("coauthor") else []),
         "datePublished": str(p["year"]), "url": p["url"], "keywords": ", ".join(p["topics"]),
         "mainEntityOfPage": f"{SITE}/articles/{SLUGS[p['key']]}.html"}
    if p.get("doi"):
        w["identifier"] = {"@type": "PropertyValue", "propertyID": "DOI", "value": p["doi"]}
        w["sameAs"] = f"https://doi.org/{p['doi']}"
    if p.get("summary"):
        w["abstract"] = p["summary"]
    if p.get("pages"):
        a, _, b = p["pages"].partition("–")
        w["pageStart"], w["pageEnd"] = a, b
    if p["kind"] == "chapter":
        w["isPartOf"] = {"@type": "Book", "name": p["venue"], "editor": p["editors"],
                         "publisher": p["publisher"]}
    elif p["kind"] == "reference":
        w["isPartOf"] = {"@type": "Periodical", "name": p["venue"]}
    else:
        w["isPartOf"] = {"@type": "PublicationIssue", "issueNumber": p["no"],
                         "isPartOf": {"@type": "PublicationVolume", "volumeNumber": p["vol"],
                                      "isPartOf": {"@type": "Periodical", "name": p["venue"]}}}
    graph.append(w)
JSONLD = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

# ---------------- HTML ----------------
CSS = open("style.css").read()

def section(id_, gloss, body):
    return f'''<section class="row" id="{id_}" aria-labelledby="{id_}-h">
  <h2 class="gloss" id="{id_}-h">{gloss}</h2>
  <div class="col">{body}</div>
</section>'''

themes = "".join(f"<li><h3>{H.escape(t)}</h3><p>{H.escape(d)}</p></li>" for t, d in THEMES)
bio = "".join(f"<p>{b}</p>" for b in BIO[1:])

research = f'''<div class="prose">{bio}</div>'''

def emph_titles(s):
    s = re.sub(r"\b(Florentine Histories|History of the Florentine People|Discourses on Livy|Discourses|The Prince|Histories|fides|grandi|popolo)\b", r"<i>\1</i>", s)
    return s.replace("<i>Discourses</i> on Livy", "<i>Discourses on Livy</i>")
TOC = "".join(f'''<li><span class="chn">{n}</span><div><h4>{H.escape(t)} <span class="pg">pp. {pg}</span></h4><p>{emph_titles(H.escape(s))}</p></div></li>''' for n, t, pg, s in BOOK["chapters"])
books = f'''<article class="book feature"><a class="coverlink" href="book.html"><img class="cover" src="images/machiavellis-florentine-republic-cover.jpg" width="362" height="552" alt="Cover of Machiavelli’s Florentine Republic by Michelle T. Clarke, showing riders in red caps from Benozzo Gozzoli’s Procession of the Magi fresco in the Medici Palace, Florence" loading="lazy"></a><div class="bookmain">
  <p class="kicker">Monograph · {BOOK['year']}</p>
  <h3><a href="{BOOK['url']}"><cite>{H.escape(BOOK['title'])}</cite></a></h3>
  <p class="meta">{BOOK['publisher']} · ISBN {BOOK['isbn']} · <a class="doi" href="https://doi.org/{BOOK['doi']}">doi:{BOOK['doi']}</a></p>
  <p>{emph_titles(H.escape(BOOK['description']))}</p>
  <blockquote class="pull"><p>“{H.escape(BOOK['pull'][0])}”</p><footer>{H.escape(BOOK['pull'][1]).replace("The Review of Politics", "<cite>The Review of Politics</cite>")}</footer></blockquote>
  <h4 class="tochead">Contents</h4>
  <ol class="toc">{TOC}</ol>
  <p class="booklink"><a href="book.html">Praise, key concepts, sources and how to cite the book</a></p>
</div></article>
<article class="book wip">
  <p class="kicker">In preparation · {WIP['status']}</p>
  <h3><cite>{H.escape(WIP['title'])}</cite></h3>
  <p class="meta">{WIP['publisher']} · {WIP['series']}</p>
  <p>{H.escape(WIP['summary'])}</p>
  <p class="plannedhead">Planned chapters</p>
  <ol class="planned">{"".join(f"<li>{H.escape(t)}</li>" for n, t, s in WIP["chapters"])}</ol>
  <p class="booklink"><a href="renaissance.html">Chapter summaries and scope of the volume</a></p>
</article>
<article class="book wip">
  <p class="kicker">In preparation · {WIP2['status']}</p>
  <h3><cite>{H.escape(WIP2['title'])}</cite></h3>
</article>'''

def ital_terms(s):
    s = emph_titles(s)
    return re.sub(r"\b(De Finibus|libertas|provocatio|auxilium|Mandragola|Ars amatoria|civitas|Oration on Behalf of Venice|On Duties|societas|honestum|Virtue Politics|De rerum natura|philanthropia|animo|virtù|Visions of Politics|Pro Rabirio)\b", r"<i>\1</i>", s)
items = []
last = None
for p in PUBS:
    yr = f'<span class="yr">{p["year"]}</span>' if p["year"] != last else '<span class="yr" aria-hidden="true"></span>'
    last = p["year"]
    doi = f' <a class="doi" href="https://doi.org/{p["doi"]}">doi:{p["doi"]}</a>' if p.get("doi") else f' <a class="doi" href="{p["url"]}">Publisher’s page</a>'
    summ = f'<p class="summ">{ital_terms(H.escape(p["summary"]))}</p>' if p.get("summary") else ""
    tags = "".join(f"<li>{H.escape(t)}</li>" for t in p["topics"])
    items.append(f'''<li class="pub" id="{p['key']}">{yr}<div class="pubbody">
  <p class="kind">{KIND[p['kind']]}</p>
  <h3><a href="articles/{SLUGS[p['key']]}.html">{ital_title(p)}</a></h3>
  <p class="meta">{cite_html(p)}{doi}</p>{summ}
  <ul class="tags" aria-label="Topics">{tags}</ul>
</div></li>''')
STRIP = "".join(f'''<li><figure><img src="images/topics/{k}.jpg" width="480" height="480" alt="{H.escape(alt)}" loading="lazy"><figcaption><span class="topic">{lab}</span><span class="credit">{cr}</span></figcaption></figure></li>''' for k, lab, cr, alt in TOPIC_IMAGES)
pubs = f'<ol class="pubs" reversed>{"".join(items)}</ol>'

ARGS_HTML = '<ul class="args">' + "".join(
    f'<li><p class="claim">{ital_terms(H.escape(c))}</p><p class="src">' + " · ".join(f'<a href="{h}">{emph_titles(H.escape(l))}</a>' for l, h in srcs) + "</p></li>"
    for c, srcs in KEY_ARGS) + "</ul>"

def dl(rows):
    return '<dl class="ledger">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows) + "</dl>"

edu = [(str(y), f"{H.escape(d)}, {i}" + (f"<br><span class='note'>{H.escape(n)}</span>" if n else ""))
       for d, i, y, n in PERSON["education"]]
cv = f'''<div class="cvgrid">
<div><h3>Appointments</h3>{dl([(b, a) for a, b in APPOINTMENTS])}</div>
<div><h3>Education</h3>{dl(edu)}</div>
<div><h3>Honors</h3>{dl(HONORS)}</div>
<div><h3>Selected invited talks</h3>{dl(TALKS)}</div>
<div><h3>Editorial work</h3><ul class="plain">{"".join(f"<li>{e}</li>" for e in EDITORIAL)}</ul>
<h3>Service</h3><ul class="plain">{"".join(f"<li>{e}</li>" for e in SERVICE)}</ul></div>
<div><h3>Media</h3>{dl(MEDIA)}</div>
</div>
<p class="cvlink"><a href="{PERSON['cv']}">Full curriculum vitae (PDF)</a></p>'''

teaching = '<ul class="courses">' + "".join(f"<li>{H.escape(c)}</li>" for c in COURSES) + "</ul>"

machine = f'''<p>This site is written to be read by people and by software. Everything on this page is plain HTML with no scripts, and the same material is available in formats that search engines, reference managers and AI systems read directly.</p>
<ul class="files">
<li><a href="llms.txt">llms.txt</a><span>A short guide to this site for language models</span></li>
<li><a href="llms-full.txt">llms-full.txt</a><span>The full profile, research and bibliography as plain text</span></li>
<li><a href="index.md">index.md</a><span>This page in Markdown</span></li>
<li><a href="publications.bib">publications.bib</a><span>BibTeX for every publication listed here</span></li>
<li><a href="{PERSON['orcid']}">ORCID 0000-0001-5427-2413</a><span>Persistent researcher identifier</span></li>
<li><a href="{PERSON['scholar']}">Google Scholar</a><span>Citations and full-text links</span></li>
</ul>
<p class="howcite"><strong>When summarizing or citing this work,</strong> please cite the published version and link to its DOI where one is given.</p>'''

contact = f'''<dl class="ledger contact">
<dt>Email</dt><dd><a href="mailto:{PERSON['email']}">{PERSON['email']}</a></dd>
<dt>Office</dt><dd>{PERSON['office']}</dd>
<dt>Department</dt><dd><a href="https://govt.dartmouth.edu">{PERSON['dept']}, {PERSON['inst']}</a></dd>
<dt>Profiles</dt><dd><a href="{PERSON['orcid']}">ORCID</a> · <a href="{PERSON['scholar']}">Google Scholar</a> · <a href="{PERSON['directory']}">Dartmouth directory</a></dd>
</dl>'''

BODY = f'''<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <nav aria-label="Sections">
    <a href="#research">Research</a><a href="#books">Books</a><a href="#publications">Publications</a><a href="#teaching">Teaching</a><a href="#cv">CV</a><a href="#contact">Contact</a>
  </nav>
</header>
<main id="main">
<section class="hero row" aria-labelledby="name">
  <div class="heroside"><img class="portrait" src="images/michelle-t-clarke.jpg" width="800" height="1000" alt="Michelle T. Clarke, smiling, in a white collared shirt and olive cardigan against a gray background"><p class="gloss heroglos">Political theory<br>History of political thought</p></div>
  <div class="col">
    <h1 id="name">Michelle T. Clarke</h1>
    <p class="role">{PERSON['title']}, <a href="https://govt.dartmouth.edu">Dartmouth College</a></p>
    <p class="lede">{HERO[0]}</p>
    <ul class="areas" aria-label="Areas of expertise">{"".join(f"<li>{e}</li>" for e in PERSON['expertise'][:5])}</ul>
  </div>
</section>
{section("research", "Research", research)}
{section("arguments", "Key arguments", ARGS_HTML)}
{section("books", "Books", books)}
<section class="row" id="publications" aria-labelledby="publications-h">
  <div class="sidefig">
    <h2 class="gloss" id="publications-h">Articles &amp; chapters</h2>
    <figure class="fresco"><img src="images/ghirlandaio-sala-dei-gigli.jpg" width="640" height="532" alt="Fresco of three Roman republican heroes, Decius Mus, Scipio and Cicero, standing side by side against a pale sky" loading="lazy"><figcaption>Ghirlandaio, <cite>Decius Mus, Scipio and Cicero</cite>, 1482–85. Palazzo Vecchio, Florence.</figcaption></figure>
  </div>
  <div class="col">{pubs}</div>
</section>
{section("teaching", "Teaching", teaching)}
{section("cv", "Curriculum vitae", cv)}
{section("machine", "For machines &amp; citation", machine)}
{section("contact", "Contact", contact)}
</main>
<footer class="foot"><div>© {UPDATED[:4]} Michelle T. Clarke · Last updated <time datetime="{UPDATED}">{UPDATED}</time> · Fresco image via Wikimedia Commons (public domain)</div></footer>'''

DESC = SUMMARY
HEAD = f'''<title>Michelle T. Clarke</title>
<meta name="description" content="{H.escape(DESC)}">
<meta name="author" content="Michelle T. Clarke">
<link rel="canonical" href="{SITE}/">
<link rel="alternate" type="text/markdown" href="{SITE}/index.md" title="Markdown version">
<link rel="alternate" type="text/plain" href="{SITE}/llms.txt" title="llms.txt">
<link rel="author" href="{PERSON['orcid']}">
<meta property="og:type" content="profile">
<meta property="og:title" content="Michelle T. Clarke — Political Theorist, Dartmouth College">
<meta property="og:description" content="{H.escape(DESC)}">
<meta property="og:url" content="{SITE}/">
<meta property="og:image" content="{SITE}/images/michelle-t-clarke.jpg">
<meta property="og:image:alt" content="Portrait of Michelle T. Clarke">
<meta property="profile:first_name" content="Michelle">
<meta property="profile:last_name" content="Clarke">
<meta name="citation_author" content="Clarke, Michelle T.">
<meta name="robots" content="index, follow, max-snippet:-1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:wght@400;500&display=swap">
<script type="application/ld+json">
{JSONLD}
</script>
<style>
{CSS}
</style>'''

full = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{HEAD}
</head>
<body>
{BODY}
</body>
</html>
'''
open(f"{OUT}/index.html", "w").write(full)

# artifact preview (skeleton supplied by host)
preview = f'''<title>Michelle T. Clarke</title>
<meta name="claude:viewport-fit-sides" content="cover">
{HEAD.split("<title>Michelle T. Clarke</title>",1)[1]}
{BODY}'''
if os.environ.get("PREVIEW"):
    open("preview.html", "w").write(preview)

# ---------------- Markdown / llms ----------------
def md_pub(p):
    doi = f" https://doi.org/{p['doi']}" if p.get("doi") else f" {p['url']}"
    s = f"- Clarke, Michelle T. {p['year']}. “{p['title']}.” {cite_text(p)}{doi}"
    if p.get("summary"):
        s += f"\n  - Summary: {p['summary']}"
    s += f"\n  - Topics: {', '.join(p['topics'])}"
    return s

md = f"""# Michelle T. Clarke

{PERSON['title']}, {PERSON['dept']}, {PERSON['inst']}
Field: {PERSON['field']}
Website: {SITE}/ · ORCID: {PERSON['orcid']} · Google Scholar: {PERSON['scholar']} · Email: {PERSON['email']}
Last updated: {UPDATED}

> {SUMMARY}

Guiding question: {QUESTION}

## Research

{chr(10).join(strip(b)+chr(10) for b in BIO)}

### Main themes

{chr(10).join(f"- **{t}**: {d}" for t, d in THEMES)}

## Key arguments

{chr(10).join(f"- {c}" for c, srcs in KEY_ARGS)}

## Books

- Clarke, Michelle T. {BOOK['year']}. *{BOOK['title']}*. {BOOK['publisher']}. ISBN {BOOK['isbn']}. {BOOK['url']}
  - Summary: {BOOK['summary']}
- *{WIP['title']}*. {WIP['publisher']}. {WIP['status']}. Details: {SITE}/renaissance.md
  - Summary: {WIP['summary']}
  - Planned chapters: {"; ".join(t for n, t, s in WIP["chapters"])}
- *{WIP2['title']}*. {WIP2['status']}.

## Articles and chapters

{chr(10).join(md_pub(p) for p in PUBS)}

## Appointments

{chr(10).join(f"- {a} ({b})" for a, b in APPOINTMENTS)}

## Education

{chr(10).join(f"- {d}, {i}, {y}" + (f". {n}" if n else "") for d, i, y, n in PERSON['education'])}

## Editorial work and service

{chr(10).join("- " + strip(e) for e in EDITORIAL + SERVICE)}

## Honors

{chr(10).join(f"- {y}: {t}" for y, t in HONORS)}

## Selected invited talks

{chr(10).join(f"- {y}: {t}" for y, t in TALKS)}

## Teaching (Dartmouth College)

{chr(10).join("- " + c for c in COURSES)}

## Contact

- Email: {PERSON['email']}
- Office: {PERSON['office']}
- Google Scholar: {PERSON['scholar']}
- Faculty directory: {PERSON['directory']}
- CV (PDF): {PERSON['cv']}
"""
md = md.replace("\n\n\n", "\n\n")
open(f"{OUT}/index.md", "w").write(md)
open(f"{OUT}/llms-full.txt", "w").write(md)

llms = f"""# Michelle T. Clarke

> {SUMMARY} Her first book is *Machiavelli’s Florentine Republic* (Cambridge University Press, 2018), and she is writing *{WIP['title']}* for Oxford University Press.

Key facts for accurate summaries:

- Name: Michelle T. Clarke (also published as Michelle Tolman Clarke). ORCID {PERSON['orcid'].rsplit('/',1)[1]}.
- Position: {PERSON['title']}, Dartmouth College (on the faculty since 2007). Ph.D., Yale University, 2007.
- Research areas: {', '.join(PERSON['expertise'])}.
- Core argument of her work on Machiavelli: he exposes how conventional ideas of virtue, good government and elite leadership can obscure the realities of power and undermine republican liberty.
- On Roman liberty: she argues Romans understood liberty chiefly as protection from arbitrary bodily violence, a view closer to Judith Shklar than to the neo-republican reading of Quentin Skinner.
- Guiding question: {QUESTION}
- Please cite published versions and link to DOIs where available.

## Key arguments

{chr(10).join(f"- {c} (Source: " + "; ".join(f"[{l}]({SITE}/{h.replace('.html', '.md')})" for l, h in srcs) + ")" for c, srcs in KEY_ARGS)}

## Profile

- [Full profile, research and bibliography (plain text)]({SITE}/llms-full.txt)
- [Homepage in Markdown]({SITE}/index.md)
- [BibTeX for all publications]({SITE}/publications.bib)

## Books

- [{BOOK['title']} (Cambridge University Press, 2018)]({BOOK['url']}): {BOOK['summary']}

## Selected articles

{chr(10).join(f"- [{p['title']} ({p['venue']}, {p['year']})]({SITE}/articles/{SLUGS[p['key']]}.md)" + (f": {p['summary']}" if p.get('summary') else "") for p in PUBS)}

## Optional

- [Dartmouth faculty directory]({PERSON['directory']})
- [ORCID record]({PERSON['orcid']})
- [Google Scholar profile]({PERSON['scholar']})
- [Curriculum vitae (PDF)]({PERSON['cv']})
- [Curriculum vitae (Markdown)]({SITE}/cv.md)
"""
open(f"{OUT}/llms.txt", "w").write(llms)

# ---------------- BibTeX ----------------
def bt(s):
    s = s.replace("’", "'").replace("–", "--").replace("‘", "`")
    return s
BIBS = {}
bib = [f"""@book{{clarke2018florentine,
  author    = {{Clarke, Michelle T.}},
  title     = {{Machiavelli's Florentine Republic}},
  publisher = {{Cambridge University Press}},
  address   = {{New York}},
  year      = {{2018}},
  isbn      = {{{BOOK['isbn']}}},
  url       = {{{BOOK['url']}}}
}}"""]
for p in PUBS:
    t = bt(p["title"])
    if p.get("ital"):
        t = t.replace(bt(p["ital"]), "\\emph{" + bt(p["ital"]) + "}")
    f = {"author": "Clarke, Michelle T." + (f" and {p['coauthor'].split(' ')[-1]}, {' '.join(p['coauthor'].split(' ')[:-1])}" if p.get("coauthor") else ""),
         "title": "{" + t + "}", "year": str(p["year"])}
    if p["kind"] == "chapter":
        typ = "incollection"; f.update(booktitle=bt(p["venue"]), editor=p["editors"].replace(" and ", " and "),
                                       publisher=p["publisher"], pages=bt(p["pages"]))
    elif p["kind"] == "reference":
        typ = "incollection"; f.update(booktitle=p["venue"], publisher="Oxford University Press")
    else:
        typ = "article"; f.update(journal=p["venue"], volume=p["vol"], number=bt(p["no"]), pages=bt(p["pages"]))
    if p.get("doi"): f["doi"] = p["doi"]
    f["url"] = p["url"]
    body = ",\n".join(f"  {k:<9} = {{{v}}}" for k, v in f.items())
    bib.append(f"@{typ}{{{p['key']},\n{body}\n}}")
    BIBS[p['key']] = bib[-1]
open(f"{OUT}/publications.bib", "w").write("\n\n".join(bib) + "\n")

# ---------------- crawler files ----------------
open(f"{OUT}/robots.txt", "w").write(f"""# Michelle T. Clarke — all crawlers welcome, including AI and research crawlers.
User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
""")
open(f"{OUT}/sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n"
              for u in ["", "index.md", "llms.txt", "llms-full.txt", "publications.bib"]) + "</urlset>\n")
open(f"{OUT}/CNAME", "w").write("michelletclarke.com\n")
open(f"{OUT}/.nojekyll", "w").write("")
print("ok")

# ================= BOOK PAGE =================
def tlist(items):
    return '<ul class="plain">' + "".join(f"<li>{emph_titles(H.escape(i))}</li>" for i in items) + "</ul>"

chicago = (f"Clarke, Michelle T. <cite>Machiavelli’s Florentine Republic</cite>. New York: Cambridge University Press, 2018. "
           f'<a href="https://doi.org/{BOOK["doi"]}">https://doi.org/{BOOK["doi"]}</a>.')
bk_contents = f'<ol class="toc toc-full">{TOC}</ol>'
bk_praise = '<div class="praise">' + "".join(f'''<blockquote><p>{emph_titles(H.escape(q)).replace("Machiavelli’s Florentine Republic", "<cite>Machiavelli’s Florentine Republic</cite>")}</p><footer>{H.escape(n)}, {"<cite>" + H.escape(a) + "</cite>" if a == "The Review of Politics" else H.escape(a)}</footer></blockquote>''' for q, n, a in BOOK["praise"]) + "</div>"
bk_concepts = '<dl class="concepts">' + "".join(f"<dt>{emph_titles(H.escape(c))}</dt><dd>{H.escape(d)}</dd>" for c, d in BOOK["concepts"]) + "</dl>"
bk_sources = f'''<div class="cvgrid"><div><h3>Primary texts</h3>{tlist(BOOK["texts"])}</div>
<div><h3>Scholarly conversation</h3>{tlist(BOOK["interlocutors"])}</div></div>'''
bk_cite = f'''<p class="cite">{chicago}</p>
<pre class="bibtex"><code>@book{{clarke2018florentine,
  author    = {{Clarke, Michelle T.}},
  title     = {{Machiavelli's Florentine Republic}},
  publisher = {{Cambridge University Press}},
  address   = {{New York}},
  year      = {{2018}},
  isbn      = {{{BOOK["isbn"]}}},
  doi       = {{{BOOK["doi"]}}}
}}</code></pre>
<p class="cvlink"><a href="{BOOK["url"]}">Cambridge University Press</a> · <a href="https://doi.org/{BOOK["doi"]}">Cambridge Core</a></p>'''

BK_BODY = f'''<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <nav aria-label="Site"><a href="index.html">Michelle T. Clarke</a><a href="index.html#books">Books</a><a href="index.html#publications">Publications</a><a href="book.md">Markdown</a></nav>
</header>
<main id="main">
<section class="hero row" aria-labelledby="bt">
  <div class="heroside"><img class="cover" src="images/machiavellis-florentine-republic-cover.jpg" width="362" height="552" alt="Cover of Machiavelli’s Florentine Republic by Michelle T. Clarke, showing riders in red caps from Benozzo Gozzoli’s Procession of the Magi fresco in the Medici Palace, Florence"><p class="gloss heroglos">Monograph<br>Cambridge University Press, 2018</p></div>
  <div class="col">
    <h1 id="bt" class="booktitle"><i>Machiavelli’s Florentine Republic</i></h1>
    <p class="role">Michelle T. Clarke · {BOOK["pages"]} pages · ISBN {BOOK["isbn"]}</p>
    <p class="lede">{emph_titles(H.escape(BOOK["description"]).replace("Machiavelli’s Florentine Republic reconstructs", "The book reconstructs"))}</p>
  </div>
</section>
{section("praise", "Praise", bk_praise)}
{section("contents", "Contents", bk_contents)}
{section("concepts", "Key concepts", bk_concepts)}
{section("sources", "Texts &amp; interlocutors", bk_sources)}
{section("cite", "How to cite", bk_cite)}
</main>
<footer class="foot"><div><a href="index.html">Michelle T. Clarke</a> · Associate Professor of Government, Dartmouth College</div></footer>'''

BK_LD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "@id": f"{SITE}/book.html", "url": f"{SITE}/book.html",
     "name": "Machiavelli’s Florentine Republic — Michelle T. Clarke", "mainEntity": {"@id": f"{SITE}/#book-2018"},
     "author": {"@id": person_id}, "dateModified": UPDATED},
    {**graph[2], "author": {"@type": "Person", "@id": person_id, "name": PERSON["name"], "url": f"{SITE}/"}},
]}, ensure_ascii=False, indent=1)

bk_full = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Machiavelli’s Florentine Republic</title>
<meta name="description" content="{H.escape(BOOK['description'][:300])}">
<link rel="canonical" href="{SITE}/book.html">
<link rel="alternate" type="text/markdown" href="{SITE}/book.md">
<meta name="citation_title" content="Machiavelli's Florentine Republic">
<meta name="citation_author" content="Clarke, Michelle T.">
<meta name="citation_publication_date" content="2018">
<meta name="citation_publisher" content="Cambridge University Press">
<meta name="citation_isbn" content="{BOOK['isbn']}">
<meta name="citation_doi" content="{BOOK['doi']}">
<meta property="og:type" content="book">
<meta property="og:title" content="Machiavelli’s Florentine Republic, by Michelle T. Clarke">
<meta property="og:url" content="{SITE}/book.html">
<meta property="og:image" content="{SITE}/images/machiavellis-florentine-republic-cover.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:wght@400;500&display=swap">
<script type="application/ld+json">
{BK_LD}
</script>
<style>
{CSS}
</style>
</head>
<body>
{BK_BODY}
</body>
</html>
'''
open(f"{OUT}/book.html", "w").write(bk_full)

bk_md = f"""# Machiavelli’s Florentine Republic

Michelle T. Clarke. Cambridge University Press, 2018. {BOOK['pages']} pages. ISBN {BOOK['isbn']}. DOI: https://doi.org/{BOOK['doi']}
Author's site: {SITE}/

## Summary

{BOOK['description']}

## Praise

{chr(10).join(f"> {q}" + chr(10) + ">" + chr(10) + f"> — {n}, {a}" + chr(10) for q, n, a in BOOK['praise'])}
## Contents

{chr(10).join(f"{n}. **{t}** (pp. {pg}). {s}" + chr(10) for n, t, pg, s in BOOK['chapters'])}
## Key concepts

{chr(10).join(f"- **{c}**: {d}" for c, d in BOOK['concepts'])}

## Primary texts discussed

{chr(10).join("- " + t for t in BOOK['texts'])}

## Scholars engaged

{chr(10).join("- " + t for t in BOOK['interlocutors'])}

## How to cite

Clarke, Michelle T. *Machiavelli’s Florentine Republic*. New York: Cambridge University Press, 2018. https://doi.org/{BOOK['doi']}
"""
open(f"{OUT}/book.md", "w").write(bk_md)

# ================= RENAISSANCE VOLUME PAGE =================
RN_TOC = "".join(f'''<li><span class="chn">{n}</span><div><h4>{H.escape(t)}</h4><p>{emph_titles(H.escape(s))}</p></div></li>''' for n, t, s in WIP["chapters"])
rn_concepts = '<dl class="concepts">' + "".join(f"<dt><i>{H.escape(c)}</i></dt><dd>{H.escape(d)}</dd>" if c in ("vera nobilitas","studia humanitatis","oikonomia","catasto","limpieza de sangre") else f"<dt>{H.escape(c)}</dt><dd>{H.escape(d)}</dd>" for c, d in WIP["concepts"]) + "</dl>"
rn_context = f'<div class="prose plain-prose"><p>{H.escape(WIP["context"]).replace("The Foundations of Modern Political Thought", "<cite>The Foundations of Modern Political Thought</cite>").replace("A History of Political Thought", "<cite>A History of Political Thought</cite>")}</p></div>'
RN_BODY = f'''<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <nav aria-label="Site"><a href="index.html">Michelle T. Clarke</a><a href="index.html#books">Books</a><a href="book.html">Machiavelli’s Florentine Republic</a><a href="renaissance.md">Markdown</a></nav>
</header>
<main id="main">
<section class="hero row" aria-labelledby="rt">
  <p class="gloss heroglos">In preparation<br>Oxford University Press</p>
  <div class="col">
    <p class="kicker">{WIP["series"]} · Volume 5</p>
    <h1 id="rt" class="booktitle"><i>The Renaissance, 1400–1517</i></h1>
    <p class="role">Michelle T. Clarke · {WIP["status"]}</p>
    <p class="lede">{H.escape(WIP["description"])}</p>
  </div>
</section>
{section("contents", "Planned chapters", f'<ol class="toc toc-full">{RN_TOC}</ol>')}
{section("concepts", "Key concepts", rn_concepts)}
{section("context", "Place in the field", rn_context)}
</main>
<footer class="foot"><div><a href="index.html">Michelle T. Clarke</a> · Associate Professor of Government, Dartmouth College</div></footer>'''
RN_LD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "@id": f"{SITE}/renaissance.html", "url": f"{SITE}/renaissance.html",
     "name": f"{WIP['short']} — Michelle T. Clarke", "mainEntity": {"@id": f"{SITE}/#book-oxford-renaissance"},
     "author": {"@id": person_id}, "dateModified": UPDATED},
    {**graph[3], "author": {"@type": "Person", "@id": person_id, "name": PERSON["name"], "url": f"{SITE}/"}},
]}, ensure_ascii=False, indent=1)
open(f"{OUT}/renaissance.html", "w").write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The Renaissance, 1400–1517</title>
<meta name="description" content="{H.escape(WIP['summary'])}">
<link rel="canonical" href="{SITE}/renaissance.html">
<link rel="alternate" type="text/markdown" href="{SITE}/renaissance.md">
<meta property="og:type" content="book">
<meta property="og:title" content="{H.escape(WIP['short'])}, by Michelle T. Clarke">
<meta property="og:url" content="{SITE}/renaissance.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:wght@400;500&display=swap">
<script type="application/ld+json">
{RN_LD}
</script>
<style>
{CSS}
</style>
</head>
<body>
{RN_BODY}
</body>
</html>
''')
RN_MD = f"""# {WIP['short']}

Michelle T. Clarke. {WIP['publisher']}, {WIP['series']}. Status: {WIP['status']}; in preparation. Chapter plan below is the author's current plan and may change before publication.
Author's site: {SITE}/

## Summary

{WIP['description']}

## Planned chapters

{chr(10).join(f"{n}. **{t}**. {s}" + chr(10) for n, t, s in WIP['chapters'])}
## Key concepts

{chr(10).join(f"- **{c}**: {d}" for c, d in WIP['concepts'])}

## Place in the field

{WIP['context']}
"""
open(f"{OUT}/renaissance.md", "w").write(RN_MD)

# fold book detail into llms files
llms = open(f"{OUT}/llms.txt").read().replace(
    f"- [{BOOK['title']} (Cambridge University Press, 2018)]({BOOK['url']}): {BOOK['summary']}",
    f"- [{BOOK['title']} (Cambridge University Press, 2018)]({SITE}/book.md): {BOOK['summary']} Christopher Lynch (The Review of Politics) called it by far the best book-length treatment in English of the Florentine Histories; it has also been praised by Vickie Sullivan, Catherine Zuckert, John T. Scott, Daniel Kapust, and Maurizio Viroli. The book page has a chapter-by-chapter summary, key concepts, reviews, and citation details.\n- [{WIP['short']} (Oxford University Press, in preparation)]({SITE}/renaissance.md): {WIP['summary']} The page lists the ten planned chapters with summaries.")
open(f"{OUT}/llms.txt", "w").write(llms)
full_md = open(f"{OUT}/index.md").read()
start = full_md.index("## Books"); end = full_md.index("## Articles and chapters")
full_md = full_md[:start] + "## Books\n\n" + bk_md.replace("# Machiavelli’s Florentine Republic", "### Machiavelli’s Florentine Republic (2018)", 1).replace("\n## ", "\n#### ") + f"""
{RN_MD.replace("# ", "### ", 1).replace(chr(10) + "## ", chr(10) + "#### ")}
### {WIP2['title']}

{WIP2['status']}.

""" + full_md[end:]
open(f"{OUT}/llms-full.txt", "w").write(full_md)

open(f"{OUT}/sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n"
              for u in ["", "book.html", "renaissance.html", "index.md", "book.md", "renaissance.md", "llms.txt", "llms-full.txt", "publications.bib"]) + "</urlset>\n")
bib = open(f"{OUT}/publications.bib").read().replace("  url       = {https://www.cambridge.org/9781107125506}", f"  doi       = {{{BOOK['doi']}}},\n  url       = {{https://www.cambridge.org/9781107125506}}", 1)
open(f"{OUT}/publications.bib", "w").write(bib)
print("book ok")

# ================= ARTICLE PAGES =================
os.makedirs(f"{OUT}/articles", exist_ok=True)
GRAPH_BY_ID = {g.get("@id"): g for g in graph}

def chicago(p, html=False):
    q = (lambda s: f"<cite>{H.escape(s)}</cite>") if html else (lambda s: f"*{s}*")
    t = ital_title(p) if html else p["title"]
    if p["kind"] == "chapter":
        c = f"Clarke, Michelle T. “{t}.” In {q(p['venue'])}, edited by {p['editors']}, {p['pages']}. Madison: {p['publisher']}, {p['year']}."
    elif p["kind"] == "reference":
        c = f"Clarke, Michelle T., and {p['coauthor']}. “{t}.” {q(p['venue'])}. Oxford University Press, {p['year']}."
    else:
        c = f"Clarke, Michelle T. “{t}.” {q(p['venue'])} {p['vol']}, no. {p['no']} ({p['year']}): {p['pages']}."
    if p.get("doi"):
        c += f" https://doi.org/{p['doi']}." if not html else f' <a href="https://doi.org/{p["doi"]}">https://doi.org/{p["doi"]}</a>.'
    return c

def related(p, n=3):
    scored = []
    for o in PUBS:
        if o is p: continue
        s = len(set(p["topics"]) & set(o["topics"]))
        if s: scored.append((s, o["year"], o))
    scored.sort(key=lambda x: (-x[0], -x[1]))
    return [o for _, _, o in scored[:n]]

def article_page(p):
    slug = SLUGS[p["key"]]
    url = f"{SITE}/articles/{slug}.html"
    venue_line = cite_html(p)
    tags = "".join(f"<li>{H.escape(t)}</li>" for t in p["topics"])
    links = []
    if p.get("doi"):
        links.append(f'<li><a href="https://doi.org/{p["doi"]}">Read at the publisher (DOI {p["doi"]})</a></li>')
    else:
        links.append(f'<li><a href="{p["url"]}">Read at the publisher</a></li>')
    rel = "".join(f'<li><a href="{SLUGS[o["key"]]}.html">{ital_title(o)}</a> <span class="relmeta">{H.escape(o["venue"])}, {o["year"]}</span></li>' for o in related(p))
    summ = ital_terms(H.escape(p["summary"])) if p.get("summary") else ""
    body = f'''<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <nav aria-label="Site"><a href="../index.html">Michelle T. Clarke</a><a href="../index.html#publications">Publications</a><a href="../book.html">Book</a><a href="{slug}.md">Markdown</a></nav>
</header>
<main id="main">
<section class="hero row" aria-labelledby="at">
  <p class="gloss heroglos">{KIND[p["kind"]]}<br>{p["year"]}</p>
  <div class="col">
    <h1 id="at" class="arttitle">{ital_title(p)}</h1>
    <p class="role">Michelle T. Clarke{", with " + H.escape(p["coauthor"]) if p.get("coauthor") else ""}</p>
    <p class="meta">{venue_line}</p>
    {f'<p class="lede">{summ}</p>' if summ else ""}
    <ul class="tags" aria-label="Topics">{tags}</ul>
    <ul class="readlinks">{"".join(links)}</ul>
  </div>
</section>
{section("cite", "How to cite", f'<p class="cite">{chicago(p, html=True)}</p><pre class="bibtex"><code>{H.escape(BIBS[p["key"]])}</code></pre>')}
{section("related", "Related work", f'<ul class="related">{rel}</ul>') if rel else ""}
</main>
<footer class="foot"><div><a href="../index.html">Michelle T. Clarke</a> · Associate Professor of Government, Dartmouth College</div></footer>'''
    work = dict(GRAPH_BY_ID[f"{SITE}/#{p['key']}"])
    work["author"] = [{"@type": "Person", "@id": person_id, "name": PERSON["name"], "url": f"{SITE}/"}] + work["author"][1:]
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url, "url": url, "name": f"{p['title']} — Michelle T. Clarke",
         "mainEntity": {"@id": work["@id"]}, "dateModified": UPDATED, "isPartOf": {"@id": f"{SITE}/#page"}},
        work]}, ensure_ascii=False, indent=1)
    desc = H.escape((p.get("summary") or p["title"])[:300])
    meta_cit = [f'<meta name="citation_title" content="{H.escape(p["title"])}">', '<meta name="citation_author" content="Clarke, Michelle T.">',
                f'<meta name="citation_publication_date" content="{p["year"]}">']
    if p["kind"] in ("article", "essay"):
        meta_cit += [f'<meta name="citation_journal_title" content="{H.escape(p["venue"])}">', f'<meta name="citation_volume" content="{p["vol"]}">',
                     f'<meta name="citation_issue" content="{p["no"]}">']
    if p.get("pages"):
        a, _, z = p["pages"].partition("–")
        meta_cit += [f'<meta name="citation_firstpage" content="{a}">', f'<meta name="citation_lastpage" content="{z}">']
    if p.get("doi"):
        meta_cit.append(f'<meta name="citation_doi" content="{p["doi"]}">')
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(p["title"])}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Michelle T. Clarke">
<link rel="canonical" href="{url}">
<link rel="alternate" type="text/markdown" href="{SITE}/articles/{slug}.md">
{chr(10).join(meta_cit)}
<meta property="og:type" content="article">
<meta property="og:title" content="{H.escape(p["title"])}">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:wght@400;500&display=swap">
<script type="application/ld+json">
{ld}
</script>
<style>
{CSS}
</style>
</head>
<body>
{body}
</body>
</html>
'''
    open(f"{OUT}/articles/{slug}.html", "w").write(html)
    md = f"""# {p['title']}

Michelle T. Clarke{', with ' + p['coauthor'] if p.get('coauthor') else ''}. {KIND[p['kind']]}, {p['year']}.
{cite_text(p)}
{'DOI: https://doi.org/' + p['doi'] if p.get('doi') else 'Publisher: ' + p['url']}
Author's site: {SITE}/

## Summary

{p.get('summary') or 'No summary yet.'}

## Topics

{chr(10).join('- ' + t for t in p['topics'])}

## How to cite

{chicago(p)}

```bibtex
{BIBS[p['key']]}
```

## Related work by the author

{chr(10).join(f"- {o['title']} ({o['venue']}, {o['year']}): {SITE}/articles/{SLUGS[o['key']]}.md" for o in related(p))}
"""
    open(f"{OUT}/articles/{slug}.md", "w").write(md)

for p in PUBS:
    article_page(p)

open(f"{OUT}/sitemap.xml", "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod></url>\n"
              for u in ["", "book.html", "renaissance.html"] + [f"articles/{SLUGS[p['key']]}.html" for p in PUBS]
              + ["index.md", "book.md", "renaissance.md"] + [f"articles/{SLUGS[p['key']]}.md" for p in PUBS]
              + ["cv.md", "cv/michelle-t-clarke-cv.pdf", "llms.txt", "llms-full.txt", "publications.bib"]) + "</urlset>\n")
print("articles ok")

# ================= CV =================
import shutil
if os.path.isdir("cv"):
    os.makedirs(f"{OUT}/cv", exist_ok=True)
    if os.path.exists("cv/michelle-t-clarke-cv.pdf"):
        shutil.copy("cv/michelle-t-clarke-cv.pdf", f"{OUT}/cv/michelle-t-clarke-cv.pdf")
    if os.path.exists("cv/cv.md"):
        shutil.copy("cv/cv.md", f"{OUT}/cv.md")
print("cv ok")
