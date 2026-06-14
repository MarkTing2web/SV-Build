# How to Choose a Security Contractor — Image Generation & Insertion Brief
## File: /resources/guides/how-to-evaluate-security-contractor.html
## For: Anti-Gravity AI Web Builder

---

## MASTER RULES — READ BEFORE GENERATING ANY IMAGE

### Rule 1 — Generate one image at a time
Generate each image individually. After each image is saved and inserted, auto-continue to the next. Do not wait for confirmation between images.

### Rule 2 — Securevision staff appearance
Any image featuring Securevision staff must show:
- White polo shirt
- Securevision logo on the breast pocket — use the image at `/images/securevision-logo-blue.png` as the logo reference for the breast pocket
- The word SECUREVISION printed on the sleeve
- Asian male or female subject
- Professional, focused demeanour

### Rule 3 — Singapore setting
All photography prompts must produce images set in Singapore. Use Singapore-appropriate architecture and Asian subjects throughout.

### Rule 4 — No images inside callout boxes
Images must NEVER be placed inside `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div blocks. Images must always float beside full prose paragraphs in the main content flow. After inserting all images, perform a final sweep of the HTML file and confirm no `<img>` tag sits inside any callout, recommendation, or verdict div. If any is found, move it immediately above the containing div.

### Rule 5 — Do not touch anything else
After all images are generated and inserted, STOP. Do not modify any other part of the HTML file. Wait for Wee Meng to review before proceeding.

---

## IMAGE SPECS

- All body images: **960×540px, WebP, quality 85, centre-crop**
- Hero desktop: **1920×1080px, WebP, quality 85**
- Hero mobile: **1080×1920px, WebP, quality 85**

---

## IMAGE 01 — Hero Desktop

**Save to:** `/images/resources/guides/contractor/hero-evaluate-contractor.webp`
**Spec:** 1920×1080px WebP q85

**Prompt:**
Wide-angle cinematic photograph of a professional meeting between a security contractor and a Singapore property owner or facility manager. They are seated at a table reviewing documents and a laptop showing a security system proposal. Clean modern meeting room or office environment. Both subjects are Asian. Professional attire. Warm professional lighting. Photorealistic, high quality.

**Insert at:** Already referenced in the hero header background-image style attribute. Confirm the path matches:
```
style="background-image: url('/images/resources/guides/contractor/hero-evaluate-contractor.webp');"
```

---

## IMAGE 01b — Hero Mobile

**Save to:** `/images/resources/guides/contractor/hero-evaluate-contractor-mobile.webp`
**Spec:** 1080×1920px WebP q85

**Prompt:**
Portrait-format cinematic photograph of a professional meeting between a security contractor and a Singapore property owner reviewing documents. Clean modern office environment. Asian subjects, professional attire. Vertical composition, warm professional lighting, photorealistic.

**Insert at:** No HTML change needed — referenced via CSS media query for mobile hero background.

---

## IMAGE 02 — Founder Client Consultation

**Save to:** `/images/resources/guides/contractor/founder-client-consultation.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male security professional in a white polo shirt with the Securevision logo on the breast pocket (use /images/securevision-logo-blue.png as the logo reference) and SECUREVISION printed on the sleeve, sitting across a table from a Singapore property owner or MCST representative. They are reviewing printed documents together. Professional, warm and engaged expression. Office or meeting room environment. Daylight or warm interior lighting, photorealistic.

**Insert at:** "Why This Guide Exists" section. Locate the float figure block:
```html
<img alt="Ler Wee Meng Securevision founder reviewing security system documentation with a client at a Singapore property" loading="lazy" src="/images/resources/guides/contractor/founder-client-consultation.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 03 — Quotation Comparison

**Save to:** `/images/resources/guides/contractor/quotation-comparison.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of three printed security system quotation documents placed side by side on a clean office desk. The documents show different pricing, equipment lists, and scope details — the price figures visible on each document are clearly different. A pen and a pair of reading glasses are on the desk beside them. Clean, professional, well-lit. Overhead or slight angle shot. Photorealistic.

**Insert at:** Section 4, Why Three Quotations Can Differ. Locate the float figure block:
```html
<img alt="Three security system quotation documents side by side on a desk showing different pricing and scope" loading="lazy" src="/images/resources/guides/contractor/quotation-comparison.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 04 — MCST Security Review

**Save to:** `/images/resources/guides/contractor/mcst-security-review.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a small group of Asian professionals — three to four people — seated around a table in a Singapore condominium management office or meeting room, reviewing security system proposal documents and a laptop. The setting suggests an MCST council or management meeting. Professional but approachable atmosphere. Documents and laptop visible on the table. Warm meeting room lighting, photorealistic.

**Insert at:** Section 10, Who Should Be Involved in the Decision. Locate the float figure block:
```html
<img alt="MCST council meeting with managing agent reviewing security system proposal documents at Singapore condominium" loading="lazy" src="/images/resources/guides/contractor/mcst-security-review.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 05 — Handover Documentation

**Save to:** `/images/resources/guides/contractor/handover-documentation.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a security system handover documentation package on a clean desk. The package includes a folder, printed as-built drawings partially visible, a user manual, warranty card, and a printed equipment schedule. A USB drive is also visible beside the folder. Clean, professional, well-organised. Warm desk lighting, photorealistic.

**Insert at:** Section 12, Handover Requirements. Locate the float figure block:
```html
<img alt="Security system handover documentation folder with as-built drawings user manuals and warranty cards on a desk" loading="lazy" src="/images/resources/guides/contractor/handover-documentation.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 06 — Site Assessment Visit

**Save to:** `/images/resources/guides/contractor/site-assessment-visit.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male security technician in a white polo shirt with the Securevision logo on the breast pocket (use /images/securevision-logo-blue.png as the logo reference) and SECUREVISION printed on the sleeve, conducting a site assessment at a Singapore commercial or residential property. He is holding a clipboard and looking at the building entrance or a door location. Professional and focused. Daylight exterior or interior setting, photorealistic.

**Insert at:** Section 5, The Importance of a Proper Site Assessment. Insert the float figure block immediately after the opening paragraph of Section 5 and before the first subsection heading. Use this HTML:

```html
<figure class="rg-figure--float">
  <div class="rg-img-wrap rg-img-wrap--float">
    <img alt="Securevision technician conducting a site assessment at a Singapore property reviewing access points with clipboard" loading="lazy" src="/images/resources/guides/contractor/site-assessment-visit.webp"/>
  </div>
  <p class="rg-img-caption visually-hidden">A proper site assessment covers building layout, lighting, infrastructure, and future expansion plans before any recommendation is made.</p>
</figure>
```

Place this block immediately after the opening paragraph of Section 5 (`<p>A site assessment is often the difference...`) and before the first `<div class="subsection">`.

---

## COMPLETION INSTRUCTION

After all 6 images (including both hero variants — 7 files total) have been generated and inserted:

1. Perform the final sweep described in Master Rule 4 — confirm no `<img>` tag sits inside any `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div. Move any found images immediately above the containing div.

2. **STOP. Do not make any further changes to the HTML file.**

3. Wait for Wee Meng to review the page on staging before proceeding.
