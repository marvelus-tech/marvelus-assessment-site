"""Shared facts and data. Everything public-facing that more than one page uses lives here."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "site.config.json").read_text())

WEEKS = CFG["weeksPerMonth"]
RATE = CFG["previewHourlyRate"]
PRICE = CFG["assessmentPriceLabel"]            # "$1,000 + GST"
PRICE_LONG = "$1,000 AUD + GST"
CALL = CFG["callLength"]                        # "about 15 minutes"

LADDER = [
    (1, "Ad hoc", "Done differently each time, if at all."),
    (2, "Emerging", "Some pieces exist, but they are patchy."),
    (3, "Defined", "Written down and mostly followed."),
    (4, "Managed", "Measured and checked on a regular basis."),
    (5, "Optimised", "Tuned over time, with little manual effort."),
]

DIMENSIONS = [
    ("tooling", "Tooling", "Whether the software running your core work is capable, and what AI is already in use."),
    ("data", "Data readiness", "Whether your data is in one place, clean and reachable, or trapped in exports and inboxes."),
    ("process", "Process maturity", "Whether workflows are defined and repeatable, or live in individual people's heads."),
    ("automation", "Automation", "How much already runs without someone moving it along by hand."),
    ("team", "Team and AI literacy", "Whether your people are ready to use it, and whether leadership is driving it."),
]

METHOD = [
    ("Question the requirement.", "Does this work need to happen at all?"),
    ("Delete.", "Remove what should not be there."),
    ("Simplify and standardise.", "Make what is left the same way every time."),
    ("Speed up the handovers.", "Cut the waiting between people and between systems."),
    ("Automate last.", "Only where a person does not need to decide."),
]

PRICED = "Priced by headcount"
STAFF_RANGE = "15 to 150"
BOOK_CHAT = "Book the 10-minute chat"
STAFF_RATE = 53.71                               # Victorian average hourly rate, used as the default when a business does not share pay rates
EXAMPLE_TIMES, EXAMPLE_MINUTES = 10, 60          # illustrative estimator example from the call deck, not client data

NICHES = [
    ("Trades and construction", "Quotes, job scheduling, variations and invoicing."),
    ("Multi-practitioner clinics", "Bookings, reminders, intake forms and rescheduling."),
    ("Real estate", "Enquiries, inspection bookings, follow-ups and listing paperwork."),
    ("NDIS providers", "Scheduling, shift notes, plan paperwork and invoicing."),
    ("Logistics and transport", "Quotes, bookings, dispatch scheduling and invoicing."),
    ("Manufacturers and fabricators", "Quotes, job paperwork, ordering and invoicing."),
    ("Auto repair", "Bookings, quotes, parts ordering and invoicing."),
]

STAFF_STEPS = [
    ("A 10-minute chat.", "A short call with the owner. We ask where the time goes and which tasks come to mind. You decide if it is worth going further, and we say so if it is not."),
    ("The paid assessment.", "Your team does a short survey of about 5 minutes. It ends with a 15 minute chat with each person, recorded with an AI note taker only with their explicit consent."),
    ("Findings and presentation.", "A findings report with every task as times per week, minutes each, hours a year and dollars a year, ranked, with no names. Then we present it to leadership, with one working demo on your own redacted paperwork."),
    ("Optional ongoing support.", "An optional ongoing support step, scoped after the findings."),
]

ASSESSMENT_STEPS = [
    ("Pay once.", f"{PRICE_LONG} through secure checkout. No subscription and no booking link to chase."),
    ("Call when you are ready.", f"After payment you see a call-in number and your own access code. Ring any time that suits you. An AI voice agent asks the questions and follows your answers. It takes {CALL}."),
    ("We build your report.", "From what you said, we work out where your hours go, what that costs, and which fixes are worth doing first."),
    ("You decide.", "You get a written report and the call transcript. Use it yourself, hand it to your team, or ask us to help. It is your choice."),
]

OFFERS = [
    {
        "id": "staff-assessment", "name": "Staff-level AI Assessment", "tag": "Ask the people doing the work", "url": "/assessment/",
        "summary": f"For businesses with roughly {STAFF_RANGE} staff. A 10-minute chat with the owner, then a short survey and a 15 minute chat with each person on your team. You get every repeat task in hours and dollars a year, ranked, with no names.",
        "price": PRICED, "cta": "Book the 10-minute chat",
    },
    {
        "id": "digital-support", "name": "Digital support", "tag": "Chat or voice", "url": "/services/digital-support/",
        "summary": "An AI assistant that answers questions by chat or by phone, for your customers or for your own staff. It uses your information, hands off to a person when it should, and keeps a record of every conversation.",
        "price": "Scoped to your business", "cta": "Book a call",
    },
    {
        "id": "seo", "name": "SEO", "tag": "Be found", "url": "/services/seo/",
        "summary": "Search work that gets the right people to your site and makes sure they can act when they arrive. We fix what is broken, write what is missing and report what changed.",
        "price": "Scoped to your business", "cta": "Book a call",
    },
]

# The smaller first step. It sits in the assessment area next to the lead offer. It is not one of the three equal offers.
BIZ = {
    "id": "business-assessment", "name": "Business Assessment (AI Readiness)", "tag": "A smaller first step you can start now", "url": "/business-assessment/",
    "summary": f"A phone intake call of {CALL} and a full written report. You get a score out of 100, your opportunities ranked, and the monthly cost of each one in dollars.",
    "price": PRICE_LONG, "cta": "Get the Business Assessment",
}

# ---------------------------------------------------------------- quiz data
INDUSTRIES = [
    {"id": "trades", "label": "Trades and construction", "noun": "job", "nouns": "jobs", "doc": "quote",
     "tool5": "Job management software", "notes": "", "cost_extra": None,
     "kw": ["plumb", "electric", "builder", "build ", "construction", "roof", "carpent", "tradie", "trade", "hvac", "paint", "landscap", "job", "site visit"],
     "ph": "Every Friday I chase approved quotes and retype them into Xero."},
    {"id": "hospitality", "label": "Hospitality", "noun": "booking", "nouns": "bookings", "doc": "event quote",
     "tool5": "Booking or point-of-sale software", "cost_extra": "Guests book somewhere else",
     "kw": ["restaurant", "cafe", "bar ", "pub", "hotel", "venue", "catering", "function", "guest", "hospitality", "kitchen"],
     "ph": "Booking enquiries come in by phone, email and Instagram and someone has to answer them all."},
    {"id": "professional", "label": "Professional services", "noun": "client matter", "nouns": "client matters", "doc": "proposal",
     "tool5": "Practice or time-billing software", "cost_extra": None,
     "kw": ["accountant", "accounting", "law", "legal", "consult", "advis", "architect", "engineer", "bookkeep", "agency", "client matter", "proposal"],
     "ph": "We write a new proposal from scratch every time, then chase the client for a yes."},
    {"id": "health", "label": "Health and wellbeing", "noun": "appointment", "nouns": "appointments", "doc": "treatment plan",
     "tool5": "Clinic or practice management software", "cost_extra": "Patients miss appointments",
     "kw": ["clinic", "patient", "dental", "dentist", "physio", "gp ", "medical", "health", "allied", "psycholog", "wellbeing", "chiro"],
     "ph": "The front desk spends the day on reminders, reschedules and intake forms."},
    {"id": "retail", "label": "Retail and e-commerce", "noun": "order", "nouns": "orders", "doc": "quote",
     "tool5": "Online store or inventory software", "cost_extra": "Shoppers leave without buying",
     "kw": ["shop", "store", "retail", "ecommerce", "e-commerce", "online store", "shopify", "stock", "customers ask"],
     "ph": "Customers ask the same five questions by email and chat all day."},
    {"id": "other", "label": "Something else", "noun": "job", "nouns": "jobs", "doc": "quote",
     "tool5": "Job, booking or practice management software", "cost_extra": None, "kw": [],
     "ph": "Every Monday someone copies numbers from three places into one report."},
]

HOUR_BANDS = [
    {"id": "1-2", "label": "1 to 2 hours", "mid": 1.5},
    {"id": "2-5", "label": "2 to 5 hours", "mid": 3.5},
    {"id": "5-10", "label": "5 to 10 hours", "mid": 7.5},
    {"id": "10-20", "label": "10 to 20 hours", "mid": 15},
    {"id": "20-40", "label": "20 to 40 hours", "mid": 30},
    {"id": "40+", "label": "40+ hours", "mid": 50},
    {"id": "unsure", "label": "Not sure", "mid": None},
]

REVENUE_BANDS = ["Under $500K", "$500K to $1M", "$1M to $3M", "$3M to $10M", "$10M or more", "Rather not say"]

TOOLS_DEFAULT = ["Email", "Excel or Google Sheets", "Xero, MYOB, QuickBooks or other accounting software",
                 "A CRM or customer list", "{tool5}", "Word documents or PDFs", "Paper, phone calls or text messages"]
COST_DEFAULT = ["The work goes to someone else", "Customers wait longer than they should", "Someone does it after hours", "We wear the rework"]

ROLES = ["Owner or director", "Managing director or CEO", "General or operations manager", "Practice or office manager",
         "Other manager", "Team member", "Other"]
HEARD = ["Google search", "ChatGPT, Claude or another AI assistant", "LinkedIn", "Instagram or Facebook", "Referral", "Event", "Other"]

def S(text, person=False):
    return {"t": text, "person": person}

PACKS = [
 {"id": "A", "name": "Quotes, estimates and proposals",
  "kw": ["quote", "quoting", "estimate", "proposal", "tender", "pricing a", "price a"],
  "problem": "Every {doc} starts from a blank page. Someone pulls details out of {tools}, looks up what similar {nouns} cost, writes it up and chases an approval. The customer waits, and the {doc} that goes out late on a Friday is the one you lose.",
  "breaks": ["Starting each {doc} from scratch", "Waiting for someone to approve it", "Looking up old prices", "Chasing the customer for an answer", "Mistakes in the numbers"],
  "steps": [S("Capture the request"), S("Pull similar past {nouns}"), S("Draft the {doc} in your format"), S("Check the price and approve", True), S("Send and follow up after three days")],
  "week": "Save your five best recent {doc}s in one folder. That folder is what the drafting step learns from, and it costs nothing.",
  "person": "Final pricing and the decision to go ahead.",
  "prompt": "I run a business that does [what you do]. Here are two recent {doc}s and rough notes for a new {noun}. Draft the new {doc} in the same structure and tone, mark every price as [PRICE] for me to fill in, and list the questions you would ask the customer first."},
 {"id": "B", "name": "Scheduling and bookings",
  "kw": ["schedul", "roster", "booking", "appointment", "calendar", "diary", "reschedul", "dispatch", "availability", "no-show", "no show"],
  "problem": "Getting the right person to the right {noun} means juggling {tools}, the phone and whoever is standing at the counter. One change moves the whole day, and the person doing the juggling can never step away.",
  "breaks": ["Double bookings", "Last-minute changes knocking everything out", "Phone tag with customers", "Nobody sure who is free", "No-shows"],
  "steps": [S("Take the request"), S("Check who is free"), S("Book it and confirm"), S("Handle the change"), S("Make the judgement call", True)],
  "week": "Write down the five rules you follow without thinking, such as who covers which area. Those rules are the specification.",
  "person": "Priority requests and anything involving an upset customer.",
  "prompt": "Here is this week's schedule and the rules we follow. A customer just cancelled Thursday morning. Propose the new schedule, explain each move in one line and draft the update message for each affected customer."},
 {"id": "C", "name": "Invoicing and getting paid",
  "kw": ["invoice", "invoicing", "payment", "getting paid", "overdue", "debtor", "receivable", "collections", "chasing money", "chase money"],
  "problem": "The work is done long before the money arrives. Invoices are built by hand from {tools}, sent late, and then someone has to remember to chase them. Your cash sits in other people's accounts while your team does the reminding.",
  "breaks": ["Invoices going out late", "Retyping job details", "Forgetting to chase", "Awkward follow-up conversations", "Payments hard to match"],
  "steps": [S("Build the invoice"), S("Check it matches the work", True), S("Send it the day the work is done"), S("Chase at 7, 14 and 30 days"), S("Match payments in the books")],
  "week": "Pull the list of invoices more than 30 days old. The total at the bottom is what this is costing you right now.",
  "person": "Disputes, and any decision to pause work for non-payment.",
  "prompt": "Here is our list of open invoices with dates and amounts. Group them by how overdue they are, then draft three emails for the oldest one: friendly at 14 days, firm at 30, final at 60."},
 {"id": "D", "name": "Customer enquiries and follow-up",
  "kw": ["enquir", "inquir", "email", "reply", "respond", "inbox", "messages", "follow-up", "follow up", "leads", "same questions", "customers ask", "after hours", "after-hours"],
  "problem": "The inbox is the job. Questions, quote requests, complaints and check-ins all land in {tools}, and the same five answers get typed out dozens of times a week. Whatever is not answered by close of business becomes tomorrow's problem, and some of it never gets answered.",
  "breaks": ["Same questions every day", "Slow replies", "Messages in too many places", "Follow-up forgotten", "Out-of-hours enquiries missed"],
  "steps": [S("Sort what came in"), S("Draft the reply in your voice"), S("Review the sensitive ones", True), S("Send and log it"), S("Follow up if they go quiet")],
  "week": "Save your ten most common replies in one document. They are the first ten things a system learns to draft.",
  "person": "Complaints, and anything that commits you to a price or a date.",
  "prompt": "Below are ten emails from our inbox. Sort them into reply today, reply this week and no reply needed. For the ones due today, draft a reply in my voice using these three emails I wrote as examples."},
 {"id": "E", "name": "Reporting and repeated data entry",
  "kw": ["report", "spreadsheet", "data entry", "copy numbers", "copies numbers", "copying", "re-key", "rekey", "retype", "retyping", "dashboard", "reconcil"],
  "problem": "Someone spends part of every week moving numbers from {tools} into a report that nobody fully trusts. By the time it lands the week it describes is over, and the person who built it could have been doing something that earns money.",
  "breaks": ["Copying between systems", "Numbers that do not match", "Reports always late", "Nobody reads them", "One person holds it all in their head"],
  "steps": [S("Collect the data"), S("Clean it up"), S("Build the report"), S("Read it and decide", True)],
  "week": "List every report built by hand and who reads it. Cross off any nobody would miss.",
  "person": "Deciding what the numbers mean and what to do about them.",
  "prompt": "Here are the exports I combine every week for our report. Build the summary table we use, flag anything that moved more than 10 percent from last week and write the three sentence note I send to the owner."},
 {"id": "F", "name": "Ordering and supplier paperwork",
  "kw": ["supplier", "purchase order", "ordering", "stock", "inventory", "materials", "delivery", "vendor", "reorder"],
  "problem": "Every {noun} needs stock or materials, and every order needs a purchase order, a confirmation, a delivery check and a bill matched back to it. It all runs through {tools} and someone's memory, and the mistakes show up as a missing part on a Tuesday morning.",
  "breaks": ["Orders placed late", "Wrong items arriving", "Bills that do not match", "Chasing suppliers", "No record of what was ordered"],
  "steps": [S("Build the order"), S("Approve it", True), S("Send it and chase the confirmation"), S("Match the bill to the order and delivery"), S("Flag short deliveries and price changes")],
  "week": "Pick your top three suppliers by spend and standardise how you order from them first. That is most of the volume.",
  "person": "Approving spend and choosing suppliers.",
  "prompt": "Here is a job's material list and our last three orders to this supplier. Draft the new order in the same format, flag any item whose price changed and write the confirmation email."},
 {"id": "G", "name": "Hiring and onboarding",
  "kw": ["hiring", "recruit", "onboard", "new starter", "interview", "applicant", "job ad", "new staff"],
  "problem": "Every open role means writing the ad, reading applications, arranging interviews and then walking the new person through the same first week you walked the last one through. It lives in {tools} and in the head of whoever did it last time.",
  "breaks": ["Writing the ad", "Too many unsuited applications", "Interview scheduling", "Inconsistent first weeks", "Paperwork chasing"],
  "steps": [S("Write and post the role"), S("Screen applications against must-haves"), S("Interview and decide", True), S("Onboard on schedule"), S("Check in at day 7 and day 30")],
  "week": "Write down what a great first week looks like for one role. That becomes the checklist the system runs.",
  "person": "Interviews and the hiring decision.",
  "prompt": "Here is what our last good hire actually did in the role. Draft a job ad from it, a short list of must-have questions for screening and a first-week checklist."},
 {"id": "H", "name": "Approvals and job coordination",
  "kw": ["approv", "sign-off", "sign off", "signoff", "status", "handover", "hand over", "coordinat", "project", "waiting on"],
  "problem": "Nothing moves until someone signs off, and nobody can see where a {noun} is stuck without asking. Status lives in {tools} and in people's heads, so the same question gets asked three times and the answer is usually \"waiting on so-and-so\".",
  "breaks": ["Waiting on sign-off", "Asking for status all day", "Forwarded emails with no context", "Things stuck with no reminder", "No single place to look"],
  "steps": [S("Put every request in one queue with what is asked and by when"), S("Send it to the right person with context"), S("Approve, reject or \"not yet\"", True), S("Remind, then escalate"), S("Let anyone check status")],
  "week": "Write down the five approvals that happen most, who signs them and how long they usually wait. That list is the queue.",
  "person": "The decisions themselves, and anything over a dollar limit.",
  "prompt": "Here are the last 20 approval requests with dates. Show me which ones waited longest, who they waited on and what a reminder at 24 hours would have saved."},
 {"id": "Z", "name": "Your repeated task",
  "kw": [],
  "problem": "The work you described is done the same way every time, by a person, out of {tools}. That is the kind of work AI handles well: repeated, rules-based and slow only because someone has to sit through it.",
  "breaks": ["Same steps every time", "Waiting on people", "Retyping", "Checking for errors", "No record"],
  "steps": [S("Whatever starts the work lands in one place"), S("Pull the details from where they live"), S("Steps that are always the same run on their own"), S("A person checks the result", True), S("Deliver and log it")],
  "week": "Time the task once, start to finish, and write down every step. Most owners are surprised by the count.",
  "person": "The judgement call in the middle and the final sign-off.",
  "prompt": "Here is how we do [task] today, step by step. Mark which steps are always the same and which need a judgement call, and suggest the order I should automate them in."},
]

# ---------------------------------------------------------------- sample report (invented, labelled as example everywhere)
SAMPLE_DIMS = {"tooling": 4, "data": 2, "process": 3, "automation": 3, "team": 3}
SAMPLE_RATE = 50
SAMPLE_ROWS = [
    # name, hours/week, money route, note
    ("Chasing and re-keying quotes", 8, "counts", "Serves demand that is already waiting: quotes sit unsent while the team re-keys."),
    ("After-hours enquiries going unanswered", 4, "counts", "Serves demand that is already waiting: enquiries arrive overnight and go cold."),
    ("Weekly reporting built by hand", 2, "zero", "Time returns to the day with no visible change in spend, hiring or demand served, so it counts as zero."),
    ("Chasing overdue invoices", 2, "unknown", "Unknown: the owner has not said whether anyone is paid overtime for this."),
    ("Supplier order paperwork", 2, "counts", "Stops a spend: the overtime paid for this work ends."),
]

def sample_numbers():
    rows = []
    for name, h, route, note in SAMPLE_ROWS:
        cost = h * SAMPLE_RATE * WEEKS
        rows.append({"name": name, "hours": h, "rate": SAMPLE_RATE, "monthly_cost": round(cost), "route": route, "note": note})
    total_h = sum(r["hours"] for r in rows)
    total = round(total_h * SAMPLE_RATE * WEEKS)
    counted = sum(r["monthly_cost"] for r in rows if r["route"] == "counts")
    avg = sum(SAMPLE_DIMS.values()) / 5
    score = round(avg / 5 * 100)
    lowest = min(SAMPLE_DIMS, key=lambda k: SAMPLE_DIMS[k])
    return {"rows": rows, "total_hours": total_h, "total_monthly": total, "counted_monthly": counted,
            "score": score, "avg_level": avg, "lowest": lowest}

SN = sample_numbers()

# ---------------------------------------------------------------- staff-level sample findings report (illustrative example data)
# The first row is the call deck's illustrative figure. The other rows are invented for the example. None of it is client data.
STAFF_ROWS = [
    # role, task, times a week, minutes each, money route label, note
    ("Estimator", "Writing quotes from site notes and photos", EXAMPLE_TIMES, EXAMPLE_MINUTES, "Waiting work gets done", "Quotes sit unsent while the estimator writes them, so some work waits."),
    ("Office administrator", "Retyping job details into the accounting software", 25, 12, "Capacity until used", "The time returns to the day. It only becomes dollars when something changes because of it."),
    ("Project coordinator", "Chasing approvals and missing information", 12, 20, "Capacity until used", "Waiting is part of the delay. Faster replies free time but do not stop any spend by themselves."),
    ("Office administrator", "Answering the same customer questions", 30, 5, "A hire avoided", "Counts only if the business was planning to hire for this and now will not."),
    ("Accounts", "Chasing overdue invoices", 8, 15, "Not known yet", "The business has not said whether anyone is paid overtime for this, so it is not counted as dollars yet."),
]

def staff_numbers():
    rows = []
    for role, task, n, m, route, note in STAFF_ROWS:
        hours_week = n * m / 60
        hours_year = hours_week * 52
        rows.append({"role": role, "task": task, "times_per_week": n, "minutes_each": m, "hours_per_week": hours_week,
                     "hours_per_year": round(hours_year), "dollars_per_year": round(hours_year * STAFF_RATE), "route": route, "note": note})
    rows.sort(key=lambda r: -r["dollars_per_year"])
    return {"rows": rows, "total_hours_year": sum(r["hours_per_year"] for r in rows),
            "total_dollars_year": round(sum(r["hours_per_year"] for r in rows) * STAFF_RATE)}

STAFF_SN = staff_numbers()
EX_HOURS_WEEK = EXAMPLE_TIMES * EXAMPLE_MINUTES / 60            # 10
EX_HOURS_YEAR = round(EX_HOURS_WEEK * 52)                       # 520
EX_DOLLARS_YEAR = round(EX_HOURS_WEEK * 52 * STAFF_RATE)        # 27929
assert (EX_HOURS_WEEK, EX_HOURS_YEAR, EX_DOLLARS_YEAR) == (10, 520, 27929)

def aud(n):
    return "A${:,.0f}".format(n)

def money(n):
    return "${:,.0f}".format(n)

NAV = [("Staff Assessment", "/assessment/"), ("Business Assessment", "/business-assessment/"), ("Services", "/services/"), ("Results", "/results/"),
       ("Pricing", "/pricing/"), ("Insights", "/insights/"), ("About", "/about/")]

SITE_MAP = [
    ("Home", "/", "Staff-level AI Assessment first, then the three offers"),
    ("Staff-level AI Assessment", "/assessment/", f"For businesses with roughly {STAFF_RANGE} staff. {PRICED}. Book a 10-minute chat"),
    ("Business Assessment", "/business-assessment/", f"A smaller first step you can start now. {PRICE_LONG}, phone intake and scored report"),
    ("Services", "/services/", "Three equal offers"),
    ("Digital support", "/services/digital-support/", "AI chat or voice assistant, scoped to your business"),
    ("SEO", "/services/seo/", "Search work, scoped to your business"),
    ("Results", "/results/", "Placeholders until real proof is approved"),
    ("Case studies", "/case-studies/", "Index"),
    ("Case study template", "/case-studies/template/", "Template with required client approvals"),
    ("Pricing", "/pricing/", "Priced by headcount for the staff-level assessment, a fixed price for the smaller first step"),
    ("Insights", "/insights/", "Articles and outlines"),
    ("What is an AI readiness assessment?", "/insights/what-is-an-ai-readiness-assessment/", "Article"),
    ("How to work out the cost of a repeated task", "/insights/how-to-work-out-the-cost-of-a-repeated-task/", "Article"),
    ("Article outlines", "/insights/outlines/", "Six outlines, not yet written"),
    ("Article template", "/insights/template/", "Template"),
    ("Events", "/events/", "Placeholders"),
    ("About", "/about/", "MarvelUs, how we work"),
    ("Book the 10-minute chat", "/book/", "Booking with a placeholder embed slot"),
    ("AI consulting in Melbourne", "/ai-consulting-melbourne/", "Melbourne based, remote across Australia"),
    ("Sample staff-level findings report", "/report/sample/", "Example report, illustrative data, not client data"),
    ("Sample Business Assessment report", "/report/business-assessment-sample/", "Example report, invented data"),
    ("Privacy (draft)", "/privacy/", "Draft, needs lawyer review"),
    ("Terms (draft)", "/terms/", "Draft, needs lawyer review"),
    ("Cookies (draft)", "/cookies/", "Draft, needs lawyer review"),
]

def agent_data():
    base = CFG["siteUrl"]
    staff_rows = [{"rank": i + 1, "role": r["role"], "task": r["task"], "times_per_week": r["times_per_week"], "minutes_each": r["minutes_each"],
                   "hours_per_year": r["hours_per_year"], "dollars_per_year_aud": r["dollars_per_year"], "money_route": r["route"]}
                  for i, r in enumerate(STAFF_SN["rows"])]
    return {
        "offers": [{"id": o["id"], "name": o["name"], "tag": o["tag"], "price": o["price"], "url": o["url"],
                    "summary": o["summary"]} for o in OFFERS],
        "assessment_area": {
            "lead": {"id": OFFERS[0]["id"], "name": OFFERS[0]["name"], "pricing": PRICED, "url": OFFERS[0]["url"]},
            "smaller_first_step": {"id": BIZ["id"], "name": BIZ["name"], "price_label": PRICE, "url": BIZ["url"],
                                   "note": "A smaller first step you can start now."},
        },
        "assessment": {
            "name": "Staff-level AI Assessment",
            "role": "The lead offer",
            "for": f"Businesses with roughly {STAFF_RANGE} staff, owner-led or run by an owner and a general manager, with a lot of repeatable admin.",
            "idea": "We ask the people doing the work, not only the owner.",
            "pricing": {"model": PRICED, "amount": None, "published_figures": False,
                        "how_to_get_a_quote": "Book the 10-minute chat. A quote follows once we know the headcount."},
            "path": [{"step": i + 1, "name": a, "detail": b} for i, (a, b) in enumerate(STAFF_STEPS)],
            "what_is_delivered": [
                "Team survey: about 5 minutes per person, ending with a booking for a 15 minute chat.",
                "A 15 minute chat with each person, recorded with an AI note taker with explicit consent.",
                "Findings report: every task as times per week, minutes each, hours a year and dollars a year, ranked, with no names.",
                "Findings presentation to leadership, including one working demo on the business's own redacted paperwork."],
            "tasks_not_jobs_promise": "Answers are grouped by task and role, never by name. Nobody is being assessed.",
            "dollar_maths": "times per week x minutes each x 52 x pay rate = dollars a year. The Victorian average rate is used if the business prefers not to share pay rates.",
            "honesty_rule": "Hours only count as dollars when spend stops, a hire is avoided, or waiting work gets done. Recovered time is capacity until it is used.",
            "staff_time_cost": "A 5 minute survey and a 15 minute chat for each person. One call for the owner.",
            "optional_next_step": "An optional ongoing support step, scoped after the findings.",
            "consent_and_privacy": "Recording needs explicit consent. Retention plan and handling of declined recordings are placeholders until MarvelUs confirms them. Not legal advice.",
            "who_we_work_with": [{"name": n, "repeat_admin": d} for n, d in NICHES],
            "location": "Melbourne based, working remotely with businesses anywhere in Australia.",
            "sample_report_url": base + "/report/sample/",
            "book_the_chat_url": base + CFG["bookingPath"],
            "smaller_first_step": {"name": BIZ["name"], "price_label": PRICE, "url": base + BIZ["url"], "purchase_url": CFG["purchaseUrl"]},
        },
        "business_assessment": {
            "name": "Business Assessment (AI Readiness)",
            "role": "A smaller first step you can start now",
            "price": {"amount": CFG["assessmentPriceAUD"], "currency": "AUD", "gst_included": False,
                      "label": PRICE, "note": "GST is added on top of the price."},
            "duration": CALL,
            "format": "Phone intake call with an AI voice agent, then a written report",
            "report_delivery": f"Emailed {CFG['reportTurnaround']}. Operational detail still to be confirmed by MarvelUs.",
            "score": "0 to 100, a roll-up of five dimensions",
            "dimensions": [{"id": d[0], "name": d[1], "meaning": d[2]} for d in DIMENSIONS],
            "maturity_ladder": [{"level": l[0], "name": l[1]} for l in LADDER],
            "lowest_dimension_note": "The lowest dimension matters more than the headline number, because that is where the first fixes belong.",
            "process": [{"step": i + 1, "name": s[0], "detail": s[1]} for i, s in enumerate(ASSESSMENT_STEPS)],
            "method": [{"step": i + 1, "name": m[0], "detail": m[1]} for i, m in enumerate(METHOD)],
            "cost_maths": f"hours per week x hourly rate x {WEEKS} = cost per month",
            "roi_rule": [
                "Hours only count as money if spend stops, a planned hire is avoided, or confirmed waiting demand gets served.",
                "One of those per workflow, never two.",
                "Revenue effects are counted as gross profit, not revenue.",
                "Every figure traces to something the client said. Missing facts stay unknown.",
                "If the hours just disappear into the day, the number is zero."],
            "purchase_url": CFG["purchaseUrl"],
            "sample_report_url": base + "/report/business-assessment-sample/",
            "details_url": base + BIZ["url"],
        },
        "pricing": {
            "staff_level_assessment": {"model": PRICED, "amount": None, "published_figures": False, "cta": "Book the 10-minute chat to get a quote"},
            "business_assessment": {"amount": CFG["assessmentPriceAUD"], "currency": "AUD", "gst_included": False, "label": PRICE,
                                    "note": "A smaller first step you can start now."},
            "digital_support": {"price": None, "label": "Scoped to your business", "cta": "Book a call"},
            "seo": {"price": None, "label": "Scoped to your business", "cta": "Book a call"},
            "notes": "The staff-level assessment is priced by headcount and has no published figures. Digital support and SEO have no published price.",
        },
        "sample_report": {
            "label": "Example only, illustrative data, not client data",
            "url": base + "/report/sample/",
            "pay_rate_used_aud_per_hour": STAFF_RATE,
            "pay_rate_note": "Victorian average, used as the default when a business does not share pay rates.",
            "illustration": {"role": "Estimator", "task": "Writing quotes", "times_per_week": EXAMPLE_TIMES, "minutes_each": EXAMPLE_MINUTES,
                             "hours_per_week": EX_HOURS_WEEK, "hours_per_year": EX_HOURS_YEAR, "dollars_per_year_aud": EX_DOLLARS_YEAR},
            "ranked_tasks": staff_rows,
            "total_hours_per_year": STAFF_SN["total_hours_year"],
            "total_dollars_per_year_aud": STAFF_SN["total_dollars_year"],
            "honesty_rule": "Hours only count as dollars when spend stops, a hire is avoided, or waiting work gets done. Recovered time is capacity until it is used.",
            "business_assessment_sample_url": base + "/report/business-assessment-sample/",
        },
        "quiz": {
            "url": base + "/#start",
            "steps": ["Your website (optional)", "The bottleneck", "The hours", "Where it breaks", "The tools", "The cost",
                      "The size (annual revenue band, AUD)", "Your first name", "Building your result"],
            "extra_screens": ["Industry check", "Email gate (demo, nothing is sent)", "Result (example-style preview)"],
            "result_next_steps": {"primary": "Book the 10-minute chat (staff-level assessment)", "secondary": f"Business Assessment, {PRICE_LONG}"},
            "stored_or_transmitted": "Nothing. The quiz runs in the browser only.",
            "preview_hourly_rate_aud": RATE,
        },
        "contact": {
            "state": "placeholder",
            "email": CFG["contactEmail"] or None,
            "phone": CFG["contactPhone"] or None,
            "booking_path": CFG["bookingPath"],
            "booking_embed_connected": bool(CFG["bookingEmbedUrl"]),
            "message": "Contact email and phone are not published yet. Use the booking page for the 10-minute chat.",
        },
        "location": {"base": "Melbourne, Australia", "delivery": "Remote, anywhere in Australia"},
        "site_map": [{"title": t, "path": p, "note": n} for t, p, n in SITE_MAP],
    }
