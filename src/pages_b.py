from engine import *
from content_core import *
from pages_a import report_mock

SCOPED = "Scoped to your business"

@page("/services/", "Services | MarvelUs",
      "Three practical services from MarvelUs: AI digital support by chat or voice, SEO, and the paid Business Assessment (AI Readiness).")
def services():
    h = [hero("Services", "Three ways MarvelUs helps. One plain approach to all of them.",
        "We would rather do a few things well than sell you everything. Each service stands on its own, and each one is built around what your business really spends its time on.",
        buy_btn() + book_btn(), crumb=[("Home", "/"), ("Services", "/services/")])]
    good = {"digital-support": "Businesses with the same questions arriving all day, or enquiries arriving after hours.",
            "seo": "Businesses that rely on local or online search and are not showing up where they should.",
            "business-assessment": "Owners who want to know where to start before they spend on anything."}
    longer = {"digital-support": "An AI assistant that answers for your business, on your website, by text or by phone. It can serve your customers, your own staff, or both.",
              "seo": "Search work that brings the right people to you and gives them an easy way to act.",
              "business-assessment": f"A phone call of {CALL} and a written report with a score out of 100, ranked opportunities and dollar costs."}
    cs = []
    for o in OFFERS:
        cs.append(f'<article class="card card--offer"><p class="tag">{esc(o["tag"])}</p><h2 class="h3">{esc(o["name"])}</h2><p class="card__price">{esc(o["price"])}</p><p>{esc(longer[o["id"]])}</p><p><strong>Good for:</strong> {esc(good[o["id"]])}</p><p class="card__link"><a class="text-link text-link--arrow" href="{o["url"]}">Read more</a></p></article>')
    h.append(section(f'<div class="cards cards--3 cards--equal">{"".join(cs)}</div>'))
    h.append(section('<h2>How we choose what to do first</h2>' + numbered([
        ("Look.", "We start with how the work really runs, not with a tool."),
        ("Count.", "We put hours and dollars on what we find."),
        ("Rank.", "The biggest, safest fix goes first."),
        ("Prove.", "We measure the result against the number we started with.")]), "section--dim"))
    h.append(section('<h2>When we will tell you not to buy.</h2><p class="lede">If a simpler process, a setting in your current software or a conversation with your team will do the job, we will say so. If the numbers do not justify a project, we will say that too. A smaller honest job beats a bigger one that disappoints you.</p>'))
    h.append(section(f'<h2>Proof</h2><p>{ph("one real result per service (digital support, SEO, assessment), each with client permission and how it was measured. Hide this block until at least one is ready", "proof")}</p>', "section--dim"))
    h.append(cta_band("Not sure which one fits?", "Try the one minute preview and we will point you to it.", [quiz_btn(), book_btn()]))
    return "\n".join(h)

DS_FAQ = [
 ("Will customers know it is AI?", "Yes. It says so at the start. People are fine with it when it is quick and useful, and when they can reach a person."),
 ("What if it gets something wrong?", "We test it hard first, limit it to what you have approved, and review conversations after launch. When it is unsure it hands over instead of guessing."),
 ("Does it need our customer data?", "Only what the job needs. We agree what it can see before launch. [[PH:legal|confirm data handling and where data is stored]]"),
 ("Can it work for staff only?", "Yes. Many businesses start there because it carries less risk and shows quick value."),
 ("What does it cost?", "It is scoped to your business, so there is no list price. [Book a call](/book/) and we will talk through what it would take."),
]

@page("/services/digital-support/", "AI digital support by chat or voice | MarvelUs",
      "An AI assistant that answers your customers or your staff by chat or phone, using your information and handing over to a person when it should.",
      schema=[lambda: service_ld("Digital support (AI chat or voice)", "An AI assistant that answers customers or staff by chat or phone, scoped to the business.", "/services/digital-support/")])
