import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

repo_root = r"C:\Projects\SV-Build"
images_dir = r"C:\Projects\SV-Build\images\insights"

# Step 1: Get all webp files in images/insights (non-recursive)
disk_files = []
for entry in os.scandir(images_dir):
    if entry.is_file() and entry.name.lower().endswith('.webp'):
        disk_files.append(entry.name)

disk_files = sorted(disk_files)

# Step 2: Read contents of all files where references could exist
# We will search these file contents for the filenames.
search_texts = []

# Helper to load file content safely
def load_file_content(path, encoding='utf-8'):
    if not os.path.exists(path):
        return ""
    try:
        with open(path, 'r', encoding=encoding) as f:
            return f.read()
    except Exception:
        # Fallback to latin-1 if utf-8 fails
        try:
            with open(path, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception:
            return ""

# A. Insights html files recursively
for root, dirs, files in os.walk(os.path.join(repo_root, "insights")):
    for file in files:
        if file.endswith('.html'):
            search_texts.append(load_file_content(os.path.join(root, file)))

# B. site-config.js (loaded as UTF-16)
search_texts.append(load_file_content(os.path.join(repo_root, "site-config.js"), encoding='utf-16'))

# C. Root and other html files recursively (skip insights since we already loaded it, but let's just do all html files in repo)
for root, dirs, files in os.walk(repo_root):
    # Skip node_modules and .git folders
    if 'node_modules' in root or '.git' in root or '.vercel' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            # If not already loaded under insights
            full_path = os.path.join(root, file)
            if not full_path.startswith(os.path.join(repo_root, "insights")):
                search_texts.append(load_file_content(full_path))

# D. nav-footer.js
search_texts.append(load_file_content(os.path.join(repo_root, "nav-footer.js")))

# Join all search texts for fast substring checking
all_search_text = "\n".join(search_texts)

# Step 3: Find orphans
orphans = []
referenced = []

for filename in disk_files:
    # If the filename appears anywhere in the combined search text, it is referenced
    if filename in all_search_text:
        referenced.append(filename)
    else:
        orphans.append(filename)

# Generate output content
output_lines = [
    "# Orphan Images — Safe to Delete",
    f"Total files on disk: {len(disk_files)}",
    f"Total files referenced: {len(referenced)}",
    f"Total orphans: {len(orphans)}",
    "",
    "## Files to delete",
    ""
]

for filename in orphans:
    output_lines.append(f'del "C:\\Projects\\SV-Build\\images\\insights\\{filename}"')

output_path = os.path.join(repo_root, "orphan-images-final.md")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(output_lines))

print(f"Total files on disk: {len(disk_files)}")
print(f"Total files referenced: {len(referenced)}")
print(f"Total orphans found: {len(orphans)}")
