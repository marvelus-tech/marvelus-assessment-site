from engine import *
from content_core import *

def ladder_bars(levels, highlight=None):
    rows = []
    for key, name, meaning in DIMENSIONS:
        lv = levels[key]
        segs = "".join(f'<span class="seg{" seg--on" if i < lv else ""}"></span>' for i in range(5))
        low = " dim--low" if key == highlight else ""
        lname = LADDER[lv - 1][1]
        rows.append(f'<li class="dim{low}"><span class="dim__name">{esc(name)}</span>'
                    f'<span class="dim__bar" role="img" aria-label="{esc(name)}: level {lv} of 5, {lname}">{segs}</span>'
                    f'<span class="dim__val">{lv} of 5 · {lname}{" · lowest" if key == highlight else ""}</span></li>')
    return f'<ul class="dims">{"".join(rows)}</ul>'

def report_mock():
    r = SN
    top3 = r["rows"][:3]
    items = "".join(f'<li>{sample_tag(x["name"])}</li>' for x in top3)
    return f'''<div class="mock" role="group" aria-label="Example report card, invented data">
<p class="stamp">Example only, not a client result</p>
<p class="mock__title">Business Assessment report</p>
<div class="tiles">
<div class="tile"><p class="tile__label">Readiness score</p><p class="tile__num">{sample_tag(f"{r['score']} / 100")}</p></div>
<div class="tile"><p class="tile__label">Lost time a week</p><p class="tile__num">{sample_tag(f"{r['total_hours']} hours")}</p></div>
<div class="tile"><p class="tile__label">Cost of that time a month</p><p class="tile__num">{sample_tag(money(r['total_monthly']))}</p></div>
</div>
<p class="mock__sub">Opportunities, ranked</p>
<ol class="mock__list">{items}</ol>
<p class="small">How the cost is worked out: hours a week &times; hourly rate &times; {WEEKS} weeks in a month. In this example, {r['total_hours']} hours &times; ${SAMPLE_RATE} &times; {WEEKS} = {money(r['total_monthly'])} a month, roughly {money(r['total_monthly']*12)} a year.</p>
<p class="small muted">The ${SAMPLE_RATE} rate is only for the example. Your report uses your own rate. Your report uses your own hours, your own rate and your own words.</p>
</div>'''

def quiz_panel():
    return '''<section class="quiz" id="start" hidden aria-label="Free preview quiz">
<div class="wrap wrap--quiz"><div id="quiz-root" class="quiz__root" data-quiz="1"></div>
<noscript><p class="notice">The preview needs JavaScript. You can still <a class="text-link" href="/book/">book a call</a> or <a class="text-link" href="{{PURCHASE}}">get the assessment</a>.</p></noscript></div></section>'''

HOME_FAQ = [
 ("What is the Business Assessment?", f"A paid, one-off review of how your business spends its time. You phone in, an AI voice agent runs a guided conversation of {CALL}, and we turn your answers into a written report. The report gives you a score out of 100, a ranked list of opportunities and a dollar cost for each."),
 ("Is the voice agent a real person?", "No. It is an AI voice agent, and it says so at the start of the call. It is built to ask follow-up questions on what you tell it, the way a good interviewer would. [[PH:ops|confirm who at MarvelUs reviews each report, and how, before saying a person stands behind it]]"),
 ("What does it cost?", f"The Business Assessment is {PRICE_LONG}, once. GST is not included in the $1,000. The free preview quiz costs nothing. Digital support and SEO are scoped to your business, so there is no list price. [Book a call](/book/) and we will talk it through."),
 ("How do you work out the dollar figures?", f"Simple maths you can check. Hours a week, times the hourly value of that work, times {WEEKS} weeks in a month. If you tell us 18 hours a week at $50 an hour, that is $3,897 a month. The report shows every number and where it came from. Hours only count as money if spend stops, a planned hire is avoided or waiting demand gets served."),
 ("What if the answer is \"do not use AI\"?", "Then we say so. Sometimes the fix is a changed process, a setting in software you already pay for, or a better form. A report that tells you where not to spend is still worth having."),
 ("Who is this for?", "Owner-run and small to mid-sized businesses: trades, hospitality, professional services, health, retail and others. If a handful of people spend a lot of their week on repeated admin, enquiries or follow-up, it is a good fit."),
 ("How long until I see results?", f"The preview takes about a minute. The paid assessment takes {CALL} on the phone, and we email your report {CFG['reportTurnaround']}."),
 ("What happens to my information?", "It stays with you and us. We do not sell it, share it or reuse it. The transcript is yours. The free preview runs in your browser and sends nothing. See our [Privacy page](/privacy/), which is still a draft."),
]