def digital_support():
    h = [hero("Digital support", "An assistant that answers when your team cannot.",
        "Many of the questions your business gets are the same ones, again and again. Opening hours, pricing, how to book, where an order is, how a process works. A digital support assistant answers them by chat on your site or by phone, so your team can spend its time on the harder things. It can face customers, face your own staff, or do both.",
        buy_btn("Get the assessment first") + book_btn(), crumb=[("Home", "/"), ("Services", "/services/"), ("Digital support", "/services/digital-support/")])]
    h.append(section('<h2>What it can do</h2>' + cards([
        ("Answer common questions", "From your own material, in your own wording."),
        ("Take messages and requests", "And pass them to the right person with the details filled in."),
        ("Book and reschedule", "Where your booking system allows it. [[PH:ops|confirm which booking systems MarvelUs integrates with]]"),
        ("Work after hours", "So enquiries are not left until morning."),
        ("Support your own staff", "With answers to \"how do we do this here\" questions."),
        ("Hand over to a person", "When a customer is upset, when it is unsure, or when the matter is too important to guess.")]), "section--dim"))
    h.append(section('''<h2>Chat or voice</h2><div class="cards cards--2 cards--equal">
<article class="card"><h3>Chat</h3><p>Sits on your website or inside the tools you already use. Good for written questions and for people who want a record.</p></article>
<article class="card"><h3>Voice</h3><p>Answers the phone, takes the details and routes the call. Good for trades, clinics and anywhere the phone rings while hands are busy.</p></article></div>
<p class="small muted">Voice assistants always say they are AI at the start of a call. [[PH:legal|confirm disclosure wording and Australian call recording and consent requirements with a legal adviser]]</p>'''))
    h.append(section('<h2>How it is set up</h2>' + numbered([
        ("Map the questions.", "We list what people really ask and what the right answers are."),
        ("Write the knowledge.", "We build the answers from your material and have you check every one."),
        ("Test hard.", "We try awkward, rude and odd questions before anyone real sees it."),
        ("Go live and watch.", "We read the conversations, fix gaps and report what it handled.")]) +
        f'<p class="small muted">{ph("typical build time and ongoing support terms", "pricing")}</p>', "section--dim"))
    h.append(section('<h2>What stays with a person</h2><ul class="ticks"><li>Anything that commits you to a price or a date.</li><li>Complaints, safety concerns and distressed customers.</li><li>Anything the assistant is not sure about. It says so and hands over.</li></ul>'))
    h.append(section(f'<h2>What it costs</h2><p class="lede card__price">{SCOPED}</p><p>Digital support is scoped to your business. We do not publish a price because the size of the job decides it. Book a call and we will say what it would involve.</p><div class="btn-row">{book_btn("Book a call", "primary")}</div>', "section--dim"))
    h.append(section(f'<h2>Proof</h2><p>{ph("one real digital support result with client permission, including how conversations or hours were measured", "proof")}</p>'))
    h.append(faq(DS_FAQ, "Questions about digital support"))
    h.append(cta_band("See what a support assistant could take off your team.", None, [buy_btn(), book_btn()]))
    return "\n".join(h)

SEO_FAQ = [
 ("How long does SEO take?", "Small fixes can show in weeks. Competitive terms often take months. We show you what moved at each stage."),
 ("Do you work outside Melbourne?", "Yes. MarvelUs is based in Melbourne and delivers remotely, anywhere. [[PH:ops|confirm any market limits]]"),
 ("Can I start with the assessment?", "Yes. It often shows whether search is where your next dollar should go."),
 ("What does it cost?", "It is scoped to your business, so there is no list price. [Book a call](/book/) and we will talk through what it would take."),
]

@page("/services/seo/", "SEO for Melbourne and Australian businesses | MarvelUs",
      "Search work that gets the right people to your site and helps them act. Fixes, content and reporting, explained in plain terms.",
      schema=[lambda: service_ld("SEO", "Search engine optimisation: technical fixes, content, local search and reporting, scoped to the business.", "/services/seo/")])
