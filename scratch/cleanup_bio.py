import os
import shutil

root_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
target = os.path.join(root_dir, "images", "ler-wee-meng-bio.webp")
source = os.path.join(root_dir, "images", "about", "ler-wee-meng-bio.webp")

if not os.path.exists(target):
    if os.path.exists(source):
        shutil.copy2(source, target)
        print(f"Copied: {source} -> {target}")
    else:
        print(f"Warning: Neither target nor source exists.")
else:
    print(f"Confirmed: {target} already exists.")

to_delete = [
    os.path.join(root_dir, "images", "about", "ler-wee-meng-bio.webp"),
    os.path.join(root_dir, "images", "Temp", "ler-wee-meng-bio.webp"),
    os.path.join(root_dir, "images", "Temp", "founder-wee-meng-headshot.webp"),
    os.path.join(root_dir, "images", "Temp", "founder-wee-meng-portrait.webp")
]

deleted_files = []
for file_path in to_delete:
    if os.path.exists(file_path):
        os.remove(file_path)
        deleted_files.append(file_path)

print("\nDeleted files:")
if deleted_files:
    for f in deleted_files:
        print(f"- {f}")
else:
    print("No duplicate files found to delete.")
