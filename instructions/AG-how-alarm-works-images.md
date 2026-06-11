# AG IMAGE BRIEF — how-alarm-works.html
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

**File name:** `how-alarm-works-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/how-alarm-works-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean flat-lay or arranged photograph showing the five key components of a burglar alarm system together on a neutral surface: a PIR motion detector, an alarm panel module or circuit board, a numeric alarm keypad, an external siren/strobe unit, and a small cellular communication module or antenna. The components are arranged with clear spacing between them, slight overhead angle, soft even studio lighting. Each component is clearly identifiable. No people, no hands, no brand logos. Neutral light grey background. Editorial product photography style. The composition should suggest a complete system made up of distinct parts.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — ALARM PANEL CONCEALED INSTALLATION

**File name:** `how-alarm-works-panel.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/how-alarm-works-panel.webp`
**Insert location:** In `section3`, after the paragraph ending "...The cables and detectors may remain serviceable, but a new panel transforms what the system can do.", using this exact HTML:

```html
<img src="/images/insights/how-alarm-works-panel.webp"
  alt="Alarm panel installed in a concealed utility room location — the brain of the alarm system, hidden but central to everything"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of an alarm panel installed in a utility room, storeroom, or service riser location — a concealed but accessible position typical of professional Singapore alarm installations. The panel is mounted on a wall, clearly installed rather than placed. The surrounding environment suggests a service area — bare concrete or painted utility walls, conduit runs visible, a professional installation context. The panel itself is a current-generation unit, white or grey housing, clearly labelled. No people. Soft indoor utility lighting. Professional installation documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MODERN KEYPAD WITH TOUCHSCREEN

**File name:** `how-alarm-works-keypad.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/how-alarm-works-keypad.webp`
**Insert location:** In `section4`, after the paragraph ending "...If you feel rushed every time you enter the property and try to disarm, that can almost certainly be adjusted without any physical changes to the system.", using this exact HTML:

```html
<img src="/images/insights/how-alarm-works-keypad.webp"
  alt="Modern alarm system keypad with touchscreen display showing zone status and system controls — the user interface of a current-generation alarm system"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a modern alarm system keypad mounted on a wall in a Singapore interior. The keypad has a colour or graphic LCD touchscreen display showing zone status, armed/disarmed state, and system information. The design is clean and contemporary — white or light grey housing, flush or near-flush wall mount. Sharp focus on the keypad and display, slightly blurred Singapore interior background. No people, no hands. Soft natural interior lighting. Professional installation photography style. No brand logos.

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
{ slug: "alarm-power-cut",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "how-alarm-works", title: "How Does a Burglar Alarm System Work?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-system","security-basics","singapore"], excerpt: "How does a burglar alarm system work? Learn the five key components found in every alarm system, how they work together, and what homeowners should understand before upgrading or maintaining their security system.", image: "how-alarm-works-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: how-alarm-works.html*
*Total images: 3 (1 feature + 2 body)*