def seo():
    h = [hero("SEO", "Be easy to find, and easy to choose.",
        "Being found is only half of it. The visit has to lead somewhere. Our SEO work starts with what people search for when they need what you sell, then makes sure your site answers that clearly and loads fast, and that a visitor can easily take the next step.",
        book_btn("Book a call", "primary") + buy_btn("Get the assessment", "secondary"), crumb=[("Home", "/"), ("Services", "/services/"), ("SEO", "/services/seo/")])]
    h.append(section('<h2>What is included</h2>' + cards([
        ("Technical health", "We find and fix what stops search engines reading your site."),
        ("Search research", "We find the terms your customers really use."),
        ("Page content", "We write or rewrite the pages that matter most."),
        ("Local search", "For Melbourne and Australian businesses, your Google Business listing and local pages. [[PH:ops|confirm local SEO scope]]"),
        ("Answers for AI search", "Structured, clear answers that AI assistants can quote and link to."),
        ("Reporting", "A short, plain report each month: what we did, what moved, what is next.")]), "section--dim"))
    h.append(section('<h2>Our approach</h2>' + numbered([
        ("Audit.", "What is working, what is broken and what is missing."),
        ("Plan.", "The pages and fixes that matter most, in order."),
        ("Do.", "We make the changes or hand your team a clear list."),
        ("Report.", "Rankings, visits and enquiries compared with where we began.")])))
    h.append(section('<h2>What we do not do</h2><ul class="ticks"><li>We do not promise page one or a ranking by a date. No one honest can.</li><li>We do not buy links or use tricks that put your site at risk.</li></ul>', "section--dim"))
    h.append(section(f'<h2>What it costs</h2><p class="lede card__price">{SCOPED}</p><p>SEO is scoped to your business. We do not publish a price because the size of the site and the market decide it. Book a call and we will say what it would involve.</p><div class="btn-row">{book_btn("Book a call", "primary")}</div>'))
    h.append(section(f'<h2>Proof</h2><p>{ph("one real SEO result with client permission, including the measure and the time period", "proof")}</p>', "section--dim"))
    h.append(faq(SEO_FAQ, "Questions about SEO"))
    h.append(cta_band("Want to know where you stand in search?", None, [book_btn("Book a call", "primary"), buy_btn("Get the assessment", "secondary")]))
    return "\n".join(h)

@page("/results/", "Results | MarvelUs", "What clients have gained working with MarvelUs. Real projects, with how each result was measured.")
def results():
    h = [hero("Results", "What changed for the businesses we have worked with.",
        "Every number on this page will come from a client, with their permission, and will say how it was measured. We do not publish a figure we cannot explain.",
        buy_btn() + book_btn(), crumb=[("Home", "/"), ("Results", "/results/")])]
    h.append(section(f'<h2>Headline figures</h2><p>{ph("up to four verified totals, for example hours returned a week or enquiries answered. Each needs a source on file, a date range and a line on how it was measured. Do not show a figure that cannot be explained in a sentence", "proof")}</p>', "section--dim"))
    h.append(section(f'<h2>Featured result</h2><p>{ph("one featured client story with a photo, a quote, three outcome figures and a link to the full case study. Needs client consent", "proof")}</p>'))
    h.append(section(f'''<h2>Results by service</h2><div class="cards cards--3 cards--equal">
<article class="card"><h3>Digital support</h3><p>{ph("real result cards", "proof")}</p></article>
<article class="card"><h3>SEO</h3><p>{ph("real result cards", "proof")}</p></article>
<article class="card"><h3>Business Assessment</h3><p>{ph("real result cards, for example what the report found and what the owner did next", "proof")}</p></article></div>''', "section--dim"))
    h.append(section(f'''<div class="read"><h2>How we count.</h2>
<p>We take a measurement before we start and again after. We count hours saved only if they led to something you can see: a cost removed, a hire avoided or demand you served that was already waiting. One of those per workflow, never two. If the time just went back into the day with no visible change, we record that as no saving. {ph("confirm this measurement method matches what MarvelUs actually does", "ops")}</p></div>'''))
    h.append(section('<div class="notice"><p>We are adding client results as we get written permission. In the meantime, see <a class="text-link" href="/assessment/">how the assessment works</a>, or <a class="text-link" href="/book/">book a call</a> and ask us anything.</p></div>', "section--dim"))
    h.append(cta_band("Want a result like this for your business?"))
    return "\n".join(h)

CHIPS = ["Digital support", "SEO", "Business Assessment", "Trades", "Hospitality", "Professional services", "Health", "Retail"]

