import os
from bs4 import BeautifulSoup
import json

RESOURCES_DIR = r"C:\Projects\SV-Build\resources"

data = []

for root, dirs, files in os.walk(RESOURCES_DIR):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            title = soup.title.string if soup.title else ""
            desc_tag = soup.find("meta", attrs={"name": "description"})
            desc = desc_tag["content"] if desc_tag else ""
            
            rel_path = os.path.relpath(path, RESOURCES_DIR).replace('\\', '/')
            data.append({
                "file": "/resources/" + rel_path if rel_path != "." else "/resources/index.html",
                "title": title,
                "title_len": len(title),
                "desc": desc,
                "desc_len": len(desc)
            })

with open(r"C:\Projects\SV-Build\scratch\seo_data.json", 'w') as f:
    json.dump(data, f, indent=2)
