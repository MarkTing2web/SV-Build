# SECUREVISION WEBSITE SITEMAP

**Last Updated:** March 24, 2026  
**Total Pages Built:** 50+ HTML pages  
**Navigation Items:** 6 main menu items + search (Solutions, Systems, Brands, Portfolio, Insights, About, Search)

---

## NAVIGATION STRUCTURE

### **Desktop Navigation:**
```
[LOGO + SECUREVISION] | SOLUTIONS | SYSTEMS | BRANDS | PORTFOLIO | INSIGHTS | ABOUT | [🔍]
         ↓                  ↓          ↓         ↓                                      ↓
    (Links to home)    (Hover menu) (Hover menu) (Hover menu)                    (Search overlay)
```

### **Solutions Dropdown (Hover):**
```
SOLUTIONS (click → solutions-hub.html)
└─ On Hover:
   ├─ Residential
   ├─ Condominiums
   ├─ Commercial
   ├─ Industrial
   └─ Institutions
```

### **Systems Dropdown (Hover):**
```
SYSTEMS (click → systems.html)
└─ On Hover:
   ├─ Surveillance & CCTV
   ├─ People Access Control
   ├─ Vehicle Access & Barriers
   ├─ Platform Integration
   └─ View All →
```

### **Brands Dropdown (Hover):**
```
BRANDS (click → brands.html)
└─ On Hover (Simple Dropdown):
   ├─ Surveillance
   ├─ Access Control
   ├─ Intercom
   ├─ Alarms
   ├─ Gates & Barriers
   ├─ ─────────────
   └─ View All Brands →

Note: Categories are section headers on brands.html page
Individual brands: Hikvision, Uniview, Hanwha, Milesight (Surveillance),
Suprema, ZKTeco, HID, EntryPass (Access), Akuvox, Aiphone, Kocom (Intercom),
Ajax, RISCO, Paradox, DSC, GE/Caddx (Alarms), FAAC, MAG, Dormer (Gates)
```

### **Mobile Navigation (Hamburger Menu):**
```
Mobile Header Layout:
┌─────────────────────────┐
│ [Logo] SECURE  [☰] [🔍] │
│   ↑            ↑    ↑    │
│ Left       Center Right  │
└─────────────────────────┘

Menu Expanded (when ☰ tapped):
┌─────────────────────┐
│ ✕ MENU             │
├─────────────────────┤
│ Solutions           │ ← Links to solutions-hub.html
│ Systems             │ ← Links to systems.html
│ Brands              │ ← Links to brands.html
│ Portfolio           │ ← Links to portfolio.html
│ Insights            │ ← Links to insights.html
│ About               │ ← Links to about.html (includes contact)
├─────────────────────┤
│ 💬 WhatsApp Us      │
└─────────────────────┘

Notes:
- Logo scales down on mobile (40px → 32px → 28px)
- Wordmark scales down (22px → 18px → 16px on phones)
- **Interactive Dropdowns:** Mobile menu now features accordion-style sub-menus for deep navigation.
- WhatsApp NOT in desktop nav (only mobile menu + floating button)
```

### **Search Functionality:**

**Desktop Search (Click 🔍 icon):**
```
┌────────────────────────────────────────────────────────────┐
│ [←] [Search for products, systems, brands...          ] ✕ │
├────────────────────────────────────────────────────────────┤
│ Popular Searches:                                          │
│ • Hikvision    • Access Control    • Condo Intercom       │
│ • Ajax Alarm   • CCTV              • Auto Gates            │
└────────────────────────────────────────────────────────────┘

As user types:
┌────────────────────────────────────────────────────────────┐
│ [←] [access control                                    ] ✕ │
├────────────────────────────────────────────────────────────┤
│ Suggestions:                                               │
│ 🚪 People Access Control Systems                          │
│ 🏢 Commercial Office - Access Control                     │
│ 🏗️ Access Control Brands (Suprema, ZKTeco, HID...)        │
│ 🏘️ Condominiums - Access Control Solutions                │
└────────────────────────────────────────────────────────────┘
```

