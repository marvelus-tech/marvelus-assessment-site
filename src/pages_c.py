from engine import *
from content_core import *
from pages_a import ladder_bars

DISCLOSURE = "This guide is general information, not legal, tax or financial advice. We sell AI services, so weigh our view with that in mind."

ARTICLES = [
 {"slug": "what-is-an-ai-readiness-assessment", "topic": "Business Assessment", "type": "Guide", "read": "5 min",
  "title": "What is an AI readiness assessment?",
  "dek": "What these assessments check, what they miss and how to pick one that gives you something to do.",
  "take": ["An AI readiness assessment looks at how your business runs and where AI could help, before you spend on it.",
           "Free online scorecards are fine for a first look. They rarely tell you what to do next.",
           "A useful assessment gives you a ranked list with dollar figures, not only a score.",
           "The best result is sometimes \"fix the process first\" or \"do not use AI here\".",
           "Check how the cost figures are worked out. If you cannot check the maths, do not trust it."],
  "body": f"""## What is an AI readiness assessment?

It is a structured look at your business to work out where AI could help, where it would not and what to do first. It covers how you take enquiries, how work is delivered, which routine tasks eat the week and what money is involved. The output is usually a score, a list of opportunities or both.

## Why do one before buying anything?

Because the most common mistake is buying a tool before knowing the problem. A tool bought without a clear job tends to go unused after the first few weeks. An assessment puts a number on the problem first, so you can decide how much it is worth solving.

## What should a good assessment cover?

Look for five things.

1. **How enquiries and sales work.** How fast you reply and where follow-up drops.
2. **How work is delivered.** The steps between a yes and a finished job.
3. **Routine tasks.** Copying, chasing, retyping, reporting.
4. **Money.** What your time and your software cost.
5. **Limits to growth.** What breaks if work doubles.

A good one also scores how ready the business is. Ours scores five dimensions (tooling, data readiness, process maturity, automation, and team and AI literacy), each on a five-point ladder from ad hoc to optimised. The lowest dimension matters more than the headline number, because that is where the first fixes belong.

## How is it different from a free quiz?

A quiz asks a few multiple-choice questions and returns a number. That is fine for curiosity. A full assessment follows up on your answers, so it can tell the difference between "we chase invoices" and "we chase invoices because the first invoice goes out two weeks late". The second one is the one worth fixing.

## How should the cost be calculated?

Plainly. Hours a week × hourly rate × {WEEKS} weeks in a month. If a task takes 10 hours a week and the people doing it cost $40 an hour, that is $1,732 a month. Be careful with what the number means. Saved hours only become money when you stop paying for something, avoid a hire or serve demand that is already waiting. Otherwise they are a nicer week, which has value, but is not a dollar figure.

## What are the warning signs of a poor assessment?

- It gives a score and no next step.
- It says yes to AI for every answer.
- It will not show how a figure was worked out.
- It is free because the real goal is to sell you a large project.

## What happens after the assessment?

You have three choices. Do the work yourself, hire someone to do it or decide it is not worth it right now. All three are fine. The point is that you are choosing with numbers.""",
  "next": [("The MarvelUs Business Assessment", "/assessment/"), ("How to work out what a task costs", "/insights/how-to-work-out-the-cost-of-a-repeated-task/")],
  "sources": "add 3 to 5 real, checkable public sources, for example Australian Government AI guidance for business and a recognised public business survey on AI adoption. Verify each link and date before publishing. Cite nothing that has not been opened and read",
  "faq": [("How long does an assessment take?", f"Ours takes {CALL} on the phone. We email the report {CFG['reportTurnaround']}."),
          ("Do I need technical knowledge?", "No. You describe how work happens. We do the translation."),
          ("Is a free assessment worth doing?", "As a first look, yes. As a basis for a spend decision, usually not."),
          ("What if I am a very small business?", "Smaller businesses often see the biggest relative gains, because one person's time is a large part of the whole."),
          ("Does it replace advice from my accountant?", "No. It focuses on operations. Your accountant still advises on money and tax.")]},
 {"slug": "how-to-work-out-the-cost-of-a-repeated-task", "topic": "AI costs and returns", "type": "Playbook", "read": "4 min",
  "title": "How to work out the cost of a repeated task",
  "dek": "A five minute method for putting a dollar figure on any task that eats your week.",
  "take": [f"Cost per month = hours a week × hourly rate × {WEEKS}.",
           "Use the real cost of the person's time, not their wage alone.",
           "A number is only a saving if something changes because of it.",
           "Write down what you are unsure about. Do not fill gaps with a guess that looks exact.",
           "Do one task first, not the whole business."],
  "body": f"""## Why put a dollar figure on a task?

Because "it takes ages" does not help you decide. "$1,732 a month" does. It lets you compare a task with the price of fixing it, and it gives you something to measure against later.

## What is the formula?

Hours a week × hourly rate × {WEEKS} = cost a month. The {WEEKS} is the average number of weeks in a month (52 divided by 12). Multiply by 12 for a yearly figure.

Example. A task takes 10 hours a week across two people. Their combined cost is $40 an hour. 10 × $40 × {WEEKS} = $1,732 a month, or about $20,784 a year. This is an example, not a client result.

## What hourly rate should I use?

Use what the time costs you, not only the wage. That means pay, super, leave, software and the space they use. If you do not know the figure, ask your accountant or use a clearly labelled estimate. State the rate so a reader can change it.

## When does a saving count?

Only when it turns into something you can see. There are three common ways.

1. **You stop paying for something.** For example, less overtime or a cancelled subscription.
2. **You avoid a hire.** The work grows and you do not need to add a person.
3. **You serve demand that was already waiting.** The same team handles more enquiries or jobs.

Count one of these per task, never two. If the benefit is extra sales, use gross profit, not revenue. If none of these happens, the time simply moves elsewhere. That still has value, but record it as time, not money.

## How do I handle things I do not know?

Mark them unknown. If you do not know how many hours a task takes, time it for a week. A figure marked "estimate" is honest. A figure with false precision is not.

## What about the cost of the fix?

Subtract it. If a fix costs $3,000 and saves $1,732 a month, it pays back in a little under two months. If it saves $200 a month, it takes over a year, and you may decide it is not worth doing yet.

## What do I do with the number?

Rank your tasks by cost, check which are safest to change and start with the one that is both large and low risk.""",
  "next": [("The Business Assessment does this for the whole business", "/assessment/"), ("Try the free preview for one task", "/#start")],
  "sources": "add real, verified sources for on-costs and weeks per month, for example the Fair Work Ombudsman pay and super pages. Open and verify each link first",
  "faq": [(f"Why {WEEKS} and not 4?", "Because months have slightly more than four weeks. Using 4 under-counts by about 8 percent."),
          ("Should I include my own time?", "Yes, at what an hour of your time is worth to the business."),
          ("What if the task varies week to week?", "Use an average over a typical month."),
          ("Can a small saving still be worth it?", "Yes, if the fix is cheap and safe."),
          ("What if the number is small?", "Then the task is not your biggest problem. That is useful to know.")]},
]

