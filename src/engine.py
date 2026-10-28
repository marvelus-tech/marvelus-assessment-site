"""Tiny static-site engine: layout, helpers, mini markdown, link rewriting."""
import html, json, re
from content_core import CFG, NAV, PRICE, PRICE_LONG, agent_data

SITE = CFG["siteUrl"].rstrip("/")
PAGES = []          # (path, meta, fn)
CTX = {}            # per-page working state

def page(path, title, desc, schema=None, quiz=False, bodyclass="", extra_js=None, kind="page", nav=None):
    def deco(fn):
        PAGES.append({"path": path, "title": title, "desc": desc, "schema": schema or [], "quiz": quiz,
                      "bodyclass": bodyclass, "extra_js": extra_js or [], "fn": fn, "kind": kind})
        return fn
    return deco

# ------------------------------------------------------------------ inline helpers
def esc(s):
    return html.escape(s, quote=False)

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

ALL_PH = set()

def ph(text, kind="proof"):
    CTX.setdefault("ph", []).append(kind)
    ALL_PH.add((kind, text))
    return f'<span class="ph" data-ph="{kind}">[PLACEHOLDER: {esc(text)}]</span>'

def sample_tag(text):
    return f'<span class="sample-data" data-sample="1">{esc(text)}</span>'

def email_html():
    e = CFG["contactEmail"]
    if e:
        return f'<a href="mailto:{html.escape(e)}">{esc(e)}</a>'
    return ph("contact email", "contact")

def phone_html():
    p = CFG["contactPhone"]
    if p:
        return f'<a href="tel:{re.sub(r"[^0-9+]", "", p)}">{esc(p)}</a>'
    return ph("contact phone, optional", "contact")

def inline(s):
    s = esc(s)
    s = re.sub(r"\[\[PH:(\w+)\|(.+?)\]\]", lambda m: ph(html.unescape(m.group(2)), m.group(1)), s)
    s = re.sub(r"\[\[SAMPLE:(.+?)\]\]", lambda m: sample_tag(html.unescape(m.group(1))), s)
    s = s.replace("{{EMAIL}}", email_html()).replace("{{PHONE}}", phone_html())
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    def link(m):
        url = m.group(2).replace("{{PURCHASE}}", CFG["purchaseUrl"])
        cls = ' class="text-link"'
        ext = ' rel="noopener"' if url.startswith("http") else ""
        return f'<a{cls} href="{url}"{ext}>{m.group(1)}</a>'
    s = re.sub(r"\[([^\]]+?)\]\(([^)\s]+?)\)", link, s)
    return s

def md(text, h2ids=True):
    """Mini markdown: ## h2, ### h3, - list, 1. list, raw html blocks starting with <, paragraphs."""
    out = []
    blocks = re.split(r"\n\s*\n", text.strip("\n"))
    for b in blocks:
        b = b.strip("\n")
        if not b.strip():
            continue
        lines = b.split("\n")
        first = lines[0]
        if first.startswith("<"):
            out.append(b)
        elif first.startswith("## "):
            t = first[3:].strip()
            out.append(f'<h2 id="{slug(t)}">{inline(t)}</h2>')
            rest = "\n".join(lines[1:])
            if rest.strip():
                out.append(md(rest))
        elif first.startswith("### "):
            t = first[4:].strip()
            out.append(f'<h3 id="{slug(t)}">{inline(t)}</h3>')
            rest = "\n".join(lines[1:])
            if rest.strip():
                out.append(md(rest))
        elif all(l.startswith("- ") for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lines) + "</ul>")
        elif all(re.match(r"\d+\. ", l) for l in lines):
            out.append("<ol>" + "".join(f"<li>{inline(re.sub(r'^\d+\. ', '', l))}</li>" for l in lines) + "</ol>")
        elif first.startswith("> "):
            out.append("<blockquote><p>" + inline(" ".join(l[2:] for l in lines)) + "</p></blockquote>")
        else:
            out.append("<p>" + inline(" ".join(lines)) + "</p>")
    return "\n".join(out)

