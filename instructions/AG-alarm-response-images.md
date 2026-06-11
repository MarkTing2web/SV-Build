# AG IMAGE BRIEF — alarm-response.html
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

**File name:** `alarm-response-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-response-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A nighttime exterior photograph of a Singapore residential street or condominium driveway with a police patrol car parked outside a property. The blue and red emergency lights are on, casting coloured reflections on the road and building facade. No officers visible — car only, suggesting a response in progress. Singapore residential environment — HDB void deck or condominium drop-off, nighttime lighting from street lamps and building lights. No faces, no uniforms, no identifying details. Atmospheric, documentary photography style. Cool blue and warm amber lighting mix.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — CONTACT LIST / ACCOUNT DETAILS

**File name:** `alarm-response-contact-list.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-response-contact-list.webp`
**Insert location:** In `section3`, after the paragraph ending "...An outdated contact list can significantly slow down how quickly an alarm event is resolved.", using this exact HTML:

```html
<img src="/images/insights/alarm-response-contact-list.webp"
  alt="Alarm monitoring account contact list on a screen showing primary, secondary and third contact details for a Singapore property"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a computer or tablet screen displaying an alarm account management form or contact list. The screen shows fields for Primary Contact, Secondary Contact, Third Contact, each with name and phone number fields filled in with generic placeholder details — no real names or numbers. Clean, modern software UI. The screen is the clear subject of the image, slightly angled on a desk, soft ambient office lighting. No people, no hands. Professional editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — KEYHOLDER / PROPERTY ACCESS

**File name:** `alarm-response-keyholder.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-response-keyholder.webp`
**Insert location:** In `section6`, after the paragraph ending "...It needs a person who is reachable, willing, and able to get to the property within a reasonable time when needed.", using this exact HTML:

```html
<img src="/images/insights/alarm-response-keyholder.webp"
  alt="A set of property keys on a key ring placed on a desk or table representing keyholder arrangements for an alarm monitoring account"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean close-up photograph of a set of keys on a key ring placed on a neutral surface — a desk, table, or countertop. Two or three keys visible, standard door keys, plain and unbranded. Shallow depth of field, sharp focus on the keys, soft blurred background suggesting an office or reception environment. Simple, symbolic composition. No people, no hands. Soft even lighting, neutral background tones. Editorial product photography style.

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
{ slug: "alarm-panel",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-response", title: "What Really Happens When Your Alarm Goes Off?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-response","keyholders","singapore"], excerpt: "What really happens after your burglar alarm goes off? Learn how monitoring centres verify alarms, activate police response, work with keyholders and manage real-world alarm incidents behind the scenes.", image: "alarm-response-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-response.html*
*Total images: 3 (1 feature + 2 body)*
