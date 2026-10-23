# ============================================================
# Everything on the website comes from this file.
# Edit it, then run:  python3 build.py
# ============================================================
import datetime
UPDATED = datetime.date.today().isoformat()   # "last updated" date, set automatically
SITE = "https://michelletclarke.com"

PERSON = {
    "name": "Michelle T. Clarke",
    "title": "Associate Professor of Government",
    "dept": "Department of Government",
    "inst": "Dartmouth College",
    "inst_url": "https://home.dartmouth.edu",
    "email": "Michelle.T.Clarke@dartmouth.edu",
    "office": "Silsby Hall, Room 219A, HB 6108, Hanover, NH 03755",
    "orcid": "https://orcid.org/0000-0001-5427-2413",
    "scholar": "https://scholar.google.com/citations?user=idY581AAAAAJ",
    "directory": "https://faculty-directory.dartmouth.edu/michelle-t-clarke",
    "cv": SITE + "/cv/michelle-t-clarke-cv.pdf",   # replace cv/michelle-t-clarke-cv.pdf to update
    "field": "Political theory; history of political thought",
    "expertise": ["Machiavelli", "Roman political thought", "Renaissance humanism",
                  "Republicanism", "Cicero", "History of political thought"],
    "education": [
        ("Ph.D. with Distinction, Political Science", "Yale University", 2007, "Dissertation: Machiavelli’s Political Pluralism"),
        ("B.A. in Philosophy and Political Science, summa cum laude", "Tufts University", 2001, None),
    ],
}

SUMMARY = ("Michelle T. Clarke is a political theorist and Associate Professor of Government at "
           "Dartmouth College. She works on the history of political thought, especially Machiavelli, "
           "Roman political thought (above all Cicero), Renaissance humanism, and the foundations of "
           "modern republican ideas.")

QUESTION = ("What happens to our political ideals when we require them to operate "
            "in the world as it actually is?")

BIO = [
    "I am a political theorist specializing in the history of political thought, particularly Machiavelli, Roman political thought, Renaissance humanism, and the foundations of modern political ideas. My research examines how political thinkers inherit, reinterpret, and sometimes deliberately dismantle earlier traditions as they confront changing political realities.",
    "Much of my work asks how Machiavelli transformed the classical and Renaissance republican traditions he inherited. In <cite>Machiavelli’s Florentine Republic</cite>, I argue that Machiavelli exposes the ways in which conventional understandings of virtue, good government, and elite political leadership can obscure the realities of power and undermine republican liberty. My other work on Machiavelli explores his engagement with Roman political thought, Renaissance humanism, rhetoric and historiography, Epicureanism, gender, citizenship, and political virtue.",
    "These projects have led me increasingly backward into Roman political thought and outward into the larger intellectual world of the Renaissance. My research on Cicero explores Roman conceptions of liberty, republican citizenship, social hierarchy, and the competing philosophical traditions that Renaissance thinkers inherited.",
    "Across these projects, I approach the history of political thought as a source of argument about enduring political problems rather than simply a record of past ideas. I am particularly drawn to thinkers who refuse to abstract from conflict, inequality, ambition, contingency, and other uncomfortable realities of political life.",
]

THEMES = [
    ("Machiavelli and the republican tradition",
     "How Machiavelli transformed the classical and Renaissance republican traditions he inherited, and how conventional ideas of virtue and elite leadership can mask power and undermine liberty."),
    ("Roman political thought",
     "Cicero and Roman ideas of liberty, citizenship, social hierarchy, and the philosophical schools (including Epicureanism) that Renaissance thinkers inherited."),
    ("Renaissance humanism",
     "Rhetoric, historiography and the humanist revival of Roman virtue, and a global history of fifteenth-century political thought."),
    ("Method in the history of ideas",
     "The limits of contextualism and the role of interpretive judgment in reading political texts."),
]

BOOK = {
    "title": "Machiavelli’s Florentine Republic",
    "publisher": "Cambridge University Press", "year": 2018,
    "isbn": "9781107125506",
    "url": "https://www.cambridge.org/9781107125506",
    "summary": "Argues that Machiavelli exposes how conventional understandings of virtue, good government, and elite political leadership can obscure the realities of power and undermine republican liberty.",
}

WIP = {
    "title": "The Oxford History of Political Thought: The Renaissance, 1400–1517",
    "publisher": "Oxford University Press", "status": "Under contract",
    "summary": "A global history of political thought in the long fifteenth century that places European humanism and republicanism alongside political thinking about empire, religion, commerce, and authority across a much wider geographical world.",
}

