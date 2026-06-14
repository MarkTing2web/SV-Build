# Door Access Control Guide — Image Generation & Insertion Brief
## File: /resources/guides/door-access-guide.html
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
All photography prompts must produce images set in Singapore. Use Singapore-appropriate architecture and Asian subjects throughout.

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

**Save to:** `/images/resources/guides/access/hero-door-access.webp`
**Spec:** 1920×1080px WebP q85

**Prompt:**
Wide-angle cinematic photograph of the entrance lobby of a modern Singapore commercial office building. A sleek access control card reader is mounted beside a glass door. A professional-looking Asian woman in business attire is tapping her access card on the reader. Clean modern interior, polished floor, neutral colour scheme. Warm professional lighting. Photorealistic, high quality.

**Insert at:** Already referenced in the hero header background-image style attribute. Confirm the path matches:
```
style="background-image: url('/images/resources/guides/access/hero-door-access.webp');"
```

---

## IMAGE 01b — Hero Mobile

**Save to:** `/images/resources/guides/access/hero-door-access-mobile.webp`
**Spec:** 1080×1920px WebP q85

**Prompt:**
Portrait-format cinematic photograph of the entrance of a modern Singapore office building. Access control card reader visible beside a glass door. An Asian professional tapping an access card. Clean modern interior. Vertical composition, warm professional lighting, photorealistic.

**Insert at:** No HTML change needed — referenced via CSS media query for mobile hero background.

---

## IMAGE 02 — Access Card Reader at Door

**Save to:** `/images/resources/guides/access/access-card-reader-door.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a modern access control card reader mounted on the wall beside a glass office door in Singapore. The reader has a small LED indicator and a card tap zone. Clean office interior background, neutral wall colour. Daylight interior lighting, sharp detail on the reader, photorealistic.

**Insert at:** Section 1, What Is an Access Control System. Locate the float figure block:
```html
<img alt="Access card reader mounted beside a glass office door in Singapore showing credential tap point" loading="lazy" src="/images/resources/guides/access/access-card-reader-door.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 03 — Credential Types Overview

**Save to:** `/images/resources/guides/access/credential-types-overview.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Clean flat-lay product photograph on a white surface showing the range of access control credential types: a white access card, a small key fob, and a smartphone with a lock icon on the screen. All items arranged neatly. Soft studio lighting, photorealistic.

**Insert at:** Section 2, Component Card 1 (The Credential). Locate:
```html
<img alt="Access cards, key fobs and mobile phone showing the range of credential types for access control" loading="lazy" src="/images/resources/guides/access/credential-types-overview.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 04 — Fingerprint and Card Reader

**Save to:** `/images/resources/guides/access/access-reader-fingerprint-card.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a combination fingerprint and access card reader mounted on an office wall beside a door in Singapore. The reader has a fingerprint sensor at the top and a card tap zone below. Clean wall, professional installation. Daylight interior lighting, photorealistic, sharp detail.

**Insert at:** Section 2, Component Card 2 (The Reader). Locate:
```html
<img alt="Fingerprint and card combination reader mounted on office wall beside access-controlled door" loading="lazy" src="/images/resources/guides/access/access-reader-fingerprint-card.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 05 — Access Controller Panel

**Save to:** `/images/resources/guides/access/access-controller-panel.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an access control controller panel mounted inside a small equipment cabinet. Clearly visible wiring terminals, network cable connections, and status LED lights. Neat cable management. Clean lighting, high detail on the electronics, photorealistic.

**Insert at:** Section 2, Component Card 3 (The Controller). Locate:
```html
<img alt="Access control controller panel showing wiring terminals and network connections in equipment cabinet" loading="lazy" src="/images/resources/guides/access/access-controller-panel.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 06 — EM Lock on Door Frame

**Save to:** `/images/resources/guides/access/em-lock-door-frame.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an electromagnetic (EM) lock mounted on a door frame at a Singapore office. The lock housing is clearly visible at the top of the frame with the magnet plate on the door visible. Clean professional installation. Daylight interior lighting, photorealistic.

**Insert at:** Section 2, Component Card 4 (The Lock). Locate:
```html
<img alt="Electromagnetic lock mounted on door frame showing the magnet plate and mounting bracket" loading="lazy" src="/images/resources/guides/access/em-lock-door-frame.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 07 — Access Management Software

