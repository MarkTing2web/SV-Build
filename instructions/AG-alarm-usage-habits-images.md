# AG IMAGE BRIEF — alarm-usage-habits.html
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

**File name:** `alarm-usage-habits-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-usage-habits-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A photograph of a Singapore homeowner — Asian, middle-aged, smart casual clothing — arming a modern alarm keypad as part of an evening routine. The person is pressing the arm button on a touchscreen or graphic display keypad mounted in a Singapore residential interior hallway or entrance area. The composition should feel natural and routine — this is a habitual action, not a dramatic moment. Soft evening indoor lighting. No face needed — the person can be shown from behind or at an angle that avoids identifiable features. No Securevision branding. Professional documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — STAY MODE / NIGHT ARMING

**File name:** `alarm-usage-habits-stay-mode.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-usage-habits-stay-mode.webp`
**Insert location:** In `section2`, after the paragraph ending "...An alarm armed in stay mode every night protects the people inside the house, not just the possessions.", using this exact HTML:

```html
<img src="/images/insights/alarm-usage-habits-stay-mode.webp"
  alt="Alarm keypad showing Stay mode selected at night — arming the perimeter while allowing free movement inside the property"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a modern alarm keypad displaying "STAY" or "HOME" mode selected — the arming mode that protects the perimeter while bypassing interior motion detectors. The keypad display clearly shows the stay/home mode is active. The keypad is mounted on a wall in a Singapore residential interior. The ambient lighting suggests evening or night — the overhead lights are on but the atmosphere is quiet and domestic. No people, no hands. Sharp focus on the keypad display. Professional product photography style. No brand logos.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — ALARM EVENT LOG ON APP

**File name:** `alarm-usage-habits-event-log.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-usage-habits-event-log.webp`
**Insert location:** In `section5`, after the paragraph ending "...The system is trying to communicate something. Finding out what is almost always more useful than resetting and hoping it does not happen again.", using this exact HTML:

```html
<img src="/images/insights/alarm-usage-habits-event-log.webp"
  alt="Smartphone displaying alarm system event log with zone activation history and timestamps — the information that identifies what caused a false alarm"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a smartphone screen displaying an alarm system mobile app showing an event log or activity history. The screen shows a list of entries with timestamps, zone names (e.g. "Front Door", "Motion Zone 1"), and event types (Armed, Disarmed, Zone Activated). The interface is clean and modern — a current-generation alarm app interface. The phone is resting on a table or held at a slight angle. Soft natural lighting. No people, no hands on the phone. No specific real app brand visible. Professional editorial photography style.

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
{ slug: "network-security-systems",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-usage-habits", title: "Most Alarm Systems Are Installed Correctly But Used Incorrectly", category: "Security Planning", tags: ["burglar-alarm","alarm-usage","security-planning","singapore"], excerpt: "Most burglar alarm systems are installed correctly but used incorrectly. Learn the common mistakes homeowners make, how to use Stay Mode effectively, and why good habits matter more than expensive technology.", image: "alarm-usage-habits-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-usage-habits.html*
*Total images: 3 (1 feature + 2 body)*
