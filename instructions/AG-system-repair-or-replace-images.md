# AG IMAGE BRIEF — system-repair-or-replace.html
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

**File name:** `system-repair-or-replace-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/system-repair-or-replace-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean flat-lay or arranged photograph showing a mix of older and newer security system components side by side on a neutral surface. On one side, an older-style camera or access control reader — visibly dated, larger housing, aged plastic. On the other side, a modern equivalent — compact, clean design, clearly current generation. Between them, a length of cable suggesting the infrastructure that might be shared between old and new. The composition should suggest the repair-versus-upgrade decision — what to keep and what to replace. Neutral grey background, soft even studio lighting. No people, no hands, no brand logos. Editorial product photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — SELECTIVE UPGRADE / OLD CABLING WITH NEW CAMERA

**File name:** `system-repair-or-replace-selective.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/system-repair-or-replace-selective.webp`
**Insert location:** In `section6`, after the paragraph ending "...For an intercom system, existing cabling between apartments or floors can often carry modern IP intercom signals, making the upgrade primarily about the handsets and main unit rather than the wiring behind the walls.", using this exact HTML:

```html
<img src="/images/insights/system-repair-or-replace-selective.webp"
  alt="New IP camera being mounted at an existing camera position using existing cable infrastructure — the selective upgrade approach that retains sound cabling while replacing outdated devices"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a new, modern IP security camera being installed at an existing camera mounting position on a wall. The existing cable — an older coaxial or CAT cable — is visible emerging from the wall at the mounting point, and the new camera is being connected to it. The composition shows the transition: new hardware, existing infrastructure. The mounting position and cable are clearly existing; the camera is clearly new and modern. Singapore exterior or interior wall setting. No people — just the hardware. Natural indoor or outdoor lighting. Professional installation photography style. No brand logos.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MODERN VS OLDER CAMERA COMPARISON

**File name:** `system-repair-or-replace-comparison.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/system-repair-or-replace-comparison.webp`
**Insert location:** In `section7`, after the paragraph ending "...A property owner who last reviewed their security system in 2015 and assumed it was 'still working fine' may be significantly more exposed than they realise — not because the system has failed, but because the world it was designed for has changed substantially.", using this exact HTML:

```html
<img src="/images/insights/system-repair-or-replace-comparison.webp"
  alt="Side-by-side comparison of a ten-year-old lower-resolution camera image and a modern high-resolution camera image of the same scene — illustrating the technology gap"
  class="article-img-float-right" />
```

**Generation prompt:**
A split-image photograph showing a clear visual comparison between what an older lower-resolution security camera captures versus what a modern high-resolution camera captures of the same scene. The left half shows a blurry, pixelated, low-resolution image of a property entrance or gate area. The right half shows a crisp, high-resolution image of the same scene with clearly identifiable detail. The contrast should be obvious and striking — this illustrates the technology gap described in the article. Generic Singapore residential or commercial entrance as the subject. No identifiable faces. Clean layout with a clear dividing line between the two halves. Graphic or photographic composite style.

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
{ slug: "alarm-usage-habits",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "system-repair-or-replace", title: "My System Is 10 Years Old. Should I Repair It or Replace It?", category: "Security Planning", tags: ["security-upgrade","cctv","security-planning","singapore"], excerpt: "My security system is ten years old. Should I repair it or replace it? Learn the framework Securevision uses to help property owners decide when a repair makes sense, when an upgrade is better, and how selective upgrades can maximise value.", image: "system-repair-or-replace-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: system-repair-or-replace.html*
*Total images: 3 (1 feature + 2 body)*
