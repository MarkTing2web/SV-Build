# AG IMAGE BRIEF — self-monitoring-vs-cms.html
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

**File name:** `self-monitoring-vs-cms-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/self-monitoring-vs-cms-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A split-composition photograph. On the left half: a smartphone screen displaying a burglar alarm notification app showing an alert — "Alarm Activated — Front Door" with a timestamp. On the right half: a monitoring centre workstation screen showing an incoming alarm event on the operator interface. Both halves should feel equally present and professional. The overall image represents the choice between self-monitoring and professional monitoring — two valid paths from the same alarm event. Clean neutral background between the two elements. No people, no faces. Soft even lighting. Editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — HOMEOWNER CHECKING APP / SELF-MONITORING

**File name:** `self-monitoring-vs-cms-app.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/self-monitoring-vs-cms-app.webp`
**Insert location:** In `section2`, after the paragraph ending "...Many Singapore homeowners — particularly those in occupied condominiums where they are home most evenings — operate successfully this way.", using this exact HTML:

```html
<img src="/images/insights/self-monitoring-vs-cms-app.webp"
  alt="Smartphone displaying a burglar alarm self-monitoring app with zone status and camera access — modern self-monitoring in a Singapore home"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a smartphone displaying a clean, modern security app interface showing home alarm status — zones displayed as "OK" or "Armed", a small CCTV camera thumbnail visible, and a notification banner. The phone is placed on a table or held at a slight angle, in a clean Singapore residential interior setting — neutral tones, modern furniture slightly out of focus in the background. The screen is clearly legible. No brand names on the app interface. No people, no hands holding the phone. Soft natural home lighting. Editorial product photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — HYBRID MONITORING / BOTH PATHS ACTIVE

**File name:** `self-monitoring-vs-cms-hybrid.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/self-monitoring-vs-cms-hybrid.webp`
**Insert location:** In `section8`, after the paragraph ending "...The mobile app handles the normal cases. The monitoring centre handles the gaps.", using this exact HTML:

```html
<img src="/images/insights/self-monitoring-vs-cms-hybrid.webp"
  alt="Alarm panel settings screen showing simultaneous notification to homeowner mobile app and monitoring centre — the hybrid monitoring configuration"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of an alarm system configuration screen — either a tablet, laptop, or alarm keypad display — showing notification settings with two recipients configured: one labelled as the homeowner mobile app and one as the monitoring centre. The interface is clean and modern. The screen content clearly suggests that both paths are active simultaneously. No real names or numbers visible. Soft ambient office or home lighting. No people, no hands. Clean background. Professional product photography style.

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
{ slug: "pstn-to-ip",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "self-monitoring-vs-cms", title: "Should You Monitor Your Alarm Yourself or Use a Monitoring Centre?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","self-monitoring","singapore"], excerpt: "Self-monitoring or professional alarm monitoring? Learn the advantages, limitations and real-world considerations behind both approaches before deciding which is right for your home or business.", image: "self-monitoring-vs-cms-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: self-monitoring-vs-cms.html*
*Total images: 3 (1 feature + 2 body)*
