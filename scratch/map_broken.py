import os, re

root = r'c:\Projects\SV-Build\portfolio\condominiums'
files = [f for f in os.listdir(root) if f.endswith('.html')]

broken_imgs = [
    "prop-condo.webp",
    "prop-commercial.webp",
    "portfolio-delias.webp",
    "portfolio-scape.webp",
    "de-elias-hero.webp",
    "trilliant-hero.webp",
    "sengkang-interim-thumb.webp",
    "surya-home-thumb.webp",
    "smartflex-thumb.webp"
]

for f in files:
    with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find all <a> blocks inside related projects
        matches = re.finditer(r'<a[^>]+href=[\'"]([^\'"]+)[\'"][^>]*>.*?<img[^>]+src=[\'"]([^\'"]+)[\'"]', content, re.DOTALL)
        for m in matches:
            href = m.group(1)
            img = m.group(2)
            if any(broken in img for broken in broken_imgs):
                print(f"[{f}] {img} -> links to {href}")
