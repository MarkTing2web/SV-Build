---
name: Securevision Design System
description: Smart Security & Integrated Systems Visual Design Tokens and Guidelines
colors:
  primary: "#0056b3"
  dark-blue: "#003d82"
  accent-green: "#25d366"
  text-dark: "#1b1f23"
  text-gray: "#333333"
  text-light: "#5f6368"
  bg-light: "#f8f9fa"
  white: "#ffffff"
  border-light: "#e8eaed"
  bg-nav: "#0a0f18"
  bg-dark: "#0e1a2b"
  # Category card gradients (insights hub)
  gradient-alarm-1: "#3b0a0a"
  gradient-alarm-2: "#7f1d1d"
  gradient-cctv-1: "#0a1628"
  gradient-cctv-2: "#1e40af"
  gradient-access-1: "#0a2620"
  gradient-access-2: "#065f46"
  gradient-vehicle-1: "#2a1a00"
  gradient-vehicle-2: "#92400e"
  gradient-ip-1: "#0a2626"
  gradient-ip-2: "#0e7490"
  gradient-platform-1: "#1a0a2e"
  gradient-platform-2: "#4c1d95"
  gradient-planning-1: "#1a1a2e"
  gradient-planning-2: "#334155"
typography:
  display:
    fontFamily: "Securevision-Display, sans-serif"
    fontSize: "clamp(36px, 5.5vw, 60px)"
    fontWeight: 700
    lineHeight: 1.1
  headline:
    fontFamily: "Securevision-Display, sans-serif"
    fontSize: "clamp(26px, 3.5vw, 40px)"
    fontWeight: 700
    lineHeight: 1.2
  title:
    fontFamily: "Securevision-Display, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Securevision-Body, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Securevision-Display, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.4
rounded:
  sm: "8px"
  md: "12px"
spacing:
  section: "80px"
  gap-4col: "24px"
  gap-3col: "28px"
  gap-2col: "32px"
  card-padding: "32px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  button-primary-hover:
    backgroundColor: "{colors.dark-blue}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  button-whatsapp:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.text-dark}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  card:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "{spacing.card-padding}"
---

# Design System: Securevision

## 1. Overview

**Creative North Star: "The Blueprint Registry"**

Securevision's visual design mirrors its physical security integrations: highly organized, technical, precise, and compliant. The layout prioritizes data density, readable document structure, and clear visual division over floating layouts or decorative fluff. 

The aesthetic is built on clean horizontal grids, strong line weights, authoritative typography, and a restrained color palette. We explicitly reject SaaS-style sand/cream backgrounds and generic floating designs, favoring structured document containers that look solid, engineered, and reliable.

**Key Characteristics:**
- High readability with balanced line length (65–75ch for body prose).
- Technical density using tables, specification lists, and visual diagrams.
- Solid visual layout with clear container dividers.

## 2. Colors

The color palette is restrained and professional, conveying security, engineering rigor, and safety compliance.

### Primary
- **Primary Blue** (#0056b3): The core brand identifier. Used for solid interactive states, primary action buttons, and focal section titles.

### Secondary
- **Deep Navy** (#003d82): Used for primary hover states, active headers, and deep visual contrast.
- **WhatsApp Green** (#25d366): Dedicated solely to real-time communication CTA actions. Must pair with dark text (#1B1F23) to meet WCAG AA requirements.

### Neutral
- **Charcoal Ink** (#1b1f23): Canonical dark text color for supreme readability.
- **Muted Gray** (#5f6368): Used for auxiliary descriptions, dates, and non-essential subtitles.
- **Off-White Cool** (#f8f9fa): The default background for alternating light sections.
- **Light Gray Divider** (#e8eaed): Standard border and horizontal rules.

### Named Rules
**The Single Accent Rule.** Only one primary accent color (Primary Blue) is used for interfaces. Do not override this accent on solution or landing pages with sector-specific styling; keep the interface unified.

**The Contrast Safety Rule.** Never use white text on WhatsApp Green or light gray copy on white backgrounds. All text must pass a minimum contrast of 4.5:1.

## 3. Typography

**Display Font:** Montserrat (sans-serif)
**Body Font:** Inter (sans-serif)

The combination of the geometric, bold Montserrat for headings with the highly legible Inter for body copy ensures an authoritative, highly readable layout.

### Hierarchy
- **Display** (Bold 700, clamp(36px, 5.5vw, 60px), 1.1): Used exclusively for page-level hero headings.
- **Headline** (Bold 700, clamp(26px, 3.5vw, 40px), 1.2): For main sections.
- **Title** (Semi-bold 600, 20px, 1.3): For subtitles, component cards, and widget headers.
- **Body** (Regular 400, 15px, 1.6): For main readable prose. Cap line width at 75ch.
- **Label** (Semi-bold 600, 14px, 1.4): For button labels, tags, breadcrumbs, and eyebrow chips.

### Named Rules
**The Heading Balance Rule.** Display and headline components must use `text-wrap: balance` to prevent awkward word orphans on medium viewports.

**The Prose Line Limit Rule.** Multi-line body copy must never exceed a maximum line length of 75ch to prevent eye fatigue across technical documents.

## 4. Elevation

The elevation style is flat-by-default, emphasizing structured grid boundaries. Depth is conveyed structurally using border dividers and background block offsets.

### Shadow Vocabulary
- **Ambient Card Rest** (`0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04)`): The resting shadow for card containers, providing a very subtle, sharp lift off the page.
- **Ambient Card Hover** (`0 8px 24px rgba(0, 0, 0, 0.10), 0 2px 6px rgba(0, 0, 0, 0.06)`): Applied when an interactive card is hovered, matching the translateY(-4px) motion logic.

### Named Rules
**The Flat-At-Rest Rule.** All static surfaces remain flat. Shadow elevation is reserved exclusively for interactive elements responding to user hover or focus states.

## 5. Components

Every component is solid and confident, communicating structural durability.

### Buttons
- **Shape:** Gently curved edges (8px radius)
- **Primary:** Primary Blue background, white text, 52px height.
- **Hover / Focus:** Translate Y (-2px) with Deep Navy background transition.
- **Outline Dark:** Transparent background, 2px Primary Blue border, Primary Blue text. Transitions to solid Primary Blue background on hover.
- **WhatsApp:** WhatsApp Green background, Charcoal Ink text.

### Cards / Containers
- **Corner Style:** Rounded corners (12px radius).
- **Background:** Solid white or Off-White Cool.
- **Shadow Strategy:** Ambient Card Rest, transitioning to Ambient Card Hover on hover.
- **Border:** 1px Light Gray Divider.
- **Internal Padding:** Spacing card padding (32px).

### Navigation
- **Style:** Two-row fixed navigation. Row 1 (52px) for branding and logo, Row 2 (44px) for links. Row 1 slides up on scroll (`.scrolled` class) to compress height.

## 6. Do's and Don'ts

### Do:
- **Do** align body paragraphs and lists to a maximum readable width of 65–75ch.
- **Do** ensure all interactive card items use the `.card-clickable` class with transition and focus states.
- **Do** maintain a strict 52px height for all primary and outline buttons to preserve vertical alignment.

### Don't:
- **Don't** use border-left greater than 1px as a colored stripe on cards, callouts, or warnings (e.g., no side-stripe borders).
- **Don't** use text gradients under any circumstances. Keep headlines solid.
- **Don't** use decorative blurs or glassmorphism backgrounds.
- **Don't** use tiny tracked uppercase eyebrows above every section.
- **Don't** use numbered section markers (01, 02, 03) unless describing a sequential timeline or step-by-step process.
