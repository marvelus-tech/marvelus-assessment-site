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

def staff_mock():
    r = EX_HOURS_YEAR
    return f'''<div class="mock" role="group" aria-label="Example findings report card, illustrative data">
<p class="stamp">Illustrative example, not client data</p>
<p class="mock__title">Findings report: one task</p>
<div class="tiles">
<div class="tile"><p class="tile__label">Hours a week</p><p class="tile__num">{sample_tag(f"{EX_HOURS_WEEK:.0f} hours")}</p></div>
<div class="tile"><p class="tile__label">Hours a year</p><p class="tile__num">{sample_tag(f"{r} hours")}</p></div>
<div class="tile"><p class="tile__label">Dollars a year</p><p class="tile__num">{sample_tag(aud(EX_DOLLARS_YEAR))}</p></div>
</div>
<p class="mock__sub">An estimator writing quotes</p>
<p class="small">{EXAMPLE_TIMES} quotes a week &times; about {EXAMPLE_MINUTES} minutes each = {EX_HOURS_WEEK:.0f} hours a week. {EX_HOURS_WEEK:.0f} hours &times; 52 = {r} hours a year. {r} hours &times; A${STAFF_RATE} an hour = about {aud(EX_DOLLARS_YEAR)} a year.</p>
<p class="small muted">Illustrative only, not client data. A${STAFF_RATE} an hour is the Victorian average, used when a business prefers not to share pay rates. Recovered time is capacity, not cash, until it is put to use.</p>
</div>'''

def maths_block(cls=""):
    return section(f'''<div class="split split--top"><div>{eyebrow("The maths")}<h2 id="maths-h">Every answer becomes a dollar figure.</h2>
<p class="lede">We ask "about how many times a week, about how many minutes each". Counting events works better than asking people to estimate how long something takes.</p>
<p class="formula"><strong>times a week &times; minutes each &times; 52 &times; pay rate = dollars a year</strong></p>
<p>We use your own pay rates. If you would rather not share them, we use the Victorian average.</p>
<p><strong>Straight talk:</strong> hours only count as dollars when spend stops, a hire is avoided, or waiting work gets done. Recovered time is capacity, not cash, until it is put to use. The report says which is which.</p>
<p><a class="text-link text-link--arrow" href="/report/sample/">See a sample findings report</a></p></div>{staff_mock()}</div>''', cls, aria="maths-h")

def promise_block(cls="section--dim"):
    return section(f'''{eyebrow("The promise")}<h2 id="promise-h">Tasks, not jobs.</h2>
<p class="lede">When staff worry about their jobs, the honest answers dry up. So every chat opens the same way: this is about tasks, not jobs, and nobody is being assessed.</p>
<ul class="ticks"><li>Answers are grouped by task and role, never by name.</li><li>No names in the report.</li><li>The aim is to remove grunt work so people can do more interesting work.</li><li>Time cost to your team: a 5 minute survey and a 15 minute chat each, and one call for the owner.</li></ul>''', cls, aria="promise-h")

def who_block(cls=""):
    return section(f'''{eyebrow("Who we work with")}<h2 id="who-h">Businesses with roughly {STAFF_RANGE} staff and a lot of repeatable admin.</h2>
<p class="lede">Owner-led, or run by an owner and a general manager. The week fills up with quotes, bookings, scheduling, invoicing and enquiries. We start with these seven kinds of business, and give each the same weight.</p>
{niche_cards()}
<p class="small muted">Fewer than 15 staff? The Business Assessment, a smaller first step, is built for you. See the <a class="text-link" href="/business-assessment/">Business Assessment page</a>.</p>''', cls, id_="who-we-work-with", aria="who-h")