**Save to:** `/images/resources/guides/access/access-management-software.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a computer monitor showing an access control management software dashboard. The screen displays a user list with names, access levels, and door status indicators. Clean office desk environment. Professional lighting, photorealistic, screen content clearly visible.

**Insert at:** Section 2, Component Card 5 (The Software). Locate:
```html
<img alt="Access control management software dashboard showing user list and door status on computer screen" loading="lazy" src="/images/resources/guides/access/access-management-software.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 08 — Landed Home Side Gate Access

**Save to:** `/images/resources/guides/access/landed-home-side-gate-access.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of the side gate of a Singapore landed home with an access control keypad and card reader mounted on the gate pillar. The reader is clearly visible on the brick pillar. Tropical garden background, daylight, photorealistic.

**Insert at:** Section 4, Can Access Control Be Used in Homes. Locate the float figure block:
```html
<img alt="Access control keypad and card reader at the side gate of a Singapore landed home" loading="lazy" src="/images/resources/guides/access/landed-home-side-gate-access.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 09 — Smart Card Tap on Reader

**Save to:** `/images/resources/guides/access/smart-card-tap-reader.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an Asian hand tapping a white access card on a card reader mounted beside an office door in Singapore. The card is in close contact with the reader tap zone. Clean office background, daylight interior lighting, photorealistic, sharp detail on the card and reader.

**Insert at:** Section 5, Access Cards subsection. Locate the float figure block:
```html
<img alt="Close-up of MIFARE smart access card being tapped on card reader at Singapore office door" loading="lazy" src="/images/resources/guides/access/smart-card-tap-reader.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 10 — EM Lock on Glass Door

**Save to:** `/images/resources/guides/access/em-lock-glass-door.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an electromagnetic lock mounted on the top frame of a frameless glass door at a Singapore office. The silver lock housing is clearly visible above the glass door. The magnet plate on the door is visible where it contacts the lock. Clean professional installation. Daylight interior, photorealistic.

**Insert at:** Section 6, Electromagnetic Locks subsection. Locate the float figure block:
```html
<img alt="Electromagnetic EM lock mounted on top of glass door frame at Singapore office showing magnet housing" loading="lazy" src="/images/resources/guides/access/em-lock-glass-door.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 11 — Lift Lobby Access Reader

**Save to:** `/images/resources/guides/access/lift-lobby-access-reader.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a lift lobby access control reader mounted on the wall beside lift doors in a Singapore condominium or commercial building. An Asian resident is tapping their access card on the reader. Modern lift lobby interior, clean and well-lit. Daylight or bright interior lighting, photorealistic.

**Insert at:** Section 10, Lift Access Control. Locate the float figure block:
```html
<img alt="Lift lobby access control reader in Singapore condominium showing card tap point beside lift buttons" loading="lazy" src="/images/resources/guides/access/lift-lobby-access-reader.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 12 — Technician Maintenance

**Save to:** `/images/resources/guides/access/technician-access-maintenance.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male technician in a white polo shirt with the Securevision logo on the breast pocket (use /images/securevision-logo-blue.png as the logo reference) and SECUREVISION printed on the sleeve, inspecting an access control card reader mounted beside a door at a Singapore office. He is holding a tablet or clipboard and checking the reader. Professional and focused expression. Daylight interior, photorealistic.

**Insert at:** Section 15, Maintenance and Best Practices. Locate the float figure block:
```html
<img alt="Securevision technician in white polo shirt with Securevision logo inspecting access control reader and lock at Singapore office" loading="lazy" src="/images/resources/guides/access/technician-access-maintenance.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## COMPLETION INSTRUCTION

After all 12 images (including both hero variants — 13 files total) have been generated and inserted:

1. Perform the final sweep described in Master Rule 4 — confirm no `<img>` tag sits inside any `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div. Move any found images immediately above the containing div.

2. **STOP. Do not make any further changes to the HTML file.**

3. Wait for Wee Meng to review the page on staging before proceeding.