# ------------------------------------------------------------
# PUBLICATIONS: newest first. To add one, copy an existing entry,
# paste it at the top of the list, and change the details.
#   key      a short unique id, e.g. "clarke2027florence"
#   kind     "article", "chapter", "essay" or "reference"
#   ital     (optional) the part of the title to set in italics
#   doi      the DOI without "https://doi.org/", or None
#   summary  two or three sentences in plain language
#   topics   a few keywords
# Then add a matching line to SLUGS at the bottom of this file
# (the web address of the article's own page).
# ------------------------------------------------------------
PUBS = [
    dict(key="clarke2025rabirio", kind="article", year=2025,
         title="Liberty, the People, and Republican Constitutionalism in Cicero’s Pro Rabirio perduellionis reo",
         ital="Pro Rabirio perduellionis reo",
         venue="Polis: The Journal for Ancient Greek and Roman Political Thought", vol="42", no="1", pages="9–28",
         url="https://doi.org/10.1163/20512996-12340461", doi="10.1163/20512996-12340461",
         summary="Reads Cicero’s 63 BCE defense of Gaius Rabirius, accused of treason for his part in killing the tribune Saturninus decades earlier, as a concentrated statement of Cicero’s idea of liberty. Cicero ties libertas less to popular safeguards like provocatio (appeal to the people) and auxilium (tribunician aid) than to the consensus of good citizens, presenting liberty as the calm security of being protected from the morally degenerate and grounding it in the self-regulation of Rome’s ruling elite.",
         topics=["Cicero", "Roman liberty", "Senatus consultum ultimum", "Provocatio", "Elite leadership", "Republicanism"]),
    dict(key="clarke2023boni", kind="article", year=2023,
         title="Boni Gone Bad: Cicero’s Critique of Epicureanism in De Finibus I and II",
         ital="De Finibus",
         venue="Polis: The Journal for Ancient Greek and Roman Political Thought", vol="40", no="1", pages="25–43",
         url="https://doi.org/10.1163/20512996-12340389", doi="10.1163/20512996-12340389",
         summary="Argues that Cicero’s attack on Epicureanism in De Finibus 1 and 2 is aimed at Roman aristocrats, like the dialogue’s spokesman Lucius Torquatus, who believed Epicurean ethics could coexist with traditional Roman virtue. Cicero answers that treating virtue as a means to pleasure corrupts it: Epicureanism reduces politics to utility and borrows the language of honor while emptying it, so that it lacks decorum, the virtue needed to elevate civic life, much as Stoicism lacks the moderation needed to build consensus.",
         topics=["Cicero", "Epicureanism", "Stoicism", "Decorum", "Virtue", "Roman aristocracy"]),
    dict(key="clarke2022curing", kind="article", year=2022,
         title="Curing Virtue: Epicureanism and Erotic Fantasy in Machiavelli’s Mandragola",
         ital="Mandragola",
         venue="Political Theory", vol="50", no="6", pages="913–938",
         url="https://doi.org/10.1177/00905917221095859", doi="10.1177/00905917221095859",
         summary="Asks why Lucrezia, the heroine of Machiavelli’s comedy Mandragola, is called ‘fit to govern a kingdom.’ Tracing the play’s overlooked borrowings from Lucretius’s De rerum natura, which Machiavelli himself transcribed, and Ovid’s Ars amatoria, it argues that Machiavelli accepts Epicurean hedonism but sides with Ovid against Lucretius in rejecting the idea that happiness requires freedom from illusion. Virtue becomes a kind of seductive skill, and Lucrezia, who orders the competing desires of her household, models a princely art of staging and managing fantasy.",
         topics=["Machiavelli", "Mandragola", "Lucretius", "Ovid", "Epicureanism", "Gender", "Princely virtue"]),
    dict(key="clarke2022princes", kind="article", year=2022,
         title="Machiavelli’s Virtuous Princes: Rhetoric, Power, and the Politics of Ironic Historiography",
         venue="Journal of Politics", vol="84", no="1", pages="483–495",
         url="https://doi.org/10.1086/715596", doi="10.1086/715596",
         summary="Contrasts The Prince, where princely power rests on arms and force, with the Discourses on Livy and Florentine Histories, where princes in Rome and Florence rise through moral authority. With Cosimo de’ Medici as the central case, it shows how a reputation for generosity and good works, extended through personal rather than public channels, built networks of obligation that converted popular favor into princely rule, an art subtler than hypocrisy or heroics. Machiavelli exposes it through ironic history-writing in the tradition of Thucydides, Sallust, and Tacitus, teaching republican readers to doubt the moral language that legitimates domination.",
         topics=["Machiavelli", "Cosimo de’ Medici", "Power", "Moral authority", "Rhetoric", "Irony", "Historiography"]),
    dict(key="clarke2022style", kind="essay", year=2022,
         title="Style Is the Man Himself: Eloquence and the Revival of Roman Virtue in Renaissance Humanism",
         venue="The Good Society", vol="31", no="1–2", pages="150–157",
         url="https://scholarlypublishingcollective.org/psup/good-society/article-abstract/31/1-2/150/386690/Style-Is-the-Man-Himself-Eloquence-and-the-Revival",
         doi=None,
         summary="A review essay on James Hankins’s Virtue Politics (2019), which argues that Renaissance humanism was held together by the conviction that a community’s health depends on the character of its rulers. Clarke extends the argument through eloquence: Petrarch, following Cicero and Quintilian, held that good speech both reveals and shapes a well-ordered soul, which is why humanists cared so intensely about getting Latin right. Machiavelli, by contrast, strips Livy of his style in the Discourses, treating eloquence and virtue as separable.",
         topics=["Renaissance humanism", "James Hankins", "Petrarch", "Eloquence", "Cicero", "Machiavelli"]),
    dict(key="clarke2021societas", kind="chapter", year=2021,
         title="Machiavelli: Menace to Societas",
         ital="Societas",
         venue="The Ciceronian Tradition in Political Theory", editors="Daniel J. Kapust and Gary Remer",
         publisher="University of Wisconsin Press", pages="86–102",
         url="https://muse.jhu.edu/book/81818", doi=None,
         summary="Asks whether Machiavelli’s famous reversals of Cicero’s On Duties in The Prince (the lion and the fox, fear over love, cruelty well used) amount to a fundamental break. Cicero, the chapter argues, keeps the honorable (honestum) authoritative but redefines it as the preservation of societas, a social order rooted in natural human sociability and good faith. Machiavelli rejects societas as unsupported by history and politically dangerous, treating every state as a dominion imposed on its subjects, so that The Prince becomes a sustained attempt to think about politics without it.",
         topics=["Machiavelli", "Cicero", "On Duties", "The Prince", "Societas", "Honestum and utile", "Ciceronian tradition"]),
    dict(key="clarke2016bib", kind="reference", year=2016,
         title="Machiavelli’s Political Thought", coauthor="Vickie B. Sullivan",
         venue="Oxford Bibliographies in Political Science",
         url="http://www.oxfordbibliographies.com/view/document/obo-9780199756223/obo-9780199756223-0176.xml",
         doi=None, summary="An annotated research guide to the scholarship on Machiavelli’s political thought.",
         topics=["Machiavelli"]),
    dict(key="clarke2015imagined", kind="article", year=2015,
         title="Machiavelli and the Imagined Rome of Renaissance Humanism",
         venue="History of Political Thought", vol="36", no="3", pages="452–470",
         url="https://www.ingentaconnect.com/content/imp/hpt/2015/00000036/00000003/art00003",
         doi=None,
         summary="Asks why Machiavelli opens the Discourses on Livy by presenting Rome as unexplored territory, after a century of intense humanist study. His aim was to defend Rome as it really was against the Rome imagined by Leonardo Bruni and especially Poggio Bracciolini, whose Oration on Behalf of Venice faulted the turbulent Roman republic. Machiavelli agrees that earlier humanist portraits of Rome were idealized but rejects Poggio’s critique on historical and theoretical grounds: Rome’s tumults sustained a more popular liberty, and humanist hostility to conflict reflected an oligarchic bias. The article challenges Quentin Skinner’s view of the Discourses as a continuation of humanist orthodoxy.",
         topics=["Machiavelli", "Discourses on Livy", "Poggio Bracciolini", "Leonardo Bruni", "Renaissance humanism", "Venice", "Civic conflict", "Quentin Skinner"]),
    dict(key="clarke2014liberty", kind="article", year=2014,
         title="Doing Violence to the Roman Idea of Liberty? Freedom as Bodily Integrity in Roman Political Thought",
         venue="History of Political Thought", vol="35", no="2", pages="211–233",
         url="https://www.ingentaconnect.com/content/imp/hpt/2014/00000035/00000002/art00001",
         doi=None,
         summary="Questions the neo-republican claim, associated with Quentin Skinner and Philip Pettit, that Romans understood liberty as freedom from arbitrary power. Drawing on Roman histories and orations, it argues that libertas meant something narrower and more physical: security from unpredictable, unjustified violence, won through the collective power of the civitas and enjoyed as a legal entitlement. This idea is closer to Judith Shklar’s liberalism of fear, and through her to genuinely neo-Roman writers such as Montaigne and Montesquieu.",
         topics=["Roman liberty", "Neo-republicanism", "Quentin Skinner", "Philip Pettit", "Judith Shklar", "Bodily integrity"]),
    dict(key="clarke2013mythologies", kind="article", year=2013,
         title="The Mythologies of Contextualism: Method and Judgment in Skinner’s Visions of Politics",
         ital="Visions of Politics",
         venue="Political Studies", vol="61", no="4", pages="767–783",
         url="https://doi.org/10.1111/j.1467-9248.2012.01000.x", doi="10.1111/j.1467-9248.2012.01000.x",
         summary="Argues that Quentin Skinner’s contextualism does not deliver the interpretive method it promises. Skinner traces the ‘mythologies’ of textualist reading to its reliance on the interpreter’s judgment and presents contextualism as a discipline that minimizes judgment, yet judgment remains indispensable to his own practice. His added assumption that philosophers write chiefly for strategic, ideological ends produces a mythology of its own, casting philosophical authors as ideologues, though his insistence on recovering an author’s own perspective remains valuable.",
         topics=["Method", "Contextualism", "Quentin Skinner", "Cambridge School", "Interpretation", "Ideology"]),
    dict(key="clarke2013virtues", kind="article", year=2013,
         title="The Virtues of Republican Citizenship in Machiavelli’s Discourses on Livy",
         ital="Discourses on Livy",
         venue="Journal of Politics", vol="75", no="2", pages="317–329",
         url="https://doi.org/10.1017/S0022381613000030", doi="10.1017/S0022381613000030",
         summary="Argues that Machiavelli is skeptical of the Roman social virtues, especially aspects of fides (good faith), because they bound clients to powerful patrons and let elites gather power outside the law. Rereading the classic exemplum of Manlius Torquatus, he shows how personal loyalties endanger republican liberty and sketches a model of citizenship in which ‘unsociable’ traits are central. Republicanism, on this reading, is a politics of limits, and Machiavelli attacks the culture of personal trust from within the republican tradition itself.",
         topics=["Machiavelli", "Citizenship", "Fides", "Patronage", "Manlius Torquatus", "Republicanism"]),
    dict(key="clarke2008bacon", kind="article", year=2008,
         title="Uprooting Nebuchadnezzar’s Tree: Francis Bacon’s Criticism of Machiavellian Imperialism",
         venue="Political Research Quarterly", vol="61", no="3", pages="367–378",
         url="https://doi.org/10.1177/1065912908318845", doi="10.1177/1065912908318845",
         summary="Shows that Francis Bacon, for all his open admiration of Machiavelli, rejects Machiavelli’s model of empire. Guided by philanthropia, the relief of man’s estate, Bacon reverses three Machiavellian images (Solomon for David, the mustard seed for Nebuchadnezzar’s tree, Themistocles for Fabius Maximus) to reject violent conquest, rigid hierarchy, and conservative values in favor of an empire of humanity, prosperity, and cosmopolitanism. Philanthropia, the article argues, is what unifies Bacon’s politics and science, and it anticipates later commercial and liberal justifications of empire.",
         topics=["Francis Bacon", "Machiavelli", "Empire", "Philanthropia", "Glory"]),
    dict(key="clarke2005woman", kind="article", year=2005,
         title="On the Woman Question in Machiavelli",
         venue="Review of Politics", vol="67", no="2", pages="229–255",
         url="https://doi.org/10.1017/S0034670500033507", doi="10.1017/S0034670500033507",
         summary="Against the familiar charge of misogyny, notes that Machiavelli’s major works feature dozens of politically effective and sometimes admirable women, such as Caterina Sforza. To understand them, it reconstructs Machiavelli’s concept of animo, the natural spiritedness that becomes virtù when disciplined by a city’s institutions. Because women stand outside those institutions, they show what political outsiders do with unbridled animo, for better or worse, and Machiavelli’s treatment of them denaturalizes gender norms, so that his works can be read as feminist texts even though he was no feminist.",
         topics=["Machiavelli", "Gender", "Women", "Spiritedness (animo)", "Political outsiders", "Caterina Sforza"]),
]

