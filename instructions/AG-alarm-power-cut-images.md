# AG IMAGE BRIEF — alarm-power-cut.html
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

**File name:** `alarm-power-cut-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-power-cut-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A photograph of an alarm panel operating in low-light conditions — suggesting a power outage in the surrounding property. The alarm panel keypad display is clearly lit and active with status LEDs visible, while the background shows a darkened interior — lights off, suggesting mains power failure. The contrast between the active alarm panel and the dark background is the visual story: the alarm keeps working when the power goes out. No people. Atmospheric indoor lighting from the panel display itself. Professional editorial photography style. No brand logos.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — ELECTRICAL CABINET / MAINS ISOLATOR

**File name:** `alarm-power-cut-cabinet.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-power-cut-cabinet.webp`
**Insert location:** In `section1`, after the paragraph ending "...The attack vector that the Hollywood scenario imagines has been closed by three decades of security engineering." — actually place this in section1 after the opening two paragraphs, using this exact HTML:

```html
<img src="/images/insights/alarm-power-cut-cabinet.webp"
  alt="Electrical distribution board with circuit breakers — cutting mains power at the consumer unit does not disable a professionally installed alarm system"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a domestic electrical distribution board or consumer unit — the kind of panel with circuit breakers or MCBs that controls mains power to a Singapore property. The board is neatly installed, modern, with clearly labelled breaker switches. The image represents the Hollywood scenario — the burglar's imagined attack point. Clean, professional installation. No people, no hands. Neutral indoor lighting. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — BACKUP BATTERY IN ALARM PANEL

**File name:** `alarm-power-cut-battery.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-power-cut-battery.webp`
**Insert location:** In `section3`, after the paragraph ending "...The key point is that the backup window is measured in hours, not minutes, and that window is more than sufficient for the monitoring centre to identify the fault and respond.", using this exact HTML:

```html
<img src="/images/insights/alarm-power-cut-battery.webp"
  alt="Sealed lead-acid backup battery inside an open alarm panel — the built-in power backup that keeps the alarm running during a mains power failure"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a sealed lead-acid standby battery inside an open alarm panel enclosure. The battery is clearly visible — a standard rectangular unit in white or grey plastic with two terminal connectors. The alarm panel housing is open to show the battery in situ alongside the circuit board and wiring. The image shows the backup power component clearly as a designed-in feature of the panel. Clean, professional installation. No people, no hands. Soft even indoor lighting. Product installation photography style.

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
{ slug: "alarm-internet-cut",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-power-cut", title: "What Happens If a Burglar Cuts the Power?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-reliability","alarm-backup-power","singapore"], excerpt: "What happens if a burglar cuts the power to your property? Learn how alarm system batteries, monitoring centres and backup communications keep your alarm running during a power outage.", image: "alarm-power-cut-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-power-cut.html*
*Total images: 3 (1 feature + 2 body)*