def early_block(cls="section--dim"):
    return section(f'''{eyebrow("Honest proof")}<h2 id="early-h">We are early. Here is how we show value.</h2>
<p class="lede">There are no client results on this site yet, so we do not show any. What we do instead is measure, and show you the numbers whether they flatter us or not.</p>
{numbered([("Baseline.", "Before anything goes live we measure the task as it runs today: time, error rate and volume, on real cases."),
           ("Re-measure at 30 days.", "We measure the same things again and show you the change."),
           ("Re-measure at 60 days.", "Same measures, same cases, so the comparison is fair."),
           ("Re-measure at 90 days.", "You see what moved, what did not, and what we would keep, hold or cut.")])}
<p>Hours only count as dollars when spend stops, a hire is avoided, or waiting work gets done. Real, approved results will go on the <a class="text-link" href="/results/">Results page</a> with how each was measured.</p>''', cls, id_="we-are-early", aria="early-h")

def biz_report_mock():
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
<noscript><p class="notice">The preview needs JavaScript. You can still <a class="text-link" href="/book/">book the 10-minute chat</a> or <a class="text-link" href="{{PURCHASE}}">get the Business Assessment</a>.</p></noscript></div></section>'''

HOME_FAQ = [
 ("What is the Staff-level AI Assessment?", f"A paid assessment for businesses with roughly {STAFF_RANGE} staff. We start with a 10-minute chat with the owner. Then each person on your team does a short survey of about 5 minutes and a 15 minute chat. You get a findings report that lists every task in hours and dollars a year, ranked, with no names, and a presentation to leadership."),
 ("Why ask the staff and not only the owner?", "The people doing the work know where the time goes. The owner usually knows something is slow, but not which tasks, how often or how long. Asking the team gets the real picture."),
 ("What does it cost?", f"The staff-level assessment is {PRICED.lower()}. We do not publish figures. [Book the 10-minute chat](/book/) and we will quote once we know your headcount. The smaller first step, the Business Assessment, is {PRICE_LONG}, once, and GST is not included in the $1,000. Digital support and SEO are scoped to your business."),
 ("How do the staff chats and consent work?", "Each chat is about 15 minutes. It is recorded with an AI note taker only when the person says yes first. Answers are grouped by task and role, never by name. See the [staff-level assessment page](/assessment/#faq) for the full detail."),
 ("What is the 15 minute intake call?", f"That is the Business Assessment, the smaller first step at {PRICE_LONG}. You phone in and an AI voice agent runs a guided conversation of {CALL} about how the business runs. We email a written report with a score out of 100, ranked opportunities and a dollar cost for each, {CFG['reportTurnaround']}. It says it is an AI voice agent at the start of the call. [[PH:ops|confirm who at MarvelUs reviews each report, and how, before saying a person stands behind it]]"),
 ("How do you work out the dollar figures?", "Simple maths you can check. Times a week, times minutes each, times 52, times the pay rate. We use your pay rates, or the Victorian average if you would rather not share them. Hours only count as dollars when spend stops, a hire is avoided or waiting work gets done."),
 ("What if the answer is \"do not use AI\"?", "Then we say so. Sometimes the fix is a changed process, a setting in software you already pay for, or a better form. A report that tells you where not to spend is still worth having."),
 ("Where are you based?", "Melbourne. We work remotely with businesses anywhere in Australia."),
 ("What happens to my information?", "It stays with you and us. We do not sell it, share it or reuse it. See our [Privacy page](/privacy/), which is still a draft."),
]

@page("/", "MarvelUs | Staff-level AI assessment for Australian businesses",
      "MarvelUs is a Melbourne business that asks your team where the time goes. A staff-level AI assessment for businesses with roughly 15 to 150 staff, priced by headcount. Book a 10-minute chat.",
      quiz=True, bodyclass="home",
      schema=[lambda: service_ld("Staff-level AI Assessment", "Short survey and a 15 minute chat with each person on your team, then a ranked findings report in hours and dollars a year and a presentation to leadership. For businesses with roughly 15 to 150 staff.", "/assessment/", pricing_note="Priced by headcount. Book a 10-minute chat for a quote."),
              lambda: service_ld("Business Assessment (AI Readiness)", "A smaller first step: phone intake call and written report with a 0 to 100 score, ranked opportunities and dollar costs.", "/business-assessment/", 1000)])
def home():
    h = [quiz_panel()]
    h.append(f'''<section class="hero hero--home center" id="hero"><div class="wrap wrap--hero">
{eyebrow(f"Staff-level AI Assessment for businesses with roughly {STAFF_RANGE} staff")}
<h1>Ask the people doing the work where the time goes.</h1>
<p class="lede lede--lg">We run a short survey and a 15 minute chat with each person on your team, then show you every repeat task in hours and dollars a year, ranked, with no names. {PRICED}.</p>
<div class="btn-row btn-row--center">{chat_btn()}<a class="btn btn--secondary" href="/assessment/">How it works</a></div>
<p class="soft-line">Want a smaller first step? <a class="text-link" href="#first-step">The Business Assessment is {PRICE}.</a></p>
<p class="small muted">Melbourne based. Working remotely with businesses anywhere in Australia.</p>
</div></section>''')
    facts = [(f"{STAFF_RANGE}", "Staff, the size of business this is built for"), ("10 minutes", "The first chat, with the owner"),
             ("5 + 15 min", "Survey and chat for each person on your team"), ("No names", "Findings are grouped by task and role")]
    h.append('<section class="facts" aria-label="Key facts about the staff-level assessment"><div class="wrap"><ul class="facts__list">' +
             "".join(f'<li><p class="facts__fig">{esc(a)}</p><p class="facts__cap">{esc(b)}</p></li>' for a, b in facts) + '</ul></div></section>')
    h.append('<section class="rules-line"><div class="wrap wrap--narrow center"><p>We work to four plain rules: no hype, show the maths, say so when AI is not the answer, and keep your business data yours. <a class="text-link" href="/about/#how-we-work">How we work</a></p></div></section>')
    h.append(section(f'''{eyebrow("How it works")}<h2 id="how-h">From a 10-minute chat to a ranked list, in four steps.</h2>
