import os
import re

base_dir = r"c:\Projects\SV-Build\portfolio\industrial"

slugs = {
    "cogent-logistics-hub-cctv.html": "/portfolio/industrial/cogent-logistics-hub-cctv.html",
    "cyrus-tech-industrial.html": "/portfolio/industrial/cyrus-tech-industrial.html",
    "hoy-san-industrial.html": "/portfolio/industrial/hoy-san-industrial.html",
    "mitsubishi-elevator-face-access-bms.html": "/portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "multibase-construction-security-upgrade.html": "/portfolio/industrial/multibase-construction-security-upgrade.html",
    "smartflex-tampines.html": "/portfolio/industrial/smartflex-tampines.html",
    "sta-compliance-imaging.html": "/portfolio/industrial/sta-compliance-imaging.html",
    "sta-inspection-industrial.html": "/portfolio/industrial/sta-inspection-industrial.html",
    "stmicroelectronics-loyang-perimeter-alarm.html": "/portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html"
}

count = 0
for filename, slug in slugs.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_block = f"""<div class="sv-portfolio-block"
     data-category="industrial"
     data-exclude="{slug}"
     data-bg="sv-section-white"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have delivered security solutions for other industrial facilities across Singapore.">
</div>"""

    if filename == "hoy-san-industrial.html":
        pattern = r'<section[^>]*>(?:(?!</section>).)*?(?:Related Case Studies|Related Projects|card card-clickable).*?</section>'
        if re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_block, content, flags=re.DOTALL | re.IGNORECASE)
        else:
            content = content.replace('<footer', f'{new_block}\n<footer')
    else:
        pattern = r'<section[^>]*>(?:(?!</section>).)*?(?:Related Case Studies|Related Projects|related-project-card).*?</section>'
        if re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, new_block, content, flags=re.DOTALL | re.IGNORECASE)
        else:
            content = content.replace('<footer', f'{new_block}\n<footer')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {filename}")

print(f"Task E updated {count} files.")
