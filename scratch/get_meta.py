import os
import re

files = [
    'portfolio/managed-living/scb-worker-dormitory-jalan-papan.html',
    'portfolio/industrial/sta-compliance-imaging.html',
    'portfolio/institutions/sengkang-interim-bus-interchange.html'
]

data = []
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        title_m = re.search(r'<title>(.*?)</title>', content)
        desc_m = re.search(r'<meta name="description" content="(.*?)"', content)
        title = title_m.group(1).split('|')[0].strip() if title_m else "Title"
        desc = desc_m.group(1).strip() if desc_m else "Description"
        data.append({'slug': '/' + f, 'title': title, 'desc': desc})
        print(f"Slug: /{f}\nTitle: {title}\nDesc: {desc}\n")
