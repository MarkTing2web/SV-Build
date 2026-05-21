import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

filenames = []
for root, dirs, files in os.walk(images_dir):
    for f in files:
        filenames.append(f)

# Sort alphabetically
filenames.sort()

# Print each filename
for name in filenames:
    print(name)

# Print summary
print()
print("Total files:", len(filenames))
