import os
import re

files_to_fix = [
    ("portfolio/industrial/sta-compliance-imaging.html", "cta-facilities"),
    ("portfolio/industrial/sta-inspection-industrial.html", "cta-facilities"),
    ("portfolio/institutions/cpf-maxwell-institution.html", "cta-compliance"),
    ("resources/index.html", "cta-property"),
    ("contact.html", "cta-facilities"),
    ("contact-gateway.html", "cta-facilities"),
    ("request-site-assessment-singapore.html", "cta-facilities"),
    ("about/index.html", "cta-facilities")
]

cta_template = """
<!-- FINAL CTA -->
<section class="cta-section cta-high-impact {group}">
  <div class="container">
    <span class="eyebrow-light">Get Started</span>
    <h2>Need Expert Security Advice?</h2>
    <p>From technical planning to professional deployment. Let our 37 years of Singapore expertise turn your security goals into reality. No guesswork, just performance.</p>
    <div class="btn-group">
      <a href="/contact-gateway.html" class="btn btn-primary">Book Site Assessment</a>
      <a href="https://wa.me/6593860466" class="btn btn-wa">💬 WhatsApp an Engineer</a>
    </div>
    <p class="cta-trust">Police Licence L/PS/000267/2023P · bizSAFE Level 3 · Serving Singapore Since 2006</p>
  </div>
</section>
"""

base_dir = "c:/Projects/SV-Build"

for rel_path, group in files_to_fix:
    full_path = os.path.join(base_dir, rel_path.replace('/', os.sep))
    if not os.path.exists(full_path):
        print(f"NOT FOUND: {full_path}")
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if a cta-section exists (or cta-high-impact)
    # Match various forms of the cta section
    # If it has <!-- FINAL CTA --> it's easier
    if "<!-- FINAL CTA -->" in content:
        # Replace the entire block
        content = re.sub(r'<!-- FINAL CTA -->.*?<section[^>]*class="[^"]*(cta-section|cta-high-impact)[^"]*"[^>]*>.*?</section>', cta_template.format(group=group), content, flags=re.DOTALL)
    elif '<section class="cta-section' in content:
        content = re.sub(r'<section class="cta-section[^>]*>.*?</section>', cta_template.format(group=group), content, flags=re.DOTALL)
    else:
        # Insert before footer
        if '<footer' in content:
            # Find the position of the first <footer or footer-related comment
            pos = content.find('<footer')
            content = content[:pos] + cta_template.format(group=group) + "\n" + content[pos:]
        else:
            # Append before </body>
            pos = content.find('</body>')
            content = content[:pos] + cta_template.format(group=group) + "\n" + content[pos:]
            
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"FIXED: {rel_path}")