# ------------------------------------------------------------------ components
def btn(label, href, kind="primary", extra=""):
    return f'<a class="btn btn--{kind}" href="{href}" {extra}>{esc(label)}<span class="btn__arrow" aria-hidden="true">&rarr;</span></a>'

def buy_btn(label="Get the assessment", kind="primary", where="page"):
    return btn(label, "{{PURCHASE}}", kind, f'data-cta="purchase" data-where="{where}"')

def book_btn(label="Book a call", kind="secondary"):
    return btn(label, "/book/", kind, 'data-cta="book"')

def quiz_btn(label="Show me my #1 opportunity", kind="primary"):
    href = "#start" if CTX.get("quiz") else "/assessment/#start"
    return btn(label, href, kind, 'data-open-quiz="1"')

def book_line(prefix="Prefer to talk it through? "):
    return f'<p class="soft-line">{esc(prefix)}<a class="text-link" href="/book/">Book a call.</a></p>'

def eyebrow(t):
    return f'<p class="eyebrow">{esc(t)}</p>'

def crumbs(items):
    """items: list of (label, path or None)."""
    CTX["crumbs"] = items
    li = []
    for i, (l, p) in enumerate(items):
        if p and i < len(items) - 1:
            li.append(f'<li><a href="{p}">{esc(l)}</a></li>')
        else:
            li.append(f'<li aria-current="page">{esc(l)}</li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(li)}</ol></nav>'

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def faq(items, heading="Questions, answered.", h_id="faq", lead=None):
    """items: list of (question, answer_md). Registers FAQPage data."""
    CTX.setdefault("faq", [])
    rows = []
    for q, a in items:
        a_html = md(a)
        CTX["faq"].append((q, strip_tags(a_html)))
        rows.append(f'<details class="faq__item"><summary><span>{esc(q)}</span><span class="faq__icon" aria-hidden="true"></span></summary><div class="faq__body">{a_html}</div></details>')
    lead_html = f"<p class=\"lede\">{inline(lead)}</p>" if lead else ""
    return (f'<section class="section" id="{h_id}" aria-labelledby="{h_id}-h"><div class="wrap wrap--read">'
            f'<h2 id="{h_id}-h">{esc(heading)}</h2>{lead_html}<div class="faq">{"".join(rows)}</div></div></section>')

def cta_band(h2, sub=None, buttons=None, extra_line=None):
    sub_html = f'<p class="lede">{inline(sub)}</p>' if sub else ""
    btns = "".join(buttons) if buttons else buy_btn() + " " + book_btn()
    line = extra_line or ""
    return (f'<section class="cta-band" aria-labelledby="cta-h"><div class="wrap wrap--narrow center">'
            f'<h2 id="cta-h">{esc(h2)}</h2>{sub_html}<div class="btn-row btn-row--center">{btns}</div>{line}</div></section>')

def section(inner, cls="", id_=None, aria=None, wrap="wrap"):
    idattr = f' id="{id_}"' if id_ else ""
    ar = f' aria-labelledby="{aria}"' if aria else ""
    return f'<section class="section {cls}"{idattr}{ar}><div class="{wrap}">{inner}</div></section>'

def hero(eyebrow_t, h1, intro, buttons="", crumb=None, center=False, note=None):
    c = " center" if center else ""
    cr = crumbs(crumb) if crumb else ""
    note_html = f'<p class="small muted">{inline(note)}</p>' if note else ""
    return (f'<section class="hero hero--page{c}"><div class="wrap wrap--hero">{cr}{eyebrow(eyebrow_t)}'
            f'<h1>{esc(h1)}</h1><p class="lede lede--lg">{inline(intro)}</p>'
            f'<div class="btn-row{" btn-row--center" if center else ""}">{buttons}</div>{note_html}</div></section>')

def numbered(items, cls="steps"):
    lis = "".join(f'<li class="step"><span class="step__n" aria-hidden="true">{i+1:02d}</span><div><h3>{esc(a)}</h3><p>{inline(b)}</p></div></li>'
                  for i, (a, b) in enumerate(items))
    return f'<ol class="{cls}">{lis}</ol>'

def cards(items, cls="cards cards--3"):
    """items: list of (title, body_md_inline, link or None, tag or None)."""
    out = []
    for it in items:
        title, body, link, tag = (list(it) + [None, None])[:4]
        tag_html = f'<p class="tag">{esc(tag)}</p>' if tag else ""
        link_html = f'<p class="card__link"><a class="text-link text-link--arrow" href="{link[1]}">{esc(link[0])}</a></p>' if link else ""
        out.append(f'<article class="card">{tag_html}<h3>{esc(title)}</h3><p>{inline(body)}</p>{link_html}</article>')
    return f'<div class="{cls}">{"".join(out)}</div>'

def offer_cards(show_price=False, link_label="Read more"):
    from content_core import OFFERS
    out = []
    for o in OFFERS:
        price = f'<p class="card__price">{esc(o["price"])}</p>' if show_price else ""
        out.append(f'<article class="card card--offer"><p class="tag">{esc(o["tag"])}</p><h3>{esc(o["name"])}</h3>{price}'
                   f'<p>{inline(o["summary"])}</p><p class="card__link"><a class="text-link text-link--arrow" href="{o["url"]}">{esc(link_label)}</a></p></article>')
    return f'<div class="cards cards--3 cards--equal">{"".join(out)}</div>'

# ------------------------------------------------------------------ layout
def organization_ld():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org", "name": "MarvelUs", "url": SITE + "/",
            "description": "Melbourne-based business offering AI digital support, SEO and a paid Business Assessment, delivered remotely.",
            "areaServed": "Worldwide",
            "address": {"@type": "PostalAddress", "addressLocality": "Melbourne", "addressRegion": "VIC", "addressCountry": "AU"}}

