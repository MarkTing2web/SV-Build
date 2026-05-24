import os

target_dir = r"c:\Projects\SV-Build\images\solutions"
repo_root = r"c:\Projects\SV-Build"

all_files = []

for root, dirs, files in os.walk(target_dir):
    for file in files:
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, repo_root)
        # Convert backslashes to forward slashes and ensure it starts with /
        rel_path_formatted = "/" + rel_path.replace('\\', '/')
        all_files.append(rel_path_formatted)

all_files.sort()

for path in all_files:
    print(path)

print(f"\nTotal file count: {len(all_files)}")
