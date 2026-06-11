# AG IMAGE BRIEF — break-in-nearby-security-review.html
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

**File name:** `break-in-nearby-security-review-feature.webp`
**Size:** 640 × 360px (16:9)
**Storage path:** `/images/insights/break-in-nearby-security-review-feature.webp`
**Insert location:** Already in the HTML at `section1`. No insertion needed — just save the file.

**Generation prompt:**
A photograph of a security professional reviewing camera coverage at the rear of a Singapore landed property. The professional is Asian male, middle-aged, wearing smart casual clothing, standing in a backyard garden area looking up at a wall or fence line where a camera would be mounted. He has a tablet or clipboard. The backyard is a typical Singapore landed property rear garden — some planting, a rear fence or wall, Singapore tropical vegetation visible. Natural daylight. The composition suggests a professional assessment in progress — someone looking at the property critically and methodically. No Securevision branding or uniform. Documentary photography style.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 2 — UNPROTECTED REAR BOUNDARY / BACKYARD

**File name:** `break-in-nearby-security-review-backyard.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/break-in-nearby-security-review-backyard.webp`
**Insert location:** In `section2`, after the paragraph ending "...and only a site survey made the second one visible.", using this exact HTML:

```html
<img src="/images/insights/break-in-nearby-security-review-backyard.webp"
  alt="Singapore landed property rear garden and boundary fence — typical of properties where camera coverage focuses on the front and leaves the rear unprotected"
  class="article-img-float-right" />
```

**Generation prompt:**
A photograph of the rear garden and boundary area of a Singapore landed property. The garden is a typical Singapore residential backyard — some mature tropical planting, a rear concrete or brick boundary wall or fence, a gate or gap visible at the back. The image should convey a space that is functional but unmonitored — no camera visible, no lighting fixtures at the boundary, the kind of rear area that receives less security attention than the front of the property. Natural daylight, slightly late afternoon. No people. Documentary photography style — this should look like a genuine property condition, not a staged image.

**STOP. Show Wee Meng this image before proceeding.**

---

## IMAGE 3 — AI CAMERA WITH FLOODLIGHT

**File name:** `break-in-nearby-security-review-ai-camera.webp`
**Size:** 320 × 240px (4:3)
**Storage path:** `/images/insights/break-in-nearby-security-review-ai-camera.webp`
**Insert location:** In `section4`, after the paragraph ending "...The notification with visual confirmation is significantly more useful than a notification alone.", using this exact HTML:

```html
<img src="/images/insights/break-in-nearby-security-review-ai-camera.webp"
  alt="AI camera with integrated floodlight installed at a Singapore property rear boundary — the see it, light it, alert it solution"
  class="article-img-float-right" />
```

**Generation prompt:**
A close-up photograph of an AI security camera with an integrated or adjacent LED floodlight, mounted on a wall or post at a Singapore property boundary. The camera is a modern compact unit with a visible lens array. The floodlight is a separate or integrated LED unit capable of strong illumination. The combination represents the detection-plus-lighting solution described in the article. Clean, professional installation on a rendered wall or post. Natural outdoor daylight lighting — not a nighttime shot. No people. No brand logos. Professional installation photography style.

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
{ slug: "security-assessment-10-things",
```

Insert a new entry immediately BEFORE that line:

```js
{ slug: "break-in-nearby-security-review", title: "A Break-In Nearby Prompted This Security Review", category: "Security Planning", tags: ["security-review","case-study","security-planning","singapore"], excerpt: "A break-in near an Upper Thomson landed property prompted a homeowner to review their security system. Learn what we found during the site survey and why security systems should evolve as risks and technology change.", image: "break-in-nearby-security-review-feature.webp" },
```

Confirm the insertion to Wee Meng before closing.

---

*Brief version 1.0 — June 2026*
*Article: break-in-nearby-security-review.html*
*Total images: 3 (1 feature + 2 body)*
