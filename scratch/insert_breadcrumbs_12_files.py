import os
import re

files = [
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

print("File | Project name used | Sector link | Breadcrumb line number | Levels")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Read H1 text
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        project_name = "N/A"
        if h1_match:
            raw_h1 = h1_match.group(1)
            clean_h1 = re.sub(r'<[^>]+>', '', raw_h1).strip()
            
            # The prompt explicitly specifies checking for " — "
            if " — " in clean_h1:
                project_name = clean_h1.split(" — ")[0].strip()
            elif " - " in clean_h1:
                project_name = clean_h1.split(" - ")[0].strip()
            else:
                project_name = clean_h1
                
        # Step 2: Determine sector link and label
        sector_link = "N/A"
        sector_label = "N/A"
        if "portfolio/condominiums/" in filepath:
            sector_link = "condominiums"
            sector_label = "Condominiums"
        elif "portfolio/residential/" in filepath:
            sector_link = "residential"
            sector_label = "Residential"
            
        breadcrumb_html = f"""
  <nav class="sv-breadcrumb" aria-label="Breadcrumb">
    <div class="container">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
        <li><a href="/portfolio/{sector_link}/">{sector_label}</a></li>
        <li>{project_name}</li>
      </ul>
    </div>
  </nav>"""
        
        # Step 3: Find trust bar closing tag
        tb_match = re.search(r'<div\s+class="trust-bar"[^>]*>', content)
        tb_inserted_line = "N/A"
        if tb_match:
            tb_start = tb_match.start()
            div_count = 0
            current_idx = tb_start
            tb_end = -1
            while current_idx < len(content):
                next_open = content.find('<div', current_idx)
                next_close = content.find('</div', current_idx)
                
                if next_close == -1:
                    break
                    
                if next_open != -1 and next_open < next_close:
                    div_count += 1
                    current_idx = next_open + 4
                else:
                    div_count -= 1
                    current_idx = next_close + 5
                    if div_count == 0:
                        tb_end = content.find('>', current_idx) + 1
                        break
                        
            if tb_end != -1:
                content = content[:tb_end] + "\n" + breadcrumb_html + "\n" + content[tb_end:]
                
                tb_inserted_line = content.count('\n', 0, tb_end) + 2
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        levels = breadcrumb_html.count('<li>')
        
        print(f"{os.path.basename(filepath)} | {project_name} | {sector_link} | {tb_inserted_line} | {levels}")
        
    except Exception as e:
        print(f"{filepath} | Error: {str(e)} | N/A | N/A | N/A")
