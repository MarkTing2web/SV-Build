# Securevision — Creative Partner Brief for Gemini
## Version 1.0 — May 2026
## Purpose: Align Gemini on company identity, website architecture, content standards,
##          visual language, and image direction so it can assist across all creative tasks.

---

## PART 1 — WHO SECUREVISION IS

### The Company

**Securevision Pte Ltd** is a Singapore-based security systems integrator, established in 2006.

The founder is **Ler Wee Meng** — NUS Bachelor of Engineering, University of London LLB, 37+ years in the security industry. He is the technical and commercial authority behind the company. When the site speaks in first person, it is his voice. When the site explains an engineering decision, it reflects his judgment — not generic industry copy.

The company designs, supplies, installs, and maintains integrated security systems for Singapore properties. Their scope covers:

- **Premises Security** — CCTV cameras, AI video analytics, burglar alarms, intrusion sensors
- **Entry & Access** — Door access control, biometric readers, IP intercoms, visitor management
- **Vehicle Management** — Automatic gates, barrier systems, licence plate recognition (LPR), car park management
- **Communications** — IP phone systems (IPPBX), handsets, network infrastructure
- **Platform & Management** — VESTA (their own estate management platform), Milestone VMS, HikCentral, ZKTeco CVSecurity

**Credentials:** Police Licensed (SPF). BCA Registered. bizSAFE Level 3. 2,000+ sites protected across Singapore.

**Key brand partners:** Hikvision, Hanwha, Uniview, Milesight, Suprema, ZKTeco, HID, Akuvox, Aiphone, AJAX, RISCO, Paradox, DSC, FAAC, MAG, Dormer, Yeastar, Fanvil, Yealink, Omada (TP-Link), Ruijie.

---

### What Securevision Is — and Is Not

**They are an integrator, not an installer.** This distinction is central to the brand. An integrator designs the system architecture before specifying a single device. An installer just puts things up. Securevision always uses the word "integrator" or "we design and integrate" — never "we install" as the primary descriptor.

**They are a consultancy-first business.** The primary conversion goal of the website is to get a client to book a site assessment — not to buy a product online. There is no e-commerce, no shopping cart, no public price list.

**They speak to property decision-makers** — not end consumers, not IT managers, not DIY homeowners. The audience is:
- MCST chairs and managing agents (condominiums)
- Facilities managers and building owners (commercial, industrial)
- Business owners and office managers (commercial)
- Architects and builders (new developments)
- Private homeowners with landed properties (residential)
- Healthcare administrators and school principals (institutions)

---

### Tone of Voice

This is the most important thing to internalise before writing anything.

**Engineering-led, not marketing-led.** Securevision earns trust through specificity and honesty, not through superlatives and hype. Every claim must be defensible. Every recommendation must have a reason.

**Direct, but not cold.** The founder has 37 years of experience and speaks plainly. He does not oversell. He tells clients what they actually need — including when a cheaper solution is the right one.

**Never use these words and phrases:**
- "World-class", "best-in-class", "cutting-edge", "state-of-the-art"
- "One-stop shop", "holistic solution", "seamless integration" (as a filler phrase)
- "We are committed to...", "Our passion is...", "We pride ourselves on..."
- "Affordable", "cheapest", "best value" (on price — Securevision competes on quality and expertise, not price)
- "As a leading provider..." or any version of self-described leadership without proof

**Always use:**
- Specific outcomes — "reduced guard manpower by 40%", "zero cabling rework"
- Engineering language that is accessible — explain the why, not just the what
- Singapore-specific context — MCSTs, HDB, GCBs, NEA regulations, SPF licensing
- British English — authorisation, optimisation, licence, programme, recognisable, centre

**Sentence construction:**
- Short declarative sentences for impact — "Security that works as one system — not separate parts."
- Avoid passive voice — "We designed the system" not "The system was designed"
- Questions work well as section openers — "Why does your current intercom keep failing?"

---

## PART 2 — THE WEBSITE ARCHITECTURE

### What the Site Is

The website at **www.securevision.com.sg** (staging: **svbuild.vercel.app**) is a B2B and B2C authority and lead generation site. It is structured around **what clients are protecting**, not around what Securevision sells.

