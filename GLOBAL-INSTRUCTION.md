# SECUREVISION WEBSITE — GLOBAL DESIGN INSTRUCTION
## For use with Antigravity AI Web Builder
## Paste this document at the top of EVERY page prompt

---

## 1. PROJECT IDENTITY

**Company:** Securevision Pte Ltd
**Tagline:** Singapore's Smart Security & Operations Partner
**Established:** 2006
**Domain:** www.securevision.com.sg
**Primary CTA:** WhatsApp +65 9386 0466 (https://wa.me/6593860466)

**Tone of voice:**
- Professional but not cold
- Engineering-led — specific, precise, evidence-based
- Never salesy or hyperbolic
- Speaks to property managers, MCSTs, business owners, architects
- Singapore context throughout (use "estate", "MCST", "HDB" where appropriate)

**What this site is NOT:**
- Not an e-commerce store
- Not a product catalogue
- A systems integrator positioning — always "systems" not "products"

---

## 2. TECHNOLOGY STACK

- Plain HTML5, CSS3, vanilla JavaScript only
- No frameworks (no React, no Vue, no Bootstrap)
- No external CSS libraries
- Google Fonts via `<link>` in `<head>`
- All CSS in a `<style>` block in the `<head>` of each page
- All JS in a `<script>` block before `</body>`
- Mobile-first responsive design

---

## 3. FONTS

### Google Fonts Import (include in every page `<head>`)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

### Font Assignments
| Element | Font | Weight | Size (desktop) | Size (mobile) |
|---|---|---|---|---|
| H1 | Montserrat | 700 | clamp(32px, 5vw, 56px) | 28px min |
| H2 | Montserrat | 700 | clamp(24px, 3.5vw, 40px) | 22px min |
| H3 | Montserrat | 600 | 20px | 18px |
| H4 | Montserrat | 600 | 16px | 15px |
| Body text | Inter | 400 | 15–16px | 15px |
| Lead paragraph | Inter | 400 | 18px | 16px |
| Button labels | Montserrat | 600 | 13px | 13px |
| Eyebrow labels | Montserrat | 700 | 11px | 11px |
| Nav links | Inter | 500 | 14px | 14px |
| Small / caption | Inter | 400 | 12–13px | 12px |

### Line Heights
- Headings: 1.2
- Body text: 1.7
- Lead text: 1.7
- Buttons: 1

### Letter Spacing
- Eyebrow labels: 2px
- Button labels: 0.5px
- Nav links: 0.3px
- All caps labels: 1.5px

---

## 4. COLOUR SYSTEM

### CSS Variables (include in every `:root` block)
```css
:root {
  /* Primary */
  --primary:          #0056b3;
  --primary-dark:     #003d82;

  /* Solution category accents */
  --c-homes:          #38B000;
  --c-condos:         #4361EE;
  --c-commercial:     #FF6D00;
  --c-institutions:   #0056b3;
  --c-industrial:     #7209B7;

  /* Technology subsystem accents */
  --c-surveillance:   #2b6cb0;
  --c-people:         #319795;
  --c-vehicle:        #dd6b20;
  --c-platform:       #38a169;

  /* Brand price tier colours */
  --tier-budget:      #38a169;
  --tier-mid:         #2b6cb0;
  --tier-premium:     #7209B7;

  /* UI */
  --whatsapp:         #25d366;
  --whatsapp-dark:    #1da851;

  /* Text */
  --text-dark:        #1B1F23;
  --text-gray:        #5F6368;
  --text-light:       #8a8f98;

  /* Backgrounds */
  --bg-white:         #FFFFFF;
  --bg-light:         #F8F9FA;
  --bg-dark:          #0E1A2B;
  --bg-dark-mid:      #1a2942;

  /* Borders */
  --border:           #E8EAED;
  --border-dark:      rgba(255,255,255,0.08);

  /* Spacing */
  --space-xs:         8px;
  --space-sm:         16px;
  --space-md:         32px;
  --space-lg:         64px;
  --space-xl:         96px;

  /* Layout */
  --container:        1200px;
  --nav-height:       68px;
  --radius:           8px;
  --radius-lg:        14px;
  --radius-xl:        20px;

  /* Transitions */
  --transition:       all 0.25s ease;
}
```

### Colour Usage Rules
- Page backgrounds alternate: dark hero → white → `--bg-light` → white → `--bg-light` → dark CTA
- Never use `--primary` on dark backgrounds — use white or `#5b9ee1` (light blue) instead
- Eyebrow labels: `--primary` on light backgrounds, `rgba(255,255,255,0.5)` on dark
- Body text on white: `--text-gray`
- Body text on `--bg-light`: `--text-gray`
- Body text on dark: `rgba(255,255,255,0.75)`

---

## 5. SPACING & LAYOUT

### Container
```css
.container {
  max-width: var(--container); /* 1200px */
  margin: 0 auto;
  padding: 0 24px;
}
```

### Section Padding
| Breakpoint | Section padding top/bottom |
|---|---|
| Desktop (1200px+) | 80px |
| Laptop (1024px) | 72px |
| Tablet (768px) | 56px |
| Mobile (480px) | 48px |

### Grid System
| Use case | Desktop | Tablet | Mobile |
|---|---|---|---|
| 4-column | repeat(4,1fr) | repeat(2,1fr) | 1fr |
| 3-column | repeat(3,1fr) | repeat(2,1fr) | 1fr |
| 2-column | 1fr 1fr | 1fr 1fr | 1fr |
| 2-column featured | 1fr 1.2fr | 1fr | 1fr |
| Subsystem cards | repeat(4,1fr) | repeat(2,1fr) | 1fr |

### Grid Gaps
- Standard card grids: 24px
- Featured 2-column layouts: 56–64px
- Nav item gaps: 4px
- Button groups: 12–14px

### Card Internal Padding
- Standard card: 28px
- Large feature card: 36–40px
- Compact card: 20px
- Brand chip: 5px 14px

### Spacing Between Elements
- Eyebrow → H2: 12px
- H2 → lead paragraph: 16px
- Lead paragraph → content: 24px
- Section header → grid: 48px
- Card content stack gap: 12–14px
- Button group gap: 12px

---

## 6. RESPONSIVE BREAKPOINTS

```css
/* Desktop — default styles, no query needed */
/* 1200px+ */

/* Laptop */
@media (max-width: 1024px) {
  /* Reduce some padding, keep most layouts */
}

/* Tablet */
@media (max-width: 768px) {
  /* Collapse nav to hamburger */
  /* Stack 2-col grids to 1-col */
  /* Hide desktop mega menus */
  /* 4-col → 2-col */
  /* Section padding: 56px */
}

/* Mobile */
@media (max-width: 480px) {
  /* All grids → 1 column */
  /* Section padding: 48px */
  /* Hide hero pills */
  /* H1 font size minimum 28px */
}
```

### Specific Mobile Rules
- Navigation: hamburger button, collapsible menu, all mega menus hidden
- Hero H1: minimum 28px, maximum 36px on mobile
- Hero pills: hidden on mobile (`display:none` at 480px)
- 2-column split layouts (hero, featured sections): stack to 1 column
- Brand cards: 2-col on tablet, 1-col on mobile
- Footer grid: 2-col on tablet, 1-col on mobile (brand block spans full width)
- Trust bar: vertical stack on mobile
- Buttons: full width on mobile where in a group

---

## 7. NAVIGATION

### Structure (Desktop)
```
[LOGO + SECUREVISION] | Solutions ▾ | Systems ▾ | Brands ▾ | Portfolio | Insights | About ▾ | [🔍]
```

**Key Changes from Previous:**
- Logo + wordmark links to home (no "Home" in nav)
- "Technology" renamed to "Systems"
- "Resources" removed (content accessible via Insights)
- "Brands" added with category dropdown
- "Contact" merged into About dropdown
- WhatsApp button removed from desktop nav (accessible via floating button, mobile menu, About dropdown, footer)
- Search icon added (far right)
- Simplified dropdowns (no mega menus)

### Structure (Mobile)
```
[Logo] SECUREVISION          [☰]  [🔍]
  ↑                           ↑     ↑
Left                      Center  Right
```

**Mobile Menu (when ☰ tapped):**
```
Solutions
Systems
Brands
Portfolio
Insights
About
─────────
💬 WhatsApp Us
```

### Nav CSS
```css
nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  height: 68px;
  background: rgba(14,26,43,0.97);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
```

### Logo (LEFT SIDE OF NAV)
```html
<a href="/index.html" class="nav-logo-link" aria-label="Securevision Home">
  <img src="proprietary-assets/securevision-dark.png"
       alt="Securevision Logo"
       class="nav-logo-img">
  <span>SECUREVISION</span>
</a>
```
```css
.nav-logo-link {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
}
.nav-logo-img {
  height: 40px;
  width: auto;
}
.nav-logo-link span {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 22px;
  color: #ffffff;
  letter-spacing: 0.5px;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .nav-logo-img { height: 32px !important; }
  .nav-logo-link span { font-size: 18px !important; }
}
@media (max-width: 480px) {
  .nav-logo-img { height: 28px !important; }
  .nav-logo-link span { font-size: 16px !important; }
  .nav-logo-link { gap: 6px !important; }
}
```
  display: block;
}
@media (max-width: 768px) {
  .nav-logo-img { height: 32px; }
}
```

**Important:** On mobile, swap to dark logo if nav background becomes white. Our nav stays dark on all breakpoints so always use the light (white) logo version.

### Nav Link Styles
```css
.nav-link {
  color: rgba(255,255,255,0.8);
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 0.3px;
  padding: 24px 16px;
  text-decoration: none;
  transition: var(--transition);
}
.nav-link:hover, .nav-link.active { color: #ffffff; }
.nav-link.has-dropdown::after {
  content: ' ▾';
  font-size: 10px;
  opacity: 0.6;
}
```

### WhatsApp CTA Button (right side of nav)
```css
.nav-cta {
  background: var(--primary);
  color: #fff;
  padding: 9px 18px;
  border-radius: 6px;
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  white-space: nowrap;
  transition: var(--transition);
}
.nav-cta:hover { background: var(--primary-dark); }
```

### Simple Dropdown Styles (Hover Menus)
```css
.simple-dropdown {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  padding: 8px;
  min-width: 180px;
  display: none;
  z-index: 200;
}
.nav-item:hover .simple-dropdown {
  display: block;
}
.simple-dropdown a {
  display: block;
  padding: 9px 14px;
  border-radius: 5px;
  text-decoration: none;
  font-size: 13px;
  color: var(--text-dark);
  transition: 0.2s;
}
.simple-dropdown a:hover {
  background: var(--bg-light);
  color: var(--primary);
}
```

### Dropdown Content by Menu Item
| Menu Item | Dropdown Content | Behavior |
|-----------|------------------|----------|
| **Solutions** | Residential, Condominiums, Commercial, Industrial, Institutions | Simple dropdown |
| **Systems** | Surveillance & CCTV, People Access Control, Vehicle Access & Barriers, Platform Integration | Simple dropdown |
| **Brands** | Surveillance, Access Control, Intercom, Alarms, Gates & Barriers, View All Brands → | Simple dropdown with categories |
| **Portfolio** | (none) | Direct link to portfolio.html |
| **Insights** | (none) | Direct link to insights.html |
| **About** | Company Story, Founder, Awards & Certifications, ─────, Contact Us, WhatsApp | Simple dropdown with contact |

### Mobile Menu
```css
.mobile-toggle {
  display: none; /* shown at 768px and below */
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  padding: 8px;
  align-items: center;
  justify-content: center;
}
.mobile-toggle svg {
  display: block;
}
@media (max-width: 768px) {
  .mobile-toggle { display: flex; }
}

.mobile-menu {
  display: none;
  background: var(--bg-dark);
  border-top: 1px solid rgba(255,255,255,0.08);
  padding: 16px 24px 24px;
}
.mobile-menu.active { display: block; }
.mobile-menu-item {
  display: block;
  padding: 13px 0;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
  font-weight: 500;
  font-size: 15px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  cursor: pointer;
}
.mobile-menu-item:hover { color: #ffffff; }

/* Mobile: No submenus - direct links to hub pages */
```

### Nav Menu Items (Final Structure)
```
Logo + Wordmark → index.html (click to go home)

Desktop Menu Items:
Solutions      → solutions-hub.html    (dropdown: 5 property types)
Systems        → systems.html          (dropdown: 4 system types)
Brands         → brands.html           (dropdown: 6 categories)
Portfolio      → portfolio.html        (no dropdown)
Insights       → insights.html         (no dropdown)
About          → about.html            (dropdown: company info + contact)
Search Icon    → (search functionality)

Mobile Menu Items (when ☰ tapped):
Solutions      → solutions-hub.html    (no submenu)
Systems        → systems.html          (no submenu)
Brands         → brands.html           (no submenu)
Portfolio      → portfolio.html
Insights       → insights.html
About          → about.html
─────────
💬 WhatsApp Us → https://wa.me/6593860466
```

**Note:** WhatsApp is NOT in desktop nav. It's accessible via:
- Floating button (bottom-right, always visible)
- Mobile menu (last item)
- About dropdown (desktop)
- Footer (all pages)

---

## 8. HERO SECTION (standard — all non-homepage pages)

```css
.hero {
  background: linear-gradient(135deg, #0E1A2B 0%, #1a2942 100%);
  padding: calc(var(--nav-height) + 72px) 0 72px;
  color: #ffffff;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  /* Accent glow — use page-specific colour at 15–20% opacity */
  background: radial-gradient(ellipse 60% 70% at 65% 50%,
    rgba(0,86,179,0.18) 0%, transparent 70%);
}
```

**Hero padding rule:** Always `calc(68px + 72px)` on desktop to account for fixed nav. Reduces to `calc(68px + 48px)` on mobile.

**Accent glow colours per page type:**
- General / Technology pages: `rgba(0,86,179,0.18)` (primary blue)
- Private Homes pages: `rgba(56,176,0,0.18)` (green)
- Condominium pages: `rgba(67,97,238,0.18)` (blue)
- Commercial pages: `rgba(255,109,0,0.18)` (orange)
- Industrial pages: `rgba(114,9,183,0.18)` (purple)
- Surveillance pages: `rgba(43,108,176,0.2)`
- People Access pages: `rgba(49,151,149,0.2)`
- Vehicle Access pages: `rgba(221,107,32,0.2)`
- Platform pages: `rgba(56,161,105,0.2)`

---

## 9. BUTTONS

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 28px;
  border-radius: var(--radius);
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  text-decoration: none;
  border: 2px solid transparent;
  cursor: pointer;
  transition: var(--transition);
  white-space: nowrap;
}

/* Primary */
.btn-primary {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
}
.btn-primary:hover {
  background: var(--primary-dark);
  border-color: var(--primary-dark);
  transform: translateY(-2px);
}

/* Secondary / Outline */
.btn-secondary {
  background: transparent;
  color: var(--primary);
  border-color: var(--primary);
}
.btn-secondary:hover {
  background: var(--primary);
  color: #ffffff;
  transform: translateY(-2px);
}

/* White outline (on dark backgrounds) */
.btn-outline-white {
  background: transparent;
  color: #ffffff;
  border-color: rgba(255,255,255,0.5);
}
.btn-outline-white:hover {
  border-color: #ffffff;
  background: rgba(255,255,255,0.1);
}

/* WhatsApp */
.btn-whatsapp {
  background: var(--whatsapp);
  color: #ffffff;
  border-color: var(--whatsapp);
}
.btn-whatsapp:hover {
  background: var(--whatsapp-dark);
  border-color: var(--whatsapp-dark);
  transform: translateY(-2px);
}

/* Small variant */
.btn-sm {
  padding: 9px 18px;
  font-size: 12px;
}

/* Mobile: full width in groups */
@media (max-width: 480px) {
  .btn-group .btn { width: 100%; justify-content: center; }
}
```

---

## 10. STANDARD COMPONENTS

### Eyebrow Label
```css
.eyebrow {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--primary);
  margin-bottom: 12px;
}
.eyebrow-light { color: rgba(255,255,255,0.5); }
```

### Section Header (centred, used above grids)
```css
.section-header {
  text-align: center;
  margin-bottom: 48px;
}
.section-header h2 { margin-bottom: 14px; }
.section-header p {
  font-size: 17px;
  color: var(--text-gray);
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.7;
}
```

### Standard Card
```css
.card {
  background: var(--bg-white);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 28px;
  transition: var(--transition);
}
.card:hover {
  box-shadow: 0 8px 32px rgba(0,0,0,0.10);
  transform: translateY(-3px);
}
```

### Dark Gradient Card (for framework callouts, founder card etc.)
```css
.card-dark {
  background: linear-gradient(135deg, #0E1A2B 0%, #1a2942 100%);
  border-radius: var(--radius-xl);
  padding: 40px;
  color: #ffffff;
  position: relative;
  overflow: hidden;
}
.card-dark::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at top right,
    rgba(0,86,179,0.25) 0%, transparent 60%);
}
.card-dark > * { position: relative; z-index: 1; }
```

### Stat Number
```css
.stat-number {
  font-family: 'Montserrat', sans-serif;
  font-size: 40px;
  font-weight: 700;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  font-size: 13px;
  color: var(--text-gray);
  font-weight: 500;
}
```

### Badge / Tag Pill
```css
.badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.badge-primary { background: var(--primary); color: #fff; }
.badge-budget  { background: var(--tier-budget); color: #fff; }
.badge-mid     { background: var(--tier-mid); color: #fff; }
.badge-premium { background: var(--tier-premium); color: #fff; }
.badge-soon    { background: var(--bg-light); color: var(--text-gray); border: 1px solid var(--border); }
.badge-new     { background: #e8f5e9; color: #2e7d32; }
```

### Checklist (ticked list)
```css
.check-list { list-style: none; }
.check-list li {
  display: flex;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
  font-size: 14px;
  color: var(--text-dark);
}
.check-list li:last-child { border-bottom: none; }
.check-list li::before {
  content: '✓';
  width: 20px; height: 20px;
  background: var(--primary);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
  flex-shrink: 0;
  margin-top: 1px;
}
```

---

## 11. FOOTER (identical on every page)

### Structure
6-column grid on desktop → 3-col on tablet → 1-col on mobile.

```
[Brand block] | Solutions | Technology & Brands | Portfolio | Resources & Insights | Company
```

### Brand Block content
- Logo: `<img src="/images/securevision-logo-light.svg" alt="Securevision" height="36">`
- Tagline: "Singapore's integrated security systems specialist since 2006."
- Contact line: 📞 +65 9386 0466 · ✉️ info@securevision.com.sg
- Social icons row (see Social Media section below)

### Footer Columns
**Solutions:** Private Homes · Condominiums · Commercial · Institutions · Industrial · Find My Solution

**Technology & Brands:** Surveillance · People Access · Vehicle Access · Platform · All 20 Brands

**Portfolio:** All Projects · The L'viv · SCAPE · STA · Cyrus Tech

**Resources & Insights:** All Resources · CCTV Guide · All Insights · Security Planning · Case Studies

**Company:** About Us · Awards · Contact · WhatsApp

### Footer Bottom Bar
```
© 2025 Securevision Pte Ltd  |  Police License L/PS/000267/2023P  |  bizSAFE Level 4  |  BCA Registered
Serving Singapore Since 2006  |  info@securevision.com.sg
```

### Footer CSS
```css
footer {
  background: var(--bg-dark);
  color: rgba(255,255,255,0.5);
  padding: 56px 0 24px;
  font-size: 13px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1fr 1fr 1fr;
  gap: 32px;
  margin-bottom: 40px;
}
.footer-col h4 {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.7);
  margin-bottom: 14px;
}
.footer-col ul { list-style: none; }
.footer-col li { margin-bottom: 8px; }
.footer-col a {
  color: rgba(255,255,255,0.45);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s;
}
.footer-col a:hover { color: #ffffff; }
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.06);
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 10px;
  font-size: 12px;
}
@media (max-width: 1024px) {
  .footer-grid { grid-template-columns: 1fr 1fr 1fr; gap: 28px; }
  .footer-brand { grid-column: 1 / -1; }
}
@media (max-width: 480px) {
  .footer-grid { grid-template-columns: 1fr; }
}
```

---

## 12. SOCIAL MEDIA

### Confirmed Profiles
- Facebook: `https://www.facebook.com/securevision`
- LinkedIn: `https://www.linkedin.com/company/securevision-pte-ltd`
- WhatsApp: `https://wa.me/6593860466`

### Social Icons Row (in footer brand block)
```html
<div class="social-row">
  <a href="https://www.facebook.com/securevision" target="_blank" rel="noopener" aria-label="Securevision on Facebook" class="social-icon">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
      <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
    </svg>
  </a>
  <a href="https://www.linkedin.com/company/securevision-pte-ltd" target="_blank" rel="noopener" aria-label="Securevision on LinkedIn" class="social-icon">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
      <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
      <rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>
    </svg>
  </a>
  <a href="https://wa.me/6593860466" target="_blank" rel="noopener" aria-label="WhatsApp Securevision" class="social-icon">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
      <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
    </svg>
  </a>
</div>
```

```css
.social-row {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}
.social-icon {
  width: 36px; height: 36px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,0.6);
  text-decoration: none;
  transition: var(--transition);
}
.social-icon:hover {
  background: var(--primary);
  border-color: var(--primary);
  color: #ffffff;
}
```

---

## 13. IMAGE & LOGO SPECIFICATIONS

### File Structure
```
/images/
  securevision-logo-light.svg    ← white logo for dark nav/dark backgrounds
  securevision-logo-dark.svg     ← dark logo for light backgrounds
  og-default.jpg                 ← 1200×630px Open Graph default image
  /brands/
    hikvision.png
    hanwha.png
    uniview.png
    milesight.png
    ajax.png
    risco.png
    paradox.png
    dsc.png
    ge-caddx.png
    zkteco.png
    suprema.png
    hid.png
    entrypass.png
    microengine.png
    akuvox.png
    aiphone.png
    kocom.png
    faac.png
    mag.png
    dormer.png
  /badges/
    badge-spf.png                ← Singapore Police Force licence
    badge-bizsafe.png            ← bizSAFE Level 4
    badge-bca.png                ← BCA Registered
  /portfolio/
    lviv-hero.jpg
    scape-hero.jpg
    sta-hero.jpg
    cyrus-hero.jpg
  /team/
    ler-wee-meng.jpg             ← founder photo
```

### Logo Usage Rules
- Nav (dark background): always use `securevision-logo-light.svg`
- Footer (dark background): always use `securevision-logo-light.svg`
- Any light background context: use `securevision-logo-dark.svg`
- Nav logo height: 40px desktop, 32px mobile
- Footer logo height: 36px
- Always include descriptive `alt` text

### Brand Partner Logos
- Display at 40px height, auto width
- Greyscale by default: `filter: grayscale(100%) opacity(0.6)`
- Colour on hover: `filter: none; opacity: 1`
- Use in brands.html, brand pages, about.html, and surveillance/access/vehicle subsystem pages

### Image Placeholders
When real images are not yet available, use a dark gradient placeholder:
```html
<div class="img-placeholder" style="aspect-ratio:16/9; background:linear-gradient(135deg,#0E1A2B,#1a2942); border-radius:12px; display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.3); font-size:13px;">
  [Image placeholder]
</div>
```

---

## 14. SEO REQUIREMENTS (every page)

### Required `<head>` elements
```html
<!-- 1. Meta charset and viewport -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- 2. Title (max 60 characters) -->
<title>[Page-specific title] | Securevision Singapore</title>

<!-- 3. Meta description (140–160 characters, unique per page) -->
<meta name="description" content="[Unique description for this page]">

<!-- 4. Canonical (use live domain when available) -->
<link rel="canonical" href="https://www.securevision.com.sg/[page-slug]">

<!-- 5. Open Graph -->
<meta property="og:title" content="[Same as title tag]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">
<meta property="og:url" content="https://www.securevision.com.sg/[page-slug]">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Securevision">

<!-- 6. Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

### Schema (homepage and contact page)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Securevision Pte Ltd",
  "description": "Singapore's integrated security systems specialist since 2006. CCTV, alarm, access control, and vehicle access systems.",
  "url": "https://www.securevision.com.sg",
  "telephone": "+6562864796",
  "email": "info@securevision.com.sg",
  "logo": "https://www.securevision.com.sg/images/securevision-logo-dark.svg",
  "image": "https://www.securevision.com.sg/images/og-default.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Blk 1013 Geylang East Avenue 3 #02-142",
    "addressLocality": "Singapore",
    "postalCode": "389728",
    "addressCountry": "SG"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "17:00"
    }
  ],
  "foundingDate": "2006",
  "areaServed": "Singapore",
  "hasCredential": "Police Licence L/PS/000267/2023P"
}
</script>
```

### H1 Rule
- Exactly ONE H1 per page — no more, no less
- H1 is always the page's primary keyword phrase
- Never use H1 for the site name — that's what the logo is for

### Title Tag Formats by page type
```
Homepage:        Securevision | Smart Security & Operations Partner Singapore
Solution pages:  [Property Type] Security Solutions Singapore | Securevision
Systems landing: Integrated Security Systems Singapore | Securevision
Subsystem pages: [System Name] | Securevision Singapore
Brand pages:     [Brand] [Category] Installer Singapore | Securevision
Portfolio pages: [Project Name] — Portfolio | Securevision Singapore
About:           About Securevision | Operations Partner Since 2006
Insights:        Security Insights & Resources | Securevision Singapore
```

**Note:** Contact and Resources no longer have dedicated pages

---

## 15. FLOATING WHATSAPP BUTTON (every page)

```html
<!-- Floating WhatsApp — place just before </body> -->
<a href="https://wa.me/6593860466"
   class="wa-float"
   target="_blank"
   rel="noopener"
   aria-label="Chat with Securevision on WhatsApp">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
  </svg>
  <span class="wa-float-label">Chat with us</span>
</a>
```

```css
.wa-float {
  position: fixed;
  bottom: 28px;
  right: 28px;
  z-index: 999;
  background: var(--whatsapp);
  color: #ffffff;
  border-radius: 50px;
  padding: 14px 20px 14px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  box-shadow: 0 4px 20px rgba(37,211,102,0.4);
  transition: var(--transition);
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  font-size: 13px;
}
.wa-float:hover {
  background: var(--whatsapp-dark);
  transform: translateY(-3px);
  box-shadow: 0 8px 28px rgba(37,211,102,0.5);
}
.wa-float-label { white-space: nowrap; }
@media (max-width: 480px) {
  .wa-float { padding: 14px; border-radius: 50%; }
  .wa-float-label { display: none; }
}
```

---

## 16. COMPANY CONSTANTS

Use these exact values throughout all pages. Never paraphrase or estimate.

```
Company name:     Securevision Pte Ltd
Established:      2006
Years operating:  Calculate dynamically: new Date().getFullYear() - 2006
Founder:          Ler Wee Meng
Founder quals:    Bachelor of Engineering, NUS · Bachelor of Laws (LLB), UOL
Founder exp:      35+ years in the security industry
Police Licence:   L/PS/000267/2023P
bizSAFE:          Level 4
BCA:              Registered Contractor
Sites protected:  2,000+
WhatsApp:         +65 9386 0466
WhatsApp URL:     https://wa.me/6593860466
Phone:            +65 6286 4796
Email:            info@securevision.com.sg
Address line 1:   Blk 1013 Geylang East Avenue 3 #02-142
Address line 2:   Singapore 389728
Near:             Opposite Paya Lebar MRT
Hours:            Monday–Friday 8:00am–5:00pm
                  Saturday by appointment
                  Sunday closed
Facebook:         https://www.facebook.com/securevision
LinkedIn:         https://www.linkedin.com/company/securevision-pte-ltd
```

### Proprietary Frameworks
```
SECURE™  —  Site-Engineered Controls for Unified Risk Elimination
VESTA™   —  Securevision Enterprise Platform
GantryGo™ — Vehicle Gantry Intercom System
```

---

## 17. PAGE TEMPLATES REFERENCE

| Page type | Template name | Pages using it |
|---|---|---|
| Homepage | CLARITY (13 sections) | index.html only |
| Solution pages | Structure B (9 sections) | 13 solution pages |
| Technology landing | Tech Landing (8 sections) | technology.html |
| Subsystem pages | Subsystem (8 sections) | 4 subsystem pages |
| Brand pages | Brand (5 sections) | 20 brand pages |
| Portfolio landing | Portfolio Hub | portfolio.html |
| Portfolio project | Project Detail | 4 project pages |
| About | Unique | about.html |
| Contact | Unique | contact.html |
| Resources | Unique | resources.html |
| Insights | Unique | insights.html |

---

## 18. SECTION BACKGROUND SEQUENCE

Apply this alternating sequence on every multi-section page:

```
Section 1 (Hero):      dark gradient (#0E1A2B → #1a2942)
Section 2:             white (#FFFFFF)
Section 3:             light gray (#F8F9FA)
Section 4:             white (#FFFFFF)
Section 5:             light gray (#F8F9FA)
Section 6:             white (#FFFFFF)
...continues alternating...
Final section (CTA):   dark gradient (#0E1A2B → #1a2942)
```

---

## 19. ACCESSIBILITY RULES

- All images must have descriptive `alt` text
- All icon-only links must have `aria-label`
- Colour contrast: minimum 4.5:1 for body text
- All interactive elements must be keyboard-focusable
- `lang="en"` on every `<html>` tag
- Skip-to-content link not required but all pages must have logical heading order (H1 → H2 → H3)
- Never use colour alone to convey information

---

## 20. JAVASCRIPT CONVENTIONS

- Vanilla JS only — no jQuery, no libraries
- All scripts in a single `<script>` block before `</body>`
- Dynamic year calculation on every page:
```javascript
const yearsSince = new Date().getFullYear() - 2006;
document.querySelectorAll('.years-since').forEach(el => el.textContent = yearsSince);
```
- Mobile menu toggle function:
```javascript
function toggleMobileMenu() {
  document.getElementById('mobileMenu').classList.toggle('active');
}
function toggleSubmenu(id) {
  const sub = document.getElementById(id);
  const isOpen = sub.style.display === 'block';
  document.querySelectorAll('.mobile-submenu').forEach(s => s.style.display = 'none');
  if (!isOpen) sub.style.display = 'block';
}
```

---

## HOW TO USE THIS DOCUMENT

1. **Copy this entire document**
2. **Paste it at the top of every Antigravity prompt**
3. **Add the specific page instruction below it** using this format:

```
--- PAGE INSTRUCTION ---
Page:     [page name]
File:     [filename.html]
Template: [template name from Section 17]
Accent:   [colour hex for this page type]

[Specific sections, content, and structure for this page]
```

The global instruction provides the rules. The page instruction provides the content. Together they produce a consistent, professional, SEO-ready page every time.

---

*Securevision Global Design Instruction v1.0 — March 2026*
*Do not modify without updating all dependent page prompts*
