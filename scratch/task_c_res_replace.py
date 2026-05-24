import os
import re

files = [
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

markers = [
    '<span class="eyebrow">Discovery Path</span>',
    '<h2>Explore Related Solutions</h2>',
    '<!-- DISCOVERY PATH -->',
    '<!-- SECTION 9 -->'
]

new_section = """<!-- ═══ DISCOVERY PATH ═══ -->
<section class="portfolio-section sv-section-grey section-spacing">
  <div class="container">
    <div class="section-header text-center">
      <span class="eyebrow">Discovery Path</span>
      <h2>Explore Related Solutions</h2>
      <p class="text-left mt-16">Deepen your understanding of the systems and approach used in this project.</p>
    </div>
    <div class="sv-systems-block"
         data-systems="premises,entry-access,vehicle-lpr,ip-telephony,network"
         data-eyebrow=""
         data-heading=""
         data-intro=""
         data-desc-vehicle-lpr="Auto gates, sliding gates, and remote entry — secure your driveway and control vehicle access to your home.">
    </div>
  </div>
</section>"""

updated_count = 0
for rel_path in files:
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    found_marker = None
    for marker in markers:
        if marker in content:
            found_marker = marker
            break
            
    if not found_marker:
        print(f"ERROR: No marker found in {rel_path}")
        continue
        
    marker_idx = content.find(found_marker)
    
    # Search backwards for <section
    sec_start = content.rfind("<section", 0, marker_idx)
    if sec_start == -1:
        print(f"ERROR: Could not find <section backwards in {rel_path}")
        continue
        
    # Search forwards for </section>
    sec_end = content.find("</section>", marker_idx)
    if sec_end == -1:
        print(f"ERROR: Could not find </section> forwards in {rel_path}")
        continue
    sec_end += len("</section>")
    
    # Let's inspect indentation before the <section
    line_start = content.rfind("\n", 0, sec_start)
    if line_start == -1:
        indent = ""
    else:
        indent = content[line_start+1:sec_start]
        
    # indent each line of the new section
    indented_new_section = "\n".join(
        (indent + line if line.strip() else line)
        for line in new_section.splitlines()
    )
    
    # Check if there is a comment immediately preceding sec_start
    text_before = content[:sec_start]
    last_comment_match = list(re.finditer(r'<!--.*?-->', text_before, re.DOTALL))
    replace_start = sec_start
    if last_comment_match:
        last_comment = last_comment_match[-1]
        between = text_before[last_comment.end():]
        if between.strip() == "" and ("DISCOVERY PATH" in last_comment.group(0) or "SECTION" in last_comment.group(0) or "Explore Related Solutions" in last_comment.group(0)):
            replace_start = last_comment.start()
            comment_line_start = content.rfind("\n", 0, replace_start)
            if comment_line_start == -1:
                indent = ""
            else:
                indent = content[comment_line_start+1:replace_start]
            
            # re-indent new_section
            indented_new_section = "\n".join(
                (indent + line if line.strip() else line)
                for line in new_section.splitlines()
            )
            
    print(f"Replacing in {rel_path}: from index {replace_start} to {sec_end}")
    
    # Write updated content
    new_content = content[:replace_start] + indented_new_section + content[sec_end:]
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated_count += 1

print(f"Task C complete: {updated_count} files replaced.")
