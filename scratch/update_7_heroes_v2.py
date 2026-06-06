import os

workspace = r"c:\Projects\SV-Build"

def inject_style(html_path, style_str):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already injected this specific background-image
    if "background-image: url" in style_str:
        # Extract the url from style_str to check if it's already in the file
        import re
        match = re.search(r"background-image:\s*url\('([^']+)'\)", style_str)
        if match and match.group(1) in content:
            print(f"Skipping {html_path} - already injected.")
            return

    if "</style>" in content:
        content = content.replace("</style>", style_str + "\n</style>")
    else:
        content = content.replace("</head>", "<style>\n" + style_str + "\n</style>\n</head>")
        
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected into {html_path}")

# File 1
mobile = f"/images/portfolio/healthcare/surya-home-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/healthcare/surya-home-mobile.webp")):
    mobile = f"/images/portfolio/healthcare/surya-home-mobile.webp"

style = f"""  :root {{ --page-accent: #319795; }}
  .portfolio-hero {{ background-image: url('/images/portfolio/healthcare/surya-home-hero.webp'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
inject_style(os.path.join(workspace, "portfolio/healthcare/surya-home.html"), style)


# File 2
mobile = f"/images/portfolio/industrial/sta-compliance-imaging-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/industrial/sta-compliance-imaging-mobile.webp")):
    mobile = f"/images/portfolio/industrial/sta-compliance-imaging-mobile.webp"

style = f"""  :root {{ --page-accent: #744210; }}
  .portfolio-hero {{ background-image: url('/images/portfolio/industrial/sta-compliance-imaging-hero.webp'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
inject_style(os.path.join(workspace, "portfolio/industrial/sta-compliance-imaging.html"), style)


# File 3
mobile = f"/images/portfolio/institutions/sengkang-interim-bus-interchange-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/institutions/sengkang-interim-bus-interchange-mobile.webp")):
    mobile = f"/images/portfolio/institutions/sengkang-interim-bus-interchange-mobile.webp"

style = f"""  :root {{ --page-accent: #1a56a0; }}
  .portfolio-hero {{ background-image: url('/images/portfolio/institutions/sengkang-interim-bus-interchange-hero.webp'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
inject_style(os.path.join(workspace, "portfolio/institutions/sengkang-interim-bus-interchange.html"), style)


# File 4
mobile = f"/images/portfolio/managed-living/scb-worker-dormitory-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/managed-living/scb-worker-dormitory-mobile.webp")):
    mobile = f"/images/portfolio/managed-living/scb-worker-dormitory-mobile.webp"

style = f"""  :root {{ --page-accent: #276749; }}
  .portfolio-hero {{ background-image: url('/images/portfolio/managed-living/scb-worker-dormitory-hero.webp'); }}
  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
inject_style(os.path.join(workspace, "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"), style)


# File 5
p = os.path.join(workspace, "portfolio/data-centres/fort-st-engineering.html")
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
if "fort-st-engineering-rel.webp" in c:
    c = c.replace("url('/images/portfolio/data-centres/fort-st-engineering-rel.webp')", "url('/images/portfolio/data-centres/fort-st-engineering-hero.webp')")
mobile = "/images/portfolio/data-centres/fort-st-engineering-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/data-centres/fort-st-engineering-mobile.webp")):
    mobile = "/images/portfolio/data-centres/fort-st-engineering-mobile.webp"
if "fort-st-engineering-mobile.webp" not in c and "background-position: center" not in c.split(".portfolio-hero")[1:]:
    mobile_style = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
    c = c.replace("</style>", mobile_style + "\n</style>")
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print(f"Processed {p}")

# File 6
p = os.path.join(workspace, "portfolio/commercial/scape-commercial.html")
mobile = "/images/portfolio/commercial/scape-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/commercial/scape-mobile.webp")):
    mobile = "/images/portfolio/commercial/scape-mobile.webp"
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
if "scape-mobile.webp" not in c and "background-position: center" not in c:
    mobile_style = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
    c = c.replace("</style>", mobile_style + "\n</style>")
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print(f"Processed {p}")

# File 7
p = os.path.join(workspace, "portfolio/commercial/scape-smart-booking-access.html")
mobile = "/images/portfolio/commercial/scape-hero.webp"
if os.path.exists(os.path.join(workspace, "images/portfolio/commercial/scape-mobile.webp")):
    mobile = "/images/portfolio/commercial/scape-mobile.webp"
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()
if "scape-mobile.webp" not in c and "background-position: center" not in c:
    mobile_style = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{ background-image: url('{mobile}'); background-position: center; }}
  }}"""
    c = c.replace("</style>", mobile_style + "\n</style>")
with open(p, 'w', encoding='utf-8') as f:
    f.write(c)
print(f"Processed {p}")
