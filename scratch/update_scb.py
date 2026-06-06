import re

path = r"c:\Projects\SV-Build\portfolio\managed-living\scb-worker-dormitory-jalan-papan.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace desktop hero
desktop_str = ".portfolio-hero { background-image: url('/images/portfolio/managed-living/scb-worker-dormitory-hero.webp'); }"
# We need to find the existing `.portfolio-hero { ... }` that has background-image
# It could be `.portfolio-hero { background-image: url('something'); }`
# Let's just replace `.portfolio-hero { background-image: url(.*?); }` with the new one
content = re.sub(r'\.portfolio-hero\s*\{\s*background-image:\s*url\([^)]+\);\s*\}', desktop_str, content)

# Check mobile
mobile_str = """  @media (max-width: 768px) {
    .portfolio-hero { background-image: url('/images/portfolio/managed-living/scb-worker-dormitory-hero.webp'); background-position: center; }
  }"""
if "@media (max-width: 768px)" not in content:
    # Insert it before </style>
    content = content.replace("</style>", mobile_str + "\n</style>")
else:
    # Replace existing mobile
    content = re.sub(r'@media\s*\(\s*max-width:\s*768px\s*\)\s*\{[^}]+\}', mobile_str, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated SCB HTML")