APPOINTMENTS = [
    ("Associate Professor of Government, Dartmouth College", "2015–present"),
    ("Assistant Professor of Government, Dartmouth College", "2007–2015"),
]

WIP2 = {"title": "Roman Political Thought", "status": "In progress"}

EDITORIAL = [
    "Co-editor (with Jeffrey Church), <cite>Concepts in the History of Political Thought</cite>, book series, Oxford University Press",
    "Co-editor (with Daniel Kapust and John T. Scott), special issue of <cite>Polis</cite> 40, no. 1 (2023), in memory of Rex Stem",
]

TALKS = [
    ("2024", "Inaugural Conference of the Association for the History of Political Thought, University of Texas at Austin"),
    ("2024", "Old Lessons for New Challenges: What the Past Can Teach About AI and New Media, Tocqueville Forum, University of Houston"),
    ("2023", "Keynote, The Reception of Roman Ideas and Practices, European Research Council and University of Padua"),
    ("2023", "The Sources of Machiavelli’s Thought and Works, Villa Vigoni, Menaggio"),
    ("2023", "LeFrak Forum, Michigan State University"),
    ("2019", "Harvard Early Modern Workshop and Political Theory Colloquium"),
    ("2018", "Mandragola at 500, University of Wisconsin–Madison"),
    ("2013", "Conference on the 500th Anniversary of Machiavelli’s Prince, Harvard University"),
]

