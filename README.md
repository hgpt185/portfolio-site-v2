# portfolio-site-v2

Hemesh Gupta's portfolio, closely following the banner, overlapping portrait, typography, spacing, and two-column project layout of [adityayadav.website](https://www.adityayadav.website/). Content comes from hemeshgupta.site.

**Live:** https://hgpt185.github.io/portfolio-site-v2/

About, Experience, Projects, Contact; responsive mobile layout; persistent dark/light themes; accessible social and source-code links. Static HTML/CSS/JavaScript, with no build step.

## Preview

Run `python3 -m http.server 8000` and open http://localhost:8000, or open `index.html` directly.

## Edit and deploy

Content is in `index.html`; `content.json` preserves the original source data. Styles are in `styles.css`, and theme behavior in `script.js`. GitHub Pages deploys `main` from `/ (root)`.

Impeccable is installed locally under `.agents/skills/impeccable/` (ignored by Git); its optional engine needs network access. Product constraints are in `PRODUCT.md`; the design specification is in `DESIGN.md`. Asset provenance and the banner generation prompt are in `assets/SOURCES.md`.
