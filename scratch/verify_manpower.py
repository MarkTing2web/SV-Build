import re

with open("solutions/reduce-guard-manpower.html", encoding="utf-8") as fh:
    content = fh.read()

lviv    = "L'Viv" in content
proof   = "Proof of Outcome" in content
typical = "Typical Outcomes" in content
cards   = len(re.findall(r'<div class="card">', content))
grid    = "grid-3 mt-48" in content

print(f"L'Viv removed:          {not lviv}   (expected: True)")
print(f"Proof of Outcome gone:  {not proof}  (expected: True)")
print(f"Typical Outcomes added: {typical}   (expected: True)")
print(f"grid-3 mt-48 present:   {grid}   (expected: True)")
