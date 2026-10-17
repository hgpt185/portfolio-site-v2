---
name: Hemesh Gupta Portfolio
description: Reference-led personal portfolio with a photographic masthead and editorial project rows.
colors:
  accent-dark: "#e6ab89"
  accent-light: "#93502d"
  background-dark: "#19181a"
  foreground-dark: "#fafafa"
  body-dark: "#d1d5db"
  muted-dark: "#9ca3af"
  rule-dark: "#374151"
  image-dark: "#242328"
  background-light: "#fff"
  foreground-light: "#111"
  body-light: "#374151"
  muted-light: "#626975"
  rule-light: "#d1d5db"
  image-light: "#f3f4f6"
  selection: "#c27f58"
  selection-light: "#f4cfaa"
  selection-text-light: "#3b281e"
  toggle-background: "#19181ae8"
  toggle-hover: "#302b2a"
typography:
  display:
    fontFamily: "Poppins, sans-serif"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "36px"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "0.025em"
  job-title:
    fontFamily: "Poppins, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: 1.4
  project-title:
    fontFamily: "Poppins, sans-serif"
    fontSize: "23px"
    fontWeight: 600
    lineHeight: 1.35
  subtitle:
    fontFamily: "Poppins, sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.625
  job-description:
    fontFamily: "Inter, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.75
  project-description:
    fontFamily: "Inter, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.65
  metadata:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.625
  project-tag:
    fontFamily: "Inter, sans-serif"
    fontSize: "10px"
    fontWeight: 400
    lineHeight: 1.625
rounded:
  toggle: "7px"
  image: "12px"
  portrait: "50%"
spacing:
  step-4: "4px"
  step-6: "6px"
  step-8: "8px"
  step-10: "10px"
  step-12: "12px"
  step-14: "14px"
  step-16: "16px"
  step-18: "18px"
  step-20: "20px"
  step-24: "24px"
  step-28: "28px"
  step-30: "30px"
  step-32: "32px"
  step-36: "36px"
  step-40: "40px"
  step-44: "44px"
  step-48: "48px"
  step-62: "62px"
  step-64: "64px"
  step-80: "80px"
components:
  theme-toggle:
    backgroundColor: "{colors.toggle-background}"
    textColor: "{colors.background-light}"
    rounded: "{rounded.toggle}"
    width: "38px"
    height: "38px"
  theme-toggle-hover:
    backgroundColor: "{colors.toggle-hover}"
  project-image:
    backgroundColor: "{colors.image-dark}"
    rounded: "{rounded.image}"
  project-tags:
    textColor: "{colors.muted-dark}"
    typography: "{typography.project-tag}"
  job-row:
    typography: "{typography.job-description}"
    textColor: "{colors.body-dark}"
    padding: "0 0 30px"
  contact-link:
    textColor: "{colors.body-dark}"
  social-navigation:
    textColor: "{colors.body-dark}"
---
# Design System: Hemesh Gupta Portfolio

## Overview

**Creative North Star: "The Reference-Led Portfolio"**

A calm, photographic portfolio grounded in the user-pinned Aditya Yadav reference: a wide sunset masthead, overlapping circular portrait, bold personal title, condensed section headings, and spacious project rows. Warm imagery supplies character while neutral surfaces keep professional content readable.

This specification records the completed replacement implementation in index.html, styles.css, and script.js. The reference supplies layout and typography authority; assets/SOURCES.md records the permitted new banner, the optimized user portrait, and illustrative project imagery. Values were extracted manually from code because the Impeccable engine download was blocked; no detector result or exact live-reference pixel fidelity is claimed.

**Key Characteristics:**
- Photographic masthead and overlapping portrait.
- Poppins titles, Bebas Neue sections, and Inter reading text.
- Flat sections, fine dividers, and generous project spacing.
- Dark default with a complete persisted light theme.

## Colors

The palette pairs charcoal or clean white with cool neutral text and a restrained warm accent. Frontmatter owns exact values; theme suffixes describe the corresponding semantic role.

### Primary
- **Warm Peach / Burnt Sienna:** `accent-dark` and `accent-light` color hovered links and keyboard focus.
- **Copper / Apricot Selection:** dark mode uses `selection` with white text; light mode uses `selection-light` with `selection-text-light`, matching the sunrise portrait backdrop.

### Neutral
- **Charcoal / White:** background tokens cover the page; foreground tokens carry titles.
- **Silver / Slate:** body tokens carry descriptive text; muted tokens carry secondary metadata and icons.
- **Slate Rule / Mist Rule:** rule tokens separate sections and jobs and color understated contact underlines.
- **Deep Image / Pale Image:** image tokens provide loading surfaces beneath project photographs.
- **Translucent Charcoal:** the theme control retains its dark background and white icon in either theme; its hover token supplies feedback.

