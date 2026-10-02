# Hyderabad Tech Jobs 🟢

**A free, auto-updating board for software, data, AI, cloud and other tech roles in Hyderabad and remote — refreshed every 2 hours.**

### 👉 [Browse the live board »](https://ganeshreddy08.github.io/Hyd-Tech/)

---

## Why I built this

Job-hunting is a grind of open tabs. This board gathers public technology roles in Hyderabad and remote listings, with direct links to the original posting.

I got tired of checking job feeds by hand, so I built one that checks them for me.
The scheduled workflow refreshes its sources every two hours and filters to technology roles. Remote jobs are open worldwide, with a country filter populated from the current results. No account is needed.

## Who it helps

- **Freshers and new grads** looking for entry-level roles
- **Experienced engineers** filtering from 0 to 9+ years
- **Career switchers** looking for Hyderabad or remote technology roles

If that's you, this is yours to use freely.

## A note 🍀

Job searching is hard, and it can make you feel small — especially when you're doing it from
a new country, a new field, or after a setback. Please remember: a rejection is one company on
one day, not a verdict on you. The right role often comes after the one that felt like "the
one." Keep applying, keep building, keep going. You only need it to work **once**.

This board exists to take one annoying part off your plate so you have more energy for the
parts that matter. Rooting for you. 💚

---

| | |
| --- | --- |
| 🔄 **Refresh** | every 2 hours via GitHub Actions |
| 🎯 **Scope** | Hyderabad and remote technology roles; Hyderabad hybrid where the source labels it |
| 🏢 **Sources** | public job feeds and configured company/staffing career pages |
| 🧹 **Filtered** | software, data, AI/ML, cloud, security, QA and other IT roles |
| 📦 **Archive** | full searchable board at [`docs/index.html`](docs/index.html) · raw data in [`data/jobs.json`](data/jobs.json) |
| 🧭 **Sibling** | [JobsBuddy](https://github.com/SIDDARTHAREDDY8/JobsBuddy) does the same for full-time, H1B-sponsor roles |

## 🆕 Live Jobs

<!-- JOBS:START -->
### 🆕 5 new roles this update · 126 tracked total · updated `2026-10-02T22:42:25+00:00`

| Firm | New roles |
| --- | ---: |
| Artech | 3 |
| Mindlance | 1 |
| Cincinnati Children's Hospital | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Software Engineering - Software Engineer II](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=33190116#/jobs/33190116) | Artech | Remote, CA | 2026-10-02 |
| [Gaming - Gameplay Software Engineer III](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=33189557#/jobs/33189557) | Artech | Remote, CA | 2026-10-02 |
| [Agronomic Modeling -- Data Scientist](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=33188736#/jobs/33188736) | Artech | Remote, IA | 2026-10-02 |
| [Software Engineer II](https://www2.jobdiva.com/portal/?a=7fjdnw91pq69jlvngz1gp518iugamw00c66623tmx447r7e3lkr3gqqpqjhpy8mo&compid=0&jobid=29411305#/jobs/29411305) | Mindlance | Remote, CA | 2026-10-02 |
| [EMR Analyst I - Epic Billing](https://cincinnatichildrens.wd5.myworkdayjobs.com/careersatcincinnatichildrens/job/Remote/EMR-Analyst-I---Epic-Billing_JR225598) | Cincinnati Children's Hospital | Remote | 2026-10-02 |
<!-- JOBS:END -->

## How it works

```
config/firms.yaml   →  one entry per firm (URL + how to read its job cards)
scraper/engine.py   →  fetch each firm (api / api_html / dom / apify_search)
scraper/filters.py  →  keep tech roles in Hyderabad or remote
scraper/store.py    →  dedupe + first-seen tracking into data/jobs.json
build_site.py       →  render data/jobs.json into docs/index.html (GitHub Pages)
build_readme.py     →  inject newly-found roles into this README (JOBS markers)
.github/workflows   →  run every 2 hours, commit fresh jobs + site + README
```

Each firm can run in one of two modes:

- **`dom`** — Playwright renders the page and reads job cards via CSS selectors.
  Works on any site. Breaks if the firm redesigns (just re-fix the selectors).
- **`api`** — call the JSON endpoint the page itself calls (DevTools → Network → XHR).
  Faster and more stable. Use it when you can find the endpoint.

## Setup

```bash
cd HyderabadTechJobs
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```bash
python run.py                      # all firms
python run.py --only "TEKsystems"  # one firm
python run.py --headful            # watch the browser (debug selectors)
python build_site.py               # rebuild the HTML board
open docs/index.html
```

## Calibrating a firm  (the one manual step)

Career pages differ, so each firm needs its selectors confirmed once:

1. Open the firm's job-search URL in Chrome.
2. Right-click a job listing → **Inspect**.
3. Find the repeating container element → that's your `card` selector.
4. Inside it, find the title / location / link elements → fill those selectors.
5. Run `python run.py --only "<Firm>" --headful` and watch it pull jobs.

**Tip:** before writing selectors, check the **Network → XHR** tab. If you see a
clean JSON request returning the jobs, switch that firm to `mode: api` instead —
it's far more reliable than scraping rendered HTML.

## Adding more firms

Append to `config/firms.yaml`. Your Desktop already has
`Comprehensive_List_of_US_Tech_Staffing_&_Vendor_Companies.pdf` — pull names from there.

## Notes / honesty

- These firms **want** their jobs found (that's how they fill reqs), so listings are
  public — no login wall.
- Be polite: the 2-hour cron is the refresh interval. Don't hammer.
- Some firms use anti-bot (Cloudflare). If a firm returns nothing in `dom` mode,
  it may need `mode: api` or an Apify Actor.
- Selectors in `firms.yaml` are **starting points** and must be confirmed live.
