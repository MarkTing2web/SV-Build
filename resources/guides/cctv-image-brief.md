# CCTV Guide — Image Generation & Insertion Brief
## File: /resources/guides/cctv-guide.html
## For: Anti-Gravity AI Web Builder

---

## MASTER RULES — READ BEFORE GENERATING ANY IMAGE

### Rule 1 — Generate one image at a time
Generate each image individually. After each image is saved and inserted, auto-continue to the next. Do not wait for confirmation between images.

### Rule 2 — Securevision staff appearance
Any image featuring Securevision staff must show:
- White polo shirt
- Securevision logo on the breast pocket — use the image at `/images/securevision-logo-blue.png` as the logo reference for the breast pocket
- The word SECUREVISION printed on the sleeve
- Asian male or female subject
- Professional, focused demeanour

### Rule 3 — Singapore setting
All photography prompts must produce images set in Singapore. Use Singapore-appropriate architecture, tropical vegetation, and Asian subjects throughout.

### Rule 4 — No images inside callout boxes
Images must NEVER be placed inside `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div blocks. Images must always float beside full prose paragraphs in the main content flow. After inserting all images, perform a final sweep of the HTML file and confirm no `<img>` tag sits inside any callout, recommendation, or verdict div. If any is found, move it immediately above the containing div.

### Rule 5 — Do not touch anything else
After all images are generated and inserted, STOP. Do not modify any other part of the HTML file. Wait for Wee Meng to review before proceeding.

---

## IMAGE SPECS

- All body images: **960×540px, WebP, quality 85, centre-crop**
- Hero desktop: **1920×1080px, WebP, quality 85**
- Hero mobile: **1080×1920px, WebP, quality 85**

---

## IMAGE 01 — Hero Desktop

**Save to:** `/images/resources/guides/cctv/hero-cctv-guide.webp`
**Spec:** 1920×1080px WebP q85

**Prompt:**
Wide-angle cinematic photograph of the exterior of a modern Singapore commercial building or condominium at dusk. Multiple CCTV cameras visible mounted at the entrance — a dome camera on the ceiling of the porch and a bullet camera on the exterior wall. Security signage visible near the entrance. Modern architecture, Singapore tropical vegetation, warm evening lighting. Professional real estate photography quality, photorealistic.

**Insert at:** Already referenced in the hero header background-image style attribute. Confirm the path matches:
```
style="background-image: url('/images/resources/guides/cctv/hero-cctv-guide.webp');"
```

---

## IMAGE 01b — Hero Mobile

**Save to:** `/images/resources/guides/cctv/hero-cctv-guide-mobile.webp`
**Spec:** 1080×1920px WebP q85

**Prompt:**
Portrait-format cinematic photograph of the exterior of a modern Singapore commercial building or condominium at dusk. Multiple CCTV cameras visible at the entrance. Modern architecture, tropical setting, warm evening lighting. Vertical composition, photorealistic.

**Insert at:** No HTML change needed — referenced via CSS media query for mobile hero background.

---

## IMAGE 02 — CCTV Exterior Camera

**Save to:** `/images/resources/guides/cctv/cctv-exterior-camera.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a modern bullet-style CCTV camera mounted on the exterior wall of a Singapore property. The camera is clearly visible, aimed toward the entrance area. Clean rendered wall background, tropical plants partially visible. Daylight, photorealistic, sharp detail on the camera housing.

**Insert at:** Section 1, What Is a CCTV System. Locate the float figure block:
```html
<img alt="Modern CCTV camera mounted on exterior wall of a Singapore property showing surveillance coverage" loading="lazy" src="/images/resources/guides/cctv/cctv-exterior-camera.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 03 — PoE Network Switch

**Save to:** `/images/resources/guides/cctv/poe-switch-network.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a PoE (Power over Ethernet) network switch with multiple network cables connected. The switch has indicator lights showing active ports. Mounted in a small network cabinet or on a shelf. Clean, professional installation. Even lighting, high detail on the switch and cable connections, photorealistic.

**Insert at:** Section 2, Component Card — PoE Switch. Locate:
```html
<img alt="PoE network switch with connected camera cables showing power and data delivery over single cable" loading="lazy" src="/images/resources/guides/cctv/poe-switch-network.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 04 — Security Monitor in Guardhouse

**Save to:** `/images/resources/guides/cctv/security-monitor-guardhouse.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a professional security monitor displaying a multi-camera CCTV grid layout at a Singapore condominium guardhouse security desk. The monitor shows 8 or 16 camera feeds simultaneously. A uniformed Asian male security guard is seated at the desk, alert and monitoring the screens. Professional security post environment, clean and well-lit. Daylight or indoor lighting, photorealistic.

