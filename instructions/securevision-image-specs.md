# Securevision Visual Asset Specification & Generation Guide

This document outlines the technical requirements and generation instructions for the Securevision website revamp. These specifications are optimized for **Vibe Coding** on **Vercel**, prioritizing high-speed performance via **WebP** and precise compositional control for left-aligned UI elements.

---

## 1. Core Image Specifications

All assets must be exported or generated in **WebP** format to maximize Core Web Vitals and SEO rankings.

| Asset Category | Target Resolution | Aspect Ratio | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **Desktop Hero** | 1920 × 1080 px | 16:9 | High-impact page headers |
| **Mobile Hero** | 1080 × 1920 px | 9:16 | Vertical-first mobile headers |
| **Solution Cards** | 800 × 800 px | 1:1 (Square) | Grid navigation (index.html) |
| **Portfolio / Case Study** | 1200 × 800 px | 3:2 | Project showcases |

---

## 2. Compositional & UI Safety Rules

To ensure text readability and UI integrity, follow these spatial rules:

### Hero Images (Desktop & Mobile)
* **The Right-Weighted Rule:** The focal subject (person, hardware, interaction) must be contained within the **right 40%** of the frame.
* **Negative Space:** The left 60% must be clean architectural space or a smooth, out-of-focus background. This is "Safe Space" for left-aligned H1 headers and Blue CTAs.
* **Contrast:** Ensure high tonal contrast between the background and white text.

### Card Images (1:1 Square)
* **The Macro Rule:** Focus on tight crops of hardware (biometric readers, cameras, LPR sensors) or close-up interactions (hand touching a screen).
* **Centering:** Subjects should be center-weighted. No safe space for text is required as text will live below the image.

---

## 3. Anti-Gravity Instruction Suite (The Prompt)

Use this structured instruction when generating new assets to ensure three consistent versions of the same visual concept:

**System Instruction:** Generate a 3-part professional visual suite for Securevision. Final output must be optimized for **WebP**.

**Subject Matter:** [INSERT SUBJECT, e.g., A professional woman interacting with a minimalist biometric reader in a modern Singapore office lobby.]

**Visual Style:** Cinematic, architectural photography, neutral tones with "Securevision Blue" (#0056b3) accents. High clarity, professional lighting.

**Required Versions:**
1.  **Version A: Wide Hero (16:9)** - 1920 x 1080 px. The subject must be on the **far right**. The left side must be architectural negative space for text overlays.
2.  **Version B: Macro Card (1:1)** - 800 x 800 px. A sharp, centered close-up of the security hardware/interaction.
3.  **Version C: Mobile Hero (9:16)** - 1080 x 1920 px. The subject must be centered vertically to ensure visibility on narrow screens.

---

## 4. Vercel & Vibe Coding Implementation

* **Responsive Heroes:** Use the `9:16` asset for mobile breakpoints to prevent awkward cropping of horizontal images.
* **Alt Text Strategy:**
    * *Hero Alt Text:* Describe the environment and integrated nature (e.g., "Integrated facial recognition entry system in a corporate Singapore lobby").
    * *Card Alt Text:* Describe the specific hardware/action (e.g., "Macro shot of a contactless biometric access control reader").
* **Performance:** Leverage Vercel’s Image Optimization. Ensure `loading="lazy"` is applied to all **Solution Cards**, but keep the **Hero Image** as `loading="eager"` or `priority` for better Largest Contentful Paint (LCP).