**Mobile Search (Tap 🔍 icon):**
```
┌─────────────────────────┐
│ [←] [Search...      ] ⌨️ │
├─────────────────────────┤
│                         │
│ Popular:                │
│ • Hikvision             │
│ • Access Control        │
│ • Ajax Alarm            │
│ • Condo Intercom        │
│                         │
│ (Results appear below   │
│  as user types)         │
│                         │
└─────────────────────────┘
```

**What Search Indexes:**
- ✅ All page titles
- ✅ Main headings (H1, H2)
- ✅ Product/brand names (Hikvision, Suprema, Ajax, etc.)
- ✅ System names (Surveillance, Access Control, Intercom, etc.)
- ✅ Sector names (Residential, Condominiums, Commercial, etc.)
- ✅ Key features and specifications
- ✅ FAQ questions

**Search Features:**
- Auto-complete suggestions as you type
- Categorized results (Systems, Brands, Solutions)
- "Did you mean..." for typos
- Popular searches displayed when empty
- Mobile-optimized full-screen overlay
- Fast client-side search (instant results)

**Implementation:**
- Phase 1: Client-side search using Lunr.js or Fuse.js
- Phase 2: Track search analytics (what users look for)
- Phase 3: Optimize based on user behavior

---

## COMPLETE SITE STRUCTURE