@page("/case-studies/", "Case studies | MarvelUs", "Client stories from MarvelUs, with the problem, what we did and how the result was measured.")
def case_studies():
    h = [hero("Case studies", "Client stories", "Short, factual accounts of what we did, what changed and how we know.", "", crumb=[("Home", "/"), ("Case studies", "/case-studies/")])]
    chips = '<button type="button" class="chip" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="chip" data-filter="{slug(c)}" aria-pressed="false">{esc(c)}</button>' for c in CHIPS)
    cards_html = ""
    for i, (svc, ind) in enumerate([("Digital support", "Trades"), ("SEO", "Retail"), ("Business Assessment", "Professional services")], 1):
        cards_html += (f'<article class="card card--proof" data-tags="{slug(svc)} {slug(ind)}"><p class="tag">{esc(ind)} · {esc(svc)}</p>'
                       f'<h3>{ph(f"case study {i}: one-line outcome, client name only with permission", "proof")}</h3>'
                       f'<p class="card__link"><span class="muted">Read the story (when published)</span></p></article>')
    h.append(section(f'''<div class="chips" role="group" aria-label="Filter case studies">{chips}</div>
<div class="cards cards--3 cards--equal" id="cs-grid">{cards_html}</div>
<p class="notice" id="cs-empty" hidden>No case studies match that combination yet. <button type="button" class="linklike" data-filter="all">Show all</button></p>
<p class="notice">Case studies are on the way. We publish each one only with the client's written permission. The cards above are placeholders, not clients.</p>'''))
    h.append(section('<p class="small"><a class="text-link text-link--arrow" href="/case-studies/template/">See the case study template</a></p>', "section--tight"))
    h.append(cta_band("Want to find your own?", None, [buy_btn(), book_btn()]))
    return "\n".join(h)

@page("/case-studies/template/", "Case study template | MarvelUs", "The template every MarvelUs case study follows, with the client approvals needed before one is published.")
def case_template():
    h = [hero("Case study · [Industry] · [Service]", "Case study template, not a client story",
              "This page shows the layout every real case study will use. Nothing on it is a real client or result.",
              "", crumb=[("Home", "/"), ("Case studies", "/case-studies/"), ("Template", "/case-studies/template/")])]
    h.append(section(f'''<div class="layout-side"><div class="read">
<p class="stamp">Template. Not a real client.</p>
<h2>Outcome figures (up to three)</h2><p>{ph("figure, label and how it was measured", "proof")}</p>
<h2>The situation</h2><p>{ph("what was happening before, in the client's words", "proof")}</p>
<h2>What we found</h2><p>{ph("the cause, with the measurement", "proof")}</p>
<h2>What we did</h2><p>{ph("the work, step by step, including what we left for people to do", "proof")}</p>
<h2>What changed</h2><p>{ph("figures before and after, how they were measured, and what was not achieved", "proof")}</p>
<h2>In their words</h2><p>{ph("real client quote with approval", "proof")}</p>
<h2>What it cost</h2><p>{ph("only if the client agrees", "proof")}</p></div>
<aside class="side-card" aria-label="Case study facts"><h2 class="h3">Client facts</h2><dl class="kv"><dt>Client</dt><dd>{ph("only if approved", "proof")}</dd><dt>Industry</dt><dd>{ph("approved field", "proof")}</dd><dt>Size</dt><dd>{ph("approved field", "proof")}</dd><dt>Service</dt><dd>{ph("approved field", "proof")}</dd><dt>Time to result</dt><dd>{ph("approved field", "proof")}</dd><dt>Location</dt><dd>{ph("approved field", "proof")}</dd></dl></aside></div>'''))
    h.append(section('<h2>Needed from each client before publishing</h2><ul class="ticks"><li>Written permission.</li><li>An approved quote.</li><li>Approved figures.</li><li>A named contact for checking.</li><li>A logo or photo release.</li></ul>', "section--dim"))
    h.append(cta_band("Want to find your own?", None, [buy_btn(), book_btn()]))
    return "\n".join(h)

PRICING_FAQ = [
 ("Why is the assessment paid?", "Because the report is custom, and a paid piece of work gets our full attention. It is a fixed price so there are no surprises."),
 ("Is GST included?", "No. The price is $1,000 AUD plus GST. We write it as $1,000 + GST."),
 ("What currency are prices in?", "Australian dollars."),
 ("How do I pay?", "By card at secure checkout. [[PH:ops|confirm payment provider wording and how GST is shown at checkout]]"),
 ("What does digital support or SEO cost?", "They are scoped to your business, so there is no list price. [Book a call](/book/) and we will tell you what it would take."),
]

@page("/pricing/", "Pricing | MarvelUs", f"What MarvelUs costs. The Business Assessment is {PRICE_LONG}. Digital support and SEO are scoped to your business.",
      schema=[lambda: service_ld("Business Assessment (AI Readiness)", "Fixed price phone intake and written report.", "/pricing/", 1000)])
