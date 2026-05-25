import os
import re

base_dir = r"c:\Projects\SV-Build"

files = [
    ("portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", "healthcare", "/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html"),
    ("portfolio/healthcare/surya-home.html", "healthcare", "/portfolio/healthcare/surya-home.html"),
    ("portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html", "managed-living", "/portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html"),
    ("portfolio/managed-living/scb-worker-dormitory-jalan-papan.html", "managed-living", "/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"),
    ("portfolio/data-centres/fort-data-centre-access-upgrade.html", "data-centres", "/portfolio/data-centres/fort-data-centre-access-upgrade.html"),
    ("portfolio/data-centres/fort-st-engineering.html", "data-centres", "/portfolio/data-centres/fort-st-engineering.html")
]

def replace_related_section(content, replacement):
    idx = content.find("Related Case Studies")
    if idx == -1:
        idx = content.find("Related Projects")
    
    if idx != -1:
        section_start = content.rfind("<section", 0, idx)
        comment_start = content.rfind("<!--", max(0, section_start - 100), section_start)
        if comment_start != -1 and "RELATED" in content[comment_start:section_start].upper():
            section_start = comment_start
            
        section_end = content.find("</section>", idx)
        if section_start != -1 and section_end != -1:
            section_end += len("</section>")
            content = content[:section_start] + replacement + content[section_end:]
            return True, content
    
    return False, content

count = 0
for rel_path, category, slug in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    portfolio_block = f"""<div class="sv-portfolio-block"
     data-category="{category}"
     data-exclude="{slug}"
     data-bg="sv-section-white"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have delivered security solutions for similar facilities across Singapore.">
</div>"""

    replaced, new_content = replace_related_section(content, portfolio_block)
    if replaced:
        content = new_content
    else:
        if '<!-- ═══ DISCOVERY PATH ═══ -->' in content:
            content = content.replace('<!-- ═══ DISCOVERY PATH ═══ -->', portfolio_block + '\n\n  <!-- ═══ DISCOVERY PATH ═══ -->')
        else:
            if '<footer' in content:
                content = re.sub(r'([ \t]*<footer)', '\n  ' + portfolio_block + r'\n\n\1', content)
            else:
                content = re.sub(r'([ \t]*</body>)', '\n  ' + portfolio_block + r'\n\n\1', content)
                
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task F updated {count} files.")
