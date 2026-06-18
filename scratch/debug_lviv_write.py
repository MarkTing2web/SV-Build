import re

path = 'C:/Projects/SV-Build/portfolio/condominiums/the-lviv-newton-condo.html'
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()

print("Initial len:", len(content))
print("Initial application/ld+json in content:", "application/ld+json" in content)

cfg = {
    "headline": "L'viv Residences — Modernising Condo Security for Smarter Living",
    "description": "How Securevision approached estate video intercom and biometric access upgrade for L'viv Residences MCST in Newton Road,",
    "about": "Estate video intercom and biometric access upgrade — Residential / Luxury Condominium — Singapore",
    "location": "Newton Road, Singapore",
    "keywords": "luxury condominium security Singapore, video intercom, biometric access control",
    "url": "https://www.securevision.com.sg/portfolio/the-lviv-newton-condo.html",
    "image_path": "/images/portfolio/condominiums/the-lviv-hero.webp"
}

schema_template = """  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{headline}",
    "description": "{description}",
    "author": {{
      "@type": "Person",
      "name": "Ler Wee Meng",
      "jobTitle": "Founder & Director"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Securevision Pte Ltd",
      "url": "https://www.securevision.com.sg"
    }},
    "about": "{about}",
    "locationCreated": {{
      "@type": "Place",
      "name": "{location}",
      "addressCountry": "SG"
    }},
    "keywords": "{keywords}",
    "url": "{url}"
  }}
  </script>
"""

if "application/ld+json" not in content:
    schema_code = schema_template.format(
        headline=cfg["headline"],
        description=cfg["description"],
        about=cfg["about"],
        location=cfg["location"],
        keywords=cfg["keywords"],
        url=cfg["url"]
    )
    content = content.replace("</head>", schema_code + "</head>")
    print("Schema inserted. New len:", len(content))

content, count = re.subn(r'<style>.*?</style>', '<style>:root { --page-accent: #0056b3; }</style>', content, flags=re.DOTALL)
print("Style replaced count:", count)

header_regex = r'(<header\s+class="[^"]*hero-[a-zA-Z0-9\-]+"[^>]*)>'
style_attr = f' style="background: linear-gradient(to right, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.40) 50%, rgba(0,0,0,0.10) 100%), url(\'{cfg["image_path"]}\') center/cover no-repeat;"'

header_match = re.search(header_regex, content)
if header_match:
    matched_header = header_match.group(1)
    print("Matched header:", matched_header)
    if "style=" not in matched_header:
        content = re.sub(header_regex, rf'\1{style_attr}>', content, count=1)
        print("Header styled. New len:", len(content))
    else:
        print("Style already in matched header.")
else:
    print("No header match!")

with open(path, 'w', encoding='utf-8') as file:
    file.write(content)
print("File written.")