```
SECUREVISION.COM.SG
│
├── HOME (/)
│   └── ✅ index.html - Homepage
│       - Logo in header links back here
│       - "Home" removed from navigation (logo serves this purpose)
│
├── SOLUTIONS (Hub: solutions-hub.html)
│   │
│   ├── BY PROPERTY TYPE
│   │   │
│   │   ├── 1. RESIDENTIAL (/residential/)
│   │   │   ├── ✅ residential-building.html - For New Builds
│   │   │   ├── ✅ residential-existing.html - For Existing Homes
│   │   │   └── ✅ residential-trade.html - For Trade Professionals
│   │   │
│   │   ├── 2. CONDOMINIUMS (/condominiums/)
│   │   │   ├── ✅ condominiums.html - Main Landing
│   │   │   ├── ✅ condominiums-mcst.html - For MCST & Managing Agents
│   │   │   └── ✅ condominiums-security.html - For Security Partners
│   │   │
│   │   ├── 3. COMMERCIAL (/commercial/)
│   │   │   ├── ✅ commercial.html - Main Landing
│   │   │   ├── ✅ commercial-office.html - Office Solutions
│   │   │   ├── ✅ commercial-retail.html - Retail Solutions
│   │   │   └── ✅ commercial-hotel.html - Hotel Solutions
│   │   │
│   │   ├── 4. INDUSTRIAL (/industrial/)
│   │   │   └── ✅ industrial.html - Industrial Solutions
│   │   │
│   │   └── 5. INSTITUTIONS (/institutions/)
│   │       └── ✅ institutions.html - Educational & Healthcare
│   │
│   └── Cross-link to SYSTEMS hub at bottom of page
│
├── SYSTEMS (Hub: systems-hub.html)
│   │
│   ├── BY SYSTEM TYPE
│   │   ├── ✅ surveillance-systems.html - CCTV & Surveillance
│   │   ├── ✅ people-access.html - People Access Control
│   │   ├── ✅ vehicle-access.html - Vehicle Access & Barriers
│   │   └── ✅ platform-integration.html - Platform & Integration
│   │
│   └── Cross-link to SOLUTIONS hub at top of page
│
├── BRANDS (Hub: brands.html)
│   │
│   ├── SURVEILLANCE BRANDS
│   │   ├── ✅ hikvision-singapore.html - Hikvision
│   │   ├── ✅ uniview-singapore.html - Uniview
│   │   ├── ✅ hanwha-samsung-singapore.html - Hanwha (Samsung)
│   │   └── ✅ milesight-singapore.html - Milesight
│   │
│   ├── ACCESS CONTROL BRANDS
│   │   ├── ✅ suprema-singapore.html - Suprema
│   │   ├── ✅ zkteco-singapore.html - ZKTeco
│   │   ├── ✅ hid-singapore.html - HID Global
│   │   └── ✅ entrypass-singapore.html - EntryPass
│   │
│   ├── INTERCOM BRANDS
│   │   ├── ✅ akuvox-singapore.html - Akuvox
│   │   ├── ✅ aiphone-singapore.html - Aiphone
│   │   └── ✅ kocom-singapore.html - Kocom
│   │
│   ├── ALARM BRANDS
│   │   ├── ✅ ajax-alarm-singapore.html - Ajax Alarm
│   │   ├── ✅ risco-alarm-singapore.html - RISCO Alarm
│   │   ├── ✅ paradox-alarm-singapore.html - Paradox Alarm
│   │   ├── ✅ dsc-alarm-singapore.html - DSC Alarm
│   │   └── ✅ ge-caddx-alarm-singapore.html - GE/Caddx Alarm
│   │
│   ├── GATE & BARRIER BRANDS
│   │   ├── ✅ faac-singapore.html - FAAC
│   │   ├── ✅ mag-gates-singapore.html - MAG Gates
│   │   └── ✅ dormer-singapore.html - Dormer
│   │
│   └── INTEGRATION PLATFORMS
│       └── ✅ microengine-singapore.html - MicroEngine
│
├── PORTFOLIO (/portfolio/)
│   ├── ✅ portfolio.html - Portfolio Overview
│   ├── ✅ portfolio-lviv.html - L'viv Residences
│   ├── ✅ portfolio-scape.html - SCAPE Project
│   ├── ✅ portfolio-sta.html - STA Building
│   └── ✅ portfolio-cyrus.html - Cyrus Tech Park
│
├── INSIGHTS (/insights/)
│   ├── ✅ insights.html - Insights & Articles Hub
│   ├── ✅ resources.html - Resources
│   ├── ✅ cctv.html - Comprehensive CCTV Guide (Blog)
│   └── ✅ burglar-alarm.html - Comprehensive Burglar Alarm Guide (Blog)
│
└── ABOUT (/about/)
    ├── ✅ about.html - About Securevision
    │   - Company story, founder, team
    │   - SECURE™ Framework explanation
    │   - What makes us different
    │   - Certifications overview (links to awards page)
    │   - **CONTACT SECTION (integrated here)**
    │       • Address
    │       • Phone (clickable)
    │       • WhatsApp (+65 9386 0466)
    │       • Email (clickable)
    │       • Business hours
    │       • Contact form
    │       • Map embed (optional)
    │
    └── ✅ awards-certifications.html - Awards & Certifications
        - Police License L/PS/000267/2023P
        - bizSAFE Level 3
        - BCA Registered
        - Partner awards (ADV, ZKTeco, etc.)
        - Linked from About page
```

---

## COMPLETE PAGE INVENTORY (50 Pages)

### **CORE PAGES (4 pages)**
| Page | File | Nav Placement | Notes |
|------|------|---------------|-------|
| Homepage | index.html | Logo click | Logo + "SECUREVISION" wordmark links here |
| About (includes Contact) | about.html | ABOUT | Contact section integrated into this page |
| Awards & Certifications | awards-certifications.html | Linked from About | Not in main nav |
| Search Results | search.html | Search icon (🔍) | Displays search results, accessible via search icon |

### **HUB PAGES (3 pages)**
| Hub | File | Nav Placement | Purpose |
|-----|------|---------------|---------|
| Solutions Hub | solutions-hub.html | SOLUTIONS (click) | Property type gateway |
| Systems Hub | systems-hub.html | SYSTEMS (click) | System type gateway |
| Brands Hub | brands.html | BRANDS (click) | All brands overview |

