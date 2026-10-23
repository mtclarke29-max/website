# michelletclarke.com

The academic website of Michelle T. Clarke, written so that people and AI systems both read it well.

## How this folder is organized

| Item | What it is |
|---|---|
| `data.py` | **The only file you edit.** Your bio, publications, summaries, courses, reviews and everything else on the site. |
| `build.py` | Turns `data.py` into the finished website. You run it; you don't need to edit it. |
| `style.css` | The site's design (fonts, colors, layout). |
| `docs/` | The finished website. This is the folder the public sees. Never edit it by hand; `build.py` rewrites it. |
| `cv/` | Your CV: `michelle-t-clarke-cv.pdf` (linked from the site) and `cv.md` (the same CV as text, for AI tools). |
| `WIKIDATA.md` | Ready-to-paste details for creating your Wikidata entries. |

Inside `docs/`:

| File | Who it's for | What it does |
|---|---|---|
| `index.html` | Everyone | The homepage. Plain HTML, no JavaScript, with schema.org structured data (Person, Book, ScholarlyArticle, ORCID, DOIs) that search engines and AI tools use to identify you and your work. |
| `book.html`, `renaissance.html` | Everyone | Pages for *Machiavelli's Florentine Republic* and the Oxford volume. |
| `articles/` | Everyone | One page per article or chapter, with summary, topics, citation and related work, plus a Markdown copy of each. |
| `llms.txt` | Language models | A short guide to who you are and what you argue, with links to everything else. |
| `llms-full.txt`, `*.md` | Language models | The full profile, book and articles as clean Markdown. |
| `publications.bib` | Reference managers | BibTeX for every publication. |
| `robots.txt`, `sitemap.xml` | Crawlers | Welcome all crawlers, including AI crawlers, and list every page. |
| `images/` | Everyone | Your portrait, the book cover and the Ghirlandaio fresco. |
| `CNAME`, `.nojekyll` | GitHub Pages | Connect the site to michelletclarke.com. |

## Publishing on GitHub Pages (free, about 15 minutes)

1. Create a free GitHub account and a new **public** repository (any name, e.g. `website`).
2. Upload everything in this folder, keeping the `docs/` folder intact (including `docs/CNAME` and `docs/.nojekyll`).
3. In the repository, open **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, branch `main`, folder **`/docs`**.
4. At your domain registrar, add DNS records for `michelletclarke.com`:
   - Four `A` records pointing to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - A `CNAME` record for `www` pointing to `<your-github-username>.github.io`
5. Back in **Settings → Pages**, enter `michelletclarke.com` as the custom domain and tick **Enforce HTTPS** once it becomes available.

## After it's live

- Add `https://michelletclarke.com` to your ORCID record (Websites & social links) and your Dartmouth directory page. Links from those profiles tell search engines and AI systems that this site is the authoritative source about you.
- Add the site's address to your Google Scholar profile (Edit → Homepage).
- Register the site in Google Search Console and submit `https://michelletclarke.com/sitemap.xml`.
- Create your Wikidata entries using `WIKIDATA.md`.

## Updating the site

Everything — the homepage, the book and article pages, `llms.txt`, the Markdown files, the BibTeX and the sitemap — is generated from `data.py`, so they always agree.

**The easy way:** open a conversation with Claude, attach `data.py` (or this whole folder), and describe the change: "add my new article in *Polis*, here's the PDF", "change my title to Professor", "add a course". Ask for the updated folder back, then upload the changed files to GitHub.

**By hand:**

1. Open `data.py` in any text editor (TextEdit in plain-text mode works).
2. Make your change. To add a publication, copy an existing entry in the `PUBS` list, paste it at the top, and edit it; then add a matching line to `SLUGS` at the bottom of the file. The comments in the file explain each field.
3. Open Terminal in this folder and run:

   ```
   python3 build.py
   ```

   It prints `ok` when done. (If your Mac asks to install developer tools, accept; that installs Python.)
4. Upload the changed files in `docs/` to GitHub (or drag the whole `docs/` folder into the repository's web page and commit).

The "last updated" date on the site and in the sitemap is set automatically each time you build.

## Updating your CV

Your CV lives in a Claude document, "Michelle T. Clarke — Curriculum Vitae". After editing it, ask Claude for a new PDF and Markdown copy, or download the PDF yourself, and save them as `cv/michelle-t-clarke-cv.pdf` and `cv/cv.md`. Then run `python3 build.py` and upload `docs/` as usual. The site links to the PDF at https://michelletclarke.com/cv/michelle-t-clarke-cv.pdf, so the link never changes.
