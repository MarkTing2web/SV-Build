import os
import shutil

repo_root = r"d:\Ler Wee Meng\Project-Web\SV-Build"
canonical_file1 = os.path.join(repo_root, "images", "insights", "securevision-insights.webp")
canonical_file2 = os.path.join(repo_root, "images", "insights", "securevision-insights-mobile.webp")

folders_to_delete = [
    "images/temp1",
    "images/temp-port-image",
    "images/temp insights images that did some work"
]

# 1. Pre-deletion confirmation
if not os.path.exists(canonical_file1):
    print("ERROR: Canonical file 1 does not exist:", canonical_file1)
    exit(1)

if not os.path.exists(canonical_file2):
    print("ERROR: Canonical file 2 does not exist:", canonical_file2)
    exit(1)

print("CONFIRMED: Both canonical insights hero images exist. Proceeding with deletion.")

total_freed_bytes = 0
folder_stats = {}

# 2. Perform deletion and calculate stats
for rel_folder in folders_to_delete:
    full_path = os.path.join(repo_root, rel_folder.replace('/', os.sep))
    if os.path.exists(full_path):
        file_count = 0
        folder_size = 0
        for root, dirs, files in os.walk(full_path):
            for f in files:
                file_count += 1
                folder_size += os.path.getsize(os.path.join(root, f))
                
        shutil.rmtree(full_path)
        total_freed_bytes += folder_size
        folder_stats[rel_folder] = file_count
    else:
        folder_stats[rel_folder] = 0

# 3. Post-deletion confirmation
exists_after = os.path.exists(canonical_file1)

# 4. Report
print("\n--- DELETION REPORT ---")
for folder, count in folder_stats.items():
    print(f"Deleted {count} files from /{folder}/")

print(f"\nTotal disk space freed: {total_freed_bytes / (1024*1024):.2f} MB")

if exists_after:
    print(f"\nPost-deletion confirmation: /images/insights/securevision-insights.webp STILL EXISTS.")
else:
    print(f"\nPost-deletion confirmation: ERROR - Canonical file is missing!")
