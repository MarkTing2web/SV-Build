# AG IMAGE BRIEF — alarm-siren.html
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

**File name:** `alarm-siren-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-siren-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A close-up wide-angle photograph of an external burglar alarm siren and strobe unit mounted on the exterior wall of a Singapore residential or commercial property. The unit is a standard white or light grey rectangular enclosure with a visible strobe lens on the front face. Mounted visibly at height on a rendered exterior wall, clearly intended to be seen. Daytime, natural Singapore outdoor lighting. Sharp focus on the siren unit, slightly blurred background showing a typical Singapore building facade. No people. Professional installation photography style. Clean, authoritative composition — the siren should look purposeful and well-installed, not hidden or amateur.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — MOBILE APP NOTIFICATION

**File name:** `alarm-siren-mobile-notification.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-siren-mobile-notification.webp`
**Insert location:** In `section4`, after the paragraph ending "...The response process does not stop simply because the siren has stopped.", using this exact HTML:

```html
<img src="/images/insights/alarm-siren-mobile-notification.webp"
  alt="Smartphone screen showing a burglar alarm notification from a security app — modern alarm systems alert homeowners directly via mobile"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a smartphone screen displaying a push notification from a security or alarm app. The notification reads something like "Alarm Activated — Front Door — Zone 1" with a timestamp. The app interface is clean and modern. The phone is placed on a flat surface or bedside table suggesting a home environment — implying a nighttime alarm notification. Soft ambient lighting. No brand names or logos visible on the app screen. No people, no hands holding the phone. Editorial product photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — STROBE LIGHT ON EXTERIOR WALL

**File name:** `alarm-siren-strobe.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-siren-strobe.webp`
**Insert location:** In `section6`, after the paragraph ending "...The objective is to make them easy to see as well as easy to hear.", using this exact HTML:

```html
<img src="/images/insights/alarm-siren-strobe.webp"
  alt="Alarm strobe light flashing on the exterior of a Singapore property at night — the visual beacon that identifies which property has activated"
  class="article-img-float-right" />
```

**Generation prompt:**
A nighttime or low-light photograph of an external alarm unit with a strobe light actively flashing — blue-white flash illuminating the surrounding wall and facade. The siren housing is visible but the strobe flash is the dominant visual element, casting light on the building exterior. Singapore residential or commercial building background, slightly blurred. The composition emphasises the visibility of the strobe — it should look like an unmistakable visual signal. No people. Atmospheric, slightly dramatic lighting from the strobe flash itself. Documentary photography style.

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
{ slug: "false-alarms",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-siren", title: "Why Burglar Alarm Sirens Don't Ring Forever", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-siren","alarm-design","singapore"], excerpt: "Why do burglar alarm sirens stop after a few minutes? Learn how modern alarm systems use sirens, strobe lights, mobile apps and monitoring centres to protect your property without creating unnecessary disturbance.", image: "alarm-siren-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-siren.html*
*Total images: 3 (1 feature + 2 body)*