@page("/", "MarvelUs | Find where AI can save your business time and money",
      "MarvelUs is a Melbourne business offering AI digital support, SEO and a paid Business Assessment that finds where your time and money leak. Start with a free preview.",
      quiz=True, bodyclass="home",
      schema=[lambda: service_ld("Business Assessment (AI Readiness)", "Phone intake call and written report with a 0 to 100 score, ranked opportunities and dollar costs.", "/assessment/", 1000)])
def home():
    h = [quiz_panel()]
    h.append(f'''<section class="hero hero--home center" id="hero"><div class="wrap wrap--hero">
{eyebrow("Business Assessment (AI Readiness)")}
<h1>Find the one job AI should take off your team first.</h1>
<p class="lede lede--lg">Answer a few short questions about your business. You get a free preview of your biggest time leak and what it costs you each month.</p>
<div class="btn-row btn-row--center">{quiz_btn()}</div>
<p class="soft-line">Prefer to talk it through? <a class="text-link" href="/book/">Book a call.</a></p>
<p class="soft-line"><a class="text-link" href="#sample" data-open-sample="1">See a sample result</a></p>
<p class="small muted">Takes about a minute. No payment needed for the preview. Nothing you type is stored or sent.</p>
</div></section>''')
    facts = [(PRICE, "One price for the full Business Assessment, in AUD"), ("About 15 min", "Phone intake call with an AI voice agent"),
             ("0 to 100", "Your readiness score, in your written report"), ("Ranked", "Every opportunity listed in order of what it is worth")]
    h.append('<section class="facts" aria-label="Key facts about the assessment"><div class="wrap"><ul class="facts__list">' +
             "".join(f'<li><p class="facts__fig">{esc(a)}</p><p class="facts__cap">{esc(b)}</p></li>' for a, b in facts) + '</ul></div></section>')
    h.append('<section class="rules-line"><div class="wrap wrap--narrow center"><p>We work to four plain rules: no hype, show the maths, say so when AI is not the answer, and keep your business data yours. <a class="text-link" href="/about/#how-we-work">How we work</a></p></div></section>')
    h.append(section(f'<h2 class="label-h">Built on tools we use ourselves</h2><p>{ph("only AI platforms MarvelUs actually builds on, with permission to show each logo", "proof")}</p>', "section--tight"))
    h.append(section(f'<h2 class="label-h">Businesses we have worked with</h2><p>{ph("real client logos with written permission, each linking to a case study. Needs at least 4 before this row is shown. Hide this row until then", "proof")}</p>', "section--tight section--dim"))
    h.append(section(f'''<h2 id="owners-h">What owners say</h2>
<figure class="quote"><blockquote><p>{ph("one real client quote, needs the client's written permission and MarvelUs sign-off", "proof")}</p></blockquote>
<figcaption>{ph("name, role, business, where the quote came from", "proof")}<br>{ph("star rating only if it is real and checkable, for example a Google rating with the link", "proof")}</figcaption></figure>''', aria="owners-h"))
    h.append(section('<h2 id="tm-h">More from owners</h2><div class="cards cards--3">' + "".join(
        f'<article class="card card--proof"><p>{ph("real client quote, photo, name, business. Needs written permission", "proof")}</p></article>' for _ in range(3)) +
        '</div><p class="small muted">Hide this band until at least 3 approved quotes exist.</p>', "section--dim", aria="tm-h"))
    h.append(section(f'''<div class="split"><div><h2>Find out what is worth fixing.</h2>
<p class="lede">Most owners know something is eating their week. Few know which thing, or what it costs. We find it, put a dollar figure on it, and tell you what to do first.</p></div>
<div class="media-slot" role="img" aria-label="Placeholder for an original illustration">{ph("original illustration of an owner buried in admin. Commission or generate original artwork", "media")}</div></div>'''))
    h.append(section(f'''<div class="split split--rev"><div class="media-slot" role="img" aria-label="Placeholder for a photo or artwork">{ph("real photo or artwork that suits the brand. Do not name or label any person unless approved", "media")}</div>
<div><h2>Three ways we help, all of them practical.</h2>
<p class="lede">Some businesses need to answer people faster. Some need to be found. Some need to know where to start. We do all three, and we are straight about which one you need.</p>
<p><a class="text-link text-link--arrow" href="/services/">See the services</a></p></div></div>''', "section--dim"))
    h.append(section(f'''{eyebrow("What we do")}<h2 id="offers-h">Three services. Pick the one that fits today.</h2>
{offer_cards(show_price=True)}
<p class="center soft-line">Not sure which one? <a class="text-link" href="#start" data-open-quiz="1">Take the one minute quiz</a> and we will point you to it.</p>''', id_="what-we-do", aria="offers-h"))
    h.append(section(f'''{eyebrow("How it works")}<h2 id="how-h">From a phone call to a ranked list, in four steps.</h2>
<p class="lede">The Business Assessment is a paid, one-off piece of work. It starts with a short call and ends with a report you can act on, whether or not you ever hire us.</p>
{numbered(ASSESSMENT_STEPS)}
<div class="btn-row">{buy_btn()} <a class="text-link" href="#start" data-open-quiz="1">Try the free preview first</a></div>''', "section--dim", id_="how-it-works", aria="how-h"))
    h.append(section(f'''<div class="split split--top"><div>{eyebrow("Your report")}<h2 id="report-h">Numbers you can act on, not a feeling that something is off.</h2>
<p class="lede">The report scores five dimensions of how your business runs, ranks every opportunity and puts a dollar figure on each. We email it {esc(CFG["reportTurnaround"])}.</p>
<p><a class="text-link text-link--arrow" href="/report/sample/">See the full sample report</a></p></div>{report_mock()}</div>
<h3 class="mt">Proof</h3>
<p>{ph("three real case study cards, each with a real result, the client's permission and how it was measured. Hide this row until they exist", "proof")}</p>
<p><a class="text-link text-link--arrow" href="/results/">See all results</a></p>''', id_="proof", aria="report-h"))
    h.append(section(f'''<h2>Start with the assessment. Add the rest when it makes sense.</h2>
<p class="lede">The Business Assessment is {PRICE_LONG}, one time. It shows you where the money is, so you can decide what to spend on next. Digital support and SEO are scoped to your business, so there is no list price. Book a call and we will tell you what it would take.</p>
<div class="btn-row btn-row--center">{btn("See pricing", "/pricing/", "primary")} {book_btn()}</div>''', "center", id_="pricing", wrap="wrap wrap--narrow"))
    h.append(faq(HOME_FAQ))
    h.append(section(f'''<div class="agents" id="for-agents"><h2 id="agents-h">For agents</h2>
<p class="lede">This site registers tools for AI agents through WebMCP (<code>navigator.modelContext</code>) on every page. If your browser has no WebMCP, the same tools are described in plain JSON.</p>
<ul class="agents__tools"><li><code>get_offers</code> the three equal offers</li><li><code>get_assessment_details</code> price, duration, dimensions, process</li><li><code>get_pricing</code> what is priced and what is not</li><li><code>get_sample_report</code> the example report, labelled as invented</li><li><code>start_quiz_preview</code> opens the free preview here</li><li><code>get_contact</code> contact state (placeholder for now)</li><li><code>get_site_map</code> every page</li></ul>
<p>Manifest: <a class="text-link" href="/agents.json">/agents.json</a> and <a class="text-link" href="/.well-known/agent.json">/.well-known/agent.json</a></p></div>''', "section--dim", aria="agents-h"))
    h.append(cta_band("Find your #1 opportunity in about a minute.", "Free preview. No payment, no obligation.",
                      [quiz_btn(), book_btn()]))
    return "\n".join(h)

