# SECUREVISION — SOLUTION PAGE INSTRUCTION
## Page Type: Solution Pages (by Property Sector)
## Applies to: residential-security-singapore.html · condominiums.html · commercial-security-singapore.html · industrial-security-singapore.html · government-institution-security-singapore.html · healthcare-security-singapore.html
## Version 1.0 — April 2026
## This file lives at: /_instructions/INSTRUCTION-solution.md

---

## ⚠️ RULES SPECIFIC TO THIS PAGE TYPE

1. **No inline `<style>` blocks.** Solution pages use `sv-shared.css` only.
2. **Tone speaks to the decision-maker for that property type.** Residential = homeowner/developer. Condo = MCST/MA. Commercial = business owner/FM. Industrial = operations director. Government = procurement/facilities. Healthcare = administrator/operations.
3. **The 4-pillar System Architecture section is structurally fixed.** The pillars (Surveillance, People Access, Vehicle Access, Platform) are always the same. Only the typical components, ESSENTIAL/OPTIONAL labels, and descriptions change per property type.
4. **System pillar links always point to the same 4 system pages** — never to brand pages or guide pages.
5. **The "Who We Serve" section reflects sub-personas** unique to each property type — not generic.
6. **Related Solutions section links to the other 5 solution pages** — creating internal links across the hub.
7. **CTA must match the decision-making context.** MCST = "Request Estate Advisory". Homeowner = "Book Site Assessment". Commercial = "Book Site Assessment". Industrial = "Request Operational Assessment".

---

## 1. SOLUTION PAGE REFERENCE TABLE

| Page | File | Accent | Hero class | CTA class | Primary audience |
|---|---|---|---|---|---|
| Private Homes | residential-security-singapore.html | `#38B000` | `hero-res` | `cta-res` | Homeowners, developers, architects |
| Condominiums | condominiums.html | `#4361EE` | `hero-condo` | `cta-condo` | MCST, Managing Agents, estate managers |
| Commercial & Retail | commercial-security-singapore.html | `#FF6D00` | `hero-com` | `cta-com` | Business owners, facilities managers, retail operators |
| Industrial & Logistics | industrial-security-singapore.html | `#7209B7` | `hero-indus` | `cta-indus` | Operations directors, EHS managers, logistics heads |
| Institutions & Government | government-institution-security-singapore.html | `#0056b3` | `hero-gov` | `cta-gov` | Procurement officers, facilities managers, IT/security heads |
| Healthcare & Managed Living | healthcare-security-singapore.html | `#0056b3` | `hero-healthcare` | `cta-healthcare` | Administrators, operations managers, MOM compliance officers |

---

## 2. PAGE STRUCTURE (8-Section Standard)

```
[Head]
[Nav — frozen]
[Hero — property type badge, h1, 2 CTAs, trust note]
[Breadcrumb]
[Section 1: Philosophy — white]           The "why standard security fails" problem
[Section 2: System Architecture — bg-light] 4 pillars with components + system links
[Section 3: Who We Serve — white]         2–3 sub-personas specific to this sector
[Section 4: Proof / Outcomes — bg-light]  Case study reference + key result stat
[Section 5: Why Securevision — white]     3–4 differentiators for this property type
[Section 6: Related Solutions — bg-light] Links to other 5 solution pages
[Final CTA — dark full-width]
[Footer — frozen]
[WhatsApp float]
[Scripts]
```

---

## 3. HEAD TEMPLATE

```html
<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Property Type] Security Solutions Singapore | Securevision</title>
  <meta name="description" content="[140–160 chars — Securevision engineers integrated security systems for [property type] in Singapore. CCTV, access control, alarms, and vehicle barriers — one partner.]">
  <link rel="canonical" href="https://www.securevision.com.sg/[slug].html">
  <meta property="og:title" content="[Property Type] Security Solutions Singapore | Securevision">
  <meta property="og:description" content="[Same as meta description]">
  <meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">
  <meta property="og:url" content="https://www.securevision.com.sg/[slug].html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Securevision">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- sv-shared.css only — do not add sv-guides.css to solution pages -->
  <link rel="stylesheet" href="sv-shared.css">
  <script src="site-config.js"></script>

  <!-- Page accent colour — only permitted inline style -->
  <style>
    :root { --page-accent: #38B000; } /* Change per page — see reference table above */
  </style>
</head>
```

