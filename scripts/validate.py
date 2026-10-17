#!/usr/bin/env python3
"""Lightweight SEO/machine-readability checks for the static site.

Stdlib only. Run from the repo root:  python3 scripts/validate.py
Exits non-zero if any check fails.
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = "https://hgpt185.github.io/portfolio-site-v2/"
REQUIRED_FILES = [
    "index.html", "robots.txt", "sitemap.xml",
    "llms.txt", "llms-full.txt", "profile.json", "resume.html",
]

failures = []


def check(label, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {label}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(label)


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    # 1. Required files exist
    for name in REQUIRED_FILES:
        check(f"file exists: {name}", (ROOT / name).is_file())

    # 2. profile.json is valid JSON
    try:
        profile = json.loads((ROOT / "profile.json").read_text(encoding="utf-8"))
        check("profile.json parses", isinstance(profile, dict) and bool(profile.get("name")))
    except Exception as exc:
        check("profile.json parses", False, str(exc))

    # 3. JSON-LD parses and describes a Person
    try:
        blocks = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S
        )
        check("JSON-LD block present", bool(blocks))
        graph = [json.loads(b) for b in blocks]
        nodes = graph if isinstance(graph, list) else [graph]
        # unwrap @graph if present
        flat = []
        for node in nodes:
            if isinstance(node, dict) and "@graph" in node:
                flat.extend(node["@graph"])
            elif isinstance(node, dict):
                flat.append(node)
        person = next((n for n in flat if n.get("@type") == "Person"), None)
        check("JSON-LD Person node", person is not None)
        if person:
            check("Person has name/url/sameAs",
                  bool(person.get("name")) and bool(person.get("url")) and bool(person.get("sameAs")))
            check("Person url is canonical", person.get("url") == CANONICAL)
        check("JSON-LD has WebSite or WebPage",
              any(n.get("@type") in ("WebSite", "WebPage", "ProfilePage") for n in flat))
    except Exception as exc:
        check("JSON-LD parses", False, str(exc))

    # 4. Canonical link + no accidental noindex
    check("index.html has canonical link",
          f'<link rel="canonical" href="{CANONICAL}">' in html)
    check("index.html has no noindex", "noindex" not in html)

    # 5. Education section present below Experience
    exp_pos = html.find('id="experience"')
    edu_pos = html.find('id="education"')
    check("education section exists", edu_pos != -1)
    check("education sits below experience", edu_pos > exp_pos > 0)

    # 6. Metadata basics
    for needle in ('<meta name="description" content="',
                   'property="og:title"', 'name="twitter:card"'):
        check(f"metadata present: {needle[:40]}", needle in html)
    check("og:image is absolute", 'og:image" content="https://' in html)

    # 7. robots.txt: sitemap reference, allows all, names AI crawlers
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    check("robots.txt references sitemap", f"Sitemap: {CANONICAL}sitemap.xml" in robots)
    check("robots.txt allows all", "User-agent: *\nAllow: /" in robots)
    check("robots.txt names AI crawlers",
          all(b in robots for b in ("OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "PerplexityBot")))

    # 8. sitemap.xml is valid XML with the canonical URL
    try:
        tree = ET.parse(ROOT / "sitemap.xml")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [e.text for e in tree.getroot().findall("sm:url/sm:loc", ns)]
        check("sitemap.xml parses with canonical URL", locs == [CANONICAL, CANONICAL + "resume.html"], str(locs))
    except Exception as exc:
        check("sitemap.xml parses", False, str(exc))

    # 9. llms.txt / llms-full.txt mention the canonical URL
    for name in ("llms.txt", "llms-full.txt"):
        text = (ROOT / name).read_text(encoding="utf-8")
        check(f"{name} mentions canonical URL", CANONICAL in text)

    # 10. Machine-readable profile is discoverable from the page
    check("index.html links profile.json",
          'rel="alternate" type="application/json" href="profile.json"' in html)

    # 11. Recruiter-facing HTML resume and consistent internship dates
    resume = (ROOT / "resume.html").read_text(encoding="utf-8")
    check("resume page has canonical URL", CANONICAL + "resume.html" in resume)
    check("homepage visibly links resume", 'href="resume.html">View accessible resume' in html)
    check("Salesforce internship dates corrected in HTML",
          'May 2023 - Jul 2023' in html)
    check("Salesforce internship dates corrected in structured data",
          any(x.get("company") == "Salesforce" and "Intern" in x.get("role", "")
              and x.get("period") == "May 2023 - Jul 2023"
              for x in profile.get("experience", [])))
    check("full AI profile dates corrected",
          "Salesforce — Software Development Intern (May 2023 – Jul 2023)" in (ROOT / "llms-full.txt").read_text(encoding="utf-8"))

    # 12. Achievement content consistency across machine-readable sources
    if isinstance(profile, dict):
        salesforce_roles = [x for x in profile.get("experience", [])
                            if x.get("company") == "Salesforce"
                            and x.get("role") == "Software Engineer II"]
        highlights = salesforce_roles[0].get("highlights", []) if salesforce_roles else []
        check("current role has substantive achievement highlights", len(highlights) >= 3)
        full_text = (ROOT / "llms-full.txt").read_text(encoding="utf-8")
        check("achievements appear in full AI profile",
              bool(highlights) and all(h in full_text for h in highlights))
        check("achievements appear in HTML resume",
              bool(highlights) and all(h in resume for h in highlights))
        check("machine profile links HTML resume",
              profile.get("resumeHtml") == CANONICAL + "resume.html")

    print()
    if failures:
        print(f"{len(failures)} check(s) FAILED")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