**Insert at:** Section 2, Monitors and Displays subsection. Locate the float figure block:
```html
<img alt="Professional security grade monitor displaying multi-camera CCTV grid in a Singapore guardhouse control room" loading="lazy" src="/images/resources/guides/cctv/security-monitor-guardhouse.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 05 — Solar AOV Camera on Site

**Save to:** `/images/resources/guides/cctv/solar-aov-camera-site.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a solar-powered security camera mounted on a metal pole at a Singapore construction site. A small solar panel is clearly visible above the camera unit. The camera housing includes the camera body and solar panel as an integrated unit. Construction site background — scaffolding, building materials, safety fencing. Daylight, photorealistic.

**Insert at:** Section 3, Solar-Powered Cameras subsection. Locate the float figure block:
```html
<img alt="Solar-powered AOV security camera mounted on a post at a Singapore construction site with solar panel visible" loading="lazy" src="/images/resources/guides/cctv/solar-aov-camera-site.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 06 — Dome Camera on Ceiling

**Save to:** `/images/resources/guides/cctv/dome-camera-ceiling.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a vandal-resistant dome CCTV camera mounted on the ceiling of a Singapore condominium common corridor or office. The dome housing is clearly visible, showing the dark tinted dome cover. Clean ceiling, neutral colour, fluorescent or LED lighting. Slightly upward angle showing the camera in context. Photorealistic, sharp detail.

**Insert at:** Section 5, Dome Cameras subsection. Locate the float figure block:
```html
<img alt="Vandal-resistant dome camera mounted on ceiling of a Singapore condominium corridor showing discreet housing" loading="lazy" src="/images/resources/guides/cctv/dome-camera-ceiling.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 07 — Turret Camera at Entrance

**Save to:** `/images/resources/guides/cctv/turret-camera-entrance.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a turret (eyeball) CCTV camera mounted on the wall beside the entrance of a Singapore landed home or small office. The ball-socket mounting is visible, with the camera module angled toward the entrance. The exposed lens is clearly visible. Clean wall background, daylight, photorealistic, sharp detail on the camera.

**Insert at:** Section 5, Turret Cameras subsection. Locate the float figure block:
```html
<img alt="Turret eyeball camera mounted at a Singapore landed home entrance showing exposed lens and ball-socket mount" loading="lazy" src="/images/resources/guides/cctv/turret-camera-entrance.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 08 — Landed Home Camera Positions

**Save to:** `/images/resources/guides/cctv/landed-home-camera-positions.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a Singapore terrace house exterior showing multiple CCTV camera positions — a camera visible at the gate, another at the main entrance, and one aimed at the car porch area. The cameras are clearly visible on the exterior. Brick gate pillars, tropical garden, residential street setting. Daylight, photorealistic.

**Insert at:** Section 7, Landed Homes subsection. Locate the float figure block:
```html
<img alt="Singapore landed home showing multiple CCTV camera positions at gate, entrance, car porch and side passage" loading="lazy" src="/images/resources/guides/cctv/landed-home-camera-positions.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 09 — Starlight vs Infrared Night Comparison

**Save to:** `/images/resources/guides/cctv/starlight-vs-infrared-night.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Split-image photograph showing a comparison between two views of the same Singapore driveway at night. Left half: monochrome black-and-white infrared CCTV footage showing a person approaching a gate. Right half: full-colour low-light footage of the same scene, showing the same person's clothing colour and skin tone clearly. Clear visual contrast between the two image types. Photorealistic, cinematic quality.

**Insert at:** Section 11, Starlight Technology subsection. Locate the float figure block:
```html
<img alt="Comparison of infrared monochrome night vision footage versus full-colour starlight technology footage at a Singapore driveway" loading="lazy" src="/images/resources/guides/cctv/starlight-vs-infrared-night.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 10 — Technician Cleaning Camera

**Save to:** `/images/resources/guides/cctv/technician-cleaning-camera.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male technician in a white polo shirt with the Securevision logo on the breast pocket (use /images/securevision-logo-blue.png as the logo reference) and SECUREVISION printed on the sleeve, using a microfibre cloth to clean the dome cover of a CCTV camera mounted on an exterior wall at a Singapore property. He is standing on a small stepladder. Professional and focused expression. Daylight, photorealistic.

**Insert at:** Section 16, Maintenance and Best Practices. Locate the float figure block:
```html
<img alt="Securevision technician in white polo shirt with Securevision logo cleaning a CCTV camera dome at a Singapore property" loading="lazy" src="/images/resources/guides/cctv/technician-cleaning-camera.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## COMPLETION INSTRUCTION

After all 10 images (including both hero variants — 11 files total) have been generated and inserted:

1. Perform the final sweep described in Master Rule 4 — confirm no `<img>` tag sits inside any `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div. Move any found images immediately above the containing div.

2. **STOP. Do not make any further changes to the HTML file.**

3. Wait for Wee Meng to review the page on staging before proceeding.
