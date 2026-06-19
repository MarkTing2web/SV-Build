import re

with open("solutions/automate-vehicle-access.html", encoding="utf-8") as fh:
    content = fh.read()

# Problem section paragraphs
m = re.search(r'The Problem.*?</section>', content, re.S)
paras = len(re.findall(r'class="section-intro"', m.group(0))) if m else 0

# FAQ
faq_items = len(re.findall(r'class="faq-item"', content))
gantrygo  = "GantryGo" in content
vesta     = "VESTA" in content
single    = "faq-grid--single" in content

print(f"Problem section paragraphs: {paras}  (expected: 3)")
print(f"FAQ items:                  {faq_items}  (expected: 5)")
print(f"GantryGo removed:           {not gantrygo}  (expected: True)")
print(f"VESTA removed:              {not vesta}  (expected: True)")
print(f"faq-grid--single:           {single}  (expected: True)")
