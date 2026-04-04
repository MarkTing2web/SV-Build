import os
import re
from bs4 import BeautifulSoup
import json

def audit_ctas(directory):
    report = {}
    
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    for filename in html_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Look for things that look like CTAs
        # 1. <a> with 'btn' class
        # 2. <a> inside 'btn-group'
        # 3. <a> with 'rel-card-footer'
        # 4. <a> with 'link-arrow'
        
        ctas = []
        
        # Primary buttons
        for btn in soup.find_all('a', class_=re.compile(r'btn|cta|button|link-arrow|rel-card-footer')):
            text = btn.get_text().strip()
            link = btn.get('href', '#')
            
            # Find a description (preceding heading or paragraph)
            description = ""
            parent = btn.parent
            # Try to find a heading in the same container or previous siblings
            prev = btn.find_previous(['h1', 'h2', 'h3', 'p'])
            if prev:
                description = prev.get_text().strip()
            
            ctas.append({
                "text": text,
                "link": link,
                "description": description[:100] + "..." if len(description) > 100 else description,
                "classes": btn.get('class', [])
            })
            
        if ctas:
            report[filename] = ctas
            
    return report

if __name__ == "__main__":
    workspace_path = r"c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build"
    results = audit_ctas(workspace_path)
    
    with open("cta_audit_report.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"Audit complete. Processed {len(results)} pages.")
