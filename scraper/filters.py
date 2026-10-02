"""Keyword + location filtering for scraped jobs.

Focused scope: core SOFTWARE ENGINEERING + DATA + AI/ML roles (plus a couple of
niche titles like Member of Technical Staff / Forward Deployed Engineer).
NOT broad IT — we drop help desk, network/sysadmin, business analyst, project
manager, QA, functional ERP/CRM consultants, support, etc.
"""
from __future__ import annotations

import re

# Keep a job only if its title matches ANY of these. This is a BROAD tech/IT
# allowlist — software, data, AI/ML, plus all of "IT" (support, infra/network,
# sysadmin, security, QA, DBA, ERP/functional, health-IT/Epic, IT PM/BA). Ambiguous
# titles ("Project Manager", "Business Analyst") are NOT keywords — they only pass
# when paired with an IT signal (" it ", "technical", "data", "software", …), so a
# non-IT PM/BA still drops. We avoid bare "engineer"/"analyst" (match mechanical/
# finance) and use phrases.
KEYWORDS = [
    # software engineer / developer (all flavors)
    "software engineer", "software developer", "software development engineer",
    "sde", " swe", "developer", "programmer", "coder",
    "full stack", "fullstack", "full-stack", "full stack engineer",
    "front end", "frontend", "front-end", "back end", "backend", "back-end",
    "web developer", "web engineer", "mobile engineer", "mobile developer",
    "ios engineer", "ios developer", "android engineer", "android developer",
    "embedded engineer", "embedded software", "firmware engineer", "game developer",
    "application engineer", "applications engineer", "api engineer", "application developer",
    # software-adjacent engineering (write code)
    "platform engineer", "cloud engineer", "devops engineer", "devops", "cloud ",
    "site reliability", "sre", "security engineer", "infrastructure engineer",
    "systems software", "distributed systems",
    # data
    "data engineer", "data scientist", "data science", "data analyst",
    "data analytics", "analytics engineer", "data architect", "database engineer",
    "big data", "etl developer", "etl engineer", "bi developer", "bi analyst",
    "business intelligence", "data warehouse", "data governance", "data management",
    # ai / ml
    "machine learning", " ml ", " mle", "ml engineer", "ai engineer", " ai ",
    "artificial intelligence", "deep learning", "nlp", "natural language",
    "llm", "genai", "generative ai", "computer vision", "applied scientist",
    "research scientist", "research engineer", "mlops", "ai/ml", "ml/ai",
    # architects
    "software architect", "data architect", "cloud architect", "solutions architect",
    "application architect", "technical architect", "enterprise architect",
    "security architect", "integration architect",
    # --- broad IT: support / infra / network / sysadmin ---
    " it ", "information technology", "help desk", "helpdesk", "service desk",
    "desktop support", "desktop technician", "technical support", "support engineer",
    "support analyst", "support specialist", "application support", "production support",
    "it support", "it specialist", "it analyst", "it technician", "it manager",
    "it director", "it lead", "it coordinator", "it administrator", "it operations",
    "system administrator", "systems administrator", "sysadmin", "system admin",
    "network engineer", "network administrator", "network analyst", "network architect",
    "noc ", "telecom", "voip", "infrastructure", "systems engineer", "systems analyst",
    "system analyst", "storage engineer", "virtualization", "vmware", "citrix",
    "site reliability", "automation engineer",
    # --- enterprise / functional / health IT ---
    "business systems analyst", "it business analyst", "systems integration",
    "epic ", "ehr", "emr", "informatics", "health information", "health it",
    "servicenow", "sharepoint", "salesforce", "dynamics", "power bi", "tableau",
    "sap ", "erp", "peoplesoft", "workday", "netsuite", "oracle dba", "oracle developer",
    "oracle apps", "functional analyst", "functional consultant", "crm developer",
    # --- qa / test ---
    "quality assurance", " qa ", "qa engineer", "qa analyst", "test engineer",
    "quality engineer", "sdet", "test automation", "tester", "test analyst",
    # --- database / data admin ---
    "database administrator", "dba", "database developer", "data administrator",
    # --- security ---
    "cybersecurity", "cyber security", "information security", "security analyst",
    "security operations", "soc analyst", "iam ", "identity and access",
    "grc", "it audit", "penetration test", "incident response", "vulnerability",
    # --- agile / IT delivery / IT-qualified PM & BA ---
    "scrum master", "product owner", "agile coach", "release manager",
    "technical writer", "technical project manager", "it project manager",
    "technical program manager", "technical product manager", "it program manager",
    "implementation consultant", "solutions consultant",
    # niche titles
    "member of technical staff", "member of the technical staff", "technical staff",
    "forward deployed",
]

