# Securevision Insights: Article Build Standards
**Version 1.6 — April 2026** (Personnel & Brand Refinement)

---

## 1. Imagery & Personnel Standards
- **Demographic**: ALL humans portrayed in company-generated imagery MUST be Asian to reflect the Singaporean demographic.
- **Context**: The background and setting MUST be recognisably Singaporean (modern architecture, specific guardhouse styles, local flora).
- **Uniforms**: Any Securevision technician or staff member MUST be pictured wearing either a **white** or **black** polo-T shirt.
- **Branding**: The word "Securevision" MUST be clearly visible (embossed/printed) on either the back, the sleeve, or the breast pocket of the staff uniform.

---

## 2. Mandatory Local Standards (UNCHANGEABLE)
1. **Breadcrumbs**: (MANDATORY) Below the nav bar.
2. **Hero Byline**: Exactly 2 lines (Name vs. Role/Metadata).
3. **Sidebar (Sticky)**:
   - **TOC**: With active scroll-spy.
   - **Founder Card**: Mandatory card with 40px circle photo, name/title, and "Need expert advice?" text leading to a WhatsApp CTA. This must be present in EVERY article.
4. **Author Bio (BOTTOM)**: 
   - The **FULL, long-form bio** (150-200 words) describing Wee Meng's 35-year engineering experience, NUS/UoL degrees, and the building of over 1,000 sites in Singapore. 
   - DO NOT shorten or paraphrase this section.
5. **Tags**: Mandatory tag pills directly after the Full Bio.
6. **Related Insights**: Centered 3-card grid using `.nav-card`.
7. **Final CTA**: Full-width section with article-specific imagery (following Personnel Standards above).

---
- **Hero Section**: Cinematic, context-relevant security image with a dark gradient overlay.
- **Layout**: `layout-with-sidebar` grid (1fr 280px).
- **Footer**: Standard `site-footer` from `sv-shared.css`.

---

## 2. Image Standards
Images must be professional, high-fidelity, and reflect the Singapore security landscape.

| Type | Dimensions | Naming Convention | Use Case |
| :--- | :--- | :--- | :--- |
| **Cover/Hero** | 1200 × 480 px | `insight-[slug]-cover.jpg` | Main hero background. |
| **In-Article** | 800 × 500 px | `insight-[slug]-[desc].jpg` | Technical context/diagrams. |
| **CTA Background** | 1600 × 600 px | `insight-[slug]-cta.jpg` | Final conversion section. |

**Standard Prompting Style**: "Professional photography, sharp architectural lines, cinematic lighting, modern security hardware, Singapore properties."

---

## 3. Sidebar Requirements (Sticky)
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

## 4. Prose & Visual Components
- **Callout Boxes**: `class="callout-box"`. Blue theme for "Key Points" or "Design Rules".
- **Verdict Boxes**: `class="verdict-box"`. Orange theme for "Securevision Verdict".
- **Section Headings**: Numbered (1. Title, 2. Title). Anchor IDs: `section1`, `section2`.

---

## 5. Article Footer & Navigation
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
   - Background image MUST correspond to the article's theme (e.g., an audit image for a tips article).

---

## Tracking Table: Insights Article Pipeline

| Article Slug | Status | Build Date | Visuals Loaded |
| :--- | :--- | :--- | :--- |
| `insights-how-to-choose-cctv` | LIVE | March 2025 | 100% |
| `insights-burglar-alarm-design` | LIVE | March 2025 | 100% |
| `insights-10-tips-securing-your-premises` | LIVE | April 2025 | 100% |


---

## 10. Technical Imagery Library (Article-Specific)

### Multi-Door Access Control Guide
- **Hero**: `images/multi-door-access-cover.jpg` (1200x480). Modern Singapore commercial lobby, glass doors, card readers. Sharp, architectural.
- **In-Article**: `images/multi-door-access-controller.jpg` (800x500). Clustered controller panel, professional wiring, clean riser install.
- **Shared Background**: `images/cta-skyline.png` (1200x480). Stunning Singapore CBD skyline at dusk. (MANDATORY shared CTA background).

### Auto Gate Motor Selection Guide
- **Hero**: `images/auto-gate-motor-cover.jpg` (1200x480). Motorised auto gate at a Singapore landed home at dusk. Gate closing or closed. Motor arm or track visible. Clean residential setting. No people.
- **In-Article 1**: `images/auto-gate-concealed-motor.jpg` (800x500). Concealed recessed swing gate motor housing set into the ground near the gate hinge. Singapore residential setting.
- **In-Article 2**: `images/auto-gate-swing-arm-motor.jpg` (800x500). FAAC swing arm motor mounted on a gate pillar, arm extended to the gate leaf. Clean installation.

### WiFi Remote Gate Control Guide
- **Hero**: `images/wifi-auto-gate-cover.jpg` (1200x480). Smartphone screen showing a gate control app (Tuya style) with open/close button visible. Gate or driveway blurred in background.
- **In-Article**: `images/wifi-gate-yet402-receiver.jpg` (800x500). YET402 WiFi 2-channel receiver module, small white unit, shown in hand or mounted inside a gate motor control panel.

---
*Securevision Pte Ltd · Police Licence L/PS/000267/2023P*
