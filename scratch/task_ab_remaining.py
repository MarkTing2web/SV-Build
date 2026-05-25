import os

base_dir = r"c:\Projects\SV-Build"

task_a_files = {
    'portfolio/industrial/cogent-logistics-hub-cctv.html': '/images/portfolio/industrial/cogent-1-logistics-hub-mobile.webp',
    'portfolio/industrial/cyrus-tech-industrial.html': '/images/portfolio/industrial/cyrus-tech-at-loyang-mobile.webp',
    'portfolio/industrial/hoy-san-industrial.html': '/images/portfolio/industrial/hoy-san-mobile.webp',
    'portfolio/industrial/mitsubishi-elevator-face-access-bms.html': '/images/portfolio/industrial/mitsubishi-elevator-singapore-mobile.webp',
    'portfolio/industrial/multibase-construction-security-upgrade.html': '/images/portfolio/industrial/multibase-construction-mobile.webp',
    'portfolio/industrial/smartflex-tampines.html': '/images/portfolio/industrial/smartflex-at-tampines-mobile.webp',
    'portfolio/industrial/sta-inspection-industrial.html': '/images/portfolio/industrial/sta-inspection-centre-sin-ming-mobile.webp',
    'portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html': '/images/portfolio/industrial/st-microelectronics-loyang-mobile.webp'
}

count_a = 0
for rel_path, mobile_path in task_a_files.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    css_block = f"""
  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{mobile_path}') !important;
    }}
  }}
"""
    if mobile_path not in content:
        content = content.replace('</style>', css_block + '</style>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count_a += 1
        print(f"Added mobile override to {rel_path}")
    else:
        count_a += 1
        print(f"Mobile override already exists in {rel_path} (counted as updated)")

print(f"Task A updated {count_a} files.")

task_b_files = [
    'portfolio/industrial/sta-compliance-imaging.html',
    'portfolio/industrial/sta-inspection-industrial.html'
]

scripts_block = """<script src="/systems-block.js"></script>
<script src="/portfolio-block.js"></script>
<script src="/nav-footer.js"></script>
"""

count_b = 0
for rel_path in task_b_files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script src="/systems-block.js"></script>' not in content:
        content = content.replace('</body>', scripts_block + '</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count_b += 1
        print(f"Added script tags to {rel_path}")
    else:
        count_b += 1
        print(f"Script tags already exist in {rel_path} (counted as updated)")

print(f"Task B updated {count_b} files.")