<p class="lede">Your team knows where the time goes. We ask them, with their time in mind: about 5 minutes for the survey and 15 for the chat. Then we show you what we found.</p>
{numbered(STAFF_STEPS)}
<div class="btn-row">{chat_btn()} <a class="text-link text-link--arrow" href="/assessment/">Read the full detail</a></div>''', "section--dim", id_="how-it-works", aria="how-h"))
    h.append(maths_block())
    h.append(promise_block())
    h.append(who_block())
    h.append(section(f'''{eyebrow("The assessment area")}<h2 id="area-h">Start with the staff-level assessment, or take a smaller first step.</h2>
<p class="lede">The staff-level assessment is the full picture, from the people who do the work. If you would rather start smaller, the Business Assessment is a fixed price phone intake and report you can start now.</p>
{assessment_area()}
<p class="center soft-line">Want a feel for it first? <a class="text-link" href="#start" data-open-quiz="1">Try the free one minute preview.</a> Nothing you type is stored or sent.</p>''', id_="assessment-area", aria="area-h"))
    h.append(section(f'''{eyebrow("What we do")}<h2 id="offers-h">Three services. Pick the one that fits today.</h2>
{offer_cards(show_price=True)}
<p class="center soft-line">Not sure which one? <a class="text-link" href="/book/">Book the 10-minute chat</a> and we will point you to it.</p>''', "section--dim", id_="what-we-do", aria="offers-h"))
    h.append(early_block("") )
    h.append(section(f'<h2 class="label-h">Built on tools we use ourselves</h2><p>{ph("only AI platforms MarvelUs actually builds on, with permission to show each logo", "proof")}</p>', "section--tight section--dim"))
    h.append(section(f'<h2 class="label-h">Client logos</h2><p>{ph("real client logos with written permission, each linking to a case study. Needs at least 4 before this row is shown. Hide this row until then", "proof")}</p>', "section--tight"))
    h.append(section(f'''<h2 id="owners-h">Owner quotes</h2>