OUTLINES = [
 ("AI readiness tools vs services", "Business Assessment", ["What is a readiness tool?", "What is a service?", "When is a free tool enough?", "What each one misses", "How to choose"]),
 ("How to choose an AI consultant in Melbourne and Australia", "Getting started", ["What should a consultant deliver?", "Questions to ask before you hire", "Red flags", "How pricing usually works", "What to ask for in writing"]),
 ("What does AI digital support cost?", "Digital support", ["Chat vs voice", "What drives the price", "Build and running costs", "What is worth paying for", "How to measure whether it worked"]),
 ("SEO for local businesses: where to start", "SEO", ["What search customers really type", "The five fixes that matter first", "Your Google Business listing", "How long it takes", "What to ignore"]),
 ("AI and customer privacy in Australia", "Digital support", ["What data does an AI assistant touch?", "What the Privacy Act expects", "What to ask a supplier", "What to put in your privacy policy"]),
 ("When AI is not the answer", "Getting started", ["Fix the process first", "Five signs a task should be removed, not automated", "When a setting in your current software is enough", "The order we work in"]),
]

TOPICS = ["Business Assessment", "AI costs and returns", "Digital support", "SEO", "Getting started"]

def article_html(a, template=False):
    body = md(a["body"])
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc) + '<li><a href="#sources">Sources</a></li><li><a href="#common-questions">Common questions</a></li>'
    take = "".join(f"<li>{inline(t)}</li>" for t in a["take"])
    nxt = "".join(f'<li><a class="text-link" href="{u}">{esc(t)}</a></li>' for t, u in a["next"])
    others = [x for x in ARTICLES if x["slug"] != a.get("slug")]
    keep = [f'<article class="card"><p class="tag">{esc(x["topic"])}</p><h3><a href="/insights/{x["slug"]}/">{esc(x["title"])}</a></h3><p>{esc(x["dek"])}</p></article>' for x in others[:3]]
    for t, tp, _ in OUTLINES:
        if len(keep) >= 3:
            break
        keep.append(f'<article class="card"><p class="tag">{esc(tp)} · Outline</p><h3><a href="/insights/outlines/#{slug(t)}">{esc(t)}</a></h3><p>Not yet written.</p></article>')
    date = ph("publish date", "dates")
    h = [f'''<article class="article"><header class="hero hero--page"><div class="wrap wrap--hero">{crumbs([("Home", "/"), ("Insights", "/insights/"), (a["topic"], "/insights/"), (a["title"], None)])}
<p class="eyebrow">{esc(a["topic"])} · {esc(a["type"])}</p><h1>{esc(a["title"])}</h1><p class="lede lede--lg">{esc(a["dek"])}</p>
<p class="byline">By MarvelUs · Published {date} · Updated {ph("updated date", "dates")} · {esc(a["read"])} read</p></div></header>
<div class="wrap layout-article"><aside class="toc" aria-label="On this page"><p class="toc__h">On this page</p><ol>{toc_html}</ol></aside>
<div class="read">
<section class="takeaways" aria-labelledby="kt"><h2 id="kt">Key takeaways</h2><ul>{take}</ul></section>
<p class="small muted">{DISCLOSURE}</p>
{body}
<h2 id="where-to-go-next">Where to go next</h2><ul>{nxt}</ul>
<h2 id="sources">Sources</h2><p>{ph(a["sources"], "sources")}</p>
<h2 id="common-questions">Common questions</h2>''']
    CTX.setdefault("faq", [])
    for q, ans in a["faq"]:
        CTX["faq"].append((q, ans))
        h.append(f'<details class="faq__item"><summary><span>{esc(q)}</span><span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__body">{md(ans)}</div></details>')
    h.append(f'''<aside class="cta-card"><h2 class="h3">Want this answered for your own business?</h2><p>The Business Assessment gives you a score, a ranked list and the dollar cost of each item.</p><div class="btn-row">{buy_btn()} {book_btn()}</div></aside>
<aside class="byline-card" aria-label="About the author"><p class="brand__mark" aria-hidden="true">M</p><div><p><strong>MarvelUs</strong></p><p class="small">A Melbourne business helping businesses use AI where it earns its place.</p></div></aside>
</div></div>
<section class="section section--dim"><div class="wrap"><h2>Keep reading</h2><div class="cards cards--3 cards--equal">{"".join(keep)}</div></div></section></article>''')
    return "\n".join(h)