def pricing():
    h = [hero("Pricing", "Clear prices, and a clear place to start.",
        "Start with the Business Assessment at a fixed price. If you want help with anything it finds, we scope that separately and in writing, so you know the cost before you agree to it.",
        "", crumb=[("Home", "/"), ("Pricing", "/pricing/")])]
    h.append(section(f'''<div class="cards cards--3 cards--equal">
<article class="card"><p class="tag">Know where to start</p><h2 class="h3">Business Assessment (AI Readiness)</h2><p class="card__price">{PRICE_LONG}</p>
<ul class="ticks"><li>A phone intake call of {CALL}</li><li>Written report with a 0 to 100 score</li><li>Ranked opportunities</li><li>Costs worked out in dollars</li><li>Call transcript</li></ul>
<p class="small muted">GST is not included in the $1,000.</p><div class="btn-row">{buy_btn()}</div></article>
<article class="card"><p class="tag">Chat or voice</p><h2 class="h3">Digital support</h2><p class="card__price">{SCOPED}</p>
<ul class="ticks"><li>Question mapping and knowledge build</li><li>Testing</li><li>Go-live and review</li><li>Ongoing reporting</li></ul><div class="btn-row">{book_btn("Book a call", "primary")}</div></article>
<article class="card"><p class="tag">Be found</p><h2 class="h3">SEO</h2><p class="card__price">{SCOPED}</p>
<ul class="ticks"><li>Audit and plan</li><li>Technical fixes and content</li><li>Monthly reporting</li></ul><div class="btn-row">{book_btn("Book a call", "primary")}</div></article></div>''', aria="x"))
    h.append(section('<h2>What drives the cost</h2><ul class="ticks"><li>The size of the job.</li><li>How many systems we connect to.</li><li>How much of the work your team does itself.</li><li>Whether you need it once or ongoing.</li></ul>', "section--dim"))
    h.append(faq(PRICING_FAQ, "Pricing questions"))
    h.append(cta_band("Start with the assessment."))
    return "\n".join(h).replace(' aria-labelledby="x"', "")

MEL_FAQ = [
 ("How much does AI consulting cost in Melbourne?", f"The Business Assessment is {PRICE_LONG}. Other work is scoped to your business."),
 ("Do you come to my office?", "Most work is done remotely. [[PH:ops|confirm any in-person availability in Melbourne]]"),
 ("Can you help a business outside Melbourne?", "Yes. Most of the work is done remotely, anywhere."),
 ("Is my data kept in Australia?", "[[PH:legal|confirm data location and storage]]"),
]

@page("/ai-consulting-melbourne/", "AI consulting in Melbourne | MarvelUs",
      "MarvelUs is a Melbourne business helping businesses with AI digital support, SEO and a scored Business Assessment, delivered remotely.",
      schema=[lambda: service_ld("AI consulting in Melbourne", "AI digital support, SEO and a scored Business Assessment from a Melbourne business, delivered remotely.", "/ai-consulting-melbourne/")])
def melbourne():
    h = [hero("Melbourne, Victoria", "AI help for Melbourne businesses that want their time back.",
        "A Melbourne team that explains things plainly and shows the cost of each fix.", buy_btn() + book_btn(),
        crumb=[("Home", "/"), ("Melbourne", "/ai-consulting-melbourne/")])]
    h.append(section('''<div class="read"><h2>What does an AI consultant in Melbourne do?</h2>
<p>We start by looking at how your business really runs: how enquiries come in, how work is delivered and which tasks eat the week.</p>
<p>We put numbers on what we find, so you can see which fixes are worth doing.</p>
<p>Then we help with the ones you choose, whether that is a digital support assistant, search work or something simpler.</p></div>'''))
    h.append(section(f'<h2>What has this done for Melbourne businesses?</h2><p>{ph("up to four real local cards with a place tag and one real outcome each, with client permission. Hide this section until real", "proof")}</p>', "section--dim"))
    h.append(section('''<h2>How do you choose an AI consultant?</h2>
<div class="table-wrap"><table><caption class="sr-only">What to look for, by need</caption><thead><tr><th scope="col">If you need</th><th scope="col">Look for</th><th scope="col">Why</th></tr></thead><tbody>
<tr><td>To know where to start</td><td>A fixed-price assessment</td><td>You get a plan with numbers before any big spend.</td></tr>
<tr><td>Customers waiting too long for answers</td><td>A digital support build with handover rules</td><td>Fast replies with a person for the hard cases.</td></tr>
<tr><td>Your site to bring in enquiries</td><td>Search work with plain monthly reports</td><td>You can see what changed.</td></tr>
<tr><td>To be sure AI fits</td><td>Someone willing to say no</td><td>A smaller honest job is better than a big one that disappoints.</td></tr></tbody></table></div>
<p><a class="text-link text-link--arrow" href="/insights/outlines/#how-to-choose-an-ai-consultant-in-melbourne-and-australia">Longer guide (outline, not yet written)</a></p>'''))
    h.append(section(f'<h2>Where do you work?</h2><p class="lede">MarvelUs is based in Melbourne and works remotely with businesses across Victoria, Australia and beyond. Calls and reports are done remotely, so where you are makes no difference.</p><p>{ph("add suburbs or regions only if you actually serve them in person", "ops")}</p>', "section--dim"))
    h.append(faq(MEL_FAQ, "Questions about AI consulting in Melbourne"))
    h.append(cta_band("Ready to start?"))
    return "\n".join(h)

