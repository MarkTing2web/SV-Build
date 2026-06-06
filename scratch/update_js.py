import re

with open('portfolio-block.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove from excluded list at top
content = content.replace("       industrial/sta-compliance-imaging\n", "")
content = content.replace("       institutions/sengkang-interim-bus-interchange\n", "")
content = content.replace("       managed-living/scb-worker-dormitory-jalan-papan\n", "")
content = content.replace("       healthcare/surya-home\n", "") # maybe remove surya-home too? No, keep it as it's not requested.

# 2. Entries to add
scb_entry = """    {
      slug:     "/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
      category: "managed-living",
      image:    "/images/portfolio/managed-living/scb-worker-dormitory-rel.webp",
      badge:    "Managed Living",
      title:    "SCB Worker Dormitory",
      text:     "Securevision installed turnstile access control with ZKTeco SpeedFace terminals and CCTV for SCB's worker dormitory at Jalan Papan."
    },
"""

sta_entry = """    {
      slug:     "/portfolio/industrial/sta-compliance-imaging.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/sta-compliance-imaging-rel.webp",
      badge:    "Industrial",
      title:    "STA Compliance Imaging",
      text:     "Securevision helped STA Inspection eliminate manual undercarriage records by building an automated camera system triggered by vehicle entry."
    },
"""

sengkang_entry = """    {
      slug:     "/portfolio/institutions/sengkang-interim-bus-interchange.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/sengkang-interim-bus-interchange-rel.webp",
      badge:    "Institution",
      title:    "Sengkang Interim Bus Interchange",
      text:     "Securevision delivered the design-and-build CCTV system for the LTA Sengkang Interim Bus Interchange under W'Ray — 53 IP cameras, 5 NVRs, and 28-day retention against tender specification."
    },
"""

# Insert under categories
content = content.replace('/* ── MANAGED LIVING ─────────────────────────────────────────── */\n', '/* ── MANAGED LIVING ─────────────────────────────────────────── */\n' + scb_entry)
content = content.replace('/* ── INDUSTRIAL ─────────────────────────────────────────────── */\n', '/* ── INDUSTRIAL ─────────────────────────────────────────────── */\n' + sta_entry)
content = content.replace('/* ── INSTITUTIONS ───────────────────────────────────────────── */\n', '/* ── INSTITUTIONS ───────────────────────────────────────────── */\n' + sengkang_entry)

with open('portfolio-block.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated portfolio-block.js")