### The Five Navigation Areas

**Solutions** — organised by property type (8 types):
1. Residential (landed homes, bungalows, GCBs)
2. Condominiums (MCST-managed estates)
3. Commercial (offices, retail, hotels, buildings)
4. Industrial (factories, warehouses, logistics)
5. Institutions (schools, government, civic)
6. Healthcare (hospitals, nursing homes, clinics)
7. Managed Living (worker dormitories, co-living)
8. Data Centres

**Systems** — organised by what the system does (5 groups):
1. Premises Security → /systems/surveillance.html
2. Entry & Access → /systems/access-control.html
3. Vehicle Management → /systems/vehicle-access.html
4. Communications → /systems/communications.html
5. Platform & Management → /systems/platform.html

**Brands** — organised by system group (5 groups matching Systems above):
1. Premises Security — Hikvision, Hanwha, Uniview, Milesight, AJAX, RISCO, Paradox, DSC
2. Entry & Access — Suprema, ZKTeco, HID, Akuvox, Aiphone, Kocom, EntryPass, MicroEngine
3. Vehicle Management — FAAC, MAG, Dormer, GantryGo (LPR software)
4. Communications — Yeastar, Fanvil, Yealink, Omada, Ruijie
5. Platform & Management — VESTA, Milestone VMS, HikCentral, ZKTeco CVSecurity

**Portfolio** — real completed projects, filterable by property type and system group

**Insights** — articles, written in Ler Wee Meng's voice as the expert founder

---

### The Congruency Principle

This is a design rule that governs all content. The same taxonomy must appear consistently across the homepage, systems hub, brands hub, portfolio, and navigation. A client who arrives at the homepage, clicks through to Systems, then to Brands, should encounter the same logical groupings at every step.

When writing any content that references Securevision's system categories, always use these exact labels:
- **Premises Security** (not "Surveillance", not "CCTV systems")
- **Entry & Access** (not "Access Control", not "People Access Control")
- **Vehicle Management** (not "Vehicle Access", not "Vehicle Access & Barriers")
- **Communications** (new category — IP phones and network)
- **Platform & Management** (not "Platform Management", not "VESTA")

---

### Page Structure Standard

Every page on the site follows an alternating section pattern:

```
Hero           — dark overlay on a background image, white text, left-aligned
Trust Bar      — Police Licensed | bizSAFE | BCA Registered | X Sites Protected
Breadcrumb     — Home > [Section] > [Page]
Section 2      — white background
Section 3      — light grey background (#F8F9FA)
Section 4      — white
Section 5      — light grey
...alternating...
Final CTA      — dark overlay on background image, centred, white text
Footer         — dark, injected by nav-footer.js
```

**Section headers are always left-aligned.** Only the CTA section is centred. This is a deliberate design rule — the site does not centre-align body content.

---

## PART 3 — DESIGN SYSTEM

### Colour Palette

| Name | Hex | Use |
|---|---|---|
| Primary Blue | `#0056b3` | Buttons, links, primary actions |
| Dark Blue | `#003d82` | Hover states, dark accents |
| Dark Navy | `#0E1A2B` | Hero overlays, dark section backgrounds |
| Deep Navy | `#1a2942` | Secondary dark, gradients |
| Text Dark | `#1B1F23` | All headings |
| Text Grey | `#333333` | Body text |
| Text Light | `#5F6368` | Secondary text, captions |
| Background Light | `#F8F9FA` | Alternating section backgrounds |
| Border Light | `#E8EAED` | Card borders, dividers |
| Accent Green | `#25d366` | WhatsApp button only — nothing else |

**Sector accent colours** (used on property type pages for badges, accents, hero tints):
| Sector | Dark accent (for text/badges) | Light (decorative only) |
|---|---|---|
| Residential / Homes | `#257000` | `#38B000` |
| Condominiums | `#2d45c4` | `#4361EE` |
| Commercial | `#B54E00` | `#FF6D00` |
| Industrial | `#5a0892` | `#7209B7` |
| Institutions | `#1B4F72` | `#2471A3` |
| Healthcare | `#0D7377` | `#17A2A7` |
| Communications | `#5a0892` | `#7209B7` |

