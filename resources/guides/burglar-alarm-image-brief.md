# Burglar Alarm Guide — Image Generation & Insertion Brief
## File: /resources/guides/burglar-alarm-guide.html
## For: Anti-Gravity AI Web Builder

---

## MASTER RULES — READ BEFORE GENERATING ANY IMAGE

### Rule 1 — Generate one image at a time
Generate each image individually. After each image is saved and inserted, auto-continue to the next. Do not wait for confirmation between images.

### Rule 2 — Securevision staff appearance
Any image featuring Securevision staff must show:
- White polo shirt
- Securevision logo on the breast pocket — use the image at `/images/securevision-logo-blue.png` as the logo reference
- The word SECUREVISION printed on the sleeve
- Asian male or female subject
- Professional, focused demeanour

### Rule 3 — Singapore setting
All photography prompts must produce images set in Singapore. Use Singapore-appropriate architecture, tropical vegetation, and Asian subjects throughout.

### Rule 4 — Image placement rule — no images inside callout boxes
Images must NEVER be placed inside `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div blocks. Images must always float beside full prose paragraphs in the main content flow. After inserting all images, perform a final sweep of the HTML file and confirm no `<img>` tag sits inside any callout, recommendation, or verdict div. If any is found, move it immediately above the callout block.

### Rule 5 — Do not touch anything else
After all images are generated and inserted, STOP. Do not modify any other part of the HTML file. Wait for Wee Meng to review before proceeding.

---

## IMAGE SPECS

- All body images: **960×540px, WebP, quality 85, centre-crop**
- Hero desktop: **1920×1080px, WebP, quality 85**
- Hero mobile: **1080×1920px, WebP, quality 85**

---

## IMAGE 01 — Hero Desktop

**Save to:** `/images/resources/guides/alarm/hero-burglar-alarm.webp`
**Spec:** 1920×1080px WebP q85

**Prompt:**
Wide-angle cinematic photograph of the exterior of a modern Singapore landed property at dusk. A visible alarm siren box with strobe light is mounted on the exterior wall near the entrance. Security camera visible above the gate. Warm interior lighting visible through windows suggesting occupancy. Tropical landscaping, brick boundary wall, private residential setting. Professional real estate photography quality, photorealistic.

**Insert at:** Already referenced in the hero `<header>` background-image style attribute. Confirm the path matches:
```
style="background-image: url('/images/resources/guides/alarm/hero-burglar-alarm.webp');"
```

---

## IMAGE 01b — Hero Mobile

**Save to:** `/images/resources/guides/alarm/hero-burglar-alarm-mobile.webp`
**Spec:** 1080×1920px WebP q85

**Prompt:**
Portrait-format cinematic photograph of the exterior of a modern Singapore landed property at dusk. Visible alarm siren box on the exterior wall, security camera above the gate, warm interior lighting through windows. Tropical landscaping. Vertical composition, photorealistic.

**Insert at:** No HTML change needed — referenced via CSS media query for mobile hero background.

---

## IMAGE 02 — External Siren and Strobe

**Save to:** `/images/resources/guides/alarm/external-siren-strobe.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a white external alarm siren box with integrated red strobe light mounted on the rendered exterior wall of a Singapore property. The unit is clearly visible and professionally installed. Daylight, sharp detail, photorealistic.

**Insert at:** Section 1, What Is a Burglar Alarm System. Locate the float figure block:
```html
<img alt="External alarm siren box and strobe light mounted on the facade of a Singapore property" loading="lazy" src="/images/resources/guides/alarm/external-siren-strobe.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 03 — Alarm Control Panel

**Save to:** `/images/resources/guides/alarm/alarm-control-panel.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an alarm control panel mounted inside a metal enclosure. Clearly visible terminal blocks for zone wiring, a sealed lead-acid backup battery, and a communication module. Neat cable management. Clean workshop lighting, high detail on the electronics, photorealistic.

