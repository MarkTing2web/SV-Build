import os
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"

files = [
    "solutions/commercial/commercial-security-systems.html",
    "solutions/condominiums/condominium-security-systems.html",
    "solutions/condominiums/managing-agents.html",
    "solutions/condominiums/mcst.html",
    "solutions/condominiums/security-contractors.html",
    "solutions/data-centres/data-centre-security-systems.html",
    "solutions/healthcare/day-care.html",
    "solutions/healthcare/healthcare-security-systems.html",
    "solutions/industrial/industrial-security-systems.html",
    "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html",
    "solutions/industrial/tech-park.html",
    "solutions/institutions/community.html",
    "solutions/institutions/govt-office.html",
    "solutions/institutions/institutions-security-systems.html",
    "solutions/institutions/schools.html",
    "solutions/managed-living/co-living.html",
    "solutions/managed-living/managed-living-security-systems.html"
]

for rel_path in files:
    filepath = os.path.join(repo_root, rel_path)
    if not os.path.exists(filepath):
        print(f"{rel_path} — NOT FOUND")
        continue

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    meta = soup.find('meta', property='og:image')
    if not meta:
        meta = soup.find('meta', attrs={"name": "og:image"})

    if meta:
        val = meta.get('content', '')
        print(f"{rel_path} — og:image: {val}")
    else:
        print(f"{rel_path} — og:image: NOT SET")