# ------------------------------------------------------------------ assessment
ASSESS_FAQ = [
 ("What is a business assessment?", "A structured look at where AI could help, based on how your work really runs. Ours covers sales and enquiries, delivery, routine tasks, money and growth limits, and ends in a scored report."),
 ("How much does it cost?", f"The preview is free. The full assessment is {PRICE_LONG}, once. GST is not included in the $1,000."),
 ("How long does it take?", f"The preview is about a minute. The call is {CALL}. We email your report {CFG['reportTurnaround']}."),
 ("What do I receive at the end?", "A written report with a score from 0 to 100, your opportunities ranked, the dollar cost of each, what to do first, and your call transcript."),
 ("Will you tell me not to use AI?", "Yes, when that is the right answer. We would rather give you a short list you can trust than a long one that costs you money."),
 ("Can I do it from outside Australia?", "Yes. MarvelUs is based in Melbourne and everything is delivered remotely, anywhere. The price is in Australian dollars. [[PH:ops|confirm the call-in number works from outside Australia, and whether an Australian number is added]]"),
]

@page("/assessment/", "Business Assessment (AI Readiness) | MarvelUs",
      f"A free one minute preview, then a paid Business Assessment: a {CALL} phone intake with an AI voice agent and a report with a 0 to 100 score, ranked opportunities and dollar costs. {PRICE_LONG}.",
      quiz=True,
      schema=[lambda: service_ld("Business Assessment (AI Readiness)", "Phone intake call and written report scored across five dimensions, with ranked opportunities and dollar costs.", "/assessment/", 1000)])