**Insert at:** Section 2, Component Card 1 (Control Panel). Locate:
```html
<img alt="Burglar alarm control panel showing zone terminals, backup battery and communication modules" loading="lazy" src="/images/resources/guides/alarm/alarm-control-panel.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 04 — Alarm Keypad with Zone Display

**Save to:** `/images/resources/guides/alarm/alarm-keypad-zones.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a modern alarm keypad with LCD display showing zone status information, mounted on an interior wall near a doorway at a Singapore home. Backlit display, numeric keypad, professional installation. Daylight interior lighting, photorealistic.

**Insert at:** Section 2, Component Card 2 (Zones). Locate:
```html
<img alt="Alarm keypad showing zone status display and arming controls at a Singapore property entrance" loading="lazy" src="/images/resources/guides/alarm/alarm-keypad-zones.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 05 — External Alarm Siren Unit (Component Card)

**Save to:** `/images/resources/guides/alarm/alarm-siren-external.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a white external alarm siren and strobe light unit mounted on the exterior wall of a Singapore property. The unit shows the speaker grille and strobe lens clearly. Clean professional installation against a rendered wall. Daylight, photorealistic.

**Insert at:** Section 2, Component Card 3 (Sirens & Strobe Lights). Locate:
```html
<img alt="External alarm siren and strobe light unit mounted on the exterior wall of a Singapore property" loading="lazy" src="/images/resources/guides/alarm/alarm-siren-external.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 06 — Tamper Switch Close-Up

**Save to:** `/images/resources/guides/alarm/alarm-tamper-switch.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Extreme close-up photograph of the rear of an alarm sensor housing showing the small tamper switch — a spring-loaded pin that protrudes from the back of the sensor enclosure. The switch and its housing are in sharp focus. Clean white background or mounted on a wall surface. Macro photography, photorealistic.

**Insert at:** Section 2, Component Card 4 (Tamper Protection). Locate:
```html
<img alt="Close-up of alarm sensor showing tamper switch mechanism on the rear of the housing" loading="lazy" src="/images/resources/guides/alarm/alarm-tamper-switch.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 07 — Dual-Path Communicator Module

**Save to:** `/images/resources/guides/alarm/alarm-dual-path-communicator.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of an alarm communicator module showing both an Ethernet/IP port and a SIM card slot for GSM mobile network connection. The module is mounted inside an alarm enclosure alongside other components. Clear detail on the connection ports. Clean lighting, photorealistic.

**Insert at:** Section 2, Component Card 5 (Communication Paths). Locate:
```html
<img alt="Alarm communicator module showing IP and GSM dual-path communication connections" loading="lazy" src="/images/resources/guides/alarm/alarm-dual-path-communicator.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 08 — Backup Battery Inside Panel

**Save to:** `/images/resources/guides/alarm/alarm-backup-battery.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a sealed lead-acid backup battery inside an alarm control panel enclosure. The battery label is visible showing voltage and ampere-hour rating. Neat wiring connections. Clean lighting, photorealistic.

**Insert at:** Section 2, Component Card 6 (Backup Batteries). Locate:
```html
<img alt="Sealed lead-acid backup battery inside an alarm control panel enclosure" loading="lazy" src="/images/resources/guides/alarm/alarm-backup-battery.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 09 — Wireless Alarm Hub and Sensors

**Save to:** `/images/resources/guides/alarm/wireless-alarm-hub-sensors.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Clean product-style photograph of a modern wireless alarm hub and a small selection of compact wireless sensors arranged on a white surface. The hub is a small rectangular unit. The sensors include a motion detector, a door contact, and a siren. Modern minimalist design, soft studio lighting, photorealistic.

**Insert at:** Section 3, Wireless Alarm Systems subsection. Locate the float figure block:
```html
<img alt="Wireless alarm hub and compact sensor set on a white surface showing modern wireless alarm components" loading="lazy" src="/images/resources/guides/alarm/wireless-alarm-hub-sensors.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 10 — PIR Motion Detector Installed

**Save to:** `/images/resources/guides/alarm/pir-motion-detector.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a white PIR motion detector mounted in the upper corner of a room at a Singapore property. The detector is aimed diagonally across the room. Clean interior wall, neutral paint colour, daylight interior lighting. The detector coverage angle is implied by its position. Photorealistic.