---

## 4. HERO SECTION

```html
<header class="hero-high-impact hero-[PAGE]">
  <div class="container">
    <span class="eyebrow-light">[Property Type Category — e.g. "Condominiums & Estates"]</span>
    <h1 class="hero-title-main">[Headline — outcome-focused, not product-focused]</h1>
    <p class="hero-subtitle-main">[One sentence: what Securevision delivers for this property type. Max 200 chars.]</p>
    <div class="btn-group">
      <a href="request-site-assessment-singapore.html?intent=[slug]-assessment" class="btn btn-primary">[Primary CTA label]</a>
      <a href="https://wa.me/6593860466" class="btn btn-whatsapp-standard">WhatsApp an Engineer</a>
    </div>
    <p class="hero-trust-note">[Short trust line — e.g. "Serving condominiums and MCSTs across Singapore since 2006."]</p>
  </div>
</header>
```

### Hero CTA labels by property type
| Page | Primary CTA |
|---|---|
| Private Homes | "Book Site Assessment" |
| Condominiums | "Request Estate Advisory" |
| Commercial | "Book Site Assessment" |
| Industrial | "Request Operational Assessment" |
| Institutions | "Request Security Consultation" |
| Healthcare | "Request Compliance Assessment" |

---

## 5. SECTION 1 — PHILOSOPHY (white)

The problem statement. Why standard, fragmented security fails this specific property type. This section differentiates Securevision before any product is mentioned.

Structure: eyebrow + h2 + 1 paragraph + 3 philosophy cards (image + heading + 2 sentences each).

**Philosophy card topics by property type:**
- **Residential:** Engineering-first approach / Whole-home integration / One partner for life
- **Condominiums:** Fragmented systems create blind spots / MCST continuity / Operational efficiency
- **Commercial:** Security that feels welcoming / Intelligent retail insights / Single point of accountability
- **Industrial:** Perimeter logic / Compliance documentation / 24/7 operational continuity
- **Institutions:** Mission-critical uptime / Audit trail compliance / Multi-site consistency
- **Healthcare:** Resident welfare first / MOM compliance / Visitor management without bottlenecks

---

## 6. SECTION 2 — SYSTEM ARCHITECTURE (bg-light)

The 4-pillar section. **Structure is fixed** — do not change pillar names, order, or system page links. Only the descriptions, typical components, and ESSENTIAL/OPTIONAL labels change per property type.