HONORS = [
    ("2020", "Apgar Award for Innovative Teaching, Dartmouth"),
    ("2019", "Senior Fellowship, Institute for Advanced Study, Central European University (declined)"),
    ("2015", "Elizabeth R. and Robert A. Jeffe 1972 Fellowship"),
    ("2014, 2015", "Walter and Constance Burke Junior Faculty Research Award"),
    ("2013", "Dartmouth Junior Faculty Fellowship"),
]

MEDIA = [("2013", "Interviewed for “Machiavelli: The Prince of Paradox,” <cite>Ideas with Paul Kennedy</cite>, CBC Radio")]

SERVICE = [
    "Co-Chair, APSA Division 1: Political Thought and Philosophy (2025)",
    "AHPT Book Award Committee (2024–2025)",
    "APSA Nominating Committee (2024)",
]

COURSES = ["Political Ideas", "Roman Political Thought", "Machiavelli and Machiavellianism",
           "Classical Political Realism: Power and Statecraft in the Ancient World",
           "Democratic Theory", "Plutarch’s Guide to Leadership",
           "The Political Philosophy of Nietzsche", "The Political Philosophy of J.J. Rousseau", "An Intellectual History of Racism",
           "The Political Theory of Game of Thrones", "Humanities I and II", "Government Honors Program"]