### **SECTOR SOLUTIONS (11 pages)**
| Sector | Page | File | Nav Path |
|--------|------|------|----------|
| **Residential** | New Builds | residential-building.html | Solutions → Residential |
| | Existing Homes | residential-existing.html | Solutions → Residential |
| | Trade Professionals | residential-trade.html | Solutions → Residential |
| **Condominiums** | Main Landing | condominiums.html | Solutions → Condominiums |
| | MCST & Managing Agents | condominiums-mcst.html | Solutions → Condominiums |
| | Security Partners | condominiums-security.html | Solutions → Condominiums |
| **Commercial** | Main Landing | commercial.html | Solutions → Commercial |
| | Office Solutions | commercial-office.html | Solutions → Commercial |
| | Retail Solutions | commercial-retail.html | Solutions → Commercial |
| | Hotel Solutions | commercial-hotel.html | Solutions → Commercial |
| **Industrial** | Main Landing | industrial.html | Solutions → Industrial |
| **Institutions** | Main Landing | institutions.html | Solutions → Institutions |

### **SYSTEM SOLUTIONS (4 pages)**
| System | File | Nav Path |
|--------|------|----------|
| Surveillance & CCTV | surveillance-systems.html | Systems → Surveillance |
| People Access Control | people-access.html | Systems → Access Control |
| Vehicle Access & Barriers | vehicle-access.html | Systems → Vehicle Access |
| Platform Integration | platform-integration.html | Systems → Integration |

### **BRAND PAGES (21 pages)**
| Category | Brand | File | Nav Path |
|----------|-------|------|----------|
| **Surveillance** | Hikvision | hikvision-singapore.html | Brands → Surveillance |
| | Uniview | uniview-singapore.html | Brands → Surveillance |
| | Hanwha (Samsung) | hanwha-samsung-singapore.html | Brands → Surveillance |
| | Milesight | milesight-singapore.html | Brands → Surveillance |
| **Access Control** | Suprema | suprema-singapore.html | Brands → Access Control |
| | ZKTeco | zkteco-singapore.html | Brands → Access Control |
| | HID Global | hid-singapore.html | Brands → Access Control |
| | EntryPass | entrypass-singapore.html | Brands → Access Control |
| **Intercom** | Akuvox | akuvox-singapore.html | Brands → Intercom |
| | Aiphone | aiphone-singapore.html | Brands → Intercom |
| | Kocom | kocom-singapore.html | Brands → Intercom |
| **Alarm** | Ajax | ajax-alarm-singapore.html | Brands → Alarms |
| | RISCO | risco-alarm-singapore.html | Brands → Alarms |
| | Paradox | paradox-alarm-singapore.html | Brands → Alarms |
| | DSC | dsc-alarm-singapore.html | Brands → Alarms |
| | GE/Caddx | ge-caddx-alarm-singapore.html | Brands → Alarms |
| **Gates/Barriers** | FAAC | faac-singapore.html | Brands → Gates |
| | MAG Gates | mag-gates-singapore.html | Brands → Gates |
| | Dormer | dormer-singapore.html | Brands → Gates |
| **Integration** | MicroEngine | microengine-singapore.html | Brands → Integration |

### **PORTFOLIO & INSIGHTS (7 pages)**
| Section | Page | File | Nav Placement |
|---------|------|------|---------------|
| **Portfolio** | Overview | portfolio.html | PORTFOLIO |
| | L'viv Residences | portfolio-lviv.html | Via portfolio.html |
| | SCAPE | portfolio-scape.html | Via portfolio.html |
| | STA Building | portfolio-sta.html | Via portfolio.html |
| | Cyrus Tech Park | portfolio-cyrus.html | Via portfolio.html |
| **Insights** | Insights Hub | insights.html | INSIGHTS |
| | Resources | resources.html | Via insights |
| | CCTV Guide | cctv.html | Resources / Insights |
| | Burglar Alarm | burglar-alarm.html | Resources / Insights |

---

## URL STRUCTURE (Production)

### **Core & Hub Pages**
```
securevision.com.sg/                          (Homepage)
securevision.com.sg/about/                    (About + Contact)
securevision.com.sg/awards-certifications/    (Awards)
securevision.com.sg/solutions/                (Solutions Hub)
securevision.com.sg/systems/                  (Systems Hub)
securevision.com.sg/brands/                   (Brands Hub)
```