### Fixed pillar structure:
```html
<section id="system-architecture" style="padding:80px 0; background:var(--bg-light);">
  <div class="container">
    <span class="eyebrow">System Architecture</span>
    <h2>What Systems Do [Property Type] Need?</h2>
    <p>[1–2 sentence intro scoped to this property type]</p>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:32px; margin-top:48px;">

      <!-- Pillar 1: Surveillance & Detection — always ESSENTIAL -->
      <div class="card">
        <img src="images/pillar_surveillance.png" alt="Surveillance & Detection" style="width:100%; border-radius:8px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3>Surveillance & Detection</h3>
          <span class="badge badge-primary">ESSENTIAL</span>
        </div>
        <p>[2–3 sentences scoped to this property type]</p>
        <p><strong>Typical components:</strong></p>
        <ul>[4 bullet points — specific to this property type]</ul>
        <a href="surveillance-detection.html" style="color:var(--primary-blue); font-weight:600; font-size:14px;">Learn More About Surveillance →</a>
      </div>

      <!-- Pillar 2: People Access Control — ESSENTIAL or RECOMMENDED depending on property -->
      <div class="card">
        <img src="images/pillar_people_access.png" alt="People Access Control" style="width:100%; border-radius:8px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3>People Access Control</h3>
          <span class="badge badge-primary">[ESSENTIAL / RECOMMENDED]</span>
        </div>
        <p>[2–3 sentences scoped to this property type]</p>
        <p><strong>Typical components:</strong></p>
        <ul>[4 bullet points]</ul>
        <a href="people-access-control.html" style="color:var(--primary-blue); font-weight:600; font-size:14px;">Learn More About People Access →</a>
      </div>

      <!-- Pillar 3: Vehicle Access & Barriers — varies by property type -->
      <div class="card">
        <img src="images/pillar_vehicle_access.png" alt="Vehicle Access" style="width:100%; border-radius:8px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3>Vehicle Access & Barriers</h3>
          <span class="badge badge-primary">[ESSENTIAL / RECOMMENDED / OPTIONAL]</span>
        </div>
        <p>[2–3 sentences scoped to this property type]</p>
        <p><strong>Typical components:</strong></p>
        <ul>[4 bullet points]</ul>
        <a href="vehicle-access-control.html" style="color:var(--primary-blue); font-weight:600; font-size:14px;">Learn More About Vehicle Access →</a>
      </div>

      <!-- Pillar 4: Platform Management — OPTIONAL for most, ESSENTIAL for condos/institutions -->
      <div class="card">
        <img src="images/pillar_platform.png" alt="Platform Management" style="width:100%; border-radius:8px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h3>Platform Management</h3>
          <span class="badge badge-primary">[ESSENTIAL / OPTIONAL]</span>
        </div>
        <p>[2–3 sentences scoped to this property type]</p>
        <p><strong>Typical components:</strong></p>
        <ul>[4 bullet points]</ul>
        <a href="integrated-security-platform.html" style="color:var(--primary-blue); font-weight:600; font-size:14px;">Learn More About Platform Integration →</a>
      </div>

    </div>
  </div>
</section>
```

### ESSENTIAL/OPTIONAL labels by property type:

| Pillar | Homes | Condos | Commercial | Industrial | Institutions | Healthcare |
|---|---|---|---|---|---|---|
| Surveillance | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL |
| People Access | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL | ESSENTIAL |
| Vehicle Access | ESSENTIAL | ESSENTIAL | RECOMMENDED | ESSENTIAL | RECOMMENDED | OPTIONAL |
| Platform | OPTIONAL | ESSENTIAL | RECOMMENDED | RECOMMENDED | ESSENTIAL | RECOMMENDED |

---

## 7. SECTION 3 — WHO WE SERVE (white)

2–3 persona cards specific to this property type. Each card: image, persona name, bullet list of their specific concerns, CTA linking to a sub-page if one exists.

### Personas by property type:

**Private Homes:**
- Existing Homeowner (upgrade/fix) → home-security-upgrade-singapore.html
- New Build / A&A project → new-build-security-singapore.html
- Trade & Architect partner → security-partner-architects-singapore.html

**Condominiums:**
- MCST & Council → condominiums-mcst.html
- Managing Agent → condominiums-mcst.html
- Security Contractor → condominiums-security.html

**Commercial:**
- Office & HQ → commercial-office.html
- Retail & Shop Lots → commercial-retail.html
- Hotels & Hospitality → commercial-hotel.html

**Industrial:** Single persona (Operations Director) — link to portfolio for proof
**Institutions:** Single persona (Facilities/Procurement) — link to portfolio
**Healthcare:** Single persona (Administrator/Operations) — link to portfolio

---

## 8. SECTION 4 — PROOF / OUTCOMES (bg-light)

Reference to the most relevant portfolio case study for this property type. Do not reproduce full case study — one card with: project name, property type badge, 1 sentence outcome, 1 key stat, link to full case study.

### Case study reference by property type:
| Property Type | Reference Project | Key Stat |
|---|---|---|
| Private Homes | L'viv Residences | 40% reduction in guard workload |
| Condominiums | L'viv Residences | 450+ residents on self-service access |
| Commercial | SCAPE | 87% reduction in incident response time |
| Industrial | Cyrus Tech Park | 85% reduction in false alarm callouts |
| Institutions | STA Building | 99.7% system uptime |
| Healthcare | *(use general outcome)* | AI face recognition eliminates queue bottlenecks |