**System group accent colours** (used on systems pages):
| System | Accent |
|---|---|
| Premises Security | `#2b6cb0` |
| Entry & Access | `#319795` |
| Vehicle Management | `#dd6b20` |
| Communications | `#5a0892` |
| Platform & Management | `#38a169` |

---

### Typography

Three fonts, Google Fonts, always loaded together:
- **Montserrat** — all headings (H1–H4), button labels, eyebrow labels, badges
- **Inter** — all body text, lead paragraphs, captions
- **Outfit** — used selectively on the homepage and portfolio for display headlines

| Element | Font | Weight | Size |
|---|---|---|---|
| H1 | Montserrat | 800 | clamp(36px, 5.5vw, 68px) |
| H2 | Montserrat | 700 | clamp(26px, 3.5vw, 40px) |
| H3 | Montserrat | 600 | 20px |
| Eyebrow label | Montserrat | 700 | 11–12px, all caps, 2px letter-spacing |
| Body | Inter | 400 | 15–16px |
| Lead paragraph | Inter | 400 | 18px |
| Button | Montserrat | 600 | 13px, all caps |

---

## PART 4 — CONTENT WRITING RULES

### The Securevision Writing Formula

Every page and section follows this structure of thinking, in order:
1. **Problem** — what challenge does this client face?
2. **Insight** — what does Securevision know that most clients don't?
3. **Approach** — how does Securevision think about solving it?
4. **Evidence** — what has Securevision done that proves it?
5. **Action** — what should the client do next?

Not every section hits all five — but the overall page arc should follow this sequence. Never start with the solution before establishing the problem.

---

### Section Heading Standards

**H2 section headings** are outcome-oriented or problem-framing — not label-only:
- Good: "When Your Intercom Fails at 11pm, Everything Stops."
- Good: "Most CCTV Systems Record. Ours Detect."
- Bad: "Our CCTV Solutions" or "About Our Services"

**Eyebrow labels** (the small all-caps label above the H2) are factual context-setters:
- Good: "The Operational Challenge", "What We've Learned", "Proven Results"
- Bad: "Introduction", "Section 3", "Overview"

---

### Card and List Copy Standards

Each card (capability card, feature card, system card) follows this structure:
- **H3**: Short, specific label — 2–5 words
- **Body**: 1–2 sentences. Specific. No padding. The second sentence adds a detail the first didn't.
- No bullet-pointed features inside cards — prose only

Example of good card copy:
> **Licence Plate Recognition**
> 99%+ accuracy on Singapore plates, ensuring resident vehicles pass through without guard intervention. Integrated with your visitor pre-registration list for seamless guest entry.

Example of bad card copy:
> **LPR System**
> Our advanced AI-powered LPR solution provides cutting-edge vehicle recognition capabilities for your property.

---

### CTA Copy Standards

Every CTA section has:
- **Eyebrow:** Short context label (e.g. "Site Assessment", "Integrated Consultation")
- **H2:** A tension-creating headline — not a command, a consequence. Example: "The Right Platform Starts With the Right Assessment." Not "Contact Us Today."
- **Subtitle:** One sentence expanding on why the action matters. Specific to the page topic.
- **Primary button:** Action label (e.g. "Book a Site Assessment", "Book a Consultation")
- **Secondary button:** WhatsApp — "💬 WhatsApp an Engineer"
- **Trust note:** "Police Licence [number] · bizSAFE Level 3 · Serving Singapore Since 2006"

---

### What to Avoid in All Copy

| Avoid | Because |
|---|---|
| "We are proud to offer..." | Padding with no meaning |
| "A wide range of solutions" | Vague — say which solutions |
| "Trusted by hundreds of clients" | Weak — use the actual number (2,000+ sites) |
| "State-of-the-art technology" | Meaningless — say what the technology does |
| "Competitive pricing" | Securevision does not compete on price |
| Passive voice | "The system was designed" → "We designed the system" |
| Rhetorical "we" questions | "Are you looking for security?" → cut it |
| Ellipsis for drama... | Not the brand voice |

---

