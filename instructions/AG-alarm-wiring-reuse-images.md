# AG IMAGE BRIEF — alarm-wiring-reuse.html
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

**File name:** `alarm-wiring-reuse-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-wiring-reuse-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean close-up photograph of alarm system wiring and cable terminations inside or around an alarm panel. Neat runs of alarm cables — typically thin multi-core cables in white or grey — terminating at zone input terminals on an alarm panel circuit board or terminal block. The wiring is tidy and professional, suggesting a well-installed system. The panel cover is partially open or removed to show the cable terminations. No people, no hands. Soft even lighting. Professional installation photography style. The image should convey the message that this wiring infrastructure has longevity and reuse value.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — CABLE CONTINUITY TESTING

**File name:** `alarm-wiring-reuse-cable-test.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-wiring-reuse-cable-test.webp`
**Insert location:** In `section7`, after the paragraph ending "...A circuit that tests cleanly can be reused with confidence. One that shows faults needs to be investigated before committing to a panel connection.", using this exact HTML:

```html
<img src="/images/insights/alarm-wiring-reuse-cable-test.webp"
  alt="Technician using a multimeter to test alarm cable continuity during a system upgrade assessment"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a digital multimeter being used to test electrical continuity on alarm cables. The multimeter probes are connected to bare wire ends or terminal connections. The meter display shows a continuity reading. The cables being tested are typical alarm detection cables — thin, multi-core, white or grey. The image suggests a professional site assessment process — testing before deciding. Hands visible holding the probes are acceptable in this case as they are essential to the composition. Soft even workshop or property interior lighting. Professional technical photography style. No faces visible.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — OLD VS NEW ALARM PANEL SIDE BY SIDE

**File name:** `alarm-wiring-reuse-panel-upgrade.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-wiring-reuse-panel-upgrade.webp`
**Insert location:** In `section6`, after the paragraph ending "...Replacing the communicator with an IP and cellular module is not an optional upgrade — it is eventually a necessity for any property that wants to remain on professional monitoring.", using this exact HTML:

```html
<img src="/images/insights/alarm-wiring-reuse-panel-upgrade.webp"
  alt="Old alarm panel alongside a new modern replacement — the panel and communicator are typically what gets replaced during an alarm upgrade while existing cables are retained"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph showing an older alarm panel and a new modern alarm panel side by side — or an older panel being removed from a wall with a new panel ready to replace it. The older panel should look visibly dated — larger housing, older display, simpler design from the 1990s or early 2000s. The new panel should look current — compact, clean lines, modern keypad or touchscreen interface. The image represents the upgrade process where the panel is replaced while cables behind the wall are retained. No people. Professional installation photography style. Clean interior wall background. Neutral lighting.

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
{ slug: "self-monitoring-vs-cms",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-wiring-reuse", title: "Can I Reuse My Existing Alarm Wiring?", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-upgrade","alarm-wiring","singapore"], excerpt: "Can you reuse existing alarm wiring when upgrading a burglar alarm system? Learn when cables and detectors can be retained, what usually needs replacing and how homeowners can reduce costs during an alarm upgrade.", image: "alarm-wiring-reuse-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-wiring-reuse.html*
*Total images: 3 (1 feature + 2 body)*
