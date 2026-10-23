# Creating your Wikidata entries

Wikidata is the free database behind Wikipedia, and one of the main sources search engines and AI systems use to tell people apart. An entry that ties your name to your ORCID, Dartmouth, your website and your book keeps you from being confused with other Michelle Clarkes.

**What already exists (checked 22 October 2026):**

- There is **no entry for you** yet (no item carries your ORCID).
- There is **no entry for *Machiavelli's Florentine Republic***.
- Your 2013 *Journal of Politics* article already exists as **Q57310686**, but your name is stored as plain text rather than linked to a person.
- Christopher Lynch's review of your book in *The Review of Politics* exists as **Q128108007**.

The steps below take about 20 minutes. Wikidata allows people to create entries about themselves as long as everything is factual and verifiable. Stick to the facts listed here.

---

## Step 1. Create an account

Go to wikidata.org, click **Create account**, and sign in.

## Step 2. Create your entry

Click **Create a new Item** in the left-hand menu and fill in:

| Field | Enter |
|---|---|
| Label | `Michelle T. Clarke` |
| Description | `American political theorist` |
| Also known as | `Michelle Tolman Clarke` · `Michelle Clarke` |

Click **Create**. On the new page, click **+ add statement** for each row below. Type the property name, then start typing the value and pick the matching item from the dropdown. The Q-numbers let you confirm you've picked the right one.

| Property | Value |
|---|---|
| instance of (P31) | human (Q5) |
| occupation (P106) | political theorist (Q15994177) |
| occupation (P106) | university teacher (Q1622272) |
| employer (P108) | Dartmouth College (Q49116). Optional qualifier: *start time* 2007 |
| educated at (P69) | Yale University (Q49112). Optional qualifiers: *academic degree* "Doctor of Philosophy", *end time* 2007 |
| educated at (P69) | Tufts University (Q49120). Optional qualifiers: *academic degree* "Bachelor of Arts", *end time* 2001 |
| field of work (P101) | history of political thought (Q3500207) |
| field of work (P101) | republicanism (Q877848) |
| field of work (P101) | Niccolò Machiavelli (Q1399) |
| ORCID iD (P496) | `0000-0001-5427-2413` |
| Google Scholar author ID (P1960) | `idY581AAAAAJ` |
| official website (P856) | `https://michelletclarke.com` |

**Adding references (optional but helpful).** References show where a fact comes from. Add one to the employer and education statements:

1. Make sure the statement itself is saved first: you should see **edit** next to it, not **publish**.
2. Under the statement, click **+ add reference**. A single empty box appears.
3. Type `reference URL` into that box. **Wait for the dropdown and click "reference URL (P854)"** in it. The box for the web address only appears after you click the dropdown suggestion; pressing Enter or just typing the name isn't enough.
4. A second box now appears to the right of the first (or below it, in a narrow window). Paste `https://faculty-directory.dartmouth.edu/michelle-t-clarke` there.
5. Click **publish** at the right-hand end of that statement.

If the second box still doesn't appear, skip the references. They aren't required, and you can add them later.

Note the Q-number Wikidata gives your new entry; you'll need it below.

## Step 3. Create an entry for the book

**Create a new Item** again:

| Field | Enter |
|---|---|
| Label | `Machiavelli's Florentine Republic` |
| Description | `2018 book by Michelle T. Clarke` |

Then add these statements:

| Property | Value |
|---|---|
| instance of (P31) | version, edition or translation (Q3331189). This should be the **only** *instance of* value. Plain "book" gives a "none-of constraint" warning, and "monograph" makes Wikidata object to the ISBN. |
| title (P1476) | `Machiavelli's Florentine Republic` (language: English) |
| author (P50) | *your new entry from Step 2* |
| publisher (P123) | Cambridge University Press (Q912887) |
| publication date (P577) | 2018 |
| ISBN-13 (P212) | `978-1-107-12550-6` |
| DOI (P356) | `10.1017/9781316410776` |
| language of work or name (P407) | English (Q1860) |
| main subject (P921) | Niccolò Machiavelli (Q1399) |
| main subject (P921) | Florentine Histories (Q691766) |
| main subject (P921) | republicanism (Q877848) |

Then go back to **your** entry and add:

| Property | Value |
|---|---|
| notable work (P800) | Machiavelli's Florentine Republic *(the new book entry)* |

## Step 4. Connect what already exists

1. **Your 2013 article (Q57310686):** search Wikidata for `Q57310686`. Under *author name string* you'll see "Michelle T. Clarke". Add a new statement *author* (P50) with your new entry, and give it the qualifier *series ordinal* = `1`. Then remove the *author name string* statement.
2. **Lynch's review (Q128108007):** add a statement *main subject* (P921) with your new book entry, which links the review to the book.

## Optional: your other articles

Your other articles aren't on Wikidata yet. Once your own entry exists, the free tool **Scholia** (scholia.toolforge.org) shows what's linked to your ORCID, and Wikidata's **Author Disambiguator** tool helps match articles to you. You can also ask Claude to prepare a batch file for Wikidata's **QuickStatements** tool, which creates the remaining articles from their DOIs in one go. New accounts may need a few days of ordinary edits before QuickStatements is unlocked.