### **Sector Solutions**
```
securevision.com.sg/residential/building/
securevision.com.sg/residential/existing/
securevision.com.sg/residential/trade/
securevision.com.sg/condominiums/
securevision.com.sg/condominiums/mcst/
securevision.com.sg/condominiums/security/
securevision.com.sg/commercial/
securevision.com.sg/commercial/office/
securevision.com.sg/commercial/retail/
securevision.com.sg/commercial/hotel/
securevision.com.sg/industrial/
securevision.com.sg/institutions/
```

### **System Solutions**
```
securevision.com.sg/surveillance-systems/
securevision.com.sg/people-access/
securevision.com.sg/vehicle-access/
securevision.com.sg/platform-integration/
```

### **Brand Pages**
```
securevision.com.sg/brands/hikvision/
securevision.com.sg/brands/suprema/
securevision.com.sg/brands/akuvox/
securevision.com.sg/brands/ajax/
securevision.com.sg/brands/faac/
[etc. for all 21 brand pages]
```

### **Portfolio & Insights**
```
securevision.com.sg/portfolio/
securevision.com.sg/portfolio/lviv/
securevision.com.sg/portfolio/scape/
securevision.com.sg/portfolio/sta/
securevision.com.sg/portfolio/cyrus/
securevision.com.sg/insights/
securevision.com.sg/resources/
```

---

## USER JOURNEY EXAMPLES

### **Journey 1: Property Owner (Solutions-First)**
```
User: "I need security for my condo"
↓
Clicks Logo/Homepage
↓
Sees hero or clicks "SOLUTIONS" in nav
↓
Lands on solutions-hub.html
↓
Clicks "Condominiums"
↓
Lands on condominiums.html (main landing)
↓
Clicks "For MCST & Managing Agents"
↓
Lands on condominiums-mcst.html
↓
Sees integrated systems for condos
↓
Clicks WhatsApp CTA or Request Assessment
```

### **Journey 2: Tech-Savvy User (System-First)**
```
User: "I want to understand access control"
↓
Google search: "access control systems Singapore"
↓
Lands on people-access.html
↓
Reads system overview
↓
Sees "This system is used in:" links to sectors
↓
Clicks "Commercial Offices"
↓
Lands on commercial-office.html
↓
Sees complete office security solution
↓
Clicks WhatsApp CTA
```

### **Journey 3: Brand Searcher**
```
User: "Hikvision Singapore authorized dealer"
↓
Google search
↓
Lands on hikvision-singapore.html
↓
Reads about Hikvision systems we install
↓
Sees "Where we install Hikvision:" links
↓
Clicks relevant sector (e.g., "Commercial")
↓
Lands on commercial.html
↓
Explores solutions
↓
Clicks Contact via About page
```

### **Journey 4: Mobile User**
```
User on mobile
↓
Lands on homepage
↓
Taps hamburger menu ☰
↓
Taps "Solutions"
↓
Lands on solutions-hub.html (no dropdown on mobile)
↓
Browses property types
↓
Taps "Residential"
↓
Browses residential sub-pages
↓
Taps WhatsApp button (sticky on mobile)
```

---

## CROSS-LINKING STRATEGY

### **Hub Pages Cross-Link:**
- **solutions-hub.html** → "Looking for a specific system? Browse by System Type →" links to systems.html
- **systems.html** → "Not sure what you need? Find solutions for your property type →" links to solutions-hub.html

### **Sector Pages Link to Systems:**
- condominiums-mcst.html → Links to people-access.html, surveillance-systems.html, etc.
- commercial-office.html → Links to people-access.html, surveillance-systems.html, etc.

### **System Pages Link to Sectors:**
- surveillance-systems.html → "Used in: Residential, Condominiums, Commercial, Industrial"
- people-access.html → "Used in: Condominiums, Commercial, Industrial, Institutions"

### **Brand Pages Link Both Ways:**
- hikvision-singapore.html → Links to surveillance-systems.html AND relevant sector pages
- suprema-singapore.html → Links to people-access.html AND relevant sector pages

