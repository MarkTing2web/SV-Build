with open("solutions/condominiums/condominium-security-systems.html", encoding="utf-8") as fh:
    content = fh.read()

wrong  = "/images/solutions/condominiums/condominium-security-systems-hero.webp" in content
correct = "/images/solutions/hero-solutions/condominium-security-systems-hero.webp" in content
mobile  = "condominium-security-systems-hero-mobile.webp" in content

print(f"Wrong path removed:    {not wrong}  (expected: True)")
print(f"Correct path present:  {correct}  (expected: True)")
print(f"Mobile image present:  {mobile}  (expected: True)")
