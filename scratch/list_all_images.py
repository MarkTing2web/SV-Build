import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

filenames = []
for root, dirs, files in os.walk(images_dir):
    for f in files:
        filenames.append(f)

# Sort alphabetically
filenames.sort()

output_file = r"c:\Projects\SV-Build\scratch\list_all_images_output.txt"
with open(output_file, 'w', encoding='utf-8') as out_f:
    for name in filenames:
        out_f.write(f"{name}\n")
    out_f.write("\n")
    out_f.write(f"Total file count: {len(filenames)}\n")
