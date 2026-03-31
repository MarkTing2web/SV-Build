# Securevision Insights Blog — Content & Image Standards

**Reference document for Anti-Gravity and all future article builds**
Version 1.1 · April 2026

---

## 1. Purpose of this document

This document defines the exact standards for every Securevision Insights article. Use it at the start of any new chat session with Claude or Anti-Gravity so that all articles are built consistently without needing to repeat instructions.

It covers: image sizes, the author bio, the hero byline, article structure, file naming conventions, tag taxonomy, and image prompts per article.

---

## 2. Image standards

Every article uses four types of images. The sizes below are the display sizes. Always supply the source file at 2× the display size so it looks sharp on retina screens.

### 2.1 Hero avatar — byline row at the top of the article

- Display size: 64 × 64 px
- Shape: circle (border-radius 50%)
- CSS: object-fit: cover
- File: `images/ler-wee-meng-bio.jpeg`
- Alt text: Ler Wee Meng, Founder and CEO of Securevision Pte Ltd

This replaces the WL initials circle. The same file is used across all articles.

### 2.2 Author bio block — bottom of every article

- Display size: 120 × 120 px
- Shape: circle (border-radius 50%)
- CSS: object-fit: cover
- File: `images/ler-wee-meng-bio.jpeg`
- Alt text: Ler Wee Meng, Founder and CEO of Securevision Pte Ltd

Same file as the hero avatar. The CSS handles the different display sizes.

### 2.3 Article cover image — wide banner below the hero

- Display size: 1200 × 480 px minimum
- Orientation: landscape
- File size: under 200 KB
- Format: JPG or WebP
- File naming: `images/[article-slug]-cover.jpg`

The image sits behind a dark overlay so it does not need to be perfectly composed. Strong subject matter and reasonable quality are enough.

### 2.4 In-article images — inside the body sections

- Display size: 800 × 500 px
- Width: full width of the prose column
- File size: under 150 KB per image
- Format: JPG or WebP
- Border-radius: 12px (matches site style)
- Always include descriptive alt text — this is an E-E-A-T signal
- File naming: `images/[article-slug]-[description].jpg`

### 2.5 Night vision / comparison image

- Display size: 1000 × 450 px
- Split-frame comparison — wider than standard in-article images
- Left half: standard IR greyscale. Right half: colour night vision. Same location, same darkness.

---

## 3. Author bio — standard text

Use this exact text in every article. Do not paraphrase or shorten it. The full bio appears once per article, at the bottom of the article body, after the last section and before the tags and share row.

### 3.1 Bio block structure

- Label: ABOUT THE AUTHOR (uppercase, small text)
- Left side: author photo at 120 × 120 px circle
- Right side: name, title, and bio paragraphs

### 3.2 Name and title line

```
Ler Wee Meng
Founder & CEO, Securevision Pte Ltd
```

### 3.3 Bio text — use verbatim

Wee Meng has over 35 years of experience in security systems engineering and integration. He holds a BEng in Electrical and Electronic Engineering from the National University of Singapore and a law degree from the University of London.

He founded Securevision in 2006 and has since led security system deployments across more than 1,000 sites in Singapore — spanning residential properties, condominiums, commercial buildings, industrial facilities, and institutions.

His technical focus spans CCTV and AI video analytics, IP intercom systems, access control, licence plate recognition, and integrated platform design. He is the architect behind VESTA, Securevision's unified security platform built specifically for condominium management in Singapore.

Wee Meng works directly with managing agents, MCSTs, property developers, architects, and security companies to design systems that are engineered for the site, not sold off a catalogue.

Securevision holds Police Licence No. L/PS/000267/2023P and is registered with the Building and Construction Authority of Singapore.

---

## 4. Hero byline — what goes at the top of every article

The hero byline row sits inside the dark hero header, below the article headline and lede. It shows four things only. Do not add credentials or extra text here — the full bio at the bottom does that work.

### 4.1 Elements in order

- Photo: `images/ler-wee-meng-bio.jpeg` at 64 × 64 px circle
- Name: Wee Meng Ler
- Title: Founder & CEO · Securevision
- Date: Month YYYY (e.g. March 2025)
- Read time: X min read
- Tags: primary topic tags for that article

### 4.2 What to remove

Remove any credentials, qualifications, or years-of-experience text from the hero byline. That information belongs only in the bio block at the bottom of the article.

---

## 5. Article structure — order of elements top to bottom

1. Nav
2. Hero header — category pill, headline, lede, byline row, cover image
3. Article body — prose sections with sidebar
4. Author bio block — after the last section, before tags
5. Tags
6. Share row — LinkedIn, WhatsApp, Copy link
7. CTA box — consultation call to action
8. Article prev/next navigation
9. Related articles list
10. Footer

### 5.1 Section numbering in headings

Number sections in the heading text: 1, 2, 3 etc. Do not use S1, S2 or any prefix. HTML anchor IDs use section1, section2 etc. for TOC linking.

### 5.2 Callout boxes

Use for key points and design rules. Navy left border, light blue background. Label in uppercase above the text. CSS class: `callout-box`.

### 5.3 Verdict boxes

Use for Wee Meng's direct opinion or recommendation. Red left border, warm background. Always labelled SECUREVISION VERDICT. CSS class: `verdict-box`.

---

## 6. File naming conventions

### 6.1 Article HTML files

```
insights-[topic-slug].html
```

Examples:
- `insights-how-to-choose-cctv.html`
- `insights-burglar-alarm-design.html`
- `insights-upgrade-condo-intercom.html`

### 6.2 Cover images

```
images/[topic-slug]-cover.jpg
```

