import os
import re

files = [
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

print("File | Garbage removed | H1 text used as project name | Breadcrumb inserted after trust-bar line | Levels in breadcrumb")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        garbage_removed = "No"
        nav_tag = '<nav id="sv-nav"></nav>'
        start_nav = content.find(nav_tag)
        
        if start_nav != -1:
            nav_end_idx = start_nav + len(nav_tag)
            hero_idx = content.find('<header class="hero')
            
            if hero_idx != -1 and hero_idx > nav_end_idx:
                content = content[:nav_end_idx] + "\n\n  " + content[hero_idx:]
                garbage_removed = "Yes"
                
        # Find h1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        project_name = "N/A"
        if h1_match:
            raw_h1 = h1_match.group(1)
            project_name = re.sub(r'<[^>]+>', '', raw_h1).strip()
            # Replace multiple spaces/newlines with a single space if any
            project_name = re.sub(r'\s+', ' ', project_name)
            
        breadcrumb_html = f"""  <nav class="sv-breadcrumb" aria-label="Breadcrumb">
    <div class="container">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
        <li><a href="/portfolio/condominiums/">Condominiums</a></li>
        <li>{project_name}</li>
      </ul>
    </div>
  </nav>"""
        
        # Find trust bar end
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
                content = content[:tb_end] + "\n\n" + breadcrumb_html + "\n" + content[tb_end:]
                
                # compute line number for reporting
                # The line before we added \n\n
                tb_inserted_line = content.count('\n', 0, tb_end) + 1
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        levels = breadcrumb_html.count('<li>')
        
        print(f"{filepath} | {garbage_removed} | {project_name} | {tb_inserted_line} | {levels}")
        
    except Exception as e:
        print(f"{filepath} | Error: {str(e)} | N/A | N/A | N/A")