### **Portfolio Links to Everything:**
- portfolio-lviv.html → Links to condominiums-mcst.html, akuvox-singapore.html, entrypass-singapore.html

---

## CONVERSION POINTS

### **Every Page Includes:**
1. **Primary CTA:** "Request Free Assessment" button/form
2. **Secondary CTA:** WhatsApp button (+65 9386 0466)
3. **Trust Elements:** 
   - Police License L/PS/000267/2023P
   - 19+ years experience
   - bizSAFE Level 3, BCA certifications
   - Client logos/testimonials (where relevant)

### **Contact Accessibility:**
| Method | Location | Implementation |
|--------|----------|----------------|
| Contact Form | About page | Embedded form section |
| WhatsApp | Sticky button | Bottom-right on all pages |
| Phone | About page + Footer | Clickable tel: link |
| Email | About page + Footer | Clickable mailto: link |
| Address | About page + Footer | With map embed |

### **Footer CTA (All Pages):**
```
┌─────────────────────────────────────────────────────────┐
│  READY TO UPGRADE YOUR SECURITY?                        │
│                                                         │
│  [Request Free Assessment]  [WhatsApp: +65 9386 0466]  │
│                                                         │
│  📞 [Phone]  |  ✉️ [Email]  |  📍 [Address]             │
│                                                         │
│  Police License: L/PS/000267/2023P  |  bizSAFE Level 3   │
└─────────────────────────────────────────────────────────┘
```

---

## SEO OPTIMIZATION

### **Primary Keywords by Section:**
| Section | Primary Keywords | Secondary Keywords |
|---------|-----------------|-------------------|
| Homepage | security systems Singapore | CCTV, access control, alarm |
| Residential | home security Singapore, auto gate | video intercom, home CCTV |
| Condominiums | condo security upgrade, IP intercom | MCST security, visitor management |
| Commercial | office security Singapore, retail CCTV | loss prevention, time attendance |
| Industrial | warehouse security, perimeter | LPR, vehicle barriers |
| Institutions | school security, hospital access | campus security, compliance |

### **Brand SEO (Each Page):**
- Primary: `[Brand] Singapore` (e.g., "Hikvision Singapore")
- Secondary: `[Brand] authorized dealer Singapore`
- Tertiary: `[Brand] installer Singapore`, `[System] [Brand]`

### **Long-tail SEO:**
- "Best CCTV for condominiums Singapore"
- "Access control system for office Singapore"
- "Hikvision authorized dealer Singapore"
- "Condo intercom upgrade Singapore"
- "Retail security camera system Singapore"

---

## TECHNICAL SPECIFICATIONS

### **Design System:**
- **Primary Color:** #0056b3 (Blue)
- **Accent Color:** #25d366 (WhatsApp Green)
- **Fonts:** 
  - Headings: Montserrat (600, 700)
  - Body: Inter (400, 500)
- **Logo:** securevision-logo-dark.svg
- **Mobile Breakpoints:** 768px (tablet), 1024px (desktop)

### **Navigation Specifications:**
- **Desktop:** Logo left, nav items center/right, 6 items
- **Mobile:** Hamburger menu, logo center, WhatsApp in menu
- **Hover:** Dropdowns on Solutions, Systems, Brands
- **Click:** All items link to hub/main pages

### **Responsive Behavior:**
- **Desktop (>1024px):** Full navigation with hover dropdowns
- **Tablet (768px-1024px):** Full navigation, may collapse some items
- **Mobile (<768px):** Hamburger menu, no dropdowns, direct links to hubs

### **Common Elements (All Pages):**
- Hero sections with value propositions
- Trust badges (Police License, bizSAFE 4, BCA, 19+ years)
- System-by-system breakdowns
- Size/scale-based configurations (where applicable)
- FAQ sections (7-8 questions)
- CTA sections (Request Assessment + WhatsApp)
- Footer with contact info and quick links

---

## FRAMEWORK CONSISTENCY

