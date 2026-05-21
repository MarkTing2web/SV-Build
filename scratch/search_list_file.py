import os

repo_root = r"c:\Projects\SV-Build"
list_file = os.path.join(repo_root, "scratch", "all_image_filenames.txt")

keywords = ["data-centre", "healthcare", "industrial", "reduce-manpower"]

with open(list_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    for kw in keywords:
        # replace hyphen with space or underscore just in case
        if kw.lower() in line.lower() or kw.lower().replace("-", " ") in line.lower() or kw.lower().replace("-", "_") in line.lower():
            print(f"MATCH in list: {line}")
            break
