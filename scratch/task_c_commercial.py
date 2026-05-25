import os
import re

base_dir = r"c:\Projects\SV-Build"
files = [
    'portfolio/commercial/altitudex-sentosa-commercial.html',
    'portfolio/commercial/catholic-centre-security-partnership.html',
    'portfolio/commercial/em-services-call-centre-redhill.html',
    'portfolio/commercial/hilton-singapore-orchard-fire-door.html',
    'portfolio/commercial/scape-commercial.html',
    'portfolio/commercial/scape-smart-booking-access.html',
    'portfolio/commercial/st-engineering-mobility-cctv.html'
]

new_section = """<!-- ═══ DISCOVERY PATH ═══ -->
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
         data-desc-premises="The surveillance and detection layer behind projects like this one. See how we design CCTV, alarm, and sensor systems for commercial properties."
         data-desc-entry-access="Access control that works at the scale of a commercial building — biometrics, intercoms, visitor management, and lift control integrated into one system."
         data-desc-vehicle-lpr="Auto-gates, LPR, and barrier systems for commercial carparks and loading bays — automating vehicle flow and reducing guard dependency."
         data-desc-ip-telephony="IP phone systems and IPPBX for commercial offices — replacing legacy keyphones with modern, app-enabled internal communications."
         data-desc-network="The IP network foundation every other system depends on — managed switches, structured cabling, and WiFi designed alongside the security installation."
         data-desc-platform="One platform connecting CCTV, access, and communications — giving building management a unified operational view across all systems.">
    </div>
  </div>
</section>"""

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Add script tag
    if '<script src="/systems-block.js"></script>' not in content:
        content = content.replace('<script src="/nav-footer.js"></script>', '<script src="/systems-block.js"></script>\n  <script src="/nav-footer.js"></script>')

    # Step 2: Replace Discovery Path section
    # First, let's try to remove any existing <!-- ═══ DISCOVERY PATH ═══ --> comment so it doesn't duplicate
    content = re.sub(r'<!--\s*═══\s*DISCOVERY PATH\s*═══\s*-->\s*', '', content)
    
    content = re.sub(
        r'<section[^>]*>(?:(?!</section>).)*?(?:Discovery Path|Explore Related Solutions).*?</section>',
        new_section,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task C updated {count} files.")