def service_ld(name, desc, path, price=None):
    d = {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
         "provider": {"@id": SITE + "/#org"}, "areaServed": "Worldwide", "url": SITE + path}
    if price:
        d["offers"] = {"@type": "Offer", "priceSpecification": {"@type": "PriceSpecification", "price": str(price),
                       "priceCurrency": "AUD", "valueAddedTaxIncluded": False}, "url": SITE + path}
    return d

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": l, "item": SITE + (p or "/")} for i, (l, p) in enumerate(items) if p]}

def header_html(path):
    lis = []
    for label, p in NAV:
        cur = ' aria-current="page"' if (path == p or (p != "/" and path.startswith(p) and p not in ("/",))) else ""
        lis.append(f'<li><a href="{p}"{cur}>{esc(label)}</a></li>')
    lis.append('<li class="nav-book"><a href="/book/">Book a call</a></li>')
    return (f'<header class="site-header" id="top"><div class="wrap header-row">'
            f'<a class="brand" href="/" aria-label="MarvelUs home"><span class="brand__mark" aria-hidden="true">M</span><span class="brand__name">MarvelUs</span></a>'
            f'<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav"><span class="nav-toggle__label">Menu</span></button>'
            f'<nav id="site-nav" class="site-nav" aria-label="Main"><ul>{"".join(lis)}</ul></nav>'
            f'<a class="btn btn--primary btn--sm header-cta" href="{{{{PURCHASE}}}}" data-cta="purchase" data-where="header">Get the assessment</a>'
            f'</div></header>')

