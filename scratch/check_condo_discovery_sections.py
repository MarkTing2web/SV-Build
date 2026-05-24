import os
import re

files = [
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

markers = [
    '<span class="eyebrow">Discovery Path</span>',
    '<h2>Explore Related Solutions</h2>',
    '<!-- DISCOVERY PATH -->',
    '<!-- SECTION 9 -->'
]

for rel_path in files:
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    found_marker = None
    for marker in markers:
        if marker in content:
            found_marker = marker
            break
            
    if not found_marker:
        print(f"{rel_path}: NO MARKER FOUND")
        continue
        
    marker_idx = content.find(found_marker)
    
    # Print 100 characters before and 300 characters after the marker to understand surrounding structure
    start_snippet = max(0, marker_idx - 150)
    end_snippet = min(len(content), marker_idx + 350)
    snippet = content[start_snippet:end_snippet]
    
    print("=" * 60)
    print(f"File: {rel_path}")
    print(f"Found Marker: {found_marker}")
    print("Snippet:")
    print(snippet)