# Drop these even if a keyword matched — clearly NON-IT roles/disciplines.
# NOTE: broad-IT roles (help desk, network, sysadmin, QA, DBA, ERP, support, PM/BA)
# are NO LONGER excluded — this is now an all-IT board. We keep out non-IT engineering,
# clinical CARE (but allow health-IT/informatics), and other non-tech roles.
EXCLUDE = [
    # sales / staffing / clearance
    "sales", "account manager", "account executive", "recruiter",
    "business development", "talent acquisition", "staffing consultant",
    "clearance", "secret", "ts/sci", "polygraph", "technical recruiter",
    # field/hardware technician (not IT)
    "field service", "field technician", "datacenter technician", "data center technician",
    "cable installer", "line technician", "maintenance technician",
    # non-IT engineering disciplines
    "mechanical engineer", "civil engineer", "chemical engineer", "aerospace",
    "structural engineer", "process engineer", "manufacturing engineer",
    "sales engineer", "electrical engineer", "industrial engineer", "controls engineer",
    "environmental engineer", "petroleum", "geotechnical", "design engineer",
    "project engineer", "machining", " cnc", "tool engineer", "validation engineer",
    "facilities", "hvac",
    # clinical CARE (health-IT / informatics stay IN via KEYWORDS)
    "clinical nurse", "clinical pharmacist", "clinical research", "clinical coordinator",
    "clinical specialist", "clinical educator", "clinical trial", "clinical therapist",
    "registered nurse", "nurse", " rn ", " lpn", "physician", "therapist",
    "pharmacy", "pharmacist", "caregiver", "phlebot", "respiratory", "radiolog",
    "sonograph", "surgical", "dental", "dietitian", "patient",
    # other clearly non-IT roles
    "warehouse", "forklift", "driver", " cdl", "welder", "machinist", "assembler",
    "custodian", "janitor", "cashier", "bartender", "chef", "cook", "barista",
    "plumber", "electrician", "mechanic", "laborer", "receptionist", "machine operator",
    "production operator", "packer", "sanitation", "picker", "stocker",
    "accountant", "bookkeeper", "attorney", "paralegal", "teacher", "instructor",
    "financial analyst", "tax analyst", "accounting analyst", "procurement",
    "buyer", "merchandis", "payroll", "marketing", "graphic designer", "social media",
]


def matches_keywords(title: str) -> bool:
    t = f" {title.lower()} "
    if any(x in t for x in EXCLUDE):
        return False
    return any(k in t for k in KEYWORDS)


# Hyderabad on-site/hybrid roles and remote jobs worldwide are in scope.
REMOTE_TOKENS = ("remote", "virtual", "anywhere", "work from home", "wfh",
                 "telework", "work-from-home")


def keep_location(location: str, firm: dict | None = None) -> bool:
    loc = (location or "").strip().lower()
    if not loc:
        return False
    if re.search(r"\bhyderabad\b|\bhyd\b", loc):
        return True
    # Remote eligibility can be anywhere; country filtering happens in the UI.
    return any(token in loc for token in REMOTE_TOKENS)


def matches_location(location: str, allowed: list[str]) -> bool:
    return keep_location(location)


def apply_filters(jobs: list[dict], firm: dict) -> list[dict]:
    """Keep tech roles in Hyderabad or remote worldwide — see keep_location.

    detail_date firms (iCIMS etc.) have BLANK locations on the listing page and only
    get the real location from a per-job detail fetch later, so we let their blank
    jobs through here; run.py re-applies keep_location after that enrichment, which
    drops any still-blank — so the final board never shows an unknown location.
    """
    out = []
    keep_blank = bool(firm.get("detail_date"))
    for j in jobs:
        if not matches_keywords(j["title"]):
            continue
        loc = (j.get("location") or "").strip()
        if not loc and keep_blank:
            out.append(j)
            continue
        if keep_location(j.get("location", ""), firm):
            out.append(j)
    return out
