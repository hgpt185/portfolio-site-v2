# portfolio-site-v2

Hemesh Gupta's portfolio, closely following the banner, overlapping portrait, typography, spacing, and two-column project layout of [adityayadav.website](https://www.adityayadav.website/). Content comes from hemeshgupta.site.

**Live:** https://hgpt185.github.io/portfolio-site-v2/

About, Experience, Education, Projects, Contact; responsive mobile layout; persistent dark/light themes; accessible social and source-code links. Static HTML/CSS/JavaScript, with no build step.

> **Canonical URL note:** this repo deploys to `https://hgpt185.github.io/portfolio-site-v2/`. `hemeshgupta.site` is a separate site not managed by this repository. All metadata, sitemap, and `llms.txt` references use the GitHub Pages URL as canonical.

## Preview

Run `python3 -m http.server 8000` and open http://localhost:8000, or open `index.html` directly.

## SEO & machine-readable assets

Static files served at the site root, no build step required:

| File | Purpose |
|---|---|
| `robots.txt` | Allows all crawlers, including AI search bots (OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot); references `sitemap.xml` |
| `sitemap.xml` | Canonical homepage URL with `lastmod` (update when content changes) |
| `llms.txt` | Concise Markdown identity + section links, per the llms.txt proposal |
| `llms-full.txt` | Comprehensive Markdown mirror of all site content (experience, education, skills, projects, profiles) |
| `profile.json` | Machine-readable profile (JSON), linked from `<head>` as `rel="alternate"` |

Structured data: JSON-LD in `index.html` (`Person` + `WebSite` + `ProfilePage` via one `@graph`, consistent `#person` `@id`). Metadata: canonical URL, Open Graph, Twitter card, robots directives.

### Validation

Run the stdlib-only checker from the repo root:

```sh
python3 scripts/validate.py
```

Checks: required files exist, `profile.json` parses, JSON-LD parses and describes a Person with canonical URL, canonical link present, no `noindex`, education section sits below experience, robots.txt/sitemap.xml validity, `llms.txt` / `llms-full.txt` mention the canonical URL, `profile.json` linked from the page.

## Edit and deploy

Content is in `index.html`; `content.json` preserves the original source data (now includes education). Styles are in `styles.css`, and theme behavior in `script.js`. GitHub Pages deploys `main` from `/ (root)`.

Manual follow-up (outside the repo):
- Submit `sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- Generate a 1200×630 Open Graph image (current `og:image` is the 192×192 portrait).
- If `hemeshgupta.site` should become canonical, move it into this repo (with a `CNAME`) or make it a redirect — until then, search engines should treat the GitHub Pages URL as canonical.

Impeccable is installed locally under `.agents/skills/impeccable/` (ignored by Git); its optional engine needs network access. Product constraints are in `PRODUCT.md`; the design specification is in `DESIGN.md`. Asset provenance and the banner generation prompt are in `assets/SOURCES.md`.
