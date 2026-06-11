# AG IMAGE BRIEF — false-alarms.html
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

**File name:** `false-alarms-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/false-alarms-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A close-up photograph of an external alarm siren and strobe unit mounted on the exterior wall of a Singapore residential or commercial property. The siren is a standard white or grey rectangular enclosure with a visible strobe light lens. It is mounted at height on a rendered or painted wall. Daytime, natural outdoor Singapore lighting. Clean, sharp focus on the siren unit, slightly blurred background showing a typical Singapore building facade — HDB block, landed terrace, or commercial shophouse. No people, no faces. Professional installation photography style, similar in composition to product shots found on security manufacturer websites.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — MONITORING OPERATOR REVIEWING ALARM

**File name:** `false-alarms-operator.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/false-alarms-operator.webp`
**Insert location:** In `section2`, after the paragraph ending "...That balance is harder to maintain than it sounds — especially when false alarms make up a significant proportion of the signals received every day.", using this exact HTML:

```html
<img src="/images/insights/false-alarms-operator.webp"
  alt="Security monitoring centre operator reviewing alarm event data on screen — every alarm must be assessed before a response decision is made"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a monitoring centre workstation with a computer screen displaying alarm event data — a list of alarm activations with timestamps, zone names and status indicators. The chair is occupied but no face is visible — shoot from behind or from the side, showing the operator's hands on the keyboard or desk but not their face. The screen content is clearly visible and legible. Professional, clean monitoring centre environment. Soft ambient screen lighting. No brand names on screen. Editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — SS 558 / SINGAPORE STANDARDS REFERENCE

**File name:** `false-alarms-ss558.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/false-alarms-ss558.webp`
**Insert location:** In `section5`, after the paragraph ending "...Repeated unnecessary activations reflect on the account and affect how future alarms are treated by both the monitoring centre and the police.", using this exact HTML:

```html
<img src="/images/insights/false-alarms-ss558.webp"
  alt="Technical standards document open on a desk representing Singapore Standard SS 558 for intruder alarm system installation and operation"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean close-up photograph of a technical standards or specification document open on a desk or table. The document shows dense technical text, section headings and numbered clauses — the kind of layout found in a standards publication. No specific brand names or identifiable text visible. The document is the main subject, slightly angled on a neutral desk surface with a pen or ruler beside it. Soft even office lighting, clean background. No people, no hands. Professional editorial photography style suggesting technical and regulatory content.

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
{ slug: "video-verification",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "false-alarms", title: "Why False Alarms Matter", category: "Alarm & Intrusion", tags: ["burglar-alarm","false-alarms","alarm-monitoring","singapore"], excerpt: "False alarms are more than just an annoyance. Learn how they affect homeowners, monitoring centres and police resources, why alarm verification matters and how proper system design helps reduce unnecessary alarm activations.", image: "false-alarms-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: false-alarms.html*
*Total images: 3 (1 feature + 2 body)*
