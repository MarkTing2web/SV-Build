import os

base_dir = r"c:\Projects\SV-Build"

files = [
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html"
]

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<script src="/portfolio-block.js"></script>' not in content:
        if '<script src="/nav-footer.js"></script>' in content:
            content = content.replace('<script src="/nav-footer.js"></script>', '<script src="/portfolio-block.js"></script>\n  <script src="/nav-footer.js"></script>')
        else:
            content = content.replace('</body>', '<script src="/portfolio-block.js"></script>\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {rel_path}")

print(f"Task G updated {count} files.")
