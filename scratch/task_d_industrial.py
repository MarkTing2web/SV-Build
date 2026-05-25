import os
import re

base_dir = r"c:\Projects\SV-Build\portfolio\industrial"

files = [
    "cogent-logistics-hub-cctv.html",
    "cyrus-tech-industrial.html",
    "hoy-san-industrial.html",
    "mitsubishi-elevator-face-access-bms.html",
    "multibase-construction-security-upgrade.html",
    "smartflex-tampines.html",
    "sta-compliance-imaging.html",
    "sta-inspection-industrial.html",
    "stmicroelectronics-loyang-perimeter-alarm.html"
]

discovery_path = """<!-- ═══ DISCOVERY PATH ═══ -->
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
         data-desc-premises="The surveillance and detection layer behind industrial security. CCTV coverage designed around large footprints, perimeter lines, and shift-change blind spots."
         data-desc-entry-access="Access control at the industrial scale — biometric readers, turnstiles, and card systems that manage contractor entry, staff movements, and restricted zone protection."
         data-desc-vehicle-lpr="LPR and barrier systems for industrial carparks and loading bays — automating vehicle entry, logging movements, and removing the need for a dedicated gatehouse."
         data-desc-ip-telephony="IP communications connecting guardhouses, loading bays, and management offices across a facility — replacing legacy intercom systems with a unified IP network."
         data-desc-network="The structured cabling and switching backbone that every IP system on a facility depends on — designed to survive industrial environments and scale with future requirements."
         data-desc-platform="One management platform connecting CCTV, access events, and alarm triggers — giving security teams a single operational view across a multi-building facility.">
    </div>
  </div>
</section>"""

count = 0
for filename in files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_script = '<script src="/nav-footer.js"></script>'
    if '<script src="/systems-block.js"></script>' not in content:
        content = content.replace(target_script, '<script src="/systems-block.js"></script>\n  ' + target_script)

    pattern = r'<section[^>]*>(?:(?!</section>).)*?Explore Related Solutions.*?</section>'
    
    if re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE):
        content = re.sub(pattern, discovery_path, content, flags=re.DOTALL | re.IGNORECASE)
    else:
        content = content.replace('<footer', f'{discovery_path}\n<footer')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {filename}")

print(f"Task D updated {count} files.")
