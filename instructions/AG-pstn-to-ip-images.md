# AG IMAGE BRIEF — pstn-to-ip.html
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

**File name:** `pstn-to-ip-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/pstn-to-ip-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean product photograph of a modern alarm panel showing both a legacy telephone line port (RJ11 socket) and a modern Ethernet port (RJ45) alongside a cellular antenna connector or SIM card slot. The three connection types visible on the same unit represent the transition from PSTN to IP monitoring. The panel is white or light grey, clean professional housing, mounted on a wall or photographed on a neutral surface. Sharp focus on the connection ports, slightly blurred background. No brand logos. Soft even lighting. No people. Product installation photography style suggesting technology transition.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — COPPER TELEPHONE INFRASTRUCTURE BEING RETIRED

**File name:** `pstn-to-ip-copper-retirement.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/pstn-to-ip-copper-retirement.webp`
**Insert location:** In `section2`, after the paragraph ending "...It responded to it. And in responding, it made a transition that turned out to produce a significantly better monitoring capability than PSTN had ever offered.", using this exact HTML:

```html
<img src="/images/insights/pstn-to-ip-copper-retirement.webp"
  alt="Old copper telephone cables alongside modern fibre optic cables — representing the telecommunications infrastructure transition that forced alarm systems to move from PSTN to IP"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph showing the contrast between old copper telephone cables and modern fibre optic cables side by side — either in a cable tray, a telecommunications cabinet, or at a junction point. The copper cables should look aged and dated; the fibre cables should look clean and modern. The image represents the infrastructure transition from legacy copper telephone networks to modern fibre connectivity. Clean, professional telecommunications infrastructure setting. No people. Neutral lighting. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — MODERN IP ALARM MONITORING PLATFORM

**File name:** `pstn-to-ip-modern-platform.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/pstn-to-ip-modern-platform.webp`
**Insert location:** In `section5`, after the paragraph ending "...The telephone line is either a footnote or absent entirely.", using this exact HTML:

```html
<img src="/images/insights/pstn-to-ip-modern-platform.webp"
  alt="Modern IP-based alarm panel with cloud connectivity and mobile app integration — the current generation designed around IP from the ground up"
  class="article-img-float-right" />
```

**Generation prompt:**
A clean product photograph of a modern IP-based alarm panel — compact, slim, contemporary white housing, clearly a current-generation product. Alongside it or on the screen behind it, a smartphone displaying an alarm management app with status indicators, zone information and remote arming controls. The composition should suggest the integration of the alarm panel with mobile and cloud connectivity. No brand logos visible on either device. Clean neutral background or wall-mounted installation setting. Soft even lighting. No people. Premium product photography style.

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
{ slug: "alarm-communication-paths",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "pstn-to-ip", title: "From PSTN to IP Monitoring", category: "Alarm & Intrusion", tags: ["burglar-alarm","alarm-monitoring","ip-monitoring","singapore"], excerpt: "How did alarm monitoring evolve from telephone lines to always-on IP connectivity? Learn why PSTN networks are being retired and what modern IP monitoring means for alarm reliability in Singapore.", image: "pstn-to-ip-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: pstn-to-ip.html*
*Total images: 3 (1 feature + 2 body)*