<figure class="quote"><blockquote><p>{ph("one real client quote, needs the client's written permission and MarvelUs sign-off. Hide until it exists", "proof")}</p></blockquote>
<figcaption>{ph("name, role, business, where the quote came from", "proof")}<br>{ph("star rating only if it is real and checkable, for example a Google rating with the link", "proof")}</figcaption></figure>''', "section--dim", aria="owners-h"))
    h.append(section(f'''<div class="split"><div>{eyebrow("Melbourne based, Australia wide")}<h2>Local to Melbourne. Working across Australia.</h2>
<p class="lede">We are based in Melbourne and work remotely with businesses anywhere in Australia. Prices are in Australian dollars, and where we use a pay rate as a default, it is the Victorian average.</p>
<p><a class="text-link text-link--arrow" href="/ai-consulting-melbourne/">AI consulting in Melbourne</a></p></div>
<div class="media-slot" role="img" aria-label="Placeholder for a photo or artwork">{ph("real photo or artwork that suits the brand, for example Melbourne. Do not name or label any person unless approved", "media")}</div></div>'''))
    h.append(faq(HOME_FAQ))
    h.append(section(f'''<div class="agents" id="for-agents"><h2 id="agents-h">For agents</h2>
<p class="lede">This site registers tools for AI agents through WebMCP (<code>navigator.modelContext</code>) on every page. If your browser has no WebMCP, the same tools are described in plain JSON.</p>
<ul class="agents__tools"><li><code>get_offers</code> the three equal offers, with the assessment area</li><li><code>get_assessment_details</code> the staff-level assessment, priced by headcount</li><li><code>get_business_assessment_details</code> the smaller first step, price, dimensions, process</li><li><code>get_pricing</code> what is priced and what is not</li><li><code>get_sample_report</code> the example findings report, labelled illustrative</li><li><code>start_quiz_preview</code> opens the free preview here</li><li><code>get_contact</code> contact state (placeholder for now)</li><li><code>get_site_map</code> every page</li></ul>
<p>Manifest: <a class="text-link" href="/agents.json">/agents.json</a> and <a class="text-link" href="/.well-known/agent.json">/.well-known/agent.json</a></p></div>''', "section--dim", aria="agents-h"))
    h.append(cta_band("Start with a 10-minute chat.", f"We will ask where the time goes and tell you honestly if the staff-level assessment is worth it. {PRICED}.",
                      [chat_btn(), buy_btn(f"Or start smaller: Business Assessment, {PRICE}", "secondary", "home-cta")]))
    return "\n".join(h)

# ------------------------------------------------------------------ staff-level assessment (the lead offer)
STAFF_FAQ = [
 ("What is the Staff-level AI Assessment?", f"A paid assessment for businesses with roughly {STAFF_RANGE} staff. We ask the people doing the work, not only the owner, where their time goes. You get a findings report that puts every repeat task in hours and dollars a year, ranked, with no names, and we present it to your leadership."),
 ("Who is it for?", f"Owner-led businesses, or ones run by an owner and a general manager, with roughly {STAFF_RANGE} staff and a lot of repeatable admin such as quotes, bookings, scheduling, invoicing and enquiries. Under 15 staff, the [Business Assessment](/business-assessment/) is a better fit."),
 ("How is it priced?", f"{PRICED}. We do not publish figures. [Book the 10-minute chat](/book/) and we will give you a quote once we know how many people take part."),
 ("How much of my team's time does it take?", "A survey of about 5 minutes and a 15 minute chat for each person. One call for the owner. That is all we ask of your team."),
 ("How does the 15 minute chat work?", "It is a relaxed conversation about one person's week. We ask which tasks repeat, about how many times a week, and about how many minutes each takes. Counting events works better than asking people to guess how long something takes. We open every chat by saying it is about tasks, not jobs."),
 ("Is the chat recorded?", "Only with the person's explicit consent. We ask before the chat, and recording is done with an AI note taker. Saying no is fine. [[PH:ops|how MarvelUs handles someone who declines the recording, for example taking notes by hand, and the wording of the consent request]]"),
 ("How long are recordings kept, and who can see them?", "[[PH:legal|retention plan: how long recordings and transcripts are kept, who at MarvelUs can access them, where they are stored and how they are deleted. Needs MarvelUs sign-off and a lawyer's review before launch]] We do not sell or share them. This page describes how we work. It is not legal advice, and we are not lawyers."),
 ("Will the owner see who said what?", "No. The report has no names. Answers are grouped by task and role. Where a role is held by one person, a role can point to that person, so we agree how to handle that with you first. [[PH:ops|how MarvelUs reports roles held by only one person]]"),
 ("Is anyone's job being assessed?", "No. We assess tasks, not jobs. The aim is to remove grunt work so people can do more interesting work."),
 ("Do I have to share pay rates?", f"No. If you would rather not, we use the Victorian average, A${STAFF_RATE} an hour."),
 ("Do the hours turn into dollars?", "Only when spend stops, a hire is avoided, or waiting work gets done. Recovered time is capacity, not cash, until it is put to use. The report says which is which."),
 ("What happens after the findings?", "You get the report and a presentation to leadership, with one working demo on your own redacted paperwork. After that there is an optional ongoing support step, scoped after the findings."),
 ("What if there is nothing worth fixing?", "We say so. A short honest list is better than a long one that costs you money."),
 ("Can you work with a business outside Melbourne?", "Yes. We are based in Melbourne and work remotely with businesses anywhere in Australia."),
 ("Is there a smaller way to start?", f"Yes. The [Business Assessment](/business-assessment/) is a fixed price phone intake and report at {PRICE_LONG}. It is a smaller first step you can start now."),
]

@page("/assessment/", "Staff-level AI Assessment | MarvelUs",
      f"Ask the people doing the work. A short survey and a 15 minute chat with each person on your team, then a ranked findings report in hours and dollars a year. For businesses with roughly {STAFF_RANGE} staff. {PRICED}.",
      schema=[lambda: service_ld("Staff-level AI Assessment", "Short survey and a 15 minute chat with each person on your team, then a ranked findings report in hours and dollars a year and a presentation to leadership.", "/assessment/", pricing_note="Priced by headcount. Book a 10-minute chat for a quote.")])
def assessment():
    h = []
    h.append(hero("Staff-level AI Assessment", "Ask the people doing the work, not only the owner.",
        f"For businesses with roughly {STAFF_RANGE} staff. Your team does a short survey and a 15 minute chat. You get every repeat task in hours and dollars a year, ranked, with no names. {PRICED}.",
        chat_btn("Get a quote", src="assessment-hero") + btn("See a sample findings report", "/report/sample/", "secondary"),
        crumb=[("Home", "/"), ("Staff-level AI Assessment", "/assessment/")],
        note="Melbourne based, working remotely with businesses anywhere in Australia."))
    h.append(section(f'''{eyebrow("Why ask the team")}<h2 id="why-h">The owner knows it is slow. The team knows why.</h2>
