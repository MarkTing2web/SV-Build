import re

files = [
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        start_idx = content.find('<nav class="sv-breadcrumb"')
        if start_idx != -1:
            end_idx = content.find('</nav>', start_idx)
            if end_idx != -1:
                end_idx += len('</nav>')
                print(f"### {filepath}")
                print("```html")
                print(content[start_idx:end_idx].strip())
                print("```\n")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