def make_article_page(a):
    @page(f'/insights/{a["slug"]}/', f'{a["title"]} | MarvelUs', a["dek"])
    def _p(a=a):
        return article_html(a)
for _a in ARTICLES:
    make_article_page(_a)

@page("/insights/template/", "Article template | MarvelUs", "The layout every MarvelUs insight article follows.")
def article_template():
    t = {"slug": "template", "topic": "[Topic]", "type": "[Guide or Playbook]", "read": "[N] min", "title": "Article template, not an article",
         "dek": "Question-style headings, key takeaways, sources and common questions. Nothing on this page is real content.",
         "take": ["Five to seven takeaways go here."], "body": "## Question-style heading one?\n\nShort paragraphs, plain words.\n\n## Question-style heading two?\n\nUse a table only when it helps.",
         "next": [("Link to a related page", "/assessment/")], "sources": "3 to 5 real, verified sources", "faq": [("Common question one?", "Short answer.")]}
    return article_html(t, True)

@page("/insights/", "Insights | MarvelUs", "Plain guides on AI for Australian small and mid-sized businesses. What it costs, what it does and when it is not worth it.")
def insights():
    h = [hero("Insights", "AI explained for businesses that have a business to run.",
        "Short, straight guides. No hype, no jargon for its own sake, and no pretending that every problem needs AI.", "", crumb=[("Home", "/"), ("Insights", "/insights/")])]
    counts = {t: 0 for t in TOPICS}
    for a in ARTICLES:
        counts[a["topic"]] += 1
    for _, tp, _ in OUTLINES:
        counts[tp] += 1
    chips = '<button type="button" class="chip" data-filter="all" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" class="chip" data-filter="{slug(t)}" aria-pressed="false">{esc(t)} ({counts[t]})</button>' for t in TOPICS)
    rows = ""
    for a in ARTICLES:
        rows += (f'<article class="row" data-tags="{slug(a["topic"])}"><div class="row__meta"><p class="tag">{esc(a["topic"])}</p><p class="small muted">{esc(a["type"])} · {ph("publish date", "dates")}</p></div>'
                 f'<div><h2 class="h3"><a href="/insights/{a["slug"]}/">{esc(a["title"])}</a></h2><p>{esc(a["dek"])}</p><p class="small muted">By MarvelUs · {esc(a["read"])} read</p></div></article>')
    for t, tp, _ in OUTLINES:
        rows += (f'<article class="row row--outline" data-tags="{slug(tp)}"><div class="row__meta"><p class="tag">{esc(tp)}</p><p class="small muted">Outline, not yet written</p></div>'
                 f'<div><h2 class="h3"><a href="/insights/outlines/#{slug(t)}">{esc(t)}</a></h2><p class="small muted">Outline only. Sources need checking before this is written.</p></div></article>')
    h.append(section(f'<div class="chips" role="group" aria-label="Filter by topic">{chips}</div><div class="rows" id="ins-rows">{rows}</div><p class="small"><a class="text-link" href="/insights/template/">See the article template</a> · <a class="text-link" href="/insights/outlines/">See all outlines</a></p>'))
    h.append(cta_band("Want this answered for your own business?"))
    return "\n".join(h)

