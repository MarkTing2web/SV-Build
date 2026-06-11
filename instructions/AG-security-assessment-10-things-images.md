# AG IMAGE BRIEF — security-assessment-10-things.html
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

**File name:** `security-assessment-10-things-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/security-assessment-10-things-feature.webp`
**Insert location:** Already in the HTML at `section0`. No insertion needed — just save the file.

**Generation prompt:**
A photograph of a security professional conducting a site assessment walk-around at a Singapore landed property. The professional is Asian male, middle-aged, wearing smart casual clothing, walking along the perimeter of a Singapore terrace house or semi-detached property, looking carefully at the fence line, gate, or side passage. He is not in uniform — this is a professional assessment, not a uniformed guard. He has a clipboard or tablet. The property is a typical Singapore residential landed property — rendered walls, iron gate, mature planting. Daytime, natural Singapore outdoor lighting. Documentary photography style, slightly candid — as if photographed during the assessment itself. No Securevision branding or uniform.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — DARK SIDE PASSAGE / BLIND SPOT

**File name:** `security-assessment-10-things-blind-spot.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/security-assessment-10-things-blind-spot.webp`
**Insert location:** In `section3`, after the paragraph ending "...The important thing is identifying the blind spots deliberately rather than discovering them after an incident.", using this exact HTML:

```html
<img src="/images/insights/security-assessment-10-things-blind-spot.webp"
  alt="Dark unlit side passage between Singapore terrace houses — a typical blind spot that creates opportunity for unobserved approach"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a narrow side passage between two Singapore terrace houses — the typical 1-2 metre gap between adjoining properties. The passage is shadowed and poorly lit, with one side wall rendered and painted, the other showing a fence or wall. Some vegetation at the far end. The image should convey the sense of a concealed, unmonitored space — the kind of blind spot described in the article. Daytime but shadowed. No people. Documentary photography style — this should look like a genuine property condition, not a staged image.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — SLIDING DOOR SECURITY BAR

**File name:** `security-assessment-10-things-sliding-door.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/security-assessment-10-things-sliding-door.webp`
**Insert location:** In `section8`, after the paragraph ending "...A steel security bar dropped into the track, combined with an anti-lift device on the door itself, costs very little and changes the effort required to force entry substantially.", using this exact HTML:

```html
<img src="/images/insights/security-assessment-10-things-sliding-door.webp"
  alt="Security bar installed in a sliding door track at a Singapore residential property — a simple and effective additional security measure"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a sliding door security bar or anti-lift device installed in the bottom track of a sliding glass door or patio door at a Singapore residential property. The bar is a simple metal or solid timber rod sitting in the floor track, preventing the door from being slid open. The surrounding context is a typical Singapore residential interior — tiled floor, glass door, garden or outdoor area visible through the glass. Clean, functional. No people. Natural indoor/outdoor lighting. Documentary photography style.

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
{ slug: "how-alarm-works",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "security-assessment-10-things", title: "10 Things I Look For When Assessing a Property's Security", category: "Security Planning", tags: ["security-assessment","property-security","security-planning","singapore"], excerpt: "After more than 35 years in the security industry, these are the first things I notice when I walk around a property — and the simple improvements that make the biggest difference.", image: "security-assessment-10-things-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: security-assessment-10-things.html*
*Total images: 3 (1 feature + 2 body)*
