import os
from pathlib import Path

base_dir = Path(r"d:\Ler Wee Meng\Project-Web\SV-Build\images\resources")
paths = []

for root, _, files in os.walk(base_dir):
    for f in files:
        filepath = Path(root) / f
        rel_path = filepath.relative_to(base_dir.parent.parent).as_posix()
        paths.append(f"/{rel_path}")

paths.sort()
for p in paths:
    print(p)
print(f"\nTotal count: {len(paths)}")
