import os
import re

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

files = [
    "catholic-centre-waterloo.html",
    "changi-airport-lpr-barriers.html",
    "cpf-maxwell-institution.html",
    "das-learning-centre-woodlands.html",
    "my-world-preschool-cctv.html",
    "sengkang-interim-bus-interchange.html",
    "sfx-retreat-centre-punggol.html"
]

discovery_html = """<!-- ═══ DISCOVERY PATH ═══ -->
<section class="portfolio-section sv-section-grey section-spacing">
  <div class="container">
    <div class="section-header text-center">
      <span class="eyebrow">Discovery Path</span>
      <h2>Explore Related Solutions</h2>
      <p class="text-left mt-16">Deepen your understanding of the systems and approach used in this project.</p>
    </div>
    <div class="sv-systems-block" data-cols="3"
         data-systems="all"
         data-eyebrow=""
         data-heading=""
         data-intro=""
         data-desc-premises="Surveillance and detection for institutional facilities — CCTV coverage designed around public access areas, restricted zones, and after-hours monitoring."
         data-desc-entry-access="Access control for institutions — managing staff, visitor, and contractor entry across multiple zones while maintaining audit trails for compliance."
         data-desc-vehicle-lpr="LPR and barrier systems for institutional carparks and loading bays — logging vehicle movements and controlling access without a full-time guardhouse."
         data-desc-ip-telephony="IP communications connecting reception, security posts, and management offices — replacing legacy intercom systems with a unified network."
         data-desc-network="The IP backbone every institutional security system depends on — structured cabling and switching designed to handle public footfall and multiple concurrent systems."
         data-desc-platform="A unified platform connecting CCTV, access logs, and alarm events — giving facility management a single operational view across the entire site.">
    </div>
  </div>
</section>"""

def update_html_discovery_path(content):
    if "Discovery Path" in content:
        dp_index = content.find("Discovery Path")
        section_start = content.rfind("<section", 0, dp_index)
        
        comment_start = content.rfind("<!--", max(0, section_start - 100), section_start)
        if comment_start != -1 and "DISCOVERY PATH" in content[comment_start:section_start].upper():
            section_start = comment_start
            
        section_end = content.find("</section>", dp_index)
        if section_start != -1 and section_end != -1:
            section_end += len("</section>")
            content = content[:section_start] + discovery_html + content[section_end:]
            return content

    if "Discovery Path" not in content:
        if '<footer' in content:
            content = re.sub(r'([ \t]*<footer)', '\n  ' + discovery_html + r'\n\n\1', content)
        else:
            content = re.sub(r'([ \t]*</body>)', '\n  ' + discovery_html + r'\n\n\1', content)
    
    return content

count = 0
for filename in files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<script src="/systems-block.js"></script>' not in content:
        if '<script src="/nav-footer.js"></script>' in content:
            content = content.replace('<script src="/nav-footer.js"></script>', '<script src="/systems-block.js"></script>\n  <script src="/nav-footer.js"></script>')
        else:
            content = content.replace('</body>', '<script src="/systems-block.js"></script>\n</body>')
    
    content = update_html_discovery_path(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {filename}")

print(f"Task D updated {count} files.")
