import os
import re

files = [
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
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
         data-systems="premises,entry-access,vehicle-lpr,network,platform"
         data-eyebrow=""
         data-heading=""
         data-intro="">
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
    # We can look at the characters before sec_start up to the nearest newline.
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
    
    # We want to check if the comments <!-- ... --> immediately preceding the section are there, and replace them as well.
    # In some files, we might have:
    #   <!-- ═══════════════════════════════════════════════════════
    #        SECTION 14 — DISCOVERY PATH (sv-section-grey)
    #        ═══════════════════════════════════════════════════════ -->
    #   <section class="portfolio-section sv-section-grey section-spacing">
    # Let's see if we can find such comment headers. They start with <!-- and end with -->
    # If a comment exists immediately before the section (with only whitespace in between), we can include it in the replaced range.
    # Let's find if there is a comment immediately preceding sec_start.
    prefix = content[line_start:sec_start] if line_start != -1 else content[0:sec_start]
    # Let's search backwards for comment close --> and see if it's very close.
    # Actually, we can check if the comment block exists.
    # But wait! The new HTML has:
    # <!-- ═══ DISCOVERY PATH ═══ -->
    # which replaces the need for the old comment block.
    # Let's check how much whitespace/comment block is right before <section.
    # Let's scan backwards for <!--. If it contains "DISCOVERY PATH" or "SECTION" and is close, we can include it.
    comment_pattern = re.compile(r'<!--\s*(?:═══+|═+|─+|─\s*DISCOVERY PATH|DISCOVERY PATH|SECTION\s+\d+.*?)\s*-->\s*$', re.DOTALL)
    # Let's look at the text before sec_start
    text_before = content[:sec_start]
    # Find the last comment ending in --> and check if it's purely whitespace between that comment and sec_start
    last_comment_match = list(re.finditer(r'<!--.*?-->', text_before, re.DOTALL))
    replace_start = sec_start
    if last_comment_match:
        last_comment = last_comment_match[-1]
        between = text_before[last_comment.end():]
        if between.strip() == "" and ("DISCOVERY PATH" in last_comment.group(0) or "SECTION" in last_comment.group(0) or "Explore Related Solutions" in last_comment.group(0)):
            replace_start = last_comment.start()
            # update indent based on the line of the comment start
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

print(f"Task B complete: {updated_count} files replaced.")
