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
### 🆕 7 new roles this update · 408 tracked total · updated `2026-11-06T16:18:57+00:00`

| Firm | New roles |
| --- | ---: |
| Toptal | 2 |
| Diebold Nixdorf | 2 |
| Lemon.io | 1 |
| Cardinal Health | 1 |
| Emerson | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Operations Expert with Python for AI Supply Chain Task Design](https://remoteOK.com/remote-jobs/remote-operations-expert-with-python-for-ai-supply-chain-task-design-toptal-1137690) | Toptal | Anywhere in the World | 2026-11-06 |
| [ML Inference Engineer â Terminal-Bench Task Designer (vLLM / SGLang / TensorRT-LLM)](https://remoteOK.com/remote-jobs/remote-ml-inference-engineer-terminal-bench-task-designer-vllm-sglang-tensorrt-llm-toptal-1137689) | Toptal | Anywhere in the World | 2026-11-06 |
| [Senior Vue Developer](https://remoteOK.com/remote-jobs/remote-senior-vue-developer-lemon-io-1137688) | Lemon.io | Remote (Worldwide) | 2026-11-06 |
| [Software Engineer (C#, .NET Core, React JS, Azure, Retail Domain)](https://eeug.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20678) | Diebold Nixdorf | Hyderabad, Telangana, India | 2026-11-06 |
| [Senior Software Engineer(C#, .NET Core, React JS, Azure, Retail Domain)](https://eeug.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20677) | Diebold Nixdorf | Hyderabad, Telangana, India | 2026-11-06 |
| [Director, Enterprise Financial Planning & Analysis](https://cardinalhealth.wd1.myworkdayjobs.com/EXT/job/OH-Ohio-Work-from-Home/Director--Enterprise-Financial-Planning---Analysis_20190121-1) | Cardinal Health | OH-Ohio-Work from Home | 2026-11-06 |
| [Test Engineer](https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26013453) | Emerson | HYDERABAD, TELANGANA, India | 2026-11-06 |
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