@page("/insights/outlines/", "Article outlines | MarvelUs", "Six MarvelUs insight articles that are outlined but not yet written.")
def outlines():
    h = [hero("Insights", "Article outlines", "Six guides on the way. These are outlines only, not finished articles. Each needs real sources checked before it is written.",
              "", crumb=[("Home", "/"), ("Insights", "/insights/"), ("Outlines", "/insights/outlines/")])]
    items = ""
    for t, tp, hs in OUTLINES:
        extra = ""
        if "digital support cost" in t:
            extra = f'<p>{ph("real MarvelUs pricing is not published, so this article needs a pricing decision first", "pricing")}</p>'
        if "privacy" in t:
            extra = f'<p>{ph("legal review before publishing", "legal")}</p>'
        if "consultant" in t:
            extra = "<p class=\"small muted\">Do not name competitor firms.</p>"
        items += f'<article class="card card--outline" id="{slug(t)}"><p class="tag">{esc(tp)} · Outline</p><h2 class="h3">{esc(t)}</h2><ol>{"".join(f"<li>{esc(x)}</li>" for x in hs)}</ol>{extra}</article>'
    h.append(section(f'<div class="cards cards--2">{items}</div>'))
    h.append(cta_band("Want this answered for your own business?"))
    return "\n".join(h)

