# AG IMAGE BRIEF — false-alarm-causes.html
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

**File name:** `false-alarm-causes-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/false-alarm-causes-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A close-up photograph of a PIR motion detector mounted in the upper corner of a Singapore interior room. The detector is a standard white wedge-shaped unit with a visible Fresnel lens. In the background, slightly out of focus, a large west-facing window with afternoon sun streaming through curtains is visible — suggesting the environmental false alarm trigger the article discusses. Clean, modern Singapore residential interior. Natural afternoon lighting. No people. Professional installation photography style. The composition should show both the detector in sharp focus and the window in soft background focus — the two elements of the false alarm scenario together in one image.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — OPEN WINDOW WITH MOVING CURTAINS

**File name:** `false-alarm-causes-curtains.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/false-alarm-causes-curtains.webp`
**Insert location:** In `section6`, after the paragraph ending "...The system is not wrong. The environment needs to be managed.", using this exact HTML:

```html
<img src="/images/insights/false-alarm-causes-curtains.webp"
  alt="Open window with curtains moving in a breeze — a common cause of PIR false alarm activations in Singapore homes"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of an open window in a Singapore residential interior with light curtains or sheer drapes billowing inward from a breeze. The window is open, natural daylight coming through, curtains caught mid-movement suggesting active airflow. Clean, modern Singapore home interior — painted walls, simple window frame. The movement of the curtains is the visual focus. No people. Soft natural lighting. Documentary photography style — the image should feel like a moment captured rather than a staged product shot.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — RENOVATION / ROOM CHANGE OF USE

**File name:** `false-alarm-causes-renovation.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/false-alarm-causes-renovation.webp`
**Insert location:** In `section4`, after the paragraph ending "...the alarm system should be reviewed to match the new layout and use.", using this exact HTML:

```html
<img src="/images/insights/false-alarm-causes-renovation.webp"
  alt="Singapore interior mid-renovation with walls being reconfigured — alarm systems need to be reviewed when room layouts change"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a Singapore residential or commercial interior mid-renovation — bare concrete or plasterboard walls, construction materials present, a room in the process of being reconfigured. The space is clearly changing use or layout. Daytime, natural light through windows or openings. No workers, no people. The image should suggest a property in transition — the kind of environment where an existing alarm system may no longer be correctly configured for the new layout. Documentary photography style, neutral tones.

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
{ slug: "alarm-siren",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "false-alarm-causes", title: "The Most Common Causes of False Alarms", category: "Alarm & Intrusion", tags: ["burglar-alarm","false-alarms","alarm-detectors","singapore"], excerpt: "Why do burglar alarms go off when nobody is breaking in? Learn the most common causes of false alarms — from user mistakes and sunlight to pets, air-conditioning and poor detector placement.", image: "false-alarm-causes-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: false-alarm-causes.html*
*Total images: 3 (1 feature + 2 body)*
