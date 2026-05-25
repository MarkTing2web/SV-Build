import os
import re

base_dir = r"c:\Projects\SV-Build"

files = [
    ("portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", "healthcare"),
    ("portfolio/healthcare/surya-home.html", "healthcare"),
    ("portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html", "managed-living"),
    ("portfolio/managed-living/scb-worker-dormitory-jalan-papan.html", "managed-living"),
    ("portfolio/data-centres/fort-data-centre-access-upgrade.html", "data-centres"),
    ("portfolio/data-centres/fort-st-engineering.html", "data-centres")
]

blocks = {
    "healthcare": """<!-- ═══ DISCOVERY PATH ═══ -->
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
         data-desc-premises="Surveillance for healthcare facilities — camera placement that supports patient dignity, staff safety, and after-hours security without clinical disruption."
         data-desc-entry-access="Access control that manages clinical staff, visitors, and restricted medical areas — with audit trails that support compliance and incident review."
         data-desc-vehicle-lpr="Vehicle management for healthcare carparks — logging movements, managing visitor bay turnover, and controlling access to ambulance bays and restricted areas."
         data-desc-ip-telephony="IP communications connecting reception, nursing stations, and security posts — replacing legacy systems with a unified network across the facility."
         data-desc-network="The IP backbone that every healthcare security system depends on — reliable, segmented, and designed to coexist with clinical network infrastructure."
         data-desc-platform="A unified management platform connecting CCTV, access, and alarm events — giving facility management a single operational view across the site.">
    </div>
  </div>
</section>""",

    "managed-living": """<!-- ═══ DISCOVERY PATH ═══ -->
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
         data-desc-premises="Surveillance for managed living facilities — camera coverage balancing resident welfare with operational oversight and perimeter security."
         data-desc-entry-access="Access control for dormitories and managed residences — managing resident entry, visitor access, and restricted staff-only areas."
         data-desc-vehicle-lpr="Vehicle management for managed living carparks and loading areas — controlling access and logging movements across a shared-living environment."
         data-desc-ip-telephony="IP communications connecting management offices, guardhouses, and communal areas — a unified network replacing fragmented legacy intercom systems."
         data-desc-network="The structured cabling and switching backbone underpinning every IP system across the facility — designed for reliability in a high-occupancy environment."
         data-desc-platform="One platform connecting CCTV, access logs, and alarm events — giving facility managers a single operational view across the entire property.">
    </div>
  </div>
</section>""",

    "data-centres": """<!-- ═══ DISCOVERY PATH ═══ -->
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
         data-desc-premises="Surveillance for data centre environments — camera coverage at server hall entry points, raised floors, and perimeter zones where physical access is the last line of defence."
         data-desc-entry-access="Multi-factor access control for data centres — biometrics, card, and PIN combinations that enforce least-privilege access to server halls and restricted zones."
         data-desc-vehicle-lpr="Vehicle management for data centre compounds — controlling delivery vehicle access, logging movements, and securing loading bay entry."
         data-desc-ip-telephony="IP communications connecting security posts, reception, and operations centres — a unified network across a facility where every layer of access matters."
         data-desc-network="Managed switching and structured cabling for data centre security infrastructure — isolated from production networks, designed for zero single points of failure."
         data-desc-platform="A unified management platform connecting physical access, CCTV, and alarm systems — the operations layer that ties every security control together.">
    </div>
  </div>
</section>"""
}

def update_html_discovery_path(content, discovery_html):
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
for rel_path, category in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<script src="/systems-block.js"></script>' not in content:
        if '<script src="/nav-footer.js"></script>' in content:
            content = content.replace('<script src="/nav-footer.js"></script>', '<script src="/systems-block.js"></script>\n  <script src="/nav-footer.js"></script>')
        else:
            content = content.replace('</body>', '<script src="/systems-block.js"></script>\n</body>')
            
    content = update_html_discovery_path(content, blocks[category])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task E updated {count} files.")