Examples:
- `images/how-to-choose-cctv-cover.jpg`
- `images/burglar-alarm-design-cover.jpg`

### 6.3 In-article images

```
images/[article-slug]-[description].jpg
```

Examples:
- `images/cctv-legacy-analogue.jpg`
- `images/cctv-hd-analogue-toggle.jpg`
- `images/cctv-network-ip.jpg`
- `images/cctv-night-vision-comparison.jpg`

### 6.4 Author photo — one file used everywhere

```
images/ler-wee-meng-bio.jpeg
```

Do not create separate files for different sizes. CSS handles all size variations.

---

## 7. Instructions for Anti-Gravity

When building any new Insights article, apply all of the following without being asked each time:

- Hero avatar: replace any initials circle with `images/ler-wee-meng-bio.jpeg` at 64 × 64 px, circle crop, object-fit cover
- Hero byline title: always **Founder & CEO · Securevision** — never Managing Director
- Hero byline: name, title, date, read time, tags only — no credentials in this row
- Author bio block: insert after the last article section, before tags, using the exact bio text in Section 3 of this document
- Author bio photo: `images/ler-wee-meng-bio.jpeg` at 120 × 120 px, circle crop, object-fit cover
- Cover image: 1200 × 480 px minimum, file under 200 KB
- In-article images: 800 × 500 px, border-radius 12px, file under 150 KB, always with alt text
- Section headings: numbered 1, 2, 3 — not S1, S2, S3
- Sidebar author card: title reads **Founder & CEO** — never Managing Director
- Apply tags from Section 9 for the article being built

---

## 8. Articles built so far

Update this table as each article is completed.

| Article | Category | File | Tags | Status |
|---|---|---|---|---|
| How to Choose the Right CCTV System | Security Planning | `insights-how-to-choose-cctv.html` | CCTV · NVR · Security Planning · Buying Guide · Homeowner · Commercial · Singapore | Built — Fully Standards Compliant |
| Understanding Your Burglar Alarm System Design | Security Planning | `insights-burglar-alarm-design.html` | Burglar Alarm · Security Planning · System Design · Homeowner · Condominium · Singapore | Built — Fully Standards Compliant |

---

## 9. Tag taxonomy

Tags are applied to every article. Use tags from each group below as relevant. Do not invent new tags — add them to this document first so the taxonomy stays consistent across all articles.

### 9.1 System tags — what the article is about technically

- CCTV
- Burglar Alarm
- Door Access
- Intercom
- Auto Gate
- LPR
- VESTA
- NVR
- AI Analytics

### 9.2 Topic tags — the angle or purpose of the article

- Security Planning
- System Design
- Buying Guide
- Installation
- Integration
- Troubleshooting
- Maintenance

### 9.3 Audience tags — who the article is for

- Homeowner
- Condominium
- MCST
- Commercial
- Industrial
- Architect

### 9.4 Location tag — always on every article

- Singapore

### 9.5 Tags per article — apply these exactly when building

**How to Choose the Right CCTV System**
`CCTV` `NVR` `Security Planning` `Buying Guide` `Homeowner` `Commercial` `Singapore`

**Understanding Your Burglar Alarm System Design**
`Burglar Alarm` `Security Planning` `System Design` `Homeowner` `Condominium` `Singapore`

---

## 10. Image prompts per article

Use these prompts when generating or commissioning images. All sizes refer to the finished display size — supply source files at 2×.

---

### Article 1 — How to Choose the Right CCTV System

**Cover image** · 1200 × 480 px · `images/how-to-choose-cctv-cover.jpg`
Wide-angle shot of modern IP CCTV cameras mounted on the exterior corner of a commercial building in Singapore. Daytime. Clean architecture. Cameras clearly visible and purposeful.

**In-article image 1** · 800 × 500 px · `images/cctv-legacy-analogue.jpg`
Close-up of an old analogue CCTV dome camera, visibly aged. Mounted on a yellowed wall bracket. Contrasts with the cleanliness of modern IP equipment.

**In-article image 2** · 800 × 500 px · `images/cctv-hd-analogue-toggle.jpg`
A dome camera with the back cover open or a clear shot of the mode selector toggle switch showing TVI / CVI / AHD / CVBS options. Technical detail clearly visible.

**In-article image 3** · 800 × 500 px · `images/cctv-network-ip.jpg`
A modern Hikvision or Hanwha IP dome or bullet camera. Clean current model. Mounted neatly on a ceiling or wall. No clutter.

**In-article image 4** · 1000 × 450 px · `images/cctv-night-vision-comparison.jpg`
Split frame. Left side: standard IR greyscale footage of a car park or corridor at night, washed out, limited detail. Right side: colour night vision of the same scene, full colour, clear detail. Same location, same darkness, different camera technology.

---

### Article 2 — Understanding Your Burglar Alarm System Design

**Cover image** · 1200 × 480 px · `images/burglar-alarm-design-cover.jpg`
Clean interior shot of a Singapore home or office hallway suggesting security and calm. No cameras visible. Lifestyle rather than technical. Warm but purposeful lighting.

**In-article image 1** · 800 × 500 px · `images/burglar-alarm-pir-detector.jpg`
A PIR motion detector mounted in the corner of a room at ceiling height, showing typical installation position. Clean white unit against a neutral wall.

**In-article image 2** · 800 × 500 px · `images/burglar-alarm-ajax-panel.jpg`
AJAX wireless alarm panel and hub, clean product shot. White background or mounted cleanly on a wall. Modern and professional looking.

---

*Securevision Pte Ltd · UEN 200614644E · Police Licence L/PS/000267/2023P · svbuild.vercel.app*