BOOK.update({
    "doi": "10.1017/9781316410776",
    "pages": "xii + 192",
    "description": "Machiavelli’s Florentine Republic reconstructs Machiavelli’s account of the threats facing modern republics from his Florentine Histories, the history of Florence commissioned by the Medici in 1520 and presented to Pope Clement VII in 1525. It argues that Machiavelli narrates the defeat of Florentine republicanism to challenge the leading humanist historians, above all Leonardo Bruni, who had celebrated Florence as a model republic. Against them, Machiavelli portrays a city that wavered between anarchy and princely rule, and reveals that conventional ideas of moral and political virtue were the Medici family’s most effective tools for advancing princely power in a city that wished to be free.",
    "chapters": [
        ("1", "Introduction", "1–26",
         "Introduces the Florentine Histories as Machiavelli’s fullest account of what threatens modern republics. Against the humanist picture of Florence as a republic equal in splendor to Rome, Machiavelli tells the story of a city that never secured a free way of life. The chapter previews the book’s four lines of argument: humanist historiography, the legacy of Roman imperialism, Medici virtue, and political culture."),
        ("2", "Another Republicanism", "27–58",
         "Shows how Bruni’s History of the Florentine People recast Florentine republicanism as rule by a virtuous ‘true nobility’, lending historical credit to Medici power. Machiavelli rejects this account and, following the earlier chroniclers, recovers republicanism as the people’s struggle to keep the grandi in check through laws and institutions. The chapter closes by arguing that Quentin Skinner and the Cambridge School have relayed Bruni’s version of republican history without seeing it as an ideological move."),
        ("3", "Italy after the Inundation", "59–91",
         "Reads the Discourses and the Histories together as an account of why modern Italy could not rebuild free political life. Machiavelli traces this weakness to Roman imperialism, which remade its subjects into dependents, so that Rome is both the model for modern republics and the source of their problems. The underlying disease is a habit of the weak submitting to the strong for protection instead of acting together, not Christianity as such."),
        ("4", "The Questionable Virtues of the Medici", "92–131",
         "Explains how Machiavelli told the truth about his Medici patrons without offending them. Through what the book calls multivocality, writing that carries different meanings for different readers in the manner of Tacitus, his praise of the Medici also exposes their strategy. Where the old nobility had attacked the republic openly and failed, the Medici co-opted it with a reputation for kindness, generosity, and loyalty, building a vast network of clients."),
        ("5", "Republican Virtue, Reconsidered", "132–157",
         "Argues that Machiavelli doubts that traditional virtues serve republican liberty any better than princely power. He is skeptical of the Roman social virtues, especially fides (good faith), because they fostered patronage, ‘sects’, and ‘parties’ that let elites gather power outside the law. This makes Machiavelli an unexpected critic of Roman political culture: Rome fell to the same prosocial virtues that later sustained the Medici party."),
        ("6", "Political Ideas in History", "158–170",
         "Draws the book’s threads together into a new picture of Machiavelli for whom good political theory depends on good history-writing. Without it, political ideas become detached from reality and vulnerable to the interests of the powerful."),
    ],
    "concepts": [
        ("grandi and popolo", "the ‘big men’ and the people, whose conflict Machiavelli treats as defining Florentine republicanism"),
        ("multivocality", "the capacity of one passage to carry different meanings for different readers, which lets Machiavelli praise and criticize the Medici at once"),
        ("fides and clientelism", "Roman good faith, which Machiavelli treats as a vice when it binds clients to powerful patrons"),
        ("effectual truth", "Machiavelli’s attention to how ideas and virtues actually work in politics, behind republican appearances"),
        ("humanist historiography", "the tradition of Bruni and Poggio, which Machiavelli corrects in the Florentine Histories"),
    ],
    "texts": ["Machiavelli, Florentine Histories", "Machiavelli, Discourses on Livy", "Machiavelli, The Prince",
              "Leonardo Bruni, History of the Florentine People", "Poggio Bracciolini, Florentine History",
              "Giovanni Villani, Nuova Cronica", "Livy", "Cicero", "Tacitus"],
    "interlocutors": ["Quentin Skinner", "Hans Baron", "J. G. A. Pocock", "Maurizio Viroli",
                      "John P. McCormick", "Vickie B. Sullivan"],
})

