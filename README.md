# MarvelUs assessment site (draft)

Static site for the MarvelUs Business Assessment (AI Readiness), digital support and SEO offers. Plain HTML, CSS and vanilla JS. No framework, no tracking, no backend.

Status: **DRAFT. Every page carries `noindex`** because placeholders remain. Live preview: https://marvelus-tech.github.io/marvelus-assessment-site/

## Edit and rebuild

All constants live in `site.config.json` (purchase URL, contact email and phone, price label, turnaround line, booking embed URL, `noindex`, site URL). Page content is in `src/*.py`. Then:

    python3 src/build.py     # writes every HTML page, assets/js/site-data.js, quiz-data.js, agents.json, sitemap.xml, robots.txt
    python3 src/check.py     # links, anchors, one h1, titles, forbidden strings

Python 3 only, standard library. Commit the generated files too: GitHub Pages serves the repo root from `main`.

## Launch checklist

1. **Remove noindex**: set `"noindex": false` in `site.config.json`, rebuild. Update `siteUrl` if the site moves to a custom domain.
2. **Contact**: fill `contactEmail` and `contactPhone` in `site.config.json`. Every placeholder for them turns into a mailto or tel link.
3. **Booking**: set `bookingEmbedUrl` (https only). It fills the embed slot on `/book/`.
4. **Replace proof placeholders** (`[PLACEHOLDER: ...]`, yellow dashed boxes): client logos, quotes, results, case studies, photos, article sources, event dates. Never invent proof. `placeholders.json` lists counts by type; delete it at launch.
5. **Legal**: Terms, Privacy and Cookies are skeletons. A qualified Australian lawyer must write or review them. Remove the draft banners.
6. **Confirm operationally**: same business day report turnaround, GST wording ("$1,000 + GST"), the call-in number from outside Australia, who reviews each report, the score roll-up method, the default $50 preview hourly rate.
7. **Wire the real things**: the email step in the quiz and the forms on `/book/` and `/events/` are UI only and send nothing (marked "demo: not sent"). Connect them to real services and update the Privacy page before launch.
8. Re-run `build.py` and `check.py`, then push.

## Notes

- Primary CTA ("Get the assessment") points at `purchaseUrl` (the existing Stripe checkout page). Secondary CTA is `/book/`.
- Agent tooling: WebMCP tools are registered on every page (`assets/js/webmcp.js`) with a fallback of `window.__marvelusTools`, `/agents.json` and `/.well-known/agent.json`.
- `.nojekyll` is present so `/.well-known/` is served by GitHub Pages.
- No cookie banner: the site sets no cookies and the quiz stores nothing. Add one if analytics or ads are added.
