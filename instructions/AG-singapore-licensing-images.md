# AG IMAGE BRIEF — singapore-licensing.html
## Version 1.0 — June 2026
## For: Anti-Gravity AI Image Generation

---

## CRITICAL RULES

- Generate ONE image at a time
- STOP after each image and show it to Wee Meng for approval
- Do NOT insert any image into the HTML until Wee Meng has approved it
- Do NOT proceed to the next image until the current one is approved
- If rejected, regenerate with the feedback given before moving on
- All images saved as .webp, stored at /images/insights/
- No Securevision staff in any of these images

---

## IMAGE 1 — FEATURE IMAGE

**File name:** `singapore-licensing-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/singapore-licensing-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean, professional photograph of an official-looking licence or certification document on a desk. The document has the visual character of a Singapore government-issued business licence — formal layout, official header, text in English, a reference number, and a stamp or seal visible. The document is the main subject, placed on a clean desk surface with perhaps a pen beside it. No specific real text or government logos visible — the document should look authentically official without reproducing any actual licence format. Soft even office lighting, neutral background. Professional editorial photography style. No people, no hands.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — EARLY ALARM SYSTEM / VINTAGE PANEL

**File name:** `singapore-licensing-vintage-panel.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/singapore-licensing-vintage-panel.webp`
**Insert location:** In `section1`, after the paragraph ending "...the trust of everyone who depends on the system.", using this exact HTML:

```html
<img src="/images/insights/singapore-licensing-vintage-panel.webp"
  alt="Older style alarm panel and keypad representing the simpler alarm systems common in Singapore before modern licensing standards"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of an older-style alarm panel and keypad mounted on a wall. The unit is visibly dated — larger, boxier housing, older-style LED or LCD display, simpler keypad layout typical of alarm systems from the 1990s or early 2000s. The panel looks functional but clearly represents an earlier generation of technology. Mounted on a plain interior wall, clean environment, natural indoor lighting. No people. Documentary photography style — the image should feel like a record of older technology rather than a product shot. Similar in character to vintage security equipment reference photos found in industry archives.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MODERN INTEGRATED SECURITY SYSTEM

**File name:** `singapore-licensing-modern-system.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/singapore-licensing-modern-system.webp`
**Insert location:** In `section5`, after the paragraph ending "...not just the alarm hardware itself.", using this exact HTML:

```html
<img src="/images/insights/singapore-licensing-modern-system.webp"
  alt="Modern integrated security system showing alarm panel, touchscreen keypad and network switch — representing the complexity of current installations"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a modern security system equipment rack or installation showing multiple components together — a compact alarm panel, a touchscreen keypad, a network switch or router, and perhaps a small UPS battery backup unit. The components are neatly installed in a communications cabinet or on a wall rack, with clean cable management. This represents the integrated, networked nature of current security installations — alarm, networking, and communications in one system. Professional installation photography style. No brand logos visible. Soft even lighting, clean background. No people.

**STOP. Show Wee Meng this image before proceeding.**

---

## AFTER ALL THREE IMAGES ARE APPROVED

1. Save all three files to `/images/insights/` at the specified sizes in `.webp` format
2. Image 1 (feature) — no insertion needed, just save the file
3. Insert Images 2 and 3 at the exact locations above using the exact HTML provided
4. Confirm each insertion before moving to the next
5. Do NOT modify any other part of the HTML file

---

## site-config.js UPDATE — do this after images are confirmed

Find the line:

```js
{ slug: "modern-detectors",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "singapore-licensing", title: "Why Security System Installers Must Be Licensed in Singapore", category: "Alarm & Intrusion", tags: ["burglar-alarm","singapore-licensing","psia","singapore"], excerpt: "Why do security system installers need a licence in Singapore? Learn how false alarms and evolving technology led to the professionalisation of the security industry and why licensing matters to property owners.", image: "singapore-licensing-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: singapore-licensing.html*
*Total images: 3 (1 feature + 2 body)*