<p class="lede">Owners usually feel where the time goes, but not which tasks, how often or how long. The people doing the work can tell you. So we ask them, one at a time, in a short, friendly chat.</p>
<p>The result is a list you can trust, because it comes from the people who do the tasks, not from a guess.</p>''', aria="why-h", wrap="wrap wrap--read"))
    h.append(section(f'''{eyebrow("The path")}<h2 id="path-h">Four steps, starting small.</h2>
{numbered(STAFF_STEPS)}''', "section--dim", id_="path", aria="path-h"))
    h.append(section(f'''<h2 id="get-h">What you get in the paid assessment.</h2>
<ul class="get-list">
<li><strong>A short team survey.</strong> About 5 minutes per person. It ends with a booking for the chat.</li>
<li><strong>A 15 minute chat with each person.</strong> Recorded with an AI note taker, only with explicit consent.</li>
<li><strong>A findings report.</strong> Every task as times per week, minutes each, hours a year and dollars a year, ranked. No names.</li>
<li><strong>A findings presentation to leadership.</strong> We walk you through it, with one working demo on your own redacted paperwork.</li></ul>
<p><a class="text-link text-link--arrow" href="/report/sample/">See a sample findings report</a></p>''', aria="get-h"))
    h.append(maths_block("section--dim"))
    h.append(promise_block(""))
    h.append(section(f'''<div class="split split--top"><div>{eyebrow("Pricing")}<h2 id="price-h">{PRICED}.</h2>
