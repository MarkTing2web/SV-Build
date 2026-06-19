with open("solutions/commercial/commercial-security-systems.html", encoding="utf-8") as fh:
    content = fh.read()

wrong_path  = "/images/solutions/commercial/commercial-security-systems-hero.webp" in content
correct     = "/images/solutions/hero-solutions/commercial-security-systems-hero.webp" in content
mobile      = "commercial-security-systems-hero-mobile.webp" in content

print(f"Wrong path removed:    {not wrong_path}  (expected: True)")
print(f"Correct path present:  {correct}  (expected: True)")
print(f"Mobile image present:  {mobile}  (expected: True)")
