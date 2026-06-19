import re

with open("solutions/improve-cctv-visibility.html", encoding="utf-8") as fh:
    content = fh.read()

m = re.search(r'Strategic Outcomes.*?</section>', content, re.S)
section = m.group(0) if m else ""

cards       = len(re.findall(r'<div class="card">', section))
squares     = len(re.findall(r'card-img-wrap--square', section))
non_squares = len(re.findall(r'"card-img-wrap"', section))
colorvu     = "ColorVu" in section
acusense    = "AcuSense" in section
storage     = "cctv-storage-square.webp" in section

print(f"Cards in section:        {cards}   (expected: 6)")
print(f"Square img wrappers:     {squares}  (expected: 6)")
print(f"Non-square img wrappers: {non_squares}  (expected: 0)")
print(f"ColorVu removed:         {not colorvu}  (expected: True)")
print(f"AcuSense removed:        {not acusense}  (expected: True)")
print(f"Storage card image:      {storage}  (expected: True)")
