# AG IMAGE BRIEF — modern-detectors.html
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

**File name:** `modern-detectors-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/modern-detectors-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean flat-lay or slight overhead photograph showing two PIR motion detectors side by side on a neutral surface. On the left, an older-style PIR detector — larger, boxier, with a simpler Fresnel lens, visibly dated in design. On the right, a modern slim PIR detector — compact, sleek white housing, more sophisticated lens pattern, clearly a newer generation. Both units are white or light grey. Neutral light grey background, soft even studio lighting, slight overhead angle. The composition should clearly suggest "old vs new" — the evolution of detector design. No people, no hands. Editorial product photography style. No brand logos visible.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — DUAL-TECHNOLOGY DETECTOR

**File name:** `modern-detectors-dual-tech.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/modern-detectors-dual-tech.webp`
**Insert location:** In `section7`, after the paragraph ending "...Many commercial installations continue to use dual-technology detectors today for exactly this reason.", using this exact HTML:

```html
<img src="/images/insights/modern-detectors-dual-tech.webp"
  alt="Dual-technology PIR and microwave motion detector mounted on a wall in a commercial Singapore installation"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a dual-technology motion detector mounted on a wall. The unit is slightly larger than a standard PIR — a white or off-white rectangular housing with a dual-lens front face indicating the two sensing technologies. Mounted at ceiling height on a clean commercial or residential wall. Sharp focus on the detector, slightly blurred background. Professional installation photography style, similar in quality and composition to product shots from Bosch, Honeywell or DSC. Soft even lighting, no harsh shadows. No people, no hands.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MODERN INTELLIGENT DETECTOR CLOSE-UP

**File name:** `modern-detectors-intelligent.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/modern-detectors-intelligent.webp`
**Insert location:** In `section8`, after the paragraph ending "...That performance difference is what homeowners and business owners are actually paying for.", using this exact HTML:

```html
<img src="/images/insights/modern-detectors-intelligent.webp"
  alt="Modern intelligent PIR motion detector with advanced Fresnel lens pattern — current generation alarm sensor technology"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up product photograph of a modern, high-specification PIR motion detector. The unit is slim, clean white housing with a sophisticated multi-segment Fresnel lens pattern on the front face — the kind of complex lens array found on premium current-generation detectors. The detector is the sole subject of the image, photographed on a neutral light grey surface or mounted on a clean wall. Macro or near-macro composition showing the lens detail clearly. Soft studio lighting, clean background, no people, no hands. Premium product photography style. No brand logos visible.

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
{ slug: "false-alarm-causes",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "modern-detectors", title: "Why Modern Motion Detectors Are Better Than Ever", category: "Alarm & Intrusion", tags: ["burglar-alarm","motion-detectors","pir-sensors","singapore"], excerpt: "Motion detectors have evolved from simple ultrasonic sensors to intelligent devices capable of analysing movement patterns and reducing false alarms. Learn how modern detector technology improves security and why upgrading old sensors may be worthwhile.", image: "modern-detectors-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: modern-detectors.html*
*Total images: 3 (1 feature + 2 body)*
