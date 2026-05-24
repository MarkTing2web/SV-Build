import os

repo_root = r"c:\Projects\SV-Build"
target_dir = os.path.join(repo_root, "images", "solutions")

all_files = []
for root, dirs, files in os.walk(target_dir):
    for f in files:
        full_path = os.path.join(root, f)
        # Compute path relative to repo root, replacing backslashes with forward slashes
        rel_path = os.path.relpath(full_path, start=repo_root)
        rel_path = "/" + rel_path.replace('\\', '/')
        all_files.append(rel_path)

all_files.sort()

output_file = r"c:\Projects\SV-Build\scratch\list_solution_images_output.txt"
with open(output_file, 'w', encoding='utf-8') as out_f:
    for f in all_files:
        out_f.write(f"{f}\n")
    out_f.write("\n")
    out_f.write(f"Total file count: {len(all_files)}\n")
