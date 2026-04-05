# SECUREVISION — PORTFOLIO CASE STUDY INSTRUCTION
## Page Type: Portfolio / Project Case Studies
## Applies to: scape.html · lviv.html · Light-at-Cairnhill.html · commercial-security-sta-building-singapore.html · industrial-security-cyrus-tech-park-singapore.html · and future case studies
## Version 1.0 — April 2026
## This file lives at: /_instructions/INSTRUCTION-portfolio.md

---

## ⚠️ RULES SPECIFIC TO THIS PAGE TYPE

1. **No inline `<style>` blocks.** Portfolio pages use `sv-shared.css` only.
2. **Every claim must be verifiable.** Camera counts, response time improvements, unit counts — all must come from the project brief. Never invent statistics.
3. **Client names and project details are confidential unless explicitly provided.** If client name is not in the brief, use sector + location (e.g. "Luxury Condominium, Buona Vista").
4. **The 60/40 narrative standard applies.** Long-form engineering narrative with 60% text / 40% image proportion. See GLOBAL-INSTRUCTION.md Section 14.
5. **The 4-stat hero strip is mandatory.** Every case study hero must have exactly 4 key project metrics.
6. **The project overview table is mandatory.** Client, Location, Sector, Project Type, Completion — all 5 rows.
7. **Systems used section links to system pages** — not brand pages.
8. **Related Projects shows 3 other case studies** — never the current project.

---

## 1. PORTFOLIO CASE STUDY REFERENCE TABLE

| Project | File | Sector | Solution page link |
|---|---|---|---|
| L'viv Residences | lviv.html | Residential — Luxury Condominium | condominiums.html |
| \*SCAPE | scape.html | Commercial — Youth Hub | commercial-security-singapore.html |
| Light@Cairnhill | Light-at-Cairnhill.html | Residential — Condominium | condominiums.html |
| STA Building | commercial-security-sta-building-singapore.html | Institutional | government-institution-security-singapore.html |
| Cyrus Tech Park | industrial-security-cyrus-tech-park-singapore.html | Industrial | industrial-security-singapore.html |

---

## 2. PAGE STRUCTURE (7-Section Standard)

```
[Head]
[Nav — frozen]
[Hero — project name, sector badge, location, 4 stats, CTA]
[Breadcrumb]
[Section 1: Project Overview — white]        overview table + systems used
[Section 2: The Challenge — bg-light]        what problem Securevision was solving
[Section 3: Our Solution — white]            what was designed and why
[Section 4: Systems & Equipment — bg-light]  what was installed (links to system pages)
[Section 5: Results — white]                 measurable outcomes
[Section 6: Related Projects — bg-light]     3 other case studies
[Final CTA — dark full-width]
[Footer — frozen]
[WhatsApp float]
[Scripts]
```

---

## 3. HEAD TEMPLATE

```html
<title>[Project Name] — Portfolio Case Study | Securevision Singapore</title>
<meta name="description" content="[140–160 chars: what Securevision did for this project and the key outcome]">
<meta property="og:image" content="https://www.securevision.com.sg/images/[project]-hero.jpg">
<meta property="og:type" content="article">
```

---

## 4. HERO SECTION

No full-bleed background image required — dark gradient with project identity.

