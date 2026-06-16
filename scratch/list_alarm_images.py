import os

folder = r"C:\Projects\SV-Build\images\resources\guides\alarm"

if os.path.exists(folder):
    files = sorted(os.listdir(folder))
    print(f"Folder: {folder}")
    print(f"Total files: {len(files)}")
    print()
    for f in files:
        full = os.path.join(folder, f)
        size = os.path.getsize(full)
        print(f"  {f}  ({size:,} bytes)")
else:
    print(f"FOLDER NOT FOUND: {folder}")
    # Check parent to see what's there
    parent = r"C:\Projects\SV-Build\images\resources\guides"
    if os.path.exists(parent):
        print(f"\nContents of parent {parent}:")
        for item in sorted(os.listdir(parent)):
            print(f"  {item}")
    else:
        print(f"Parent also not found: {parent}")
