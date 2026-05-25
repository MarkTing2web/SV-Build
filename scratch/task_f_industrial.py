import os

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

count = 0
for filename in files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target_script = '<script src="/nav-footer.js"></script>'
    if '<script src="/portfolio-block.js"></script>' not in content:
        content = content.replace(target_script, '<script src="/portfolio-block.js"></script>\n  ' + target_script)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {filename}")

print(f"Task F updated {count} files.")