```html
<header style="background:linear-gradient(135deg,#0E1A2B 0%,#1a2942 100%); padding:calc(68px + 64px) 0 64px; color:#fff;">
  <div class="container">

    <!-- Sector badge + location -->
    <div style="display:flex; gap:12px; margin-bottom:20px; flex-wrap:wrap; align-items:center;">
      <span class="badge badge-primary">[SECTOR BADGE — e.g. "RESIDENTIAL CASE STUDY"]</span>
      <span style="color:rgba(255,255,255,0.6); font-size:13px;">📍 [LOCATION]</span>
      <span style="color:rgba(255,255,255,0.6); font-size:13px;">[PROPERTY TYPE]</span>
    </div>

    <h1 style="font-family:'Montserrat',sans-serif; font-size:clamp(32px,5vw,60px); font-weight:800; color:#fff; margin-bottom:16px;">[PROJECT NAME]</h1>
    <p style="font-family:'Inter',sans-serif; font-size:20px; color:rgba(255,255,255,0.8); margin-bottom:48px;">[One-line project descriptor — e.g. "AI-Powered Security for Singapore's Premier Youth Hub"]</p>

    <!-- 4-stat strip — mandatory, exactly 4 stats -->
    <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:24px; margin-bottom:40px;">
      <div style="text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:24px 16px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:32px; font-weight:800; color:#fff; margin-bottom:6px;">[STAT 1 VALUE]</div>
        <div style="font-size:12px; color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:1px;">[STAT 1 LABEL]</div>
      </div>
      <div style="text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:24px 16px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:32px; font-weight:800; color:#fff; margin-bottom:6px;">[STAT 2 VALUE]</div>
        <div style="font-size:12px; color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:1px;">[STAT 2 LABEL]</div>
      </div>
      <div style="text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:24px 16px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:32px; font-weight:800; color:#fff; margin-bottom:6px;">[STAT 3 VALUE]</div>
        <div style="font-size:12px; color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:1px;">[STAT 3 LABEL]</div>
      </div>
      <div style="text-align:center; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:24px 16px;">
        <div style="font-family:'Montserrat',sans-serif; font-size:32px; font-weight:800; color:#fff; margin-bottom:6px;">[STAT 4 VALUE]</div>
        <div style="font-size:12px; color:rgba(255,255,255,0.6); text-transform:uppercase; letter-spacing:1px;">[STAT 4 LABEL]</div>
      </div>
    </div>

    <a href="https://wa.me/6593860466" class="btn btn-whatsapp">💬 Discuss a Similar Project</a>

  </div>
</header>
```

---

## 5. SECTION 1 — PROJECT OVERVIEW (white)

Two columns: overview table left, systems used right.

```html
<section style="padding:80px 0; background:#fff;">
  <div class="container">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:64px; align-items:start;">

      <!-- Overview table -->
      <div>
        <span class="eyebrow">Project Overview</span>
        <div class="blog-table-wrap" style="margin-top:24px;">
          <table class="blog-table">
            <tbody>
              <tr><td style="font-weight:700; width:140px;">Client</td><td>[CLIENT NAME or "Confidential — [Sector], [Location]"]</td></tr>
              <tr><td style="font-weight:700;">Location</td><td>[FULL ADDRESS or DISTRICT]</td></tr>
              <tr><td style="font-weight:700;">Sector</td><td>[SECTOR / PROPERTY TYPE]</td></tr>
              <tr><td style="font-weight:700;">Project Type</td><td>[e.g. "Complete security system upgrade" or "New installation"]</td></tr>
              <tr><td style="font-weight:700;">Completion</td><td>[MONTH YEAR]</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Systems used — links to system pages NOT brand pages -->
      <div>
        <span class="eyebrow">Systems Deployed</span>
        <div style="margin-top:24px; display:flex; flex-direction:column; gap:12px;">
          <!-- Add only systems actually used in this project -->
          <a href="surveillance-detection.html" style="display:flex; align-items:center; gap:12px; padding:16px 20px; background:var(--bg-light); border-radius:8px; text-decoration:none; color:var(--text-dark); font-weight:600; font-size:14px; border:1px solid var(--border-light); transition:0.2s;"
             onmouseover="this.style.borderColor='var(--primary-blue)'"
             onmouseout="this.style.borderColor='var(--border-light)'">
            📷 [System name — e.g. "AI Surveillance & Analytics"]
          </a>
          <!-- Repeat for each system deployed -->
        </div>
      </div>

    </div>
  </div>
</section>
```

---

## 6. SECTION 2 — THE CHALLENGE (bg-light)

Long-form narrative. 60% text / 40% image proportion per GLOBAL-INSTRUCTION.md Section 14.

Structure: eyebrow + h2 (context heading) + 2–4 challenge sub-headings (h3) with paragraphs.

Each h3 sub-challenge should:
- Name the specific problem (not generic)
- Explain why it was hard for this specific site
- Be 2–4 paragraphs

Include 1 image using `.blog-img-wrap` (16:9 aspect ratio).

---

## 7. SECTION 3 — OUR SOLUTION (white)

How Securevision approached the design. Engineering narrative — what was decided and why, not just what was installed.

Structure: eyebrow + h2 + intro paragraph + 2–3 solution pillars (each with h3 + paragraphs).

Include 1 image using `.blog-img-wrap`. Alternate image position (left/right) from Section 2.

Use `.recommendation-box` for any key design decision worth highlighting.

---

## 8. SECTION 4 — SYSTEMS & EQUIPMENT (bg-light)

What was actually installed. Technical specifics. Links to system pages.

Structure: eyebrow + h2 + component cards.

