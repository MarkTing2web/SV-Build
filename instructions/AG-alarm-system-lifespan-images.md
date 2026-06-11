# AG IMAGE BRIEF — alarm-system-lifespan.html
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

**File name:** `alarm-system-lifespan-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-system-lifespan-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean flat-lay photograph showing the key components of a burglar alarm system arranged on a neutral surface: a sealed lead-acid backup battery, a PIR motion detector, an alarm panel circuit board or module, and a length of alarm cable coiled neatly. The components are spread out with spacing between them, slight overhead angle. The composition suggests a collection of parts with different ages and lifespans. Soft even studio lighting, neutral light grey surface, no people, no hands. Editorial product photography style. No brand logos visible. The battery should look noticeably more dated or worn than the other components to suggest it ages fastest.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — BACKUP BATTERY REPLACEMENT

**File name:** `alarm-system-lifespan-battery.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-system-lifespan-battery.webp`
**Insert location:** In `section3`, after the paragraph ending "...The cost of discovering the battery was flat during the one power failure that coincided with a genuine intrusion attempt is considerably higher.", using this exact HTML:

```html
<img src="/images/insights/alarm-system-lifespan-battery.webp"
  alt="Sealed lead-acid backup battery inside an alarm panel — alarm batteries typically need replacement every three to four years"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a sealed lead-acid standby battery inside an alarm panel enclosure. The battery is a standard rectangular sealed unit — white or grey plastic casing, two terminal connectors visible, fitted inside the alarm panel housing. The panel lid is open or partially open to show the battery in situ. The battery should look aged — slightly discoloured casing, suggesting it has been in service for some years. No people, no hands. Soft even indoor lighting. Documentary photography style suggesting a maintenance scenario.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MAINTENANCE VISIT / SYSTEM CHECK

**File name:** `alarm-system-lifespan-maintenance.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-system-lifespan-maintenance.webp`
**Insert location:** In `section7`, after the paragraph ending "...A neglected system shortens its useful life and creates silent vulnerabilities that make it less reliable than its age alone would suggest.", using this exact HTML:

```html
<img src="/images/insights/alarm-system-lifespan-maintenance.webp"
  alt="Security technician performing an alarm system maintenance check — testing detector operation and inspecting panel components"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a security technician performing a routine alarm system maintenance check. The technician is inspecting a detector or testing a panel component — a hand is visible working at close range on the equipment. The setting is a Singapore interior — a residential or commercial property. The composition suggests professional, methodical maintenance work rather than an emergency repair. No face visible. Clean, organised working environment. Soft natural indoor lighting. Professional documentary photography style.

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
{ slug: "alarm-upgrade-or-replace",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-system-lifespan", title: "How Long Should a Burglar Alarm System Last?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-maintenance","alarm-lifespan","singapore"], excerpt: "How long should a burglar alarm system last? Learn the expected lifespan of alarm panels, detectors, batteries and wiring, and discover when upgrading makes more sense than replacing the entire system.", image: "alarm-system-lifespan-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-system-lifespan.html*
*Total images: 3 (1 feature + 2 body)*
