import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

filenames = []
for root, dirs, files in os.walk(images_dir):
    for f in files:
        filenames.append(f)

# Sort alphabetically
filenames.sort()

# Write to file
output_path = os.path.join(repo_root, "scratch", "all_image_filenames.txt")
with open(output_path, "w", encoding="utf-8") as f:
    for name in filenames:
        f.write(name + "\n")
    f.write(f"\nTotal files: {len(filenames)}\n")

print(f"Saved {len(filenames)} filenames to scratch/all_image_filenames.txt")
