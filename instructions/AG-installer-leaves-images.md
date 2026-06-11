# AG IMAGE BRIEF — installer-leaves.html
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

**File name:** `installer-leaves-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/installer-leaves-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A photograph of a security installer conducting a handover with a homeowner at an alarm keypad mounted on a wall. The installer is Asian male, professional attire, pointing at or demonstrating the keypad to a homeowner who is watching attentively. The keypad is a modern touchscreen or graphic display unit mounted in a clean Singapore residential interior. The composition represents the handover moment — the transfer of knowledge from installer to owner. Natural indoor lighting. Professional documentary photography style. No Securevision branding or uniform on either person.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — ALARM KEYPAD WITH FAULT INDICATOR

**File name:** `installer-leaves-keypad-fault.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/installer-leaves-keypad-fault.webp`
**Insert location:** In `section4`, after the paragraph ending "...The entire visit takes twenty minutes. The same issue left for another six months means a flat battery during the next power outage — which may coincide with an event that matters.", using this exact HTML:

```html
<img src="/images/insights/installer-leaves-keypad-fault.webp"
  alt="Alarm keypad displaying a fault or trouble condition — the beeping keypad is the most common support call for alarm system owners"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a modern alarm system keypad displaying a fault or trouble condition on its screen. The display shows text indicating a system condition — something like "TROUBLE" or "LOW BATTERY" or a similar fault indicator, with the display lit and the message clearly visible. The keypad is mounted on a wall in a Singapore residential interior. The image should convey the "beeping keypad" scenario — the system is communicating a condition, not malfunctioning. Sharp focus on the display. Soft natural indoor lighting. No people, no hands. Professional editorial photography style. No brand logos.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — ALARM SYSTEM DOCUMENTATION / FOLDER

**File name:** `installer-leaves-documentation.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/installer-leaves-documentation.webp`
**Insert location:** In `section6`, after the paragraph ending "...A homeowner with a folder of system documentation is in a fundamentally better position than one who can only point at the keypad on the wall.", using this exact HTML:

```html
<img src="/images/insights/installer-leaves-documentation.webp"
  alt="Security system documentation folder with user manuals, zone descriptions and warranty information — the paperwork that makes future support possible"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean photograph of a folder or document wallet containing security system documentation — user manuals, a printed zone description sheet, warranty cards, and an emergency contact sheet. The documents are neatly organised and clearly readable as a collection of security system paperwork. The folder is sitting on a desk or shelf in a home environment. The image represents the importance of keeping documentation organised and accessible. No people, no hands. Soft natural home lighting. Editorial photography style. No specific brand names visible on the documents.

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
{ slug: "break-in-nearby-security-review",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "installer-leaves", title: "The Real Test Begins After the Installer Leaves", category: "Security Planning", tags: ["security-maintenance","security-support","security-planning","singapore"], excerpt: "What happens after your security system is installed? Learn why training, maintenance, documentation and long-term support are just as important as the installation itself.", image: "installer-leaves-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: installer-leaves.html*
*Total images: 3 (1 feature + 2 body)*
