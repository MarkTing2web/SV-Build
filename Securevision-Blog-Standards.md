# Securevision Insights: Article Build Standards
**Version 1.7 — April 2026** (Personnel & Global Style Refinement)

---

## 1. Imagery & Personnel Standards
- **Demographic**: ALL humans portrayed in company-generated imagery MUST be Asian to reflect the Singaporean demographic.
- **Context**: The background and setting MUST be recognisably Singaporean (modern architecture, specific guardhouse styles, local flora).
- **Uniforms**: Any Securevision technician or staff member MUST be pictured wearing either a **white** or **black** polo-T shirt.
- **Branding**: The word "Securevision" MUST be clearly visible (embossed/printed) on either the back, the sleeve, or the breast pocket of the staff uniform.

---

## 2. Global Style Components (sv-shared.css)
The following components are standardized in the global stylesheet. Do not use local `<style>` overrides for these:

1.  **Layout**: Use `<div class="layout-with-sidebar">` for the main content grid (1fr 280px).
2.  **Hero Byline**: Exactly 2 lines inside `.hero-byline-text` (`<strong>` name and `<span>` role/metadata).
3.  **Breadcrumbs**: Mandatory `.sv-breadcrumb` below the nav bar.
4.  **Sticky Sidebar**: Includes `.sticky-toc` (with scroll-spy) and the `.founder-card`.
5.  **Author Bio (Bottom)**: Use `.author-bio-footer` for the full 150–200 word biography.
6.  **Tags**: Positioned directly after the Author Bio using `.article-tags` and `.tag-pill`.
7.  **Callout Boxes**: Use `.callout-box` for "Key Points" or "Planning Points".
8.  **Verdict Boxes**: Use `.verdict-box` for the "Securevision Verdict" or "Securevision View".
9.  **Image Scaling**: Wrap images in `.article-image-box` with an optional `.image-caption`.
10. **Related Insights**: Centered 3-card grid using `.related-grid` and `.nav-card`.

---

## 3. Formatting & Structure (Prose)
- **Eyebrows**: Every major section should begin with an eyebrow span: `<span class="eyebrow">Category</span>`.
- **Section Headings**: Use `<h2>` for main sections and `<h3>` for subsections.
- **Anchor Navigation**: 
    - Wrap sections in `<section id="section1">`.
    - TOC links must match: `<a href="#section1">`.
- **Spacing**: Maintain 80px vertical padding on the `.article-body`.

---

## 4. Image Dimensions & Naming

| Type | Dimensions | Naming Convention | Use Case |
| :--- | :--- | :--- | :--- |
| **Cover/Hero** | 1200 × 480 px | `insight-[slug]-cover.jpg` | Main hero background. |
| **In-Article** | 800 × 500 px | `insight-[slug]-[desc].jpg` | Technical context/diagrams. |
| **CTA Background** | 1600 × 600 px | `insight-[slug]-cta.jpg` | Final conversion section. |

**Standard Prompting Style**: "Professional photography, sharp architectural lines, cinematic lighting, modern security hardware, Singapore properties."

---

## 5. Sidebar Requirements (Sticky)
The sidebar must remain sticky on desktop and include:
1. **Sticky TOC**: Table of contents with active scroll-spy highlighting.
2. **Author Row Card**: 
   - 40px rounded photo (`images/ler-wee-meng-bio.jpeg`).
   - Name: "Ler Wee Meng".
   - Title: "Founder & CEO · Securevision".
3. **Expert Advice Section**:
   - Copy: "Need expert advice? Discuss your site requirements with our engineering team."
   - Link: WhatsApp Support (`wa.me/6593860466`) with emoji.

---

## 6. Article Footer & Navigation
1. **Author Bio (Full)**: Positioned at the very end of the article prose.
   - 120px photo, full details of NUS BEng, UoL LLB, and 35+ years experience.
   - Must mention VESTA platform and 1,000+ site track record.
2. **Tags (MANDATORY)**: Positioned directly after the Author Bio.
   - Pill format using `.tag-pill`.
3. **Article Navigation**: `class="prev-next-nav"` using `.nav-card` (grid layout).
4. **Related Insights**: A full-width section with a centered heading.
   - Heading: `Related Security Insights` (Centered, `h2` or `h3`).
   - Cards: 3 cards showing other relevant articles.
   - Layout: 3-column grid using `.nav-card`.
5. **Final CTA**: High-impact section positioned **directly above the footer**.
   - Background image MUST correspond to the article's theme.

---

## 7. Tracking Table: Insights Article Pipeline

| Article Slug | Status | Build Date | Visuals Loaded |
| :--- | :--- | :--- | :--- |
| `insights-how-to-choose-cctv` | LIVE | March 2025 | 100% |
| `insights-burglar-alarm-design` | LIVE | March 2025 | 100% |
| `insights-10-tips-securing-your-premises` | LIVE | April 2025 | 100% |
| `insights-ai-analytics-hikvision` | LIVE | April 2026 | 100% |

---

## 8. Technical Imagery Library (Article-Specific)

### Multi-Door Access Control Guide
- **Hero**: `images/multi-door-access-cover.jpg` (1200x480). Modern Singapore commercial lobby, glass doors, card readers. Sharp, architectural.
- **In-Article**: `images/multi-door-access-controller.jpg` (800x500). Clustered controller panel, professional wiring, clean riser install.
- **Shared Background**: `images/cta-skyline.png` (1200x480). Stunning Singapore CBD skyline at dusk. (MANDATORY shared CTA background).

### Auto Gate Motor Selection Guide
- **Hero**: `images/auto-gate-motor-cover.jpg` (1200x480). Motorised auto gate at a Singapore landed home at dusk. Gate closing or closed. Motor arm or track visible. Clean residential setting. No people.
- **In-Article 1**: `images/auto-gate-concealed-motor.jpg` (800x500). Concealed recessed swing gate motor housing set into the ground near the gate hinge. Singapore residential setting.
- **In-Article 2**: `images/auto-gate-swing-arm-motor.jpg` (800x500). FAAC swing arm motor mounted on a gate pillar, arm extended to the gate leaf. Clean installation.

---
*Securevision Pte Ltd · Police Licence L/PS/000267/2023P*