---

## 9. SECTION 5 — WHY SECUREVISION (white)

3–4 differentiators written specifically for this property type's decision-maker concerns. Not generic "we're experienced" claims — specific to what matters to this audience.

**No-sales-speak rule:** Never use "best value", "lowest price", "affordable", or "cheapest". Use outcome language instead: "reduced operational liability", "lower total cost of ownership", "optimised ROI", "minimised guard dependency".

**Examples by property type:**
- **MCST/Condo:** "We stay through committee cycles" / "MCST-compliant audit trails at every AGM" / "One engineering team — no vendor fragmentation"
- **Commercial:** "Systems that feel invisible to staff" / "MAS TRM compliance for financial tenants" / "OPEX models available — no capital expenditure"
- **Industrial:** "IP67-rated for tropical outdoor environments" / "bizSAFE Level 3 certified" / "SCDF-compliant fire integration"
- **Healthcare:** "MOM regulatory documentation" / "Fail-safe door logic for fire evacuation" / "Resident dignity — no intrusive surveillance"

**After the 3 differentiator cards, the Support Lifecycle strip is mandatory.** It is already in the template — do not remove it. Update description text only if needed for sector context. The 4 stages (Site Assessment → Installation → Remote Diagnostics → Maintenance Contract) are fixed and must not be renamed or reordered.

---

## 10. SECTION 6 — RELATED SOLUTIONS (bg-light)

Links to the other 5 solution pages. Use a 3-column card grid. Show only 3 most closely related — not all 5 at once.

Always use these exact hrefs:
```
residential-security-singapore.html
condominiums.html
commercial-security-singapore.html
industrial-security-singapore.html
government-institution-security-singapore.html
healthcare-security-singapore.html
```

---

## 11. ANTI-GRAVITY PROMPT FORMAT

```
[Paste GLOBAL-INSTRUCTION.md]
[Paste INSTRUCTION-solution.md]

--- PAGE BRIEF ---
Template:   _templates/_template-solution.html
File:       [slug].html
Sector:     [Property type name]
Accent:     #[hex]
Hero class: hero-[name]
CTA class:  cta-[name]
Audience:   [Primary decision-maker]

HERO:
  Eyebrow: [Category label]
  H1: [Outcome-focused headline]
  Subtitle: [One sentence]
  CTA label: [See reference table]

PHILOSOPHY (3 cards):
  Card 1: [Heading] / [2 sentences]
  Card 2: [Heading] / [2 sentences]
  Card 3: [Heading] / [2 sentences]

SYSTEM ARCHITECTURE — typical components per pillar:
  Surveillance: [4 bullet points for this property type]
  People Access: [4 bullet points] / Label: [ESSENTIAL/RECOMMENDED]
  Vehicle Access: [4 bullet points] / Label: [ESSENTIAL/RECOMMENDED/OPTIONAL]
  Platform: [4 bullet points] / Label: [ESSENTIAL/OPTIONAL/RECOMMENDED]

WHO WE SERVE (2–3 personas):
  Persona 1: [Name] / [3–4 pain points] / [Sub-page link if exists]
  Persona 2: [Name] / [3–4 pain points] / [Sub-page link if exists]
  Persona 3: [Name if applicable] / [pain points] / [link]

PROOF:
  Project: [Name] / [1 sentence outcome] / [Key stat] / [Link to case study page]

WHY SECUREVISION (3–4 differentiators for this sector):
  1. [Heading] / [2 sentences]
  2. [Heading] / [2 sentences]
  3. [Heading] / [2 sentences]

RELATED SOLUTIONS (3 pages):
  [List 3 most relevant solution pages with their hrefs]
```

---

*Securevision · INSTRUCTION-solution.md · v1.0 · April 2026*