WIP.update({
    "short": "The Oxford History of Political Thought, Volume 5: The Renaissance (1400–1517)",
    "series": "The Oxford History of Political Thought",
    "summary": "A history of political thought in the long fifteenth century, organized by theme. It sets the humanist and republican traditions of Italy and northern Europe alongside political thinking about empire, religion, commerce, and authority across a wider world, with chapters on the Ottoman Empire, the household and gender, wealth and inequality, the origins of racism, and the emerging state system.",
    "description": "The Oxford History of Political Thought, Volume 5: The Renaissance (1400–1517) is a single-authored synthesis of political thought from the late medieval inheritance to the eve of the Reformation, written for Oxford University Press’s multi-volume Oxford History of Political Thought. It is organized by theme rather than by thinker. It retains the familiar story of the period, centered on Italian humanism, its spread north, and major figures such as Bruni, Machiavelli, Guicciardini, Erasmus, and More, while drawing on the past thirty years of scholarship to widen it. The volume also covers the political and intellectual impact of the expanding Ottoman Empire, the emergence of proto-capitalist economies and state-like structures, the gendered character of humanist political ideas, the ties between humanism and mystical traditions, the origins of racism as a modern political ideology, the diversity of fifteenth-century Jewish political thought, and political theorizing in Asia and Africa. Each chapter tells one story about one theme, relates ideas to political, economic, and cultural change, and can be read and taught on its own.",
    "context": "The book is written as the first topically organized survey of Renaissance political thought and an up-to-date synthesis of three decades of scholarship. Earlier general accounts, such as Quentin Skinner’s The Foundations of Modern Political Thought, vol. 1 (1978), the Cambridge Histories of Political Thought edited by J. H. Burns (1988) and by Burns and Mark Goldie (1991), and Janet Coleman’s A History of Political Thought (2000), say little about race, class, gender, Jewish political thought, dialogue with the Ottoman world, or European expansion. It is meant for scholars across political theory, intellectual history, Renaissance studies, classics, religion, law, political economy, gender studies, and the study of race, for undergraduate teaching, and for general readers interested in the history of political ideas.",
    "chapters": [
        ("1", "Introduction",
         "Surveys political theory as it stood in the late fourteenth century: the questions, problems, and key concepts inherited from the Middle Ages. Outlines the main developments of 1400–1517 and how scholarship on the Renaissance has changed over the past thirty years."),
        ("2", "New Worlds",
         "The rediscovery and transmission of ancient texts against a medieval past already rich in classical material. Florentine humanists’ new sense of historical distance fed curiosity about antiquity but raised doubts about whether it could be known or imitated. Humanists also helped invent two identities central to European political thought: ‘modernity’, defined against the ‘dark ages’, and ‘the West’, which Florentines claimed to defend after the fall of Constantinople in 1453. An account of Ottoman political thought corrects humanist stereotypes, and the chapter reviews debates about what humanism was."),
        ("3", "The Politics of Virtue",
         "Why humanists recovered ancient texts: to find wisdom for unstable and corrupt Italian cities. Drawing above all on Cicero, they argued for true nobility (vera nobilitas), meaning rule by merit cultivated through the studia humanitatis rather than by wealth or birth. The chapter follows humanism in Venice, Rome, Naples, Milan, and Mantua, and two radical challenges to it: Christine de Pizan’s rejection of humanist misogyny and of the idea that its ideals belonged to men alone, and Machiavelli’s claim that the humanists misread antiquity, which in fact reveals a tension between moral and political virtue."),
        ("4", "People and Princes",
         "Ideas of legitimate government and the institutions meant to realize them, as Italy stood at a crossroads after its communal republics fractured. Covers humanist debates over signorial versus republican rule; the humanist recovery of Roman law from the medieval commentators and its blending with canon and feudal law, contrasted with English common law; Poland’s Nihil Novi act and the rise of parliament; and popular uprisings outside elite discourse, such as Jack Cade’s Rebellion, the Carinthian Peasants’ Revolt, and the Udine carnival massacre, which show how ‘the people’ was defined."),
        ("5", "God, the Church, and Prophetic Power",
         "How humanism drew on and contested theological claims to political authority. Italian humanism generally assumed that classical culture and Christianity were continuous, and northern humanists such as Reuchlin, Hutten, Erasmus, and More put classical learning to work for Christian renewal, using the figure of Christ, as in Erasmus’s Paraphrases, against corrupt institutions, including the Church. The chapter also covers conciliarism, which drew on Roman law to limit papal power after the Great Schism, and the Lollards, Hussites, Waldensians, and Taborites, who held that the church was the community of believers led by Christ alone."),
        ("6", "Love, Friendship, and Family",
         "How Renaissance writers imagined the bonds of civic community and its links to marriage, friendship, and family. Christian humanists replaced medieval civic ritual with the imitation of Christ, while others relied on Aristotelian and Ciceronian accounts of natural sociability and friendship; Bruni’s translation of politike as civitas shows the eclipse of the medieval idea of communitas. The household is treated as part of the political realm, with attention to humanist writing on the oikos, the civic values that marriage was thought to embody, and the patriarchal and heteronormative assumptions behind Renaissance political thought."),
        ("7", "Wealth and Inequality",
         "Economic thought in a Europe reshaped by a rising merchant class. Humanist writing on household management (oikonomia) tried to reconcile ancient ideals with the values of its merchant patrons, balancing glory against profit and praising honesty, frugality, and foresight alongside liberality and magnificence, with some cautious defenses of avarice. The chapter then reconstructs debates over whether economic inequality is a political problem, with wealth defended as a sign of merit or attacked as a threat to liberty, and whether it should be regulated, as in disputes over progressive taxation such as the Florentine catasto."),
        ("8", "Reimagining the International Order",
         "The fifteenth-century foundations of the sovereign state in Italy, Spain, England, and above all France, in a multipolar Europe before Habsburg consolidation in 1519. Topics include sovereignty in humanist legal theory, the balance of power, debates over knightly castes, citizen militias, and mercenary armies, early ideas of reason of state, the justification and conduct of war, old and new ideas of empire, and the conditions of true peace."),
        ("9", "The Construction of Race",
         "Argues that the Renaissance saw the birth of racism, understood as belief in a group’s innate and permanent superiority, as distinct from older xenophobia. The chapter traces the racialization of Jewish identity in fifteenth-century Spain, where suspicion of conversos came to be expressed in terms of blood and the doctrine of limpieza de sangre (purity of blood). It then follows anti-Black racism tied to the Arab enslavement of Black Africans, which grew with Ottoman expansion and with papal bans on selling Christian Eastern Europeans, and the ‘Curse of Ham’ reading that reached Christian Europe through Muslim cultural and commercial contact. Classical sources supported slavery, but its racialization had more varied origins."),
        ("10", "Conclusion",
         "Summarizes the volume’s main developments, stresses how selective and creative Renaissance uses of classical ideas were, and leads into the early modern period."),
    ],
    "concepts": [
        ("vera nobilitas", "true nobility: the humanist claim that merit and virtue, not wealth or birth, qualify people to rule"),
        ("studia humanitatis", "the humanist curriculum meant to form virtuous citizens and rulers"),
        ("signoria and republic", "the rival forms of government debated in early fifteenth-century Italy"),
        ("conciliarism", "the movement to limit papal authority through church councils, drawing on Roman law"),
        ("oikonomia", "household management, the frame for humanist thinking about property, wealth, and family"),
        ("catasto", "the Florentine tax assessment, a focus of debate over taxation and inequality"),
        ("limpieza de sangre", "the Spanish doctrine of purity of blood, an early legal form of racial thinking"),
        ("reason of state and balance of power", "early ideas of statecraft and international order"),
    ],
})

