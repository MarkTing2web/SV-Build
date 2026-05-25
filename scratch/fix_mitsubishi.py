import os

filepath = r"c:\Projects\SV-Build\portfolio\industrial\mitsubishi-elevator-face-access-bms.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

mobile_path = '/images/portfolio/industrial/mitsubishi-elevator-singapore-mobile.webp'
if mobile_path not in content:
    css_block = f"""  <style>
  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{mobile_path}') !important;
    }}
  }}
  </style>
"""
    content = content.replace('</head>', css_block + '</head>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed mitsubishi")