**The Theme Pair Rule.** Switch the complete semantic palette together; keep the banner and portrait photographic in both themes.

## Typography

**Display Font:** Poppins, sans-serif. **Section Font:** Bebas Neue, sans-serif. **Body Font:** Inter, sans-serif. Fonts load from Google Fonts.

The hierarchy is role-specific rather than a mathematical scale. The normative roles in frontmatter describe desktop defaults. Identity reduces to (36px) below (768px); project titles reduce to (21px) at (480px) and below. About copy reduces to (16px) at that same small-phone breakpoint. Employment roles use Inter (14px), the contact introduction (16px), contact details (15px, then 14px on small phones), and footer text (11px). Employment periods use tabular numerals.

**The Three Roles Rule.** Use Poppins for identity and item titles, Bebas Neue for section headings, and Inter for reading text and metadata.

## Layout

Desktop uses one centered outer container (896px maximum, including 24px horizontal padding) with top/bottom padding (80px / 32px). The banner is (256px) high; the identity row has (32px) horizontal inset. A right-aligned portrait (192px) overlaps the banner by (96px). The identity and social links sit to its left. The introductory block ends with a fine divider.

Sections use padding (62px 16px 44px) and bottom rules. Headings ordinarily have (24px) bottom margin, with (40px) before the project list. Job entries use (32px) gaps and internal dividers. Each desktop project pairs two equal columns, an image and descriptive content, with a (32px) column gap and (80px) row gap. Images preserve a (16:9) frame.

At (767px) and below, top container padding becomes (40px), the banner becomes (192px), and the identity centers below a (160px) portrait overlapping by (80px). Sections use top/bottom padding (48px / 36px); projects stack with a (24px) internal gap and (64px) row gap. Project title groups center; descriptions remain left aligned.

At (480px) and below, the outer padding is (24px 12px), banner height is (180px), and section horizontal inset is (10px). Employment headings stack, placing periods below roles. Metadata spacing contracts. Footer and contact content remain simple text rows.

## Elevation & Depth

The page is flat except for the portrait's ambient shadow (`0 14px 22px -10px #0007`). Photography, overlap, spacing, and one-pixel semantic rules establish depth; jobs and project rows have no raised surfaces.

**The Portrait Depth Rule.** Reserve the ambient shadow for the overlapping portrait; project rows and experience entries remain flat.

## Shapes

The banner has square corners. The portrait is circular with a (4px) border matching the active page background. Project images use the image radius; the compact theme control uses the smaller toggle radius. These two rounded rectangles do not imply rounded section containers.

## Components

### Theme control
A compact icon button sits at the banner's top-right inset (16px). The sun appears in dark mode and the moon in light mode. Its accessible label names the destination theme. Selection persists in localStorage; unavailable storage is tolerated. Default theme is dark.

### Navigation and contact links
Social navigation is a row of inline SVG icons (24px) with a (24px) gap; it centers on mobile. Contact links use restrained underlines. Hover uses the active accent. Links and buttons share an accent outline (2px) offset by (5px) for keyboard focus. The skip link becomes visible on focus.

### Experience entries
Plain full-width text entries pair company and role with a right-aligned date on desktop. Descriptions use compact, relaxed leading. Divider and spacing establish grouping without card backgrounds.

### Project rows
Each image, title, and source icon links to the real repository. Title and source icon share a baseline; the icon is (20px). Descriptions and a wrapping technology list follow. Technology labels are plain muted text, not pill chips. On row hover, the image scales to (1.035) over (500ms) using `cubic-bezier(.16,1,.3,1)`. Reduced motion removes the transition and changes smooth scrolling to automatic.

### Identity masthead
Use assets/mountain-dusk.jpg and assets/hemesh-gupta.jpg in dark mode. In light mode, use assets/mountain-sunrise.jpg and assets/hemesh-gupta-sunrise.jpg: the portrait has a warm apricot backdrop matching the dawn sky. CSS follows the persisted theme before the first render. Preserve the documented overlap and circular crop. The header contains identity and social links; it has no separate menu bar.

## Do's and Don'ts

### Do:
- Do preserve the pinned masthead, portrait overlap, type families, and responsive project-row geometry.
- Do use the supplied portrait and keep project photographs clearly illustrative.
- Do retain visible keyboard focus, meaningful link labels, and reduced-motion support.

### Don't:
- Don't replace the reference-led layout with a dashboard, card grid, or unrelated visual identity.
- Don't introduce decorative badges, invented project interface screenshots, or heavy card shadows.