def footer_html():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><p class="brand brand--footer"><span class="brand__mark" aria-hidden="true">M</span><span class="brand__name">MarvelUs</span></p>
<p>Practical AI help for businesses that want their time back.</p>
<p>Based in Melbourne, Australia. Delivered remotely, anywhere.</p></div>
<div><h2 class="footer-h">Company</h2><ul>
<li><a href="/about/">About</a></li><li><a href="/case-studies/">Case studies</a></li><li><a href="/insights/">Insights</a></li><li><a href="/events/">Events</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/ai-consulting-melbourne/">Melbourne</a></li><li><a href="/book/">Work with us</a></li></ul></div>
<div><h2 class="footer-h">Get started</h2><ul>
<li><a href="/assessment/">Business Assessment</a></li><li><a href="/services/digital-support/">Digital support</a></li><li><a href="/services/seo/">SEO</a></li><li><a href="/book/">Book a call</a></li>
<li>Contact: {email_html()}</li><li>Phone: {phone_html()}</li></ul></div>
<div><h2 class="footer-h">Connect</h2><p>{ph("social links, only profiles that exist", "contact")}</p></div>
</div>
<div class="footer-small"><p>&copy; 2026 MarvelUs. All rights reserved.</p>
<ul class="inline-list"><li><a href="/privacy/">Privacy</a></li><li><a href="/terms/">Terms</a></li><li><a href="/cookies/">Cookies</a></li><li><a href="/cookies/#manage-cookies">Manage cookies</a></li><li>Melbourne, Australia</li><li>{ph("ABN, if shown", "legal")}</li></ul></div>
</div></footer>'''

def rel_rewrite(h, path, absolute=False):
    depth = len([p for p in path.strip("/").split("/") if p and not p.endswith(".html")])
    prefix = (SITE + "/") if absolute else ("../" * depth if depth else "./")
    def sub(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith("//"):
            return m.group(0)
        return f'{attr}="{prefix}{url.lstrip("/")}"'
    return re.sub(r'\b(href|src|action)="(/[^"]*)"', sub, h), prefix

def render_page(meta):
    CTX.clear()
    CTX["quiz"] = meta["quiz"]
    path = meta["path"]
    body = meta["fn"]()
    canonical = SITE + (path if path != "/404.html" else "/")
    schema = [organization_ld()] + [s() if callable(s) else s for s in meta["schema"]]
    if CTX.get("faq"):
        schema.append(faq_ld(CTX["faq"]))
    if CTX.get("crumbs"):
        schema.append(breadcrumb_ld(CTX["crumbs"]))
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n' for s in schema)
    robots = '<meta name="robots" content="noindex, nofollow">' if CFG["noindex"] else '<meta name="robots" content="index, follow">'
    title = meta["title"]
    desc = html.escape(meta["desc"], quote=True)
    scripts = ['assets/js/site-data.js', 'assets/js/webmcp.js', 'assets/js/main.js']
    if meta["quiz"]:
        scripts += ['assets/js/quiz-data.js', 'assets/js/quiz.js']
    scripts += meta["extra_js"]
    sc = "\n".join(f'<script src="/{s}" defer></script>' for s in scripts)
    doc = f'''<!doctype html>
<html lang="en-AU">
<head>
<!-- DRAFT BUILD: noindex is ON for every page while placeholders remain. To launch: set "noindex": false in site.config.json and run python3 src/build.py. -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#fbfaf7">
<meta property="og:site_name" content="MarvelUs">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/json" href="/agents.json" title="MarvelUs agent manifest">
<link rel="stylesheet" href="/assets/css/site.css">
{ld}<script>document.documentElement.classList.add("js")</script>
</head>
<body class="{meta["bodyclass"]}" data-path="{path}">
<a class="skip-link" href="#main">Skip to main content</a>
{header_html(path)}
<main id="main" tabindex="-1">
{body}
</main>
{footer_html()}
{sc}
</body>
</html>
'''
    doc = doc.replace("{{PURCHASE}}", CFG["purchaseUrl"])
    doc, prefix = rel_rewrite(doc, path, absolute=(path == "/404.html"))
    doc = doc.replace("<body ", f'<body data-root="{prefix}" ', 1)
    return doc, CTX.get("ph", [])
