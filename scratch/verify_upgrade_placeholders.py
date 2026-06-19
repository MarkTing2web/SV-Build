with open("solutions/upgrade-intercom-system.html", encoding="utf-8") as fh:
    content = fh.read()

placeholders = content.count("card-img-placeholder")
qr_img   = "solution-upgrade-intercom-system-qr-visitor-access.webp" in content
cable_img = "solution-upgrade-intercom-system-cabling-reuse.webp" in content

print(f"Placeholders remaining: {placeholders}  (expected: 0)")
print(f"QR image present:       {qr_img}  (expected: True)")
print(f"Cable image present:    {cable_img}  (expected: True)")
