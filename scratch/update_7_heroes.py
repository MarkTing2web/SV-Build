import os
import re

workspace = r"c:\Projects\SV-Build"

tasks = [
    {
        "file": "portfolio/healthcare/surya-home.html",
        "action": "add",
        "accent": "#319795",
        "hero_img": "surya-home-hero.webp",
        "mobile_img": "surya-home-mobile.webp",
        "dir": "healthcare"
    },
    {
        "file": "portfolio/industrial/sta-compliance-imaging.html",
        "action": "add",
        "accent": "#744210",
        "hero_img": "sta-compliance-imaging-hero.webp",
        "mobile_img": "sta-compliance-imaging-mobile.webp",
        "dir": "industrial"
    },
    {
        "file": "portfolio/institutions/sengkang-interim-bus-interchange.html",
        "action": "add",
        "accent": "#1a56a0",
        "hero_img": "sengkang-interim-bus-interchange-hero.webp",
        "mobile_img": "sengkang-interim-bus-interchange-mobile.webp",
        "dir": "institutions"
    },
    {
        "file": "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
        "action": "add",
        "accent": "#276749",
        "hero_img": "scb-worker-dormitory-hero.webp",
        "mobile_img": "scb-worker-dormitory-mobile.webp",
        "dir": "managed-living"
    },
    {
        "file": "portfolio/data-centres/fort-st-engineering.html",
        "action": "replace",
        "find_img": "fort-st-engineering-rel.webp",
        "hero_img": "fort-st-engineering-hero.webp",
        "mobile_img": "fort-st-engineering-mobile.webp",
        "dir": "data-centres"
    },
    {
        "file": "portfolio/commercial/scape-commercial.html",
        "action": "add_mobile",
        "hero_img": "scape-hero.webp",
        "mobile_img": "scape-mobile.webp",
        "dir": "commercial"
    },
    {
        "file": "portfolio/commercial/scape-smart-booking-access.html",
        "action": "add_mobile",
        "hero_img": "scape-hero.webp",
        "mobile_img": "scape-mobile.webp",
        "dir": "commercial"
    }
]

for t in tasks:
    html_path = os.path.join(workspace, t["file"])
    mobile_path = os.path.join(workspace, f"images/portfolio/{t['dir']}/{t['mobile_img']}")
    hero_path = f"/images/portfolio/{t['dir']}/{t['hero_img']}"
    
    if os.path.exists(mobile_path):
        mobile_bg = f"/images/portfolio/{t['dir']}/{t['mobile_img']}"
    else:
        mobile_bg = hero_path
        
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if t["action"] == "add":
        new_style = f"""  :root {{ --page-accent: {t['accent']}; }}
  .portfolio-hero {{ background-image: url('{hero_path}'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile_bg}'); background-position: center; }}
  }}"""
        
        if ".portfolio-hero" not in content:
            if ":root { --page-accent" in content:
                content = re.sub(r':root\s*\{\s*--page-accent:\s*#[0-9a-fA-F]+;\s*\}', new_style, content)
            else:
                content = content.replace("<style>", "<style>\n" + new_style)
        else:
            print(f"Skipping {t['file']} (already has .portfolio-hero)")
            
    elif t["action"] == "replace":
        old_bg = f"/images/portfolio/{t['dir']}/{t['find_img']}"
        content = content.replace(old_bg, hero_path)
        
        if "@media (max-width: 768px)" not in content or ".portfolio-hero" not in content.split("@media (max-width: 768px)")[1]:
            mobile_override = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile_bg}'); background-position: center; }}
  }}
"""
            content = content.replace("</style>", mobile_override + "</style>")

    elif t["action"] == "add_mobile":
        if "@media (max-width: 768px)" not in content or ".portfolio-hero" not in content.split("@media (max-width: 768px)")[1]:
            mobile_override = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile_bg}'); background-position: center; }}
  }}
"""
            content = content.replace("</style>", mobile_override + "</style>")
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {t['file']}")