# ------------------------------------------------------------------ sample report
@page("/report/sample/", "Sample Business Assessment report | MarvelUs", "An example of the report you receive from a MarvelUs Business Assessment. Invented data, not a client's report.", bodyclass="report")
def sample_report():
    from pages_a import ladder_bars
    r = SN
    lowest_name = [d[1] for d in DIMENSIONS if d[0] == r["lowest"]][0]
    rows = ""
    for i, x in enumerate(r["rows"], 1):
        cost = x["monthly_cost"]
        lab = {"counts": "Counts as money", "zero": "Counts as zero", "unknown": "Unknown"}[x["route"]]
        rows += (f'<tr><th scope="row">{i}. {sample_tag(x["name"])}</th><td>{x["hours"]}</td><td>${SAMPLE_RATE}</td>'
                 f'<td>{x["hours"]} &times; ${SAMPLE_RATE} &times; {WEEKS} = <strong>{money(cost)}</strong></td><td><span class="route route--{x["route"]}">{lab}</span><br><span class="small">{esc(x["note"])}</span></td></tr>')
    h = [f'''<section class="hero hero--page"><div class="wrap wrap--hero">{crumbs([("Home", "/"), ("Sample report", "/report/sample/")])}
<p class="banner">Example only. This is not a real client's report. Every name and number below is invented.</p>
{eyebrow("Sample report")}<h1>A sample Business Assessment report</h1>
<p class="lede lede--lg">This is what you would receive, emailed {esc(CFG["reportTurnaround"])}. A real report uses your own answers, your own hours and your own rate.</p>
<div class="btn-row">{buy_btn()} {book_btn()} <button class="btn btn--ghost" type="button" data-print>Print this page</button></div></div></section>''']
    h.append(section(f'''<h2>1. Cover</h2><dl class="kv kv--wide"><dt>Business</dt><dd>{sample_tag("Example Plumbing Pty Ltd")}</dd><dt>Date</dt><dd>{sample_tag("1 January 2027")}</dd><dt>Readiness score</dt><dd>{sample_tag(f"{r['score']} / 100")}</dd></dl>'''))
    h.append(section(f'''<h2>2. Where you are</h2><p class="lede">Five dimensions, each on a five-point ladder from ad hoc to optimised. The score is the average level shown as a share of the top level: {r["avg_level"]:.1f} of 5, which is {r["score"]} out of 100.</p>
{ladder_bars(SAMPLE_DIMS, r["lowest"])}
<p><strong>The lowest dimension is {esc(lowest_name)}.</strong> {sample_tag("Customer and job details sit in email and in exports from the accounting software, so each quote starts by hunting for them.")} That is where the first fixes belong, ahead of the headline number.</p>
<ul class="read-lines">{"".join(f"<li><strong>{esc(n)}.</strong> {sample_tag(t)}</li>" for (k, n, _), t in zip(DIMENSIONS, ["Core job and accounting software is capable and in use. No AI in use yet.", "Data is spread across inboxes and spreadsheets and is hard to reach.", "Most work is defined, with gaps at handover.", "A few reminders run on their own. Most steps are moved by hand.", "The team is open to it. Nobody owns it yet."]))}</ul>''', "section--dim"))
    h.append(section(f'''<h2>3. Your opportunities, ranked</h2><p class="lede">Ranked by what each is worth in time. The last column applies the money rule: hours only count as money when spend stops, a planned hire is avoided or confirmed waiting demand is served, one per workflow.</p>
<div class="table-wrap"><table class="report-table"><caption class="sr-only">Ranked opportunities with the maths</caption><thead><tr><th scope="col">Opportunity</th><th scope="col">Hours a week</th><th scope="col">Rate an hour</th><th scope="col">The maths</th><th scope="col">Does it count as money?</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Time cost in total: {r["total_hours"]} hours &times; ${SAMPLE_RATE} &times; {WEEKS} = <strong>{money(r["total_monthly"])} a month</strong>, about {money(r["total_monthly"]*12)} a year. Counted as money under the rule: <strong>{money(r["counted_monthly"])} a month</strong>. The rest is time, not money, or unknown.</p>'''))
    h.append(section(f'''<h2>4. The maths</h2><p>Hours a week &times; hourly rate &times; {WEEKS} weeks in a month = cost a month. Multiply by 12 for the year. Every figure traces to something said on the call. Missing facts stay unknown. Any effect on sales is counted at gross profit, not revenue. If hours just disappear into the day, the number is zero.</p>''', "section--dim"))
    h.append(section(f'''<h2>5. What to do first</h2><ol class="read-lines"><li>{sample_tag("Save your five best recent quotes in one folder, then draft new quotes from them.")}</li><li>{sample_tag("Write out-of-hours replies for the five most common enquiries and send them automatically.")}</li><li>{sample_tag("Move supplier orders to one template for your top three suppliers.")}</li></ol>
<h2>6. What to leave alone</h2><p>{sample_tag("Weekly reporting built by hand: it takes 2 hours, nobody reads it and removing it saves more than automating it. Delete it first.")}</p>'''))
    h.append(section(f'''<h2>7. Your call transcript (excerpt)</h2><div class="transcript" aria-label="Example transcript excerpt"><p><strong>Agent:</strong> {sample_tag("Tell me about the last quote you sent. What happened between the enquiry and the send?")}</p><p><strong>Owner:</strong> {sample_tag("Usually three days. I wait for the supplier price, then retype it all into the accounting software.")}</p><p><strong>Agent:</strong> {sample_tag("How many of those a week?")}</p></div>
<p class="small muted">Invented for this example. Real transcripts are yours and are not shown anywhere.</p>''', "section--dim"))
    h.append(cta_band("Get a report like this for your business.", f"The Business Assessment is {PRICE_LONG}."))
    return "\n".join(h)

