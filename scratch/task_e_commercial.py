import os

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

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target = '<script src="/nav-footer.js"></script>'
    
    if '<script src="/portfolio-block.js"></script>' not in content:
        content = content.replace(target, '<script src="/portfolio-block.js"></script>\n  ' + target)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task E updated {count} files.")