<p class="lede">The price depends on how many people take part. We do not publish figures. Book the 10-minute chat and we will quote once we know your headcount.</p>
<p class="small muted">Digital support and SEO are scoped to your business, with no list price.</p>
<div class="btn-row">{chat_btn("Get a quote", src="assessment-price")}</div></div>
<div class="card"><h3>What your team gives up</h3><ul class="ticks"><li>About 5 minutes each for the survey</li><li>About 15 minutes each for the chat</li><li>One call for the owner</li></ul></div></div>''', "section--dim", id_="pricing", aria="price-h"))
    h.append(who_block(""))
    h.append(early_block())
    h.append(section(f'''{eyebrow("A smaller first step")}<h2 id="small-h">Not ready for the full picture? Start smaller.</h2>
<p class="lede">The Business Assessment is a phone intake call of {CALL} and a scored written report, at {PRICE_LONG}. It is a smaller first step you can start now.</p>
<div class="btn-row">{buy_btn(f"Get the Business Assessment, {PRICE}")} <a class="text-link text-link--arrow" href="/business-assessment/">Read about it first</a></div>''', id_="first-step", aria="small-h"))
    h.append(faq(STAFF_FAQ, "Questions about the staff-level assessment"))
    h.append(cta_band("Start with a 10-minute chat.", f"We will ask where the time goes and tell you honestly if this is worth doing. {PRICED}.",
        [chat_btn("Get a quote", src="assessment-cta"), buy_btn(f"Or start smaller: Business Assessment, {PRICE}", "secondary", "assessment-cta")]))
    return "\n".join(h).replace(' aria-labelledby="x"', "")

# ------------------------------------------------------------------ Business Assessment ($1,000 + GST, the smaller first step)
BIZ_FAQ = [
 ("What is a business assessment?", "A structured look at where AI could help, based on how your work really runs. Ours covers sales and enquiries, delivery, routine tasks, money and growth limits, and ends in a scored report."),
 ("How much does it cost?", f"The preview is free. The full assessment is {PRICE_LONG}, once. GST is not included in the $1,000."),
 ("How long does it take?", f"The preview is about a minute. The call is {CALL}. We email your report {CFG['reportTurnaround']}."),
 ("What do I receive at the end?", "A written report with a score from 0 to 100, your opportunities ranked, the dollar cost of each, what to do first, and your call transcript."),
 ("Will you tell me not to use AI?", "Yes, when that is the right answer. We would rather give you a short list you can trust than a long one that costs you money."),
 ("What is the 15 minute intake call?", f"A phone call of {CALL} with an AI voice agent, which says it is an AI at the start. It asks how your business runs, follows up on what you say, and ends when it has what it needs. You can do it any time you like. We then write the report from your answers and email it {CFG['reportTurnaround']}."),
 ("Is the call recorded?", "The call is recorded so that we can write the report and so that you get your transcript. The voice agent tells you at the start. [[PH:legal|the exact recording notice and consent wording, and the retention plan for call recordings and transcripts]]"),
 ("Is there a bigger version?", "Yes. If you have roughly 15 to 150 staff, the [Staff-level AI Assessment](/assessment/) asks the people doing the work, not only the owner. It is priced by headcount."),
 ("Can I do it from outside Australia?", "MarvelUs is based in Melbourne and works remotely with businesses across Australia. The price is in Australian dollars. [[PH:ops|confirm whether the call-in works from outside Australia, and whether an Australian number is added]]"),
]

@page("/business-assessment/", "Business Assessment (AI Readiness) | MarvelUs",
      f"A smaller first step you can start now. A free one minute preview, then a paid Business Assessment: a {CALL} phone intake with an AI voice agent and a report with a 0 to 100 score, ranked opportunities and dollar costs. {PRICE_LONG}.",
      quiz=True,
      schema=[lambda: service_ld("Business Assessment (AI Readiness)", "Phone intake call and written report scored across five dimensions, with ranked opportunities and dollar costs.", "/business-assessment/", 1000)])
def business_assessment():
    h = [quiz_panel()]
    h.append(hero("A smaller first step you can start now", "Find out where your business leaks time and money, and what to fix first.",
        "Most readiness checks are a short form that gives you a score and nothing to do with it. Ours is a conversation. You talk through how your work really runs, and we follow what you say until we find the cause. Sometimes the answer involves AI. Often it is simpler than that.",
        buy_btn(f"Get the assessment, {PRICE}", "primary", "business-hero") + quiz_btn("Try the free preview", "secondary"),
        crumb=[("Home", "/"), ("Staff-level AI Assessment", "/assessment/"), ("Business Assessment", "/business-assessment/")]))
    h.append(section(f'''<div class="cards cards--2 cards--equal">
