import os
import re

files_list = [
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/data-centres/fort-st-engineering.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
results = []

for rel_path in files_list:
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {rel_path}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    filename = os.path.basename(rel_path)
    slug = filename.replace('.html', '')
    expected_class = f"hero-{slug}"
    
    # 1. Replace header tag & Remove inline style
    header_match = re.search(r'<header[^>]*class="[^"]*portfolio-hero[^"]*"[^>]*>', content)
    if header_match:
        header_tag = header_match.group(0)
        new_header_tag = f'<header class="hero hero-compact hero-high-impact {expected_class}">'
        content = content.replace(header_tag, new_header_tag)
    else:
        print(f"Warning: No portfolio-hero header found in {rel_path}")

    # 2. Update style block
    style_blocks = re.findall(r'<style[^>]*>.*?</style>', content, re.DOTALL)
    style_selector = "Unknown"
    has_accent = False
    
    if style_blocks:
        block = style_blocks[0]
        new_block = block
        
        # Check and replace .portfolio-hero with .hero-[SLUG]
        if ".portfolio-hero" in new_block:
            new_block = new_block.replace(".portfolio-hero", f".{expected_class}")
            style_selector = f".{expected_class}"
        elif f".{expected_class}" in new_block:
            style_selector = f".{expected_class}"
            
        # Check for --page-accent
        if ":root{--page-accent:" in new_block.replace(" ", ""):
            has_accent = True
        else:
            # Add it right after <style>
            new_block = new_block.replace("<style>", "<style>\n  :root { --page-accent: #0056b3; }")
            has_accent = True
            
        if new_block != block:
            content = content.replace(block, new_block)
            
    # 3. Remove hero-image and hero-overlay
    content = re.sub(r'\s*<img[^>]*class="[^"]*hero-image[^"]*"[^>]*>', '', content)
    content = re.sub(r'\s*<div[^>]*class="[^"]*hero-overlay[^"]*"[^>]*>\s*</div>', '', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    results.append((rel_path, expected_class, style_selector, "Yes" if has_accent else "No"))

with open(os.path.join(base_dir, r"scratch\batch_update_7_report.txt"), "w", encoding="utf-8") as f:
    f.write("File | New header class | Style block selector | --page-accent present\n")
    f.write("-" * 120 + "\n")
    for r in results:
        f.write(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}\n")