# ------------------------------------------------------------------ legal
def legal_page(path, title, desc, h1, sections, extra=""):
    @page(path, f"{title} (draft) | MarvelUs", desc)
    def _p():
        body = "".join(f"<h2 id=\"{slug(s)}\">{esc(s)}</h2><p>{ph(f'{s.lower()} text to be written or reviewed by a qualified Australian lawyer', 'legal')}</p>" for s in sections)
        return (hero("Legal", h1, "This page is a skeleton.", "", crumb=[("Home", "/"), (title, path)]) +
                section(f'<p class="banner banner--warn" role="note"><strong>Draft. Not legal text.</strong> This page must be written or reviewed by a qualified Australian lawyer before launch. Do not rely on it.</p><div class="read">{extra}{body}</div>'))
    return _p

legal_page("/privacy/", "Privacy", "Draft privacy policy skeleton for MarvelUs. Needs lawyer review before launch.", "Privacy Policy",
           ["Who we are", "What you give us", "What we collect automatically", "How we use it", "Who we share it with", "How long we keep it", "Security",
            "Your choices and rights, including access and correction under Australian privacy law", "Voice call recordings and transcripts", "Children", "Third-party links", "Changes", "Contact"])
legal_page("/terms/", "Terms", "Draft terms skeleton for MarvelUs. Needs lawyer review before launch.", "Terms",
           ["Using the site", "Information, not advice", "The free preview", "The Business Assessment (what is delivered, what it is not)", "Bookings, events and purchases", "Results and testimonials",
            "Our content", "Your content", "Third-party services", "Disclaimer", "Limitation of liability", "Governing law (Victoria, Australia)", "Changes", "Contact"])
legal_page("/cookies/", "Cookies", "Draft cookie policy skeleton for MarvelUs. Needs lawyer review before launch.", "Cookie Policy",
           ["What we use", "Your choices", "Manage cookies", "Changes", "Contact"],
           extra='<p>This draft site sets no analytics or advertising cookies, and the free preview quiz stores nothing. If that changes, a cookie bar with Accept, Keep off and Choose controls will be added, and it will honour the browser privacy signal (Global Privacy Control). The text below must then match what is actually used.</p>')

@page("/404.html", "Page not found | MarvelUs", "That page does not exist. Try the home page or the site map.", kind="404")
def notfound():
    return hero("404", "That page is not here.", "The link may be old or mistyped. Try the home page, or one of these.", btn("Home", "/", "primary") + book_btn() + buy_btn("Get the assessment", "secondary"), center=True)
