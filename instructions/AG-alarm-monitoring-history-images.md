# AG IMAGE BRIEF — alarm-monitoring-history.html
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

**File name:** `alarm-monitoring-history-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-monitoring-history-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A wide atmospheric photograph of a vintage security monitoring centre from the 1990s or early 2000s. Multiple operator workstations visible, older CRT monitors displaying text-based alarm management software, operators seated but faces not visible — shot from behind or at an angle that avoids identifiable faces. The room has the visual character of a professional operations centre from that era — functional, purpose-built, slightly dated technology. Overhead fluorescent lighting, banks of equipment, a serious working environment. No modern flat screens, no smartphones. The image should feel like a genuine documentary photograph from that period. Editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — TELEPHONE DIALLER / VINTAGE ALARM COMMUNICATOR

**File name:** `alarm-monitoring-history-dialler.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-monitoring-history-dialler.webp`
**Insert location:** In `section2`, after the paragraph ending "...The alarm industry simply made use of infrastructure that was already everywhere.", using this exact HTML:

```html
<img src="/images/insights/alarm-monitoring-history-dialler.webp"
  alt="Vintage alarm panel with built-in telephone dialler communicator — the technology that connected alarm systems to monitoring centres before the internet"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a vintage alarm panel or communicator module from the 1990s showing a built-in telephone dialler or communicator component. The unit has the visual character of security equipment from that era — functional plastic housing, terminal blocks, older-style circuit board visible if the cover is open, or a compact wall-mounted unit with telephone line connection ports visible. Aged but clean condition. Mounted on a wall or photographed on a neutral surface. Documentary photography style suggesting historical security technology. No people. Neutral lighting.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — TELEPHONE LINE / PSTN CONNECTION

**File name:** `alarm-monitoring-history-pstn.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-monitoring-history-pstn.webp`
**Insert location:** In `section5`, after the paragraph ending "...Even a cut line no longer meant a silent alarm.", using this exact HTML:

```html
<img src="/images/insights/alarm-monitoring-history-pstn.webp"
  alt="Telephone line junction box and cable — the PSTN infrastructure that underpinned alarm monitoring before IP communications"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a telephone line junction box, BT-style telephone socket, or PSTN cable connection point — the kind of analogue telephone infrastructure common in buildings from the 1990s. The image suggests the physical telephone line that alarm systems once depended on for communication. Clean, functional, slightly dated in character. Mounted on a wall or in a utility space. No people. Natural or soft indoor lighting. Documentary photography style — the image should feel like a record of older infrastructure rather than a product shot.

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
{ slug: "singapore-licensing",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-monitoring-history", title: "How Alarm Monitoring Worked Before the Internet", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","security-history","singapore"], excerpt: "How did burglar alarm monitoring work before the internet? Discover how alarm panels used telephone lines, diallers and Central Monitoring Stations to protect homes and businesses long before mobile apps existed.", image: "alarm-monitoring-history-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-monitoring-history.html*
*Total images: 3 (1 feature + 2 body)*
