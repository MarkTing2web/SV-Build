import os
import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\institutions\cpf-maxwell-institution.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# CLASS REPLACEMENTS
content = content.replace('class="container hero-inner"', 'class="container"')
content = content.replace('class="hero-kicker"', 'class="portfolio-kicker"')
content = content.replace('class="badge-sector"', 'class="badge badge-primary"')
content = content.replace('class="badge-meta"', 'class="portfolio-meta"')
content = content.replace('class="hero-title"', 'class="portfolio-hero-title"')
content = re.sub(r'<span class="hero-accent">(.*?)</span>', r'\1', content, flags=re.DOTALL)
content = re.sub(r'<div class="hero-context">\s*(.*?)\s*</div>', r'\1', content, flags=re.DOTALL)
content = content.replace('class="hero-sub"', 'class="portfolio-hero-subtitle"')
content = content.replace('class="hero-chips"', 'class="portfolio-taxonomy" aria-label="Project taxonomy"')
content = content.replace('class="chip"', 'class="portfolio-chip"')
content = content.replace('class="hero-stats"', 'class="portfolio-stat-grid"')
content = content.replace('class="hero-stat"', 'class="portfolio-stat"')
content = content.replace('class="stat-val"', 'class="portfolio-stat-value"')
content = content.replace('class="stat-lbl"', 'class="portfolio-stat-label"')

content = content.replace('class="sv-section sv-section-white"', 'class="portfolio-section sv-section-white section-spacing"')
content = content.replace('class="sv-section sv-section-grey"', 'class="portfolio-section sv-section-grey section-spacing"')
content = content.replace('class="overview-split"', 'class="portfolio-snapshot-grid"')
content = content.replace('class="ov-table"', 'class="portfolio-overview-table"')
content = content.replace('class="container-narrow"', 'class="container"')
content = content.replace('class="disc-link"', 'class="btn btn-outline"')
content = content.replace('class="dual-grid"', 'class="grid-2 mt-40"')
content = content.replace('class="dual-card members"', 'class="card p-32"')
content = content.replace('class="dual-card officers"', 'class="card p-32"')
content = content.replace('class="impact-strip"', 'class="grid-3 mt-40"')
content = content.replace('class="impact-card"', 'class="portfolio-result-card"')

content = re.sub(r'<span class="impact-val">(.*?)</span>', r'<h4 class="portfolio-result-title">\1</h4>', content, flags=re.DOTALL)
content = re.sub(r'<span class="impact-desc">(.*?)</span>', r'<p class="portfolio-result-text">\1</p>', content, flags=re.DOTALL)

content = content.replace('class="spec-table"', 'class="portfolio-overview-table"')
content = re.sub(r'<span class="spec-bold">(.*?)</span>', r'<strong>\1</strong>', content, flags=re.DOTALL)
content = content.replace('class="btn btn-wa"', 'class="btn btn-outline-light"')
content = content.replace('class="cta-trust"', 'class="cta-trust-note"')

# FIX 1: Remove hardcoded credentials
content = content.replace('Police Licence L/PS/000267/2023P · bizSAFE Level 3 · Serving Singapore Since 2006', 'Serving Singapore Since 2006')

# FIX 2: Breadcrumb
breadcrumb_replacement = """<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/portfolio/">Portfolio</a></li>
      <li><a href="/portfolio/institutions/">Institutions</a></li>
      <li>CPF Maxwell Service Centre</li>
    </ul>
  </div>
</nav>"""
content = re.sub(r'<nav class="sv-breadcrumb"[^>]*>.*?</nav>', breadcrumb_replacement, content, flags=re.DOTALL)

# FIX 4: Remove script BEFORE we try to extract and move the discovery path, so it's simpler
script_block = """<script>
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.toggle('active');
}
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.main-nav');
  if (nav) nav.classList.toggle('scrolled', window.scrollY > 50);
});
</script>"""
content = content.replace(script_block, "")

# FIX 3: Move Discovery Path
# Find Discovery Path
# It looks like: <section class="portfolio-section sv-section-grey section-spacing">\s*<div class="container">\s*<div class="section-header text-center">\s*<span class="eyebrow">Discovery Path</span>...
# Let's extract it using a regex or simple string operations.

start_str = '<!-- ═══ DISCOVERY PATH ═══ -->'
end_str = '</section>'
start_idx = content.find(start_str)
if start_idx != -1:
    section_start = content.find('<section', start_idx)
    if section_start != -1:
        # Find the matching closing section tag
        # Since we know there are no nested sections in this block, a simple find will do.
        section_end = content.find('</section>', section_start) + len('</section>')
        
        discovery_path_block = content[start_idx:section_end]
        
        # Remove from current location
        content = content[:start_idx] + content[section_end:]
        
        # Insert before sv-portfolio-block div
        target_idx = content.find('<div class="sv-portfolio-block"')
        if target_idx != -1:
            content = content[:target_idx] + discovery_path_block + "\n\n" + content[target_idx:]


with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

# VERIFICATION
legacy_classes = ["hero-inner", "hero-kicker", "badge-sector", "badge-meta", "hero-title",
   "hero-accent", "hero-context", "hero-sub", "hero-chips", "chip", "hero-stats",
   "hero-stat", "stat-val", "stat-lbl", "sv-section", "overview-split", "ov-table",
   "container-narrow", "disc-link", "dual-grid", "dual-card", "impact-strip",
   "impact-card", "impact-val", "impact-desc", "spec-table", "spec-bold",
   "btn-wa", "cta-trust"]

found_legacy = []
for c in legacy_classes:
    if f'class="{c}"' in content or f'class="{c} ' in content or f' {c}"' in content or f' {c} ' in content:
        found_legacy.append(c)
        
b_count = content.count('<li>', content.find('<nav class="sv-breadcrumb"'))
has_hardcoded = 'L/PS/000267/2023P' in content
disc_idx = content.find('Discovery Path')
footer_idx = content.find('<footer id="sv-footer">')
has_script = 'function toggleMobileMenu()' in content

print(f"1. Legacy classes found: {found_legacy if found_legacy else 'None'}")
print(f"2. Breadcrumb levels: {b_count}")
print(f"3. Hardcoded licence present: {has_hardcoded}")
print(f"4. Discovery Path before footer: {disc_idx != -1 and footer_idx != -1 and disc_idx < footer_idx}")
print(f"5. toggleMobileMenu script present: {has_script}")
