import os
import re

task_a_data = {
    "portfolio/condominiums/clearwater-access-salto-partnership.html": {
        "hero_path": "/images/portfolio/condominiums/the-clearwater-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/the-clearwater-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/the-clearwater-hero.webp"
    },
    "portfolio/condominiums/clearwater-cctv-upgrade.html": {
        "hero_path": "/images/portfolio/condominiums/the-clearwater-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/the-clearwater-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/the-clearwater-hero.webp"
    },
    "portfolio/condominiums/high-oak-condominium-cctv.html": {
        "hero_path": "/images/portfolio/condominiums/high-oak-condominium-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/high-oak-condominium-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/high-oak-condominium-hero.webp"
    },
    "portfolio/condominiums/hillview-park-cctv-upgrade.html": {
        "hero_path": "/images/portfolio/condominiums/hillview-park-condo-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/hillview-park-condo-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/hillview-park-condo-hero.webp"
    },
    "portfolio/condominiums/rezi-3two-condo.html": {
        "hero_path": "/images/portfolio/condominiums/rezi32-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/rezi32-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/rezi32-hero.webp"
    },
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html": {
        "hero_path": "/images/portfolio/condominiums/suites-cairnhill-hero.webp",
        "mobile_path": "/images/portfolio/condominiums/suites-cairnhill-mobile.webp",
        "og_image": "https://www.securevision.com.sg/images/portfolio/condominiums/suites-cairnhill-hero.webp"
    }
}

updated_count = 0
for rel_path, data in task_a_data.items():
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    if not os.path.exists(full_path):
        print(f"ERROR: {rel_path} does not exist!")
        continue
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Change 1: Add background-image to header tag
    # Find: <header class="portfolio-hero">
    old_header = '<header class="portfolio-hero">'
    new_header = f'<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'{data["hero_path"]}\');">'
    if old_header in content:
        content = content.replace(old_header, new_header)
        print(f"[{rel_path}] Header tag updated.")
    else:
        # Check if already has style
        if 'class="portfolio-hero"' in content and 'background-image' in content:
            print(f"[{rel_path}] Header tag already has background-image style.")
        else:
            print(f"[{rel_path}] WARNING: <header class=\"portfolio-hero\"> not found!")
            
    # Change 2: Add mobile @media override to <style> block in <head>
    mobile_block = f"""@media (max-width: 768px) {{
  .portfolio-hero {{
    background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{data["mobile_path"]}') !important;
  }}
}}"""
    
    # Let's check if @media (max-width: 768px) block for .portfolio-hero already exists
    # Or just if @media (max-width: 768px) exists in style block.
    # Let's see if style block exists:
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        if '.portfolio-hero' in style_content and 'max-width: 768px' in style_content:
            # Already exists, let's print a warning or handle replacement if needed.
            # But normally we can just replace it.
            print(f"[{rel_path}] Style override for mobile .portfolio-hero already exists in style block.")
        else:
            # We can insert it inside the existing <style> tag before </style>
            # Let's preserve indentation.
            indent_match = re.search(r'(\s*)</style>', content)
            indent = indent_match.group(1) if indent_match else "\n  "
            indented_block = "\n".join(indent + line for line in mobile_block.splitlines())
            content = content.replace('</style>', f"{indented_block}\n{indent}</style>")
            print(f"[{rel_path}] Mobile override added before </style>.")
    else:
        # No style block. Create one before </head>
        head_indent_match = re.search(r'(\s*)</head>', content)
        head_indent = head_indent_match.group(1) if head_indent_match else "\n  "
        new_style_block = f"{head_indent}<style>\n" + "\n".join(head_indent + "  " + line for line in mobile_block.splitlines()) + f"\n{head_indent}</style>"
        content = content.replace('</head>', f"{new_style_block}\n{head_indent}</head>")
        print(f"[{rel_path}] Style block created and mobile override added.")
        
    # Change 3: Fix og:image
    # If og:image already exists, replace it. Otherwise, insert it after og:site_name
    og_image_pattern = r'<meta property="og:image" content="[^"]*">'
    new_og_image = f'<meta property="og:image" content="{data["og_image"]}">'
    if re.search(og_image_pattern, content):
        content = re.sub(og_image_pattern, new_og_image, content)
        print(f"[{rel_path}] Existing og:image updated.")
    else:
        site_name_tag = '<meta property="og:site_name" content="Securevision">'
        if site_name_tag in content:
            # Get indentation of site_name_tag
            site_name_idx = content.find(site_name_tag)
            line_start = content.rfind("\n", 0, site_name_idx)
            indent = content[line_start+1:site_name_idx] if line_start != -1 else "  "
            content = content.replace(site_name_tag, f"{site_name_tag}\n{indent}{new_og_image}")
            print(f"[{rel_path}] og:image inserted after og:site_name.")
        else:
            print(f"[{rel_path}] WARNING: og:site_name tag not found, could not insert og:image.")
            
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    updated_count += 1

print(f"\nTask A complete: {updated_count} files modified.")