## PART 5 — IMAGE DIRECTION

### The Core Rule for All Images

Every image on this site must feel like it belongs to a **professional Singapore engineering firm**. Not a consumer electronics brand. Not a stock photo library. Not a Hollywood security drama. Real properties, real hardware, real people, real Singapore.

---

### People in Images

**All people must be Asian, in recognisably Singaporean settings.**

Singapore is multiracial. Images should reflect that naturally — predominantly Chinese, with Malay, Indian, and other ethnic representation woven in. The mix should feel authentic to Singapore, not artificially balanced.

**Securevision engineers and technicians:**
- White or black polo-T shirts with "Securevision" branding visible on the chest
- No generic hi-vis vests, no unbranded clothing, no hard hats unless on a construction site
- Working purposefully — installing a camera, reviewing a dashboard, walking a site — not posing

**Clients and property stakeholders:**
- Dressed professionally — business casual for office/commercial settings, smart casual for residential
- Decision-makers look like actual Singapore property managers and business owners — not models
- MCSTs and managing agents are typically older (50s–60s), pragmatic, not tech-forward
- Architects and developers are typically younger, design-conscious

---

### Singapore Settings and Architecture

**Residential:**
- Landed properties — Singapore terrace houses, semi-detached, bungalows, GCBs
- Lush tropical gardens, rendered walls, covered porticos, quality gates and fencing
- Not UK suburbia, not US tract housing, not European villas

**Condominiums:**
- Modern or 1990s–2000s estate architecture — guardhouse at entrance, covered car park, barrier arm, lobby
- Common areas: swimming pool vicinity, lift lobby, letter box area, function room entrance
- Look for: Akuvox intercom panels at door, CCTV domes overhead, card reader at gates

**Commercial:**
- Singapore office towers, business parks, shophouses converted to offices
- Lobby with reception desk, turnstile access, CCTV above entry points
- Not generic glass-box America — Singapore commercial architecture has tropical shading, greenery integration

**Industrial:**
- Tuas, Jurong, Mandai, Pioneer — flat-roof warehouses, loading bays, perimeter fencing
- Wide vehicle entry lanes, barrier arms, LPR camera mounted on gantry post
- Workers in company shirts or safety gear appropriate to the industry

**Infrastructure:**
- Singapore HDB void decks, covered walkways, multi-storey car parks
- Tropical light — not grey UK overcast, not harsh summer glare

---

### Security Hardware in Images

When hardware appears, it must look like real, modern, installed commercial equipment:

**Cameras:** Hikvision or Hanwha-style dome and bullet cameras — white or grey, ceiling or wall-mounted, with visible cable management. Not generic black cartoon cameras.

**Access terminals:** ZKTeco or Suprema face recognition terminals — sleek, vertical, touchscreen, mounted at door height. Akuvox video intercoms — clean, flush-mounted, with camera and speaker visible.

**Barriers and gates:** FAAC or MAG barrier arms — yellow-tipped white arm, control box on post, LPR camera visible above. Auto-gates — sliding or swing, powder-coated steel, remote-operated.

**IP phones:** Yeastar or Fanvil desk phones — modern SIP handsets, not old-style chunky office phones.

**Dashboards and screens:** Real UI on professional monitors — not futuristic holographic interfaces. Multiple camera feeds in a grid, access log lists, map overlays. Real-looking software, not concept renders.

---

### Photography Style

**Aim for: professional editorial photography aesthetic**
- Controlled, natural light where possible — Singapore golden hour is ideal (6–7am, 6–7pm)
- Depth of field — sharp subject, contextual background
- Clean composition — no cluttered frames, no distracting elements
- Slight cinematic grade — not oversaturated, not flat

**Hero images specifically:**
- Wide angle — the image fills the full browser width
- Subject in foreground or mid-ground, environment visible behind
- Must tolerate a dark overlay (rgba 14, 26, 43, 0.75–0.85) and remain legible as background
- Left third of image should be relatively uncluttered — text appears there

**Card and section images:**
- 16:9 or 4:3 aspect ratio
- Clear subject — not artistically ambiguous
- Hardware images: clean, well-lit, installed context (not product-on-white-background)

---