### **CLARITY Framework Applied:**
All pages follow this structure:
- **C**apture - Hero with problem/opportunity statement
- **L**ogic - Systems/solutions breakdown with reasoning
- **A**ssurance - Credentials, licensing, certifications, case studies
- **R**elevance - Sector-specific pain points and solutions
- **I**llustrate - Visual examples, configurations, diagrams
- **T**ech Fit - System/product recommendations
- **Y**ield - ROI, benefits, outcomes, results

### **Recurring Page Elements:**
- Persona routing (where applicable)
- System-by-system deep dives
- Configuration by property size/type
- Case study placeholders
- Brand showcases with "Why we choose X" sections
- Integration value propositions
- Clear next steps (CTA)

---

## CONTENT STATUS

### ✅ **COMPLETE (50 pages)**
All HTML pages built with full structure

### ⏳ **CONTENT TO ENHANCE**
| Priority | Item | Details Needed |
|----------|------|----------------|
| **HIGH** | About page | Integrate contact section, company story, team |
| **HIGH** | Portfolio case studies | Photos, metrics, client testimonials |
| **HIGH** | Brand page content | Product images, installation photos |
| **MEDIUM** | Hub pages | Ensure strong routing, cross-linking |
| **MEDIUM** | Client testimonials | Quotes from satisfied clients |
| **MEDIUM** | Insights articles | Blog posts, how-to guides, industry updates |
| **LOW** | Video content | Installation videos, product demos |

### 🔄 **PAGES TO BUILD (Future)**
| Priority | Page | Purpose |
|----------|------|---------|
| **LOW** | Privacy Policy | Legal requirement |
| **LOW** | Terms of Service | Legal requirement |
| **LOW** | Sitemap (HTML) | SEO & user navigation |
| **LOW** | 404 Page | Custom error page |

---

## FILE NAMING CONVENTION

### **Current Files:**
```
/mnt/user-data/uploads/
├── index.html (Homepage)
├── about.html (About + Contact)
├── awards-certifications.html
├── solutions-hub.html (Solutions Hub - may need to create)
├── technology.html (Rename to: systems.html)
├── brands.html (Brands Hub)
├── residential-building.html
├── residential-existing.html
├── residential-trade.html
├── condominiums.html
├── condominiums-mcst.html
├── condominiums-security.html
├── commercial.html
├── commercial-office.html
├── commercial-retail.html
├── commercial-hotel.html
├── industrial.html
├── institutions.html
├── surveillance-systems.html
├── people-access.html
├── vehicle-access.html
├── platform-integration.html
├── [21 brand pages]
├── portfolio.html
├── portfolio-lviv.html
├── portfolio-scape.html
├── portfolio-sta.html
├── portfolio-cyrus.html
├── insights.html
└── resources.html
```

### **Files to Create/Modify:**
1. **Create:** solutions-hub.html (if not exists)
2. **Create:** search.html (search results page)
3. **Rename:** technology.html → systems.html
4. **Modify:** about.html (add contact section)
5. **Review:** All hub pages for strong routing
6. **Implement:** Search functionality (client-side with Lunr.js or Fuse.js)

---

## ANALYTICS & TRACKING (To Implement)

### **Key Metrics:**
| Metric | Purpose |
|--------|---------|
| Page views by sector | Identify hottest sectors |
| Hub page interactions | See which path users take |
| CTA click rates | Conversion optimization |
| WhatsApp clicks | Direct inquiry tracking |
| Form submissions | Lead generation |
| Time on page | Content engagement |
| Scroll depth | Content consumption |
| Bounce rate | Content relevance |
| Mobile vs Desktop | Device optimization |

### **Conversion Goals:**
1. Contact form submission (About page)
2. WhatsApp click (sticky button)
3. Phone click (About page, footer)
4. Email click (About page, footer)
5. Request Assessment button clicks
6. Portfolio case study views
7. Brand page engagement
8. Hub page → sector page flow

---

## MAINTENANCE SCHEDULE

