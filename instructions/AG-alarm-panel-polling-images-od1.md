# AG IMAGE BRIEF — alarm-panel-polling.html
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

**File name:** `alarm-panel-polling-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/alarm-panel-polling-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A monitoring centre operator workstation with a screen showing an alarm account management interface. The screen displays a list of accounts with status indicators — some showing "OK", one showing a flag or warning status suggesting a missed test signal. The screen is the focal point, slightly angled, soft ambient workstation lighting. The overall composition suggests the monitoring task of checking communication health across many accounts. No faces visible — operator chair visible but not occupied, or shot from an angle that avoids any face. Clean professional environment. No brand names on screen. Editorial photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — TELEPHONE INFRASTRUCTURE / INCOMING LINES

**File name:** `alarm-panel-polling-telephone-lines.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-panel-polling-telephone-lines.webp`
**Insert location:** In `section3`, after the paragraph ending "...without placing excessive demand on the telephone capacity.", using this exact HTML:

```html
<img src="/images/insights/alarm-panel-polling-telephone-lines.webp"
  alt="Telephone patch panel or distribution frame in a communications room — representing the physical telephone infrastructure that monitoring centres had to manage"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of a telephone patch panel, distribution frame, or punch-down block — the kind of physical telephone line termination infrastructure found in a communications room or server room from the 1990s to 2000s. Dense rows of telephone line connections, cable management, patch cables. The image should convey the scale and physical reality of managing many telephone lines. Clean, functional, slightly dated in character. No people. Neutral lighting. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — IP MONITORING / MODERN NETWORK EQUIPMENT

**File name:** `alarm-panel-polling-ip-monitoring.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/alarm-panel-polling-ip-monitoring.webp`
**Insert location:** In `section6`, after the paragraph ending "...What did not change was the underlying principle.", using this exact HTML:

```html
<img src="/images/insights/alarm-panel-polling-ip-monitoring.webp"
  alt="Modern network switch and alarm panel with IP connectivity — representing the transition from telephone line to IP-based alarm monitoring"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean photograph of a modern network switch or router alongside an alarm panel or communications module — representing the IP connectivity that replaced telephone line monitoring. The equipment is current-generation: compact, clean lines, LED status indicators visible. Mounted in a comms cabinet or on a wall rack with neat cable management. Professional installation photography style. No brand logos visible. Soft even lighting. No people.

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
{ slug: "alarm-monitoring-history",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "alarm-panel-polling", title: "Why Alarm Panels Used to Call Home Every Seven Days", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","security-history","singapore"], excerpt: "Why did alarm panels send test signals every seven days? Discover the hidden engineering behind telephone-line alarm monitoring and how monitoring centres managed tens of thousands of accounts before the internet era.", image: "alarm-panel-polling-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: alarm-panel-polling.html*
*Total images: 3 (1 feature + 2 body)*
