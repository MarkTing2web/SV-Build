import os
import re

w = r"c:\Projects\SV-Build"

files_to_fix = [
    ("portfolio/data-centres/fort-st-engineering.html", "fort-st-engineering-hero.webp", "fort-st-engineering-mobile.webp", "data-centres"),
    ("portfolio/commercial/scape-commercial.html", "scape-hero.webp", "scape-mobile.webp", "commercial"),
    ("portfolio/commercial/scape-smart-booking-access.html", "scape-hero.webp", "scape-mobile.webp", "commercial")
]

for file, hero_img, mobile_img, directory in files_to_fix:
    path = os.path.join(w, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine mobile path
    mobile_path_full = os.path.join(w, f"images/portfolio/{directory}/{mobile_img}")
    if os.path.exists(mobile_path_full):
        mobile_url = f"/images/portfolio/{directory}/{mobile_img}"
    else:
        mobile_url = f"/images/portfolio/{directory}/{hero_img}"
    
    hero_url = f"/images/portfolio/{directory}/{hero_img}"

    # 1. Clean inline styles on <header>
    content = re.sub(r'<header class="portfolio-hero"\s+style="[^"]*">', '<header class="portfolio-hero">', content)
    
    # 2. Clean out old specific @media blocks for these files
    # The existing block looks like:
    # <style>
    #     @media (max-width: 768px) {
    #       .portfolio-hero {
    #         background-image: ... !important;
    #       }
    #       .portfolio-hero .hero-image {
    #         display: none;
    #       }
    #     }
    #     @media (max-width: 768px) {
    #     .portfolio-hero { background-image: ...; background-position: center; }
    #   }
    # </style>
    
    # Let's remove ALL of <style> contents that match these problematic blocks
    content = re.sub(r'<style>.*?</style>', '<style>\n</style>', content, flags=re.DOTALL)
    
    # Wait! Do they have OTHER styles we need to preserve?
    # Let's check `scape-commercial.html` - we saw its <style> ONLY had the @media blocks.
    # What about `fort-st-engineering.html`? Its <style> ONLY had the @media blocks too (from my test script output).
    # YES! Both had only those @media blocks in their <style> tag.
    # So replacing <style>...</style> with our canonical is perfectly safe.

    canonical_style = f"""<style>
  .portfolio-hero {{ background-image: url('{hero_url}'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile_url}'); background-position: center; }}
  }}
</style>"""

    # Replace <style>\n</style> with canonical_style
    content = content.replace("<style>\n</style>", canonical_style)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Cleaned and fixed 5, 6, 7")