**Insert at:** Section 4, PIR Motion Detectors subsection. Locate the float figure block:
```html
<img alt="PIR motion detector mounted in the corner of a Singapore office or home showing detection coverage angle" loading="lazy" src="/images/resources/guides/alarm/pir-motion-detector.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 11 — Door Contact Sensor

**Save to:** `/images/resources/guides/alarm/door-contact-sensor.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a white magnetic door contact sensor installed on a door frame and door leaf at a Singapore property. The two-part sensor — magnet on the door and contact on the frame — are clearly visible in close proximity. Clean professional installation. Daylight, photorealistic.

**Insert at:** Section 4, Door and Window Contact Sensors subsection. Locate the float figure block:
```html
<img alt="Magnetic door contact sensor installed on a door frame and door leaf at a Singapore property" loading="lazy" src="/images/resources/guides/alarm/door-contact-sensor.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 12 — Homeowner Checking Alarm App

**Save to:** `/images/resources/guides/alarm/homeowner-alarm-app.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian woman in casual clothing holding a smartphone showing an alarm monitoring app with zone status and a notification alert visible on the screen. She is inside a Singapore home, natural indoor lighting, relaxed but attentive expression. Warm domestic atmosphere, photorealistic.

**Insert at:** Section 6, Tier 2 — Self-Monitoring via Smartphone subsection. Locate the float figure block:
```html
<img alt="Asian homeowner checking alarm notification on smartphone app showing zone status and alert details" loading="lazy" src="/images/resources/guides/alarm/homeowner-alarm-app.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 13 — Alarm and CCTV Integration on Phone

**Save to:** `/images/resources/guides/alarm/alarm-cctv-integration-phone.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a smartphone screen showing a split view — an alarm notification on one side and a live CCTV camera feed showing the exterior of a Singapore property on the other. The screen content is clearly legible. The phone is held in an Asian hand. Clean background, natural lighting, photorealistic.

**Insert at:** Section 7, Integration with CCTV subsection. Locate the float figure block:
```html
<img alt="Smartphone screen showing alarm notification alongside CCTV live view from a Singapore property" loading="lazy" src="/images/resources/guides/alarm/alarm-cctv-integration-phone.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 14 — Landed Home with Alarm Signage

**Save to:** `/images/resources/guides/alarm/landed-home-alarm-setup.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a Singapore terrace house exterior showing a visible external alarm siren box mounted on the wall near the entrance and a CCTV camera above the gate. Alarm warning sticker visible on the gate pillar. Brick gate pillars, tropical landscaping, residential street setting. Daylight, photorealistic.

**Insert at:** Section 8, Singapore Landed Home subsection. Locate the float figure block:
```html
<img alt="Singapore terrace house with visible external alarm siren box and CCTV camera at the entrance" loading="lazy" src="/images/resources/guides/alarm/landed-home-alarm-setup.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 15 — Technician Testing Alarm Sensor

**Save to:** `/images/resources/guides/alarm/technician-testing-alarm.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male technician in a white polo shirt with the Securevision logo on the breast pocket (use /images/securevision-logo-blue.png as the logo reference) and SECUREVISION printed on the sleeve, holding a sensor tester device up to a PIR motion detector mounted on an interior wall at a Singapore property. Professional and focused. Daylight interior, photorealistic.

**Insert at:** Section 10, Maintenance and Testing. Locate the float figure block:
```html
<img alt="Securevision technician in white polo shirt with Securevision logo testing an alarm sensor at a Singapore property" loading="lazy" src="/images/resources/guides/alarm/technician-testing-alarm.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## COMPLETION INSTRUCTION

After all 15 images (including both hero variants) have been generated and inserted:

1. Perform the final sweep described in Master Rule 4 — confirm no `<img>` tag sits inside any `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div. Move any found images immediately above the containing div.

2. **STOP. Do not make any further changes to the HTML file.**

3. Wait for Wee Meng to review the page on staging before proceeding.
