#!/usr/bin/env python3
"""Self-checks: links, anchors, h1, forbidden strings, meta uniqueness, rough HTML balance."""
import os, re, sys, pathlib, collections, json
from html.parser import HTMLParser
ROOT = pathlib.Path(__file__).resolve().parent.parent
FORBID = ["\u2014", "\u2013", r"&mdash;", r"&ndash;", r"&#8212;", r"&#8211;"]
# The long forbidden-word list is kept outside this public repo. Set ASSESS_FORBID_FILE to use another path.
_ext = pathlib.Path(os.environ.get("ASSESS_FORBID_FILE", "/workspace/.assess-site-forbidden.txt"))
if _ext.exists():
    FORBID += [l.strip() for l in _ext.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
else:
    print("note: external forbidden list not found, only the dash checks ran")
VOID = {"meta","link","br","hr","img","input","source","wbr","path","rect","circle"}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.ids=set(); s.links=[]; s.h1=0; s.stack=[]; s.errs=[]; s.title=""; s.in_title=False; s.meta={}; s.canon=None; s.scripts=[]; s.lang=None
    def handle_starttag(s, t, a):
        a=dict(a)
        if "id" in a:
            if a["id"] in s.ids: s.errs.append("dup id "+a["id"])
            s.ids.add(a["id"])
        if t=="a" and "href" in a: s.links.append(a["href"])
        if t=="h1": s.h1+=1
        if t=="title": s.in_title=True
        if t=="meta" and a.get("name"): s.meta[a["name"]]=a.get("content","")
        if t=="meta" and a.get("property"): s.meta[a["property"]]=a.get("content","")
        if t=="link" and a.get("rel")=="canonical": s.canon=a.get("href")
        if t=="script" and a.get("src"): s.scripts.append(a["src"])
        if t=="link" and a.get("href") and a.get("rel") in ("stylesheet","icon"): s.links.append(a["href"])
        if t=="html": s.lang=a.get("lang")
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s, t):
        if t in VOID: return
        if not s.stack or s.stack[-1]!=t:
            s.errs.append(f"mismatched </{t}> (open: {s.stack[-3:]})")
            if t in s.stack:
                while s.stack and s.stack.pop()!=t: pass
        else: s.stack.pop()
    def handle_data(s, d):
        if s.in_title: s.title+=d
    def handle_endtag_title(s): pass
def endtitle(p): p.in_title=False
pages = {}
for f in sorted(ROOT.rglob("*.html")):
    if ".git" in f.parts or "src" in f.parts: continue
    t=f.read_text(encoding="utf-8")
    p=P(); orig=p.handle_endtag
    def het(tag, p=p, orig=orig):
        if tag=="title": p.in_title=False
        orig(tag)
    p.handle_endtag=het
    p.feed(t); p.text=t; pages[f]=p
errors=[]; 
for f,p in pages.items():
    rel=f.relative_to(ROOT)
    if p.h1!=1: errors.append(f"{rel}: h1 count {p.h1}")
    for e in p.errs: errors.append(f"{rel}: {e}")
    if p.stack: errors.append(f"{rel}: unclosed {p.stack}")
    if not p.title.strip(): errors.append(f"{rel}: no title")
    if not p.meta.get("description"): errors.append(f"{rel}: no description")
    if not p.canon: errors.append(f"{rel}: no canonical")
    if "noindex" not in p.meta.get("robots",""): errors.append(f"{rel}: no noindex")
    if not p.meta.get("og:title"): errors.append(f"{rel}: no og:title")
    if p.lang!="en-AU": errors.append(f"{rel}: lang {p.lang}")
titles=collections.Counter(p.title for p in pages.values()); descs=collections.Counter(p.meta.get("description") for p in pages.values())
for k,v in titles.items():
    if v>1: errors.append(f"dup title: {k}")
for k,v in descs.items():
    if v>1: errors.append(f"dup description: {k[:60]}")
# links
nlinks=0
for f,p in pages.items():
    rel=f.relative_to(ROOT)
    for h in p.links+p.scripts:
        if re.match(r"(https?:|mailto:|tel:|javascript:|data:)", h): continue
        nlinks+=1
        base,_,frag=h.partition("#"); base=base.split("?")[0]
        if f.name=="404.html" and base.startswith("/"): pass
        tgt = f if base=="" else (f.parent/base).resolve()
        if tgt.is_dir(): tgt=tgt/"index.html"
        if not tgt.exists(): errors.append(f"{rel}: broken link {h}"); continue
        if frag and frag not in ("sample",) and tgt.suffix==".html":
            tp=pages.get(tgt)
            if tp is None or frag not in tp.ids: errors.append(f"{rel}: missing anchor {h}")
# forbidden
for f in list(ROOT.rglob("*")):
    if not f.is_file() or ".git" in f.parts or f.suffix in (".pyc",) or "src" in f.parts and f.name!="check.py" and False: continue
    if f.suffix not in (".html",".js",".css",".json",".xml",".txt",".svg",".md",".py",".config") and f.name!="CNAME": continue
    if f.name=="check.py": continue
    if f.parts[-2:]==("src",f.name) : pass
    t=f.read_text(encoding="utf-8", errors="ignore")
    # scan visible/shipped text; the py sources are scanned too
    for pat in FORBID:
        for m in re.finditer(pat, t, re.I):
            ctx=t[max(0,m.start()-40):m.end()+40].replace("\n"," ")
            errors.append(f"forbidden '{pat}' in {f.relative_to(ROOT)}: ...{ctx}...")
print(f"pages {len(pages)}, internal links checked {nlinks}")
for e in errors: print("ERR", e)
print("OK" if not errors else f"{len(errors)} problems")
sys.exit(1 if errors else 0)
