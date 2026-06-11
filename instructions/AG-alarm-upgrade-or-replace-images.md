# AG IMAGE BRIEF — alarm-upgrade-or-replace.html
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

**File name:** `alarm-upgrade-or-replace-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-upgrade-or-replace-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A close-up photograph of an older alarm keypad showing visible signs of age — yellowed or discoloured plastic housing, worn key surfaces, an older-style LED or LCD display. The keypad is mounted on a wall in a Singapore interior setting. The image should convey the sense of a system that has reached the end of its era — functional but clearly dated. Sharp focus on the keypad, slightly blurred background showing a typical Singapore residential or commercial wall. No people. Natural indoor lighting. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — SYSTEM ASSESSMENT / INSPECTION

**File name:** `alarm-upgrade-or-replace-assessment.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-upgrade-or-replace-assessment.webp`
**Insert location:** In `section6`, after the paragraph ending "...A recommendation that retains everything to minimise cost without acknowledging genuine component age or communication obsolescence is similarly incomplete.", using this exact HTML:

```html
<img src="/images/insights/alarm-upgrade-or-replace-assessment.webp"
  alt="Security technician inspecting alarm panel components during an upgrade assessment — testing before recommending"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of an open alarm panel with internal components visible — circuit board, terminals, wiring connections. A hand is visible using a probe or indicator to check a specific component. The image suggests a professional technical assessment — someone looking carefully at what is there before making a recommendation. The panel interior should be clearly visible and the composition should feel like purposeful inspection rather than casual observation. No faces visible. Soft even indoor lighting. Professional technical photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — TARGETED UPGRADE / NEW PANEL WITH OLD CABLES

**File name:** `alarm-upgrade-or-replace-targeted.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-upgrade-or-replace-targeted.webp`
**Insert location:** In `section3`, after the paragraph ending "...The homeowner ends up with a system that performs like a current installation.", using this exact HTML:

```html
<img src="/images/insights/alarm-upgrade-or-replace-targeted.webp"
  alt="New modern alarm panel installed with existing detection cables connected — representing a targeted upgrade that retains sound infrastructure"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a new, modern alarm panel mounted on a wall with existing detection cables visible connecting into the panel's zone terminals. The panel itself is current-generation — compact, clean white housing, modern interface. The cables feeding into it are older-style multi-core alarm cables, suggesting they have been retained from a previous installation. The contrast between the new panel and the existing cables tells the targeted upgrade story. No people. Professional installation photography style. Clean interior wall background. Neutral lighting. No brand logos.

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
{ slug: "alarm-wiring-reuse",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-upgrade-or-replace", title: "Should I Upgrade or Replace My Alarm System?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-upgrade","alarm-replacement","singapore"], excerpt: "Should you upgrade or replace your burglar alarm system? Learn how to assess ageing alarm panels, detectors, communications and wiring so you can make the most cost-effective decision for your home or business.", image: "alarm-upgrade-or-replace-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-upgrade-or-replace.html*
*Total images: 3 (1 feature + 2 body)*