### **Weekly:**
- Monitor WhatsApp inquiries from website
- Track which pages generate most leads
- Review form submissions

### **Monthly:**
- Update portfolio with new projects (if any)
- Add new insights/blog posts
- Review analytics for user behavior patterns

### **Quarterly:**
- Update brand product information
- Refresh case study metrics
- Review SEO performance
- Update client testimonials

### **Annually:**
- Update awards & certifications
- Refresh homepage hero messaging
- Comprehensive content audit
- Professional photography update
- Review and update hub page routing

---

## BRAND CONSISTENCY

### **Company Information:**
- **Founded:** 2006 (19+ years experience)
- **License:** Police License L/PS/000267/2023P
- **Certifications:** bizSAFE Level 3, BCA Registered
- **Founder:** Ler Wee Meng
- **Service Area:** Singapore
- **Installations:** 2,000+ sites
- **Contact:** +65 9386 0466 (WhatsApp)

### **Positioning:**
- **Not:** Product sellers, box movers, retailers
- **But:** Systems integrators, professional installers, solution architects
- **Framework:** SECURE™ Framework
- **Proprietary Systems:** GantryGo™ (vehicle access rental), VESTA™ (people access)
- **Tagline:** "Stop Guessing. Start Seeing." / "Stop Operating Blind. Start Operating Smart."

### **Messaging Pillars:**
1. **Integration over products** - Complete systems, not boxes
2. **Professional installation** - Police licensed, 19+ years
3. **Systems thinking** - How components work together
4. **Outcome-focused** - Results, not features
5. **Sector expertise** - Deep understanding of each market

---

## NOTES

- **Navigation simplified to 6 items + search** for cleaner UX
- **Search icon (🔍) added** to far right of navigation for easy access
- **Logo + SECUREVISION links to home** (removed "Home" from nav)
- **About page includes contact section** (removed "Contact" from nav)
- **WhatsApp removed from desktop nav** for cleaner, more professional look
  - Still accessible via: floating button (always visible), mobile menu, About dropdown, footer
- **Simplified dropdowns** - Mega menus replaced with clean, simple dropdowns
  - Portfolio and Insights: No dropdown (direct links)
  - Solutions, Systems, Brands, About: Simple dropdowns
- **Hub pages** (solutions-hub.html, systems.html, brands.html) are critical for user routing
- **Search functionality** uses client-side search (Lunr.js/Fuse.js) for instant results
- **Mobile-first approach** - All dropdowns become simple links on mobile, search opens full-screen overlay
- **Mobile layout:** Logo (left) | Menu (center) | Search (right)
- **Responsive logo sizing:** 40px desktop → 32px tablet → 28px phone
- **WhatsApp CTA** prominent throughout site (+65 9386 0466) via floating button, mobile menu, footer
- **All pages mobile-responsive** with tested breakpoints
- **Consistent color scheme** (blue #0056b3, green #25d366)
- **Consistent typography** (Montserrat headings, Inter body)

---

**END OF SITEMAP**

*This sitemap reflects the final approved navigation structure with 6 main menu items. Update whenever pages are added, navigation changes, or major content updates occur.*

**Key Changes from Previous Version:**
- Removed "HOME" from navigation (logo serves this purpose)
- Removed "CONTACT" from navigation (integrated into About page)
- Renamed "TECHNOLOGY" to "SYSTEMS"
- **Added search icon (🔍)** to navigation for easy site-wide search
- **Removed WhatsApp from desktop nav** (kept in mobile menu + floating button for cleaner header)
- **Simplified all mega menus to simple dropdowns** for faster, cleaner UX
- Clarified hub page structure (solutions-hub.html, systems.html, brands.html)
- Updated navigation to 6 clean items + search: Solutions, Systems, Brands, Portfolio, Insights, About, Search
- Added mobile-specific navigation behavior (no dropdowns, direct hub links)
- Mobile layout: Logo (left) | Menu (center) | Search (right) with responsive logo sizing
- Search opens full-screen overlay on mobile with keyboard
- Emphasized cross-linking between Solutions and Systems hubs
