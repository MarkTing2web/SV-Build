import os

files = [
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\rackmount-nvr.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\security-upgrade-condo-agm.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\mcst-legal-obligations-security.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\standalone-door-access.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\reduce-false-alarms.html"
]

print("STEP 2 OUTPUT:\n")
for filepath in files:
    filename = os.path.basename(filepath)
    print(f"--- {filename} ---")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if 'images/insights' in line:
                    print(f"Line {i+1}: {line.strip()}")
    else:
        print("File not found")
    print("")

print("\nSTEP 3 OUTPUT:\n")
image_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights"
existing_images = set(os.listdir(image_dir))

for filepath in files:
    filename = os.path.basename(filepath)
    print(f"--- {filename} ---")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            img_files = re.findall(r'images/insights/([^"\'\s>]+)', content)
            unique_imgs = set(img_files)
            for img in unique_imgs:
                status = "EXISTS" if img in existing_images else "MISSING"
                print(f"{img}: {status}")
    print("")

