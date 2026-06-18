import re

with open("solutions/institutions.html", encoding="utf-8") as fh:
    content = fh.read()

cards = re.findall(
    r'<div class="sol-card-flush[^>]*>.*?</div>\s*</div>',
    content, re.S
)

for i, card in enumerate(cards[:3], 1):
    src = re.search(r'src="([^"]+)"', card)
    h3  = re.search(r'<h3>(.*?)</h3>', card)
    print(f"Card {i}: {h3.group(1) if h3 else 'n/a'}")
    print(f"  src: {src.group(1) if src else 'n/a'}")
