# AG IMAGE BRIEF — alarm-internet-cut.html
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

**File name:** `alarm-internet-cut-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-internet-cut-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean close-up photograph of an alarm panel keypad showing active status indicators — armed LEDs lit, zone indicators visible, display showing system active. The composition suggests the alarm is running and operational. In the soft background, slightly out of focus, a router or network switch with no link lights — suggesting the internet connection is down. The alarm panel in the foreground remains clearly active and operational. The contrast between the active alarm and the inactive router is the story of the image. No people. Soft interior lighting. Professional installation photography style. No brand logos.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — EXTERNAL SIREN ACTIVE / STROBE FLASHING

**File name:** `alarm-internet-cut-siren.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-internet-cut-siren.webp`
**Insert location:** In `section3`, after the paragraph ending "...The alarm may not be able to reach the monitoring centre through the broadband route — but the burglar now faces a different and more immediate problem: a loud alarm that everyone nearby can hear.", using this exact HTML:

```html
<img src="/images/insights/alarm-internet-cut-siren.webp"
  alt="External alarm siren with strobe light active on a Singapore property — the local deterrent that operates independently of internet connectivity"
  class="article-img-float-right" />
```

**Generation prompt:**
A nighttime or low-light photograph of an external alarm siren unit with its strobe light actively flashing — blue-white flash illuminating the surrounding wall and Singapore residential or commercial building facade. The siren housing is visible, the strobe flash is the dominant visual element. The image should convey immediate, loud, visible alarm activation — the local deterrent function that operates regardless of internet connectivity. No people. Atmospheric lighting from the strobe flash itself. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — DUAL PATH / CELLULAR BACKUP ACTIVE

**File name:** `alarm-internet-cut-cellular.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-internet-cut-cellular.webp`
**Insert location:** In `section6`, after the paragraph ending "...That alert is itself a signal worth investigating.", using this exact HTML:

```html
<img src="/images/insights/alarm-internet-cut-cellular.webp"
  alt="Alarm panel showing cellular backup communication active — the 4G backup path that routes alarm signals when broadband is unavailable"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of an alarm panel or communicator module with a cellular antenna or SIM card slot visible alongside an Ethernet port. The Ethernet port has no cable connected — suggesting the primary broadband path is down — while a cellular signal indicator or LED remains active. The composition represents the backup communication path taking over. Clean white or grey panel housing, mounted on a wall or photographed on a neutral surface. No brand logos. Soft even lighting. No people. Product installation photography style.

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
{ slug: "cctv-vs-alarm",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-internet-cut", title: "What Happens If a Burglar Cuts the Internet?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-reliability","communication-paths","singapore"], excerpt: "What happens if a burglar cuts your internet connection? Learn how modern alarm systems continue operating without internet access, why sirens remain effective, and how dual-path communications provide additional protection.", image: "alarm-internet-cut-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-internet-cut.html*
*Total images: 3 (1 feature + 2 body)*
