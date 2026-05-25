import os
import re

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

files = {
    "catholic-centre-waterloo.html": "/portfolio/institutions/catholic-centre-waterloo.html",
    "changi-airport-lpr-barriers.html": "/portfolio/institutions/changi-airport-lpr-barriers.html",
    "cpf-maxwell-institution.html": "/portfolio/institutions/cpf-maxwell-institution.html",
    "das-learning-centre-woodlands.html": "/portfolio/institutions/das-learning-centre-woodlands.html",
    "my-world-preschool-cctv.html": "/portfolio/institutions/my-world-preschool-cctv.html",
    "sengkang-interim-bus-interchange.html": "/portfolio/institutions/sengkang-interim-bus-interchange.html",
    "sfx-retreat-centre-punggol.html": "/portfolio/institutions/sfx-retreat-centre-punggol.html"
}

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
    
    # Try finding grid of cards without heading if missing
    # But for safety, let's just insert before DISCOVERY PATH
    return False, content

count = 0
for filename, slug in files.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    portfolio_block = f"""<div class="sv-portfolio-block"
     data-category="institutions"
     data-exclude="{slug}"
     data-bg="sv-section-white"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have delivered security solutions for other institutional facilities across Singapore.">
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
    print(f"Updated {filename}")

print(f"Task E updated {count} files.")
