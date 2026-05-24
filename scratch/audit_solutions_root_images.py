import os

repo_root = r"c:\Projects\SV-Build"
solutions_root_dir = os.path.join(repo_root, "images", "solutions")

# Step 1: List files in root of images/solutions/ only
files_in_root = []
if os.path.exists(solutions_root_dir):
    for entry in os.scandir(solutions_root_dir):
        if entry.is_file():
            files_in_root.append(entry.name)

files_in_root.sort()

# Step 2: Gather all .html and .css files in the entire repo
exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'artifacts', '.github'}
search_files = []

for root, dirs, filenames in os.walk(repo_root):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for fn in filenames:
        if fn.endswith('.html') or fn.endswith('.css'):
            search_files.append(os.path.join(root, fn))

# Load content of all search files into memory to make search extremely fast
file_contents = {}
for sf in search_files:
    try:
        with open(sf, 'r', encoding='utf-8', errors='ignore') as f:
            file_contents[sf] = f.read()
    except Exception as e:
        pass

# Search each solution image filename in the file contents
usage_map = {img: [] for img in files_in_root}

for img in files_in_root:
    for sf, content in file_contents.items():
        if img in content:
            rel_sf = os.path.relpath(sf, repo_root).replace('\\', '/')
            usage_map[img].append(rel_sf)

# Step 3: Report results
used_count = 0
not_used_count = 0
not_used_list = []

for img in files_in_root:
    rel_img_path = f"/images/solutions/{img}"
    used_files = sorted(list(set(usage_map[img])))
    if used_files:
        print(f"{rel_img_path} — USED IN: {', '.join(used_files)}")
        used_count += 1
    else:
        print(f"{rel_img_path} — NOT USED")
        not_used_count += 1
        not_used_list.append(rel_img_path)

print("\n" + "="*50)
print(f"Total files in root: {len(files_in_root)}")
print(f"Used: {used_count}")
print(f"Not used: {not_used_count}")
print("List all not used files:")
for item in not_used_list:
    print(f"  - {item}")
