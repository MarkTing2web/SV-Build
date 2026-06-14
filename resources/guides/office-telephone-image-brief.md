# Business Phone Systems Guide — Image Generation & Insertion Brief
## File: /resources/guides/office-telephone-guide.html
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
All photography prompts must produce images set in Singapore. Use Singapore-appropriate architecture, office environments, and Asian subjects throughout.

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

**Save to:** `/images/resources/guides/telephony/hero-office-telephone.webp`
**Spec:** 1920×1080px WebP q85

**Prompt:**
Wide-angle cinematic photograph of a modern Singapore office environment showing a professional reception counter with an IP desk phone prominently visible. A well-dressed Asian receptionist is speaking on the phone. Clean modern office interior, glass partitions visible in the background, warm professional lighting. High quality photorealistic image suitable for a business technology guide hero.

**Insert at:** Already referenced in the hero header background-image style attribute. Confirm the path matches:
```
style="background-image: url('/images/resources/guides/telephony/hero-office-telephone.webp');"
```

---

## IMAGE 01b — Hero Mobile

**Save to:** `/images/resources/guides/telephony/hero-office-telephone-mobile.webp`
**Spec:** 1080×1920px WebP q85

**Prompt:**
Portrait-format cinematic photograph of a modern Singapore office reception counter with an IP desk phone. An Asian professional at the desk. Clean modern office interior. Vertical composition, warm professional lighting, photorealistic.

**Insert at:** No HTML change needed — referenced via CSS media query for mobile hero background.

---

## IMAGE 02 — Reception IP Phone

**Save to:** `/images/resources/guides/telephony/reception-ip-phone.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a modern IP desk phone on a clean reception counter in a Singapore office. The phone has a colour display and multiple function buttons. Professional reception environment, neutral colour scheme. Daylight or warm interior lighting, photorealistic, sharp detail on the phone.

**Insert at:** Section 1, Do Businesses Still Need Phone Systems. Locate the float figure block:
```html
<img alt="Singapore office receptionist answering calls on a modern IP desk phone at a professional reception counter" loading="lazy" src="/images/resources/guides/telephony/reception-ip-phone.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 03 — Multi-Branch Connectivity

**Save to:** `/images/resources/guides/telephony/multi-branch-connectivity.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Clean infographic-style illustration showing a map of Singapore and Johor Bahru with two office building icons connected by a network line. Labels indicate "Singapore Office" and "JB Warehouse". A phone icon on the connection line suggests unified telephony. Simple, professional, modern flat design style. Blue and white colour scheme. Not photographic — clean vector illustration style.

**Insert at:** Section 6, Multi-Branch Businesses subsection. Locate the float figure block:
```html
<img alt="Map of Singapore and Johor Bahru showing connected office locations on a single IP phone network" loading="lazy" src="/images/resources/guides/telephony/multi-branch-connectivity.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 04 — SIP Door Phone at Entrance

**Save to:** `/images/resources/guides/telephony/sip-door-phone-entrance.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Close-up photograph of a modern SIP video door phone mounted on the wall beside the entrance of a Singapore office building or warehouse. The door phone has a visible camera lens, a call button, and a small speaker grille. Clean wall background, professional installation. Daylight exterior or interior lighting, photorealistic, sharp detail on the device.

**Insert at:** Section 11, Office Door Phones and Visitor Communication. Locate the float figure block:
```html
<img alt="Fanvil SIP video door phone mounted at a Singapore office entrance showing visitor call button and camera" loading="lazy" src="/images/resources/guides/telephony/sip-door-phone-entrance.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 05 — Yeastar Fanvil System

**Save to:** `/images/resources/guides/telephony/yeastar-fanvil-system.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of a Yeastar IP PBX appliance unit placed on a server shelf or office desk beside two Fanvil IP desk phones. The equipment is clearly visible and professionally arranged. Clean background, good lighting showing product detail. Professional product photography style, photorealistic.

**Insert at:** Section 15, Yeastar IP PBX Systems subsection. Locate the float figure block:
```html
<img alt="Yeastar P-Series IP PBX appliance and Fanvil IP desk phones on an office desk in Singapore" loading="lazy" src="/images/resources/guides/telephony/yeastar-fanvil-system.webp"/>
```
Confirm src path matches and image is saved correctly.

---

## IMAGE 06 — Softphone on Mobile

**Save to:** `/images/resources/guides/telephony/softphone-mobile-worker.webp`
**Spec:** 960×540px WebP q85

**Prompt:**
Photograph of an Asian male or female professional in business casual attire, working remotely — seated at a café or home office in Singapore, using a smartphone with a business softphone application visible on the screen. The screen shows a call interface with company caller ID displayed. Natural, professional, relaxed working environment. Daylight or warm interior lighting, photorealistic.

**Insert at:** Section 9, Softphones and Hybrid Work. Insert the float figure block immediately after the section opening paragraph and before the first subsection heading "Turning Your Mobile Into an Office Extension". Use this HTML:

```html
<figure class="rg-figure--float">
  <div class="rg-img-wrap rg-img-wrap--float">
    <img alt="Asian professional using a softphone application on a smartphone to take office calls while working remotely in Singapore" loading="lazy" src="/images/resources/guides/telephony/softphone-mobile-worker.webp"/>
  </div>
  <p class="rg-img-caption visually-hidden">A softphone application turns any smartphone into a full office extension — the caller sees the company number, not the employee's personal mobile number.</p>
</figure>
```

Place this block immediately after the opening paragraph of Section 9 (`<p>One of the biggest changes in business communications...`) and before the first `<div class="subsection">`.

---

## COMPLETION INSTRUCTION

After all 6 images (including both hero variants — 7 files total) have been generated and inserted:

1. Perform the final sweep described in Master Rule 4 — confirm no `<img>` tag sits inside any `.rg-callout`, `.rg-recommendation`, or `.rg-verdict` div. Move any found images immediately above the containing div.

2. **STOP. Do not make any further changes to the HTML file.**

3. Wait for Wee Meng to review the page on staging before proceeding.
