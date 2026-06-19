with open("solutions/commercial/office.html", encoding="utf-8") as fh:
    content = fh.read()

duplicate = content.count("solution-commercial-office-cover.webp")
access_img = "office-access-control-intercom-singapore.webp" in content
cctv_img   = "solution-commercial-pillar_surveillance.webp" in content

print(f"Duplicate image removed: {duplicate == 0}  (expected: True)")
print(f"Access image present:    {access_img}  (expected: True)")
print(f"CCTV image present:      {cctv_img}  (expected: True)")