HERO = [
    "I’m a political theorist who studies how political ideas are inherited, reworked, and sometimes deliberately dismantled. Most of my work centers on Machiavelli and the traditions he drew on and transformed: the Roman republic, Cicero, and the humanists of Renaissance Florence.",
    "My first book, <a href=\"book.html\"><cite>Machiavelli’s Florentine Republic</cite></a> (Cambridge, 2018), reads his <cite>Florentine Histories</cite> as a warning about how the language of virtue and good leadership can disguise the growth of princely power. I have also written on Roman liberty, Epicureanism, rhetoric and irony, gender, citizenship, and the methods of intellectual history. I’m now writing <a href=\"renaissance.html\">the Renaissance volume</a> of <cite>The Oxford History of Political Thought</cite>, a history of political ideas from 1400 to 1517 that reaches from Florence to the Ottoman Empire.",
    "At Dartmouth I teach courses ranging from Roman political thought and Machiavelli to Nietzsche, democratic theory, and the intellectual history of racism.",
]

TOPIC_IMAGES = [
    ("machiavelli", "Machiavelli", "Santi di Tito, <cite>Portrait of Niccolò Machiavelli</cite>, late 16th c.",
     "Santi di Tito’s portrait of Niccolò Machiavelli, in a black robe with a red collar"),
    ("cicero", "Cicero &amp; Rome", "<cite>Bust of the Ludovisi Cicero</cite>, Cleveland Museum of Art",
     "Dark marble bust of Cicero in a draped toga"),
    ("florence", "Florence", "After the <cite>Pianta della Catena</cite>, c. 1470",
     "Fifteenth-century bird’s-eye view of Florence, with the cathedral dome and the Arno"),
    ("humanism", "Humanism", "Vittore Carpaccio, <cite>St. Augustine in His Study</cite>, 1502",
     "Carpaccio’s painting of a scholar at his desk in a study lined with books and instruments"),
    ("lucretius", "Epicureanism", "Lucretius, <cite>De rerum natura</cite>, manuscript for Sixtus IV, 1483",
     "Illuminated opening page of a Renaissance manuscript of Lucretius’s De rerum natura"),
    ("bacon", "Bacon &amp; empire", "Paul van Somer, <cite>Francis Bacon</cite>, 1617",
     "Portrait of Francis Bacon in a tall black hat and white ruff"),
]