def assessment():
    h = [quiz_panel()]
    h.append(hero("Business Assessment (AI Readiness)", "Find out where your business leaks time and money, and what to fix first.",
        "Most readiness checks are a short form that gives you a score and nothing to do with it. Ours is a conversation. You talk through how your work really runs, and we follow what you say until we find the cause. Sometimes the answer involves AI. Often it is simpler than that.",
        buy_btn(f"Get the assessment, {PRICE}") + quiz_btn("Try the free preview", "secondary"),
        crumb=[("Home", "/"), ("Business Assessment", "/assessment/")]))
    h.append(section(f'''<div class="cards cards--2 cards--equal">
<article class="card"><p class="tag">Free</p><h2 class="h3">The one minute preview</h2>
<p>Answer nine short questions about one task that costs you time. You get a short result that names your likely biggest opportunity, shows the steps involved and gives a rough monthly cost.</p>
<ul class="ticks"><li>Nine quick questions, about one minute</li><li>One task, mapped from start to finish</li><li>A rough monthly cost, with the assumptions shown</li><li>No payment, no obligation, nothing stored or sent</li></ul>
<div class="btn-row">{quiz_btn("Start the preview", "secondary")}</div></article>
<article class="card card--accent" id="buy"><p class="tag">Paid, one-off</p><h2 class="h3">The Business Assessment</h2>
<p class="card__price">{PRICE_LONG}</p>
<p>The full version. A guided phone call of {CALL} covers the whole business, not one task. Then you get a written report that scores where you are, ranks what is worth fixing and puts a dollar figure on each item.</p>
<ul class="ticks"><li>{CALL.capitalize()} on the phone, any time you like</li><li>A readiness score from 0 to 100, from five dimensions</li><li>Every opportunity ranked by what it is worth</li><li>Cost worked out as hours &times; rate &times; {WEEKS}, shown line by line</li><li>Your call transcript included</li><li>Report emailed {esc(CFG["reportTurnaround"])}</li></ul>
<div class="btn-row">{buy_btn()}</div>
<p class="small muted">GST is not included in the $1,000. Secure checkout. One payment, no subscription.</p></article></div>''', aria="x"))
    h.append(section(f'''<h2>What we talk about on the call</h2>
<p class="lede">The voice agent follows your answers. If you mention chasing invoices, it asks how often, who does it and what gets delayed. These are the five areas it covers.</p>
<dl class="defs">
<div><dt>Sales and enquiries</dt><dd>How leads arrive, how fast you reply, where follow-up drops off and how many turn into work.</dd></div>
<div><dt>From sold to delivered</dt><dd>The steps between a yes and a finished job. Where rework happens and where customers wait.</dd></div>
<div><dt>Hidden labour</dt><dd>The routine tasks that eat your week: email back and forth, data entry, chasing documents, writing the same proposal again.</dd></div>
<div><dt>The money side</dt><dd>What you spend on software, what an hour of your time is worth, and what you would do with ten hours back.</dd></div>
<div><dt>Limits to growth</dt><dd>What breaks if work doubles, who you would hire next and what keeps you working weekends.</dd></div></dl>''', "section--dim"))
    h.append(section(f'''<h2>What you get at the end</h2>
<p class="lede">One written report, built from your own answers, emailed {esc(CFG["reportTurnaround"])}.</p>
<ul class="get-list">
<li><strong>Your score out of 100.</strong> A roll-up of five dimensions, each scored on a five-point ladder. It comes with a note on which dimension is lowest, because that is where the first fixes belong.</li>
<li><strong>Your opportunities, ranked.</strong> Each one named plainly, with the hours it uses and what it costs you a month.</li>
<li><strong>The maths, in full.</strong> Hours a week &times; hourly rate &times; {WEEKS} = monthly cost. You can check every line.</li>
<li><strong>What to do first.</strong> The order we would tackle things and why. Some items will not need AI at all.</li>
<li><strong>Your call transcript.</strong> So you can see exactly what you told us.</li></ul>
<p><a class="text-link text-link--arrow" href="/report/sample/">See a sample report</a></p>''', aria="x"))
    h.append(section(f'''{eyebrow("What the report measures")}<h2>Five dimensions, one ladder.</h2>
<p class="lede">A real assessment scores five dimensions, each on a five-point maturity ladder from ad hoc to optimised. The headline number matters less than which dimension is lowest. That is where the recommendations should point.</p>
<dl class="defs">{"".join(f"<div><dt>{esc(n)}</dt><dd>{esc(d)}</dd></div>" for _, n, d in DIMENSIONS)}</dl>
<h3 class="mt">The ladder</h3>
<ol class="ladder">{"".join(f"<li><strong>{n}. {esc(a)}</strong> <span>{esc(b)}</span></li>" for n, a, b in LADDER)}</ol>
<p class="small muted">Your 0 to 100 score is the average of your five ladder levels, shown as a share of the top level. [[PH:ops|confirm the roll-up method with O before launch]]</p>''', "section--dim"))
    h.append(section(f'''<h2>How it works</h2>{numbered(ASSESSMENT_STEPS)}
<p class="small muted">Report delivery: emailed {esc(CFG["reportTurnaround"])}. [[PH:ops|confirm same business day turnaround is workable]]</p>''', aria="x"))
    h.append(section('''<h2>Common worries</h2>
<div class="worries">
<div><h3>"I do not have 15 minutes."</h3><p>The call is about 15. If you are working weekends or chasing the same admin every week, you are already spending far more time than that. The call shows you where it goes.</p></div>
<div><h3>"We already use project management software."</h3><p>Software does not diagnose how work moves. You can have good tools and still lose a day a week to handovers and chasing. The call looks for the pattern, not a missing app.</p></div>
<div><h3>"What about privacy?"</h3><p>What you tell us stays with you and us. We do not sell it, share it or reuse it, and the transcript is yours. The call exists to map your operation, not to collect your data.</p></div>
<div><h3>"What if it is not worth it?"</h3><p>Weigh the fee against the size of the leak. A task that costs you 18 hours a week at $50 an hour is about $46,800 a year in time. If your report finds something that size, the fee is small next to it. If it finds nothing worth fixing, we say so. We make no promises about results.</p></div></div>''', "section--dim"))
    h.append(section(f'''<div class="read"><h2>What does the assessment measure?</h2>
<p>It measures how your business runs today and where the effort goes, across tooling, data readiness, process maturity, automation, and team and AI literacy. The score gives you one number. The more useful part is which dimension is lowest, because that is where the first fixes belong.</p>
<h2>Why does it not start with AI?</h2>
<p>Because speeding up a broken process only breaks it faster. We work in the same order every time, and AI comes last.</p>
<ol>{"".join(f"<li><strong>{esc(a)}</strong> {esc(b)}</li>" for a, b in METHOD)}</ol>
<h2>How do you work out the cost?</h2>
<p>We keep it simple. Hours a week &times; hourly rate &times; {WEEKS} gives you a monthly figure. Multiply by 12 for the year.</p>
<p>Hours only turn into money in three ways: you stop paying for something, you avoid a hire you were about to make, or you serve demand that is already waiting. We count one of those per workflow, never two. Where a figure involves revenue, we use gross profit, not revenue. Every figure traces to something you told us. Where we do not know a number, the report marks it unknown instead of guessing. If the honest answer is that the saved hours just disappear into the day, the report says so and shows zero.</p>
<h2>What happens after the report?</h2>
<p>It is yours. Some people act on it alone. Others ask us to help, with digital support, SEO or other work from the report. Either is fine. See <a class="text-link" href="/case-studies/">case studies</a> and <a class="text-link" href="/pricing/">pricing</a>.</p></div>''', aria="x"))
    h.append(faq(ASSESS_FAQ, "Questions about the assessment"))
    h.append(cta_band("Start with the whole picture.", "One call, one report, one clear list of what to fix first.",
        [buy_btn(f"Get the assessment, {PRICE}"), quiz_btn("Try the free preview", "secondary")],
        '<p class="soft-line">Prefer to talk first? <a class="text-link" href="/book/">Book a call.</a></p>'))
    return "\n".join(h).replace(' aria-labelledby="x"', "")