```html
<div class="component-card">
  <div class="component-header">
    <div class="component-number">1</div>
    <h3>[System category — e.g. "AI Video Surveillance"]</h3>
  </div>
  <p>[What was installed, how many, what brand, why this choice]</p>
  <p><a href="[system-page].html" style="color:var(--primary-blue); font-weight:600;">Learn more about our [System] solutions →</a></p>
</div>
```

System page links (use these — not brand pages):
```
surveillance-detection.html
people-access-control.html
vehicle-access-control.html
integrated-security-platform.html
burglar-alarm.html
door-access.html
intercom-system-singapore.html
auto-gate-singapore.html
```

---

## 9. SECTION 5 — RESULTS (white)

Measurable outcomes only. Every stat must come from the project brief — never invented.

Structure: eyebrow + h2 + result stat cards + closing paragraph.

```html
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:28px; margin:48px 0;">
  <div class="card" style="text-align:center;">
    <div style="font-family:'Montserrat',sans-serif; font-size:48px; font-weight:800; color:var(--primary-blue); margin-bottom:8px;">[RESULT STAT]</div>
    <p style="font-size:14px; color:var(--text-gray);">[What this stat means in plain English]</p>
  </div>
  <!-- Repeat for each measurable result — max 3 cards -->
</div>
```

---

## 10. SECTION 6 — RELATED PROJECTS (bg-light)

3 other case study cards. Never link to the current project.

```html
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:28px; margin-top:40px;">
  <a href="[case-study].html" style="display:block; text-decoration:none;">
    <div class="card" style="height:100%;">
      <span class="badge badge-primary" style="margin-bottom:12px;">[SECTOR]</span>
      <h3 style="font-size:18px; margin-bottom:8px;">[Project Name]</h3>
      <p style="font-size:14px; color:var(--text-gray);">[1 sentence outcome]</p>
      <span style="color:var(--primary-blue); font-weight:600; font-size:13px; margin-top:16px; display:block;">Read Case Study →</span>
    </div>
  </a>
</div>
```

Canonical case study URLs:
```
lviv.html
scape.html
Light-at-Cairnhill.html
commercial-security-sta-building-singapore.html
industrial-security-cyrus-tech-park-singapore.html
```

---

## 11. FINAL CTA

```html
<section class="cta-section cta-high-impact cta-skyline" style="text-align:center; padding:120px 0;">
  <div class="container">
    <span class="eyebrow-light">Start Your Project</span>
    <h2 style="color:#fff; margin-bottom:20px;">Planning a Similar Project?</h2>
    <p class="subtitle">Our engineering team will assess your site, design a system architecture, and manage the project from first brief to final handover.</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html" class="btn btn-primary">Book Free Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-outline-light">💬 Discuss Your Project</a>
    </div>
  </div>
</section>
```

---

## 12. ANTI-GRAVITY PROMPT FORMAT

```
[Paste GLOBAL-INSTRUCTION.md]
[Paste INSTRUCTION-portfolio.md]

--- PAGE BRIEF ---
Template:  _templates/_template-portfolio.html
File:      [filename].html
Project:   [Project name]
Sector:    [Sector badge text]
Location:  [Address or district]
Completed: [Month Year]
Client:    [Name or "Confidential"]

HERO STATS (exactly 4):
  Stat 1: [Value] / [Label]
  Stat 2: [Value] / [Label]
  Stat 3: [Value] / [Label]
  Stat 4: [Value] / [Label]

SYSTEMS DEPLOYED:
  [List each system with its system page link]

THE CHALLENGE (2–4 sub-challenges):
  1. [Sub-challenge heading] / [Description]
  2. [Sub-challenge heading] / [Description]

OUR SOLUTION (2–3 design pillars):
  1. [Pillar heading] / [What was designed and why]
  2. [Pillar heading] / [Description]

SYSTEMS & EQUIPMENT:
  [List each system category, what was installed, quantities]

RESULTS (max 3 measurable stats):
  1. [Stat] / [Plain English explanation]
  2. [Stat] / [Explanation]
  3. [Stat] / [Explanation]

RELATED PROJECTS (3 — not this project):
  1. [Project name] / [filename] / [1 sentence outcome]
  2. [Project name] / [filename] / [1 sentence outcome]
  3. [Project name] / [filename] / [1 sentence outcome]
```

---

*Securevision · INSTRUCTION-portfolio.md · v1.0 · April 2026*