@page("/about/", "About MarvelUs", "MarvelUs is a Melbourne business helping businesses use AI where it earns its place.")
def about():
    h = [hero("About", "A Melbourne business built on one idea. Show the numbers first.",
        "Many business owners are being sold AI without being shown what it would do for them. We started MarvelUs to do it the other way round. Look at the work, count the cost and only then talk about tools.",
        "", crumb=[("Home", "/"), ("About", "/about/")])]
    h.append(section(f'<div class="media-slot media-slot--wide" role="img" aria-label="Placeholder for a team or workspace photo">{ph("real photo of the team or workspace, only with approval. No names unless approved", "media")}</div>'))
    h.append(section('<h2>What we do</h2>' + cards([("Digital support", "Assistants that answer by chat or phone.", ("Read more", "/services/digital-support/")),
        ("SEO", "Being found by the right people.", ("Read more", "/services/seo/")),
        ("Business Assessment", "A scored report that shows where to start.", ("Read more", "/assessment/"))], "cards cards--3 cards--equal"), "section--dim"))
    h.append(section(f'<h2>Who you will deal with.</h2><p>{ph("a short, honest description of the MarvelUs team, approved before launch. No individual is named or titled publicly here", "ops")}</p>'))
    h.append(section('''<h2 id="how-we-work">How we work</h2><p class="lede">These are working rules, not a certification or an award.</p>
<ul class="rules"><li><strong>No hype.</strong> We say what AI can do and what it cannot.</li><li><strong>Show the maths.</strong> Every figure in a report can be checked.</li><li><strong>Say no when it is no.</strong> If AI is not the answer, we say so.</li><li><strong>Your data is yours.</strong> We do not sell it, share it or reuse it.</li></ul>''', "section--dim"))
    h.append(section(f'<h2>Where we work</h2><p>MarvelUs is based in Melbourne, Australia. Calls and reports are done remotely, anywhere. {ph("confirm any in-person availability in Melbourne", "ops")}</p>'))
    h.append(cta_band("Let us talk.", None, [book_btn("Book a call", "primary"), buy_btn("Get the assessment", "secondary")]))
    return "\n".join(h)

@page("/events/", "Events | MarvelUs", "Talks, workshops and webinars from MarvelUs in Melbourne and online.")
def events():
    h = [hero("Events", "Come and ask us anything.", "We speak at and run small sessions for business owners. They are practical, short and open to questions.", "", crumb=[("Home", "/"), ("Events", "/events/")])]
    h.append(section(f'''<h2>Upcoming</h2><p>{ph("real upcoming events, each with a title, type tag (Talk, Workshop, Webinar), date and time in AEDT or AEST, place or link, and a Reserve a spot button", "events")}</p>
<div class="notice"><p>No events scheduled right now. Leave your email below and we will tell you about the next one.</p>
<form class="inline-form" data-demo-form="events" novalidate><label for="ev-email">Email</label><input id="ev-email" name="email" type="email" autocomplete="email" required aria-describedby="ev-note"><button class="btn btn--primary" type="submit">Tell me</button>
<p id="ev-note" class="small muted" role="status" data-demo-note>Draft: this form is not connected yet. Nothing is sent or stored.</p></form></div>'''))
    h.append(section(f'<h2>Previous events</h2><p>{ph("real past events with image, tag, title, one line, date, place and a recording link if one exists", "events")}</p>', "section--dim"))
    h.append(cta_band("Want this session for your own team or group?", "We can run a short briefing for your staff, your industry body or your networking group.", [book_btn("Book a call", "primary")]))
    return "\n".join(h)

