# AG IMAGE BRIEF — alarm-communication-paths.html
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

**File name:** `alarm-communication-paths-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-communication-paths-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean editorial diagram-style illustration or photograph showing two distinct communication paths from a property to a monitoring centre. On the left side, a building or property. On the right side, a monitoring centre icon. Between them, two clearly distinct paths — one labelled or suggested as wired/broadband (fibre cable, router icon), the other as wireless/cellular (signal waves, mobile network icon). The two paths should look visually independent — different routes, different technology. Clean, professional infographic-style composition on a neutral background, or alternatively a photograph of an alarm panel with both a network cable port and a cellular antenna visible. No people. Modern, clean aesthetic.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — BANK SECURITY / HIGH-SECURITY INSTALLATION

**File name:** `alarm-communication-paths-bank.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-communication-paths-bank.webp`
**Insert location:** In `section2`, after the paragraph ending "...That principle — eliminate the single point of failure — shaped alarm communications for decades.", using this exact HTML:

```html
<img src="/images/insights/alarm-communication-paths-bank.webp"
  alt="Singapore bank branch exterior — high-security commercial properties were early adopters of redundant alarm communication paths"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean exterior photograph of a Singapore bank branch or financial institution building facade. The building is modern and professional — glass and concrete, signage visible but no specific bank name or logo that would identify a real institution. The image should convey security and institutional credibility. Daytime, natural Singapore urban lighting. Clean composition, no people in foreground. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — DUAL PATH ALARM PANEL / CELLULAR MODULE

**File name:** `alarm-communication-paths-dual-path.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-communication-paths-dual-path.webp`
**Insert location:** In `section7`, after the paragraph ending "...The principle has not changed at all.", using this exact HTML:

```html
<img src="/images/insights/alarm-communication-paths-dual-path.webp"
  alt="Modern alarm panel with dual communication module showing both Ethernet network port and cellular 4G antenna — IP primary and mobile backup"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a modern alarm panel or communications module showing both a wired network connection (Ethernet port with cable connected) and a cellular communication component (small antenna or SIM card slot visible). The two communication technologies should be visibly distinct on the same unit. Clean white or grey housing, professional installation quality. Mounted on a wall or photographed on a neutral surface. No brand logos. Soft even lighting. No people. Product installation photography style.

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
{ slug: "alarm-panel-polling",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-communication-paths", title: "Why Banks Use Multiple Communication Paths", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","communication-paths","singapore"], excerpt: "Why do banks use multiple communication paths for alarm monitoring? Learn how leased lines, PSTN, IP networks and mobile data work together to eliminate single points of failure and improve alarm reliability.", image: "alarm-communication-paths-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-communication-paths.html*
*Total images: 3 (1 feature + 2 body)*
