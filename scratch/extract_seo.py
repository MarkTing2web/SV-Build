import glob
import os

base_dir = "C:/Projects/SV-Build"
out_path = os.path.join(base_dir, "_ai/brands-seo-tags.md")
lines_out = ["```html"]

for f in sorted(glob.glob(os.path.join(base_dir, "brands/*.html"))):
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            if '<title>' in line or '<meta name="description"' in line:
                lines_out.append(line.strip())

lines_out.append("```")

with open(out_path, 'w', encoding='utf-8') as out_file:
    out_file.write("\n".join(lines_out))