BOOK["praise"] = [
    ("… this is by far the best book-length treatment in English of Machiavelli’s longest work. Intelligent, erudite, and spirited, it should command the attention of diverse scholars and is sure to help revive interest in Machiavelli’s Florentine Histories.",
     "Christopher Lynch", "The Review of Politics"),
    ("Machiavelli’s Florentine Republic accomplishes much more than repairing the gap in the Anglophone scholarship on Machiavelli’s notoriously elusive Florentine Histories. This clear-sighted, savvy, and compelling interpretation deserves to be read by all interested in republicanism – its history, its meaning, and its ramifications. Clarke’s interpretation is sure to change the course of the scholarly conversation as it establishes Machiavelli’s critical evaluation of his city’s republican government and elucidates his understanding that the modern political problem derives from Rome’s ancient dominion.",
     "Vickie Sullivan", "Tufts University"),
    ("Machiavelli’s Florentine Histories is the last of his major works to receive intensive scholarly attention. Because it is a history, his voice is more muted than in his more explicitly theoretical works and there is a seemingly overwhelming mass of factual detail. Clarke has made a major step forward in deciphering the argument of this difficult book, particularly by bringing out the differences between Machiavelli and his civic humanist predecessors, Leonardo Bruni and Coluccio Salutati.",
     "Catherine H. Zuckert", "University of Notre Dame"),
    ("Michelle Clarke’s illuminating study of the neglected Florentine Histories reestablishes Machiavelli’s republican credentials in a new light. She situates the Histories between Machiavelli’s two better known works and gives us a new appreciation of his political theory as a whole. This excellent book offers a fresh and refreshingly independent approach to Machiavelli and the study of modern political thought.",
     "John T. Scott", "University of California, Davis"),
    ("Michelle Clarke’s Machiavelli’s Florentine Republic advances our understanding of Machiavelli in distinctive ways. Not only does Clarke carefully and persuasively show how Machiavelli rejected the historiography of predecessors like Salutati, but she also shows us a Machiavelli more skeptical of Rome – and its imperial project – than he is often made out to be. The clear and crisply written book deeply engages with Machiavelli’s context, and makes important and timely contribution to key debates in Machiavelli scholarship. Readers of Machiavelli will benefit greatly from this study.",
     "Daniel Kapust", "University of Wisconsin–Madison"),
    ("A rich scholarly literature has studied Machiavelli’s paramount role within modern republican political theory. Only a few works have reconstructed Machiavelli’s reflections on the Florentine republican experience that he contributed to shape. Michelle T. Clarke’s book offers us an excellent, elegantly written, account of Machiavelli’s considerations on the weaknesses of the Florentine republican elite that paved the way to the Medicean regime. Her work enriches our understanding of the history of republicanism and invites us to meditate from a fresh perspective on the weaknesses of the republics of our times.",
     "Maurizio Viroli", "Princeton University"),
]
BOOK["pull"] = ("By far the best book-length treatment in English of Machiavelli’s longest work.", "Christopher Lynch, The Review of Politics")

# Web address (slug) for each article's own page: articles/<slug>.html
SLUGS = {
    "clarke2025rabirio": "cicero-pro-rabirio-liberty",
    "clarke2023boni": "cicero-de-finibus-epicureanism",
    "clarke2022curing": "machiavelli-mandragola-curing-virtue",
    "clarke2022princes": "machiavelli-virtuous-princes",
    "clarke2022style": "style-is-the-man-himself-humanism",
    "clarke2021societas": "machiavelli-menace-to-societas",
    "clarke2016bib": "machiavelli-political-thought-bibliography",
    "clarke2015imagined": "machiavelli-imagined-rome-humanism",
    "clarke2014liberty": "roman-liberty-bodily-integrity",
    "clarke2013mythologies": "mythologies-of-contextualism-skinner",
    "clarke2013virtues": "machiavelli-republican-citizenship",
    "clarke2008bacon": "bacon-machiavellian-imperialism",
    "clarke2005woman": "woman-question-in-machiavelli",
}

# ------------------------------------------------------------
# KEY ARGUMENTS: one-sentence claims shown on the homepage and
# given to AI tools. Each source is (label, page on this site).
# ------------------------------------------------------------
KEY_ARGS = [
    ("In Machiavelli’s Florentine Histories, the language of virtue, not force, is what carried the Medici to princely power in a republic: generosity, loyalty, and good works built networks of obligation that hollowed out Florentine liberty.",
     [("Machiavelli’s Florentine Republic", "book.html"), ("Machiavelli’s Virtuous Princes", "articles/machiavelli-virtuous-princes.html")]),
    ("For Machiavelli, the Roman virtue of good faith (fides) was a political vice, because personal loyalty fed patronage and let elites gather power outside the law.",
     [("The Virtues of Republican Citizenship", "articles/machiavelli-republican-citizenship.html")]),
    ("Machiavelli was a sharper critic of Renaissance humanism than the Cambridge School allows: humanist portraits of Rome and Florence quietly served oligarchic rule, and he wrote against them.",
     [("Machiavelli and the Imagined Rome of Renaissance Humanism", "articles/machiavelli-imagined-rome-humanism.html"), ("Machiavelli’s Florentine Republic, ch. 2", "book.html")]),
    ("Machiavelli’s break with Cicero goes deeper than tactics: he rejects Cicero’s idea of a natural human societas and treats every state as a dominion imposed on its subjects.",
     [("Machiavelli: Menace to Societas", "articles/machiavelli-menace-to-societas.html")]),
    ("Romans understood liberty less as freedom from domination than as security from arbitrary violence, a view closer to Judith Shklar than to Quentin Skinner.",
     [("Doing Violence to the Roman Idea of Liberty?", "articles/roman-liberty-bodily-integrity.html")]),
    ("Cicero grounds liberty in the consensus of good citizens and the self-regulation of the ruling elite more than in popular safeguards like the right of appeal.",
     [("Liberty, the People, and Republican Constitutionalism", "articles/cicero-pro-rabirio-liberty.html")]),
]