<article class="card"><p class="tag">Free</p><h2 class="h3">The one minute preview</h2>
<p>Answer nine short questions about one task that costs you time. You get a short result that names your likely biggest opportunity, shows the steps involved and gives a rough monthly cost.</p>
<ul class="ticks"><li>Nine quick questions, about one minute</li><li>One task, mapped from start to finish</li><li>A rough monthly cost, with the assumptions shown</li><li>No payment, no obligation, nothing stored or sent</li></ul>
<div class="btn-row">{quiz_btn("Start the preview", "secondary")}</div></article>
<article class="card card--accent" id="buy"><p class="tag">Paid, one-off, a smaller first step</p><h2 class="h3">The Business Assessment</h2>
<p class="card__price">{PRICE_LONG}</p>
<p>The full version. A guided phone call of {CALL} covers the whole business, not one task. Then you get a written report that scores where you are, ranks what is worth fixing and puts a dollar figure on each item.</p>
<ul class="ticks"><li>{CALL.capitalize()} on the phone, any time you like</li><li>A readiness score from 0 to 100, from five dimensions</li><li>Every opportunity ranked by what it is worth</li><li>Cost worked out as hours &times; rate &times; {WEEKS}, shown line by line</li><li>Your call transcript included</li><li>Report emailed {esc(CFG["reportTurnaround"])}</li></ul>
<div class="btn-row">{buy_btn(kind="primary", where="business-card")}</div>
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
<p><a class="text-link text-link--arrow" href="/report/business-assessment-sample/">See a sample report</a></p>''', aria="x"))
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
    h.append(faq(BIZ_FAQ, "Questions about the assessment"))
    h.append(cta_band("Start with the whole picture of the business.", "One call, one report, one clear list of what to fix first.",
        [buy_btn(f"Get the assessment, {PRICE}", "primary", "business-cta"), quiz_btn("Try the free preview", "secondary")],
        '<p class="soft-line">Have 15 to 150 staff? The <a class="text-link" href="/assessment/">Staff-level AI Assessment</a> asks your whole team. <a class="text-link" href="/book/">Book the 10-minute chat.</a></p>'))
    return "\n".join(h).replace(' aria-labelledby="x"', "")
