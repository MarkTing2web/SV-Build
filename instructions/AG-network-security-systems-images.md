# AG IMAGE BRIEF — network-security-systems.html
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

**File name:** `network-security-systems-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/network-security-systems-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A clean professional photograph of a network switch cabinet or small server rack installed in a Singapore commercial or residential security installation. The cabinet contains a managed network switch with port LEDs visible, patch cables neatly organised in multiple colours, a PoE injector or PoE switch visible, and possibly a small UPS at the bottom. The cabinet is mounted on a wall or in a rack enclosure. The image represents the network infrastructure that modern security systems depend on. Clean, professional installation with good cable management. Soft even lighting — LED port indicators visible. No people. No brand logos. Professional installation photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — MANAGED SWITCH PORT DETAIL

**File name:** `network-security-systems-switch.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/network-security-systems-switch.webp`
**Insert location:** In `section4`, after the paragraph ending "...For a customer whose security cameras are their only source of overnight footage, the difference between restoring the system in five minutes and restoring it after a two-hour site visit matters.", using this exact HTML:

```html
<img src="/images/insights/network-security-systems-switch.webp"
  alt="Managed network switch with active port LEDs and patch cables — the port-level visibility that makes security network fault diagnosis fast and accurate"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of the front panel of a managed network switch showing multiple active ports with green LED indicators, patch cables connected to various ports, and a clear view of the port status lights. The image conveys the idea of port-level visibility — individual connections, each with its own status indicator. Clean professional installation. Slight overhead or angled composition showing the port array clearly. Soft even lighting so the LEDs are clearly visible. No brand logos. No people. Product installation photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — NETWORK MANAGEMENT INTERFACE ON SCREEN

**File name:** `network-security-systems-remote.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/network-security-systems-remote.webp`
**Insert location:** In `section5`, after the paragraph ending "...The alternative — arriving at a site with no diagnostic information and working through the system methodically — takes significantly longer and generates a support cost that is largely avoidable with the right infrastructure in place.", using this exact HTML:

```html
<img src="/images/insights/network-security-systems-remote.webp"
  alt="Network management dashboard on a laptop screen showing device status, port activity and bandwidth usage — remote diagnostics for a security system network"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of a laptop or monitor screen displaying a network management dashboard interface. The screen shows a device topology or port status view with green and orange indicators suggesting some devices online and one showing a fault condition. Bandwidth graphs or port utilisation charts visible. The interface is clean and modern, clearly a professional network management platform. No specific real software brand visible. Screen slightly angled on a desk. Soft ambient office lighting. No people, no hands. Professional editorial photography style.

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
{ slug: "installer-leaves",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "network-security-systems", title: "The Cameras Were Fine. The Network Was the Problem.", category: "Security Planning", tags: ["security-network","cctv-infrastructure","security-planning","singapore"], excerpt: "Why do security cameras go offline when the hardware is fine? Learn why the network is the most neglected part of a security system, why managed switches matter, and how remote diagnostics reduce downtime.", image: "network-security-systems-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: network-security-systems.html*
*Total images: 3 (1 feature + 2 body)*
