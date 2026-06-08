import re
import os

BASE_DIR = r"d:\Ler Wee Meng\Project-Web\SV-Build"

files_to_update = {
    "portfolio/commercial/scape-commercial.html": """<style>
  :root { --page-accent: #0056b3; }
  .hero-scape-commercial { background-image: url('/images/portfolio/commercial/scape-hero.webp'); }
  @media (max-width: 768px) {
    .hero-scape-commercial { background-image: url('/images/portfolio/commercial/scape-mobile.webp'); }
  }
</style>""",
    "portfolio/commercial/scape-smart-booking-access.html": """<style>
  :root { --page-accent: #0056b3; }
  .hero-scape-smart-booking-access { background-image: url('/images/portfolio/commercial/scape-hero.webp'); }
  @media (max-width: 768px) {
    .hero-scape-smart-booking-access { background-image: url('/images/portfolio/commercial/scape-mobile.webp'); }
  }
</style>""",
    "portfolio/industrial/sta-compliance-imaging.html": """<style>
  :root { --page-accent: #0056b3; }
  .hero-sta-compliance-imaging { background-image: url('/images/portfolio/industrial/sta-compliance-imaging-hero.webp'); }
  @media (max-width: 768px) {
    .hero-sta-compliance-imaging { background-image: url('/images/portfolio/industrial/sta-compliance-imaging-mobile.webp'); }
  }
</style>""",
    "portfolio/institutions/sengkang-interim-bus-interchange.html": """<style>
  :root { --page-accent: #0056b3; }
  .hero-sengkang-interim-bus-interchange { background-image: url('/images/portfolio/institutions/sengkang-interim-bus-interchange-hero.webp'); }
  @media (max-width: 768px) {
    .hero-sengkang-interim-bus-interchange { background-image: url('/images/portfolio/institutions/sengkang-interim-bus-interchange-mobile.webp'); }
  }
</style>"""
}

def replace_style_block(file_path, new_style):
    full_path = os.path.join(BASE_DIR, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace entire style block
    new_content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

for path, new_style in files_to_update.items():
    replace_style_block(path, new_style)

def update_root_accent(file_path):
    full_path = os.path.join(BASE_DIR, file_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if :root exists
    if ':root' in content:
        # replace existing --page-accent if it exists
        if '--page-accent' in content:
            content = re.sub(r'--page-accent:\s*#[0-9a-fA-F]+;', '--page-accent: #0056b3;', content)
        else:
            # add it inside :root {
            content = re.sub(r':root\s*\{', ':root { --page-accent: #0056b3;', content)
    else:
        # add :root { --page-accent: #0056b3; } as first rule in style block
        content = re.sub(r'<style>', '<style>\n  :root { --page-accent: #0056b3; }', content)
        
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

update_root_accent("portfolio/healthcare/surya-home.html")
update_root_accent("portfolio/managed-living/scb-worker-dormitory-jalan-papan.html")

# Verification
all_files = list(files_to_update.keys()) + [
    "portfolio/healthcare/surya-home.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
]

print("File | --page-accent present | Desktop image rule present | Mobile image rule present | linear-gradient in style block | Extra rules beyond 3 permitted")
print("---|---|---|---|---|---")

for path in all_files:
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        has_accent = "--page-accent: #0056b3;" in style_content
        has_desktop = "background-image: url(" in style_content and "mobile" not in style_content.split("@media")[0]
        has_mobile = "@media" in style_content and "mobile" in style_content.split("@media")[1]
        has_gradient = "linear-gradient" in style_content
        
        # count rules
        rules = [r for r in style_content.split('}') if r.strip()]
        # :root is 1 rule
        # .hero is 1 rule
        # @media is 1 block, inside it has 1 rule (which counts as 1 main block for our purpose)
        # Actually it's easier to count { to estimate rules
        # Let's count non-nested blocks roughly, or just check if it's longer than expected.
        extra_rules = len(re.findall(r'\{', style_content)) > 4 # :root, .hero, @media, .hero inside @media = 4
        
        print(f"{path} | {'Yes' if has_accent else 'No'} | {'Yes' if has_desktop else 'No'} | {'Yes' if has_mobile else 'No'} | {'Yes' if has_gradient else 'No'} | {'Yes' if extra_rules else 'No'}")
    else:
        print(f"{path} | No | No | No | No | No")