@page("/book/", "Book a call | MarvelUs", "Talk to MarvelUs about digital support, SEO or the Business Assessment. Free, and no obligation.", extra_js=["assets/js/book.js"])
def book():
    ro = "".join(f'<label class="choice"><input type="radio" name="rev" value="{esc(b)}"><span>{esc(b)}</span></label>' for b in ["Under $500K", "$500K to $2M", "$2M to $10M", "$10M+"])
    heard = "".join(f'<option>{esc(x)}</option>' for x in HEARD)
    h = [hero("Book a call", "Book a call.", "Tell us what is eating your week and we will tell you honestly whether and how we can help. It is free, and we will say so if we are not the right fit.", "",
              note="Want the full picture instead? [Get the Business Assessment]({{PURCHASE}}).", center=True)]
    h.append(section(f'''<div class="book-card" id="book"><p class="small muted">You will speak with one of the MarvelUs team about your business.</p>
<h2>Pick a time that suits you.</h2><p>Two taps, one line about your week, then choose a time. Under a minute.</p>
<p class="notice small" role="note">Draft: the booking tool is not connected yet, so this form sends nothing. It is here to show the steps.</p>
<form id="book-form" novalidate>
<fieldset class="bstep" data-step="1"><legend>Is anyone in your business already looking after AI or automation?</legend>
<label class="choice"><input type="radio" name="owner" value="Yes"><span>Yes</span></label><label class="choice"><input type="radio" name="owner" value="No"><span>No</span></label></fieldset>
<fieldset class="bstep" data-step="2" hidden><legend>What is your annual revenue? <span class="small muted">(Australian dollars)</span></legend>{ro}</fieldset>
<div class="bstep" data-step="3" hidden><label for="b-topic">What would you most like to talk about? <span class="small muted">(optional)</span></label><textarea id="b-topic" name="topic" rows="3"></textarea><button class="btn btn--secondary" type="button" data-next>Continue</button> <button class="linklike" type="button" data-next>Skip</button></div>
<div class="bstep" data-step="4" hidden>
<div class="field"><label for="b-name">Name <span aria-hidden="true">*</span></label><input id="b-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="b-email">Email <span aria-hidden="true">*</span></label><input id="b-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="b-phone">Phone <span class="small muted">(optional)</span></label><input id="b-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="b-site">Business website <span class="small muted">(optional)</span></label><input id="b-site" name="site" autocomplete="url"></div>
<div class="field"><label for="b-heard">How did you hear about us? <span class="small muted">(optional)</span></label><select id="b-heard" name="heard"><option value="">Choose one</option>{heard}</select></div>
<div class="field field--check"><label><input type="checkbox" name="tips"> Send me occasional practical tips. I can unsubscribe at any time.</label></div>
<p class="small muted">By continuing you agree to our <a class="text-link" href="/terms/">Terms</a> and <a class="text-link" href="/privacy/">Privacy Policy</a>. Both are drafts.</p>
<p class="small muted">{ph("if text reminders are used, add a consent line checked against Australian spam and privacy rules", "legal")}</p>
<button class="btn btn--primary" type="submit">Show me the times</button></div>
<p class="form-error" role="alert" hidden></p></form>
<div class="embed-slot" id="embed-slot" hidden data-embed="{esc(CFG['bookingEmbedUrl'])}"><h3>Choose a time</h3>
<div class="embed-slot__box">{ph("booking tool embed. Choose a tool and set Melbourne time as the default with a time zone picker. Nothing is embedded yet", "booking")}</div>
<p class="small muted">Free. No cost to talk it through. Times shown in your local time zone.</p></div></div>''', "center", wrap="wrap wrap--narrow"))
    h.append(section(f'<p class="center">Prefer email? Write to {email_html()}.</p>', "section--tight"))
    h.append(section(f'<h2>What owners say</h2><p>{ph("testimonial band. Hide until approved quotes exist", "proof")}</p>', "section--dim"))
    return "\n".join(h)
