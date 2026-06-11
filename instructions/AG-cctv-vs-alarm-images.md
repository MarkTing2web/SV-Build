# AG IMAGE BRIEF — cctv-vs-alarm.html
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

**File name:** `cctv-vs-alarm-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/cctv-vs-alarm-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean close-up photograph of a CCTV camera and a PIR motion detector installed on the same wall or ceiling, positioned close together. The CCTV camera is a compact dome or bullet-style IP camera. The PIR detector is a standard white wedge-shaped unit. Both are clearly visible and in sharp focus, mounted in a Singapore interior or exterior setting. The composition represents the combination approach — two different technologies working together. No people. Professional installation photography style. Soft even lighting. No brand logos visible.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — CCTV FOOTAGE REVIEW / EVIDENCE

**File name:** `cctv-vs-alarm-footage.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/cctv-vs-alarm-footage.webp`
**Insert location:** In `section2`, after the paragraph ending "...That is the difference — and depending on the situation, that difference is the entire outcome.", using this exact HTML:

```html
<img src="/images/insights/cctv-vs-alarm-footage.webp"
  alt="Computer screen showing CCTV footage review with timeline and camera grid — CCTV provides evidence and context after an alarm event"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a computer monitor or NVR screen showing a CCTV footage review interface. The screen displays a grid of camera feeds or a single camera playback with a timeline scrubber visible at the bottom, suggesting footage review after an event. The interface is clean and modern. No real faces or identifiable locations visible in the camera feeds — show generic outdoor or entrance areas. Screen is the main subject, slightly angled, soft ambient workstation lighting. No people, no hands. Professional editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — LAYERED SECURITY / COMBINED SYSTEM

**File name:** `cctv-vs-alarm-integration.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/cctv-vs-alarm-integration.webp`
**Insert location:** In `section6`, after the paragraph ending "...Integration does not make the alarm redundant in favour of CCTV, or CCTV redundant in favour of the alarm. It makes both more effective by allowing each to do what it is best at while filling the other's gaps.", using this exact HTML:

```html
<img src="/images/insights/cctv-vs-alarm-integration.webp"
  alt="Alarm management software screen showing simultaneous alarm event and associated camera feed — the integrated alarm and CCTV verification workflow"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a monitoring centre or home security management screen showing an integrated interface with both an alarm event notification and an associated camera feed displayed simultaneously. The alarm event panel on one side shows a zone activation with timestamp. The camera panel on the other side shows a live or recorded view of the relevant area. The composition represents the integrated workflow where alarm detection and visual verification happen together. Clean modern UI. No real faces or identifiable locations. No brand names. Screen slightly angled, soft ambient lighting. No people, no hands. Professional editorial photography style.

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
{ slug: "alarm-system-lifespan",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "cctv-vs-alarm", title: "Do I Still Need a Burglar Alarm If I Have CCTV?", category: "Alarm & Intrusion", tags: ["burglar-alarm","cctv","layered-security","singapore"], excerpt: "Do you still need a burglar alarm if you already have CCTV? Learn the key differences between intrusion detection and video verification, and discover why modern security systems use both technologies together.", image: "cctv-vs-alarm-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: cctv-vs-alarm.html*
*Total images: 3 (1 feature + 2 body)*
