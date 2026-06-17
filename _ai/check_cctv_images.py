import os

base = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\resources\guides"

print(f"Checking: {base}")
print(f"Exists: {os.path.exists(base)}")
print()

if os.path.exists(base):
    print("Subfolders and file counts:")
    for folder in sorted(os.listdir(base)):
        fpath = os.path.join(base, folder)
        if os.path.isdir(fpath):
            files = [f for f in os.listdir(fpath)
                     if f.lower().endswith(('.webp','.jpg','.jpeg','.png'))]
            print(f"  {folder}/  ({len(files)} images)")
            for f in sorted(files):
                size = os.path.getsize(os.path.join(fpath, f))
                print(f"    {f}  ({size:,} bytes)")
        print()