### What to Avoid in Images

| Avoid | Instead |
|---|---|
| Glowing padlocks floating in digital space | Physical hardware installed in a real building |
| Dark rooms with blue matrix screens | Real monitoring stations with normal office lighting |
| Hands on keyboards in the dark | Engineers reviewing a proper CCTV dashboard in daylight |
| Generic "businessman shaking hands" | Specific site walk with engineer and client |
| Western-looking subjects | Asian faces in Singapore settings |
| Generic stock photo CCTV cameras | Real dome or bullet cameras installed on ceilings |
| Hollywood guard room aesthetics | Actual Singapore guardhouse or monitoring room |
| Surveillance footage aesthetic (fish-eye, timestamp) | Clean, sharp editorial photography |
| Robots, AI visualisations, circuit boards | Real systems doing real things |
| Skylines of other cities | Singapore skyline — or no skyline at all |

---

## PART 6 — IMAGE DIMENSIONS BY USE

| Use | Dimensions | Notes |
|---|---|---|
| Hero background | 1920 × 1080px minimum | Must work with dark overlay |
| OG / Social share | 1200 × 630px | `/images/og-default.jpg` convention |
| Section / split-layout | 800 × 600px or 4:3 | Appears beside text |
| Card image | 600 × 400px | 3:2 or 16:9 |
| Portfolio cover | 1200 × 800px | Project thumbnail |
| Insights article cover | 1200 × 480px | Wide, short banner format |
| In-article | 800 × 500px | Inline content |
| CTA background | 1920 × 900px | Dark overlay applied in CSS |

---

## PART 7 — THE VESTA PRODUCT

VESTA is Securevision's own proprietary estate management platform, designed specifically for Singapore condominiums. It is not a generic off-the-shelf product — it was built by the Securevision team.

When mentioning VESTA in any content:
- Position it as Securevision's product — "VESTA, Securevision's estate management platform"
- Its target user is condominium operations — guard desk, resident management, visitor pre-registration, gantry management, patrol logging, facility booking
- It is distinct from professional platforms like Milestone or HikCentral, which are third-party tools Securevision integrates

---

## PART 8 — FREQUENTLY NEEDED REFERENCE DETAILS

**Company name:** Securevision Pte Ltd
**Founder:** Ler Wee Meng
**Founded:** 2006
**Primary phone:** +65 6286 4796
**WhatsApp:** +65 9386 0466 (wa.me/6593860466)
**Email:** enquiry@securevision.com.sg
**Address:** Blk 1013 Geylang East Ave 3 #02-142, Singapore 389728
**Website:** www.securevision.com.sg
**Staging:** svbuild.vercel.app

**Trust credentials (use exactly as written):**
- Police Licence [number injected by site-config.js]
- bizSAFE Level 3
- BCA Registered
- 2,000+ Sites Protected
- Serving Singapore Since 2006

**Primary CTA:** "Book a Site Assessment" (links to /request-site-assessment-singapore.html)
**WhatsApp CTA:** "💬 WhatsApp an Engineer" or "💬 Talk to an Engineer"

---

## PART 9 — HOW TO WORK WITH SECUREVISION'S CONTENT SYSTEM

The website is built and maintained using a structured content system with Claude as the primary AI partner. Claude holds the full design system, templates, and CSS in memory across sessions.

When Gemini produces content or images that will be integrated into the site:
- Use the exact taxonomy labels (Premises Security, Entry & Access, Vehicle Management, Communications, Platform & Management)
- Use the exact font and colour references from Part 3
- Write in British English throughout
- Flag anything that requires a new image path — the convention is `/images/[folder]/[descriptive-slug].[webp or png]`
- Do not invent new CSS class names — flag them with a comment and leave implementation to Claude

The goal is for Gemini-produced content and images to slot into the existing design system without requiring structural rework. When in doubt about where something fits, describe the page section it's for and the relevant property type or system group — the taxonomy is consistent enough that placement should be clear.

---

*Securevision Creative Partner Brief v1.0 — May 2026*
*Prepared for Gemini by Claude (Anthropic)*
*Update this document whenever the taxonomy, colour system, or brand voice evolves*
