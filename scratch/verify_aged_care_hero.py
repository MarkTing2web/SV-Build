import os

with open("solutions/healthcare/aged-care.html", encoding="utf-8") as fh:
    content = fh.read()

correct = "solution-healthcare-aged-care-hero.webp" in content
mobile  = "solution-healthcare-aged-care-hero-mobile.webp" in content
desktop_file = os.path.exists("images/solutions/hero-solutions/solution-healthcare-aged-care-hero.webp")
mobile_file  = os.path.exists("images/solutions/hero-solutions/solution-healthcare-aged-care-hero-mobile.webp")

print(f"Desktop path in HTML:  {correct}  (expected: True)")
print(f"Mobile path in HTML:   {mobile}  (expected: True)")
print(f"Desktop image on disk: {desktop_file}  (expected: True)")
print(f"Mobile image on disk:  {mobile_file}  (expected: True)")
