import re

text = """
    :root { --page-accent: #0056b3; }
    .hero-commercial { background-image: url('/images/solutions/hero-solutions/commercial-security-singapore.webp'); }
    @media (max-width: 768px) {
      .hero-commercial { background-image: url('/images/solutions/hero-solutions/commercial-security-singapore-mobile.webp'); }
    }
"""

stripped = re.sub(r':root\s*\{[^}]*\}', '', text)
print(f"After root:\n{stripped}")
stripped = re.sub(r'\.hero-[^\s{]+\s*\{[^}]*\}', '', stripped)
print(f"After hero:\n{stripped}")
stripped = re.sub(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', '', stripped)
print(f"After media:\n{stripped}")
print(f"Final stripped length: {len(stripped.strip())}")
print(repr(stripped.strip()))
