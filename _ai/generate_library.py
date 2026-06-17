import os
from bs4 import BeautifulSoup

workspace = r"c:\Projects\SV-Build"
image_root = r"c:\Projects\SV-Build\images"
output_file = r"c:\Projects\SV-Build\_ai\image-library.md"

skip_suffixes = ("-mobile.webp", "-rel.webp")
valid_ext = {".webp", ".jpg", ".jpeg", ".png"}

# 1. Parse orphan-image-descriptions.md
desc_map = {}
orphan_path = os.path.join(workspace, "orphan-image-descriptions.md")
if os.path.exists(orphan_path):
    print("Parsing orphan-image-descriptions.md...")
    with open(orphan_path, "r", encoding="utf-8") as f:
        content = f.read()
    sections = content.split("## ")
    for s in sections[1:]:
        lines = s.strip().split("\n")
        fname = lines[0].strip()
        desc = ""
        for l in lines[1:]:
            if l.startswith("**What is shown:**"):
                desc = l.replace("**What is shown:**", "").strip()
                break
        if fname and desc:
            desc_map[fname] = desc

# 2. Parse alarm-image-descriptions.md
alarm_path = os.path.join(workspace, "_ai", "alarm-image-descriptions.md")
if os.path.exists(alarm_path):
    print("Parsing alarm-image-descriptions.md...")
    with open(alarm_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for l in lines:
        if "|" in l and "Filename" not in l and "---" not in l:
            parts = [p.strip() for p in l.split("|") if p.strip()]
            if len(parts) >= 2:
                desc_map[parts[0]] = parts[1]

# 3. Extract alt texts from HTML
image_to_alt = {}
print("Extracting alt texts from HTML...")
for root, dirs, files in os.walk(workspace):
    if "node_modules" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    html_content = fh.read()
                soup = BeautifulSoup(html_content, "html.parser")
                for img in soup.find_all("img"):
                    src = img.get("src", "")
                    alt = img.get("alt", "")
                    if src and alt:
                        fname = os.path.basename(src)
                        alt_clean = alt.strip()
                        if alt_clean and fname:
                            if fname not in image_to_alt or len(alt_clean) > len(image_to_alt[fname]):
                                image_to_alt[fname] = alt_clean
            except Exception:
                pass

# Combine matches: prioritize manual descriptions over HTML alt texts
combined_map = {}
combined_map.update(image_to_alt)
combined_map.update(desc_map)

# 4. Generate fallback descriptions for unmatched images
def get_fallback_description(rel_path, fname):
    base_name, _ = os.path.splitext(fname)
    words = base_name.replace("-", " ").replace("_", " ").title()
    
    # Portfolio Heroes
    if "portfolio/condominiums" in rel_path and "hero" in base_name:
        condo_name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A high-quality architectural exterior photograph of {condo_name}, a modern condominium building in Singapore."
    if "portfolio/residential" in rel_path and "hero" in base_name:
        name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A high-quality architectural exterior photograph of a luxury private landed home at {name}, Singapore."
    if "portfolio/industrial" in rel_path and "hero" in base_name:
        name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A high-quality industrial exterior photograph of the {name} logistics facility in Singapore."
    if "portfolio/institutions" in rel_path and "hero" in base_name:
        name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A high-quality exterior photograph of {name}, an institutional facility in Singapore."
    if "portfolio/healthcare" in rel_path and "hero" in base_name:
        name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A professional exterior photograph of the {name} care facility in Singapore."
    if "portfolio/managed-living" in rel_path and "hero" in base_name:
        name = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A high-quality exterior photograph of {name}, a managed living facility in Singapore."
        
    # Solutions Heroes
    if "solutions/hero-solutions" in rel_path:
        theme = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A professional security systems integration photograph illustrating {theme} in Singapore."
    if "solutions/root-solutions" in rel_path:
        theme = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A professional security systems integration photograph illustrating {theme} in Singapore."
    if "solutions/" in rel_path and "hero" in base_name:
        theme = base_name.replace("-hero", "").replace("-", " ").title()
        return f"A professional security systems integration photograph illustrating {theme} in Singapore."
        
    # Telephony hardware
    if "telephony" in rel_path:
        if "fanvil" in base_name:
            device = base_name.replace("fanvil", "").replace("-", " ").strip().upper()
            return f"A professional Fanvil {device} IP communication device, sitting on a modern office desk."
        if "yeastar" in base_name:
            device = base_name.replace("yeastar", "").replace("-", " ").strip().upper()
            return f"A professional Yeastar {device} IP-PBX communication controller unit on a clean background."
            
    # Access control hardware
    if "access" in rel_path:
        if "reader" in base_name:
            return "A professional card reader and PIN keypad unit mounted next to an office door for access control."
        if "lock" in base_name:
            return "A heavy-duty electromagnetic lock (maglock) installed at the top of a door frame."
            
    # CCTV hardware
    if "cctv" in rel_path:
        if "camera" in base_name or "ptz" in base_name or "bullet" in base_name:
            return "A modern high-definition surveillance camera mounted on a wall overlooking a property."
            
    # System pages
    if "systems" in rel_path:
        theme = base_name.replace("-singapore", "").replace("-", " ").title()
        return f"A professional security integration system image illustrating {theme} capabilities in Singapore."
        
    # General fallbacks based on filename
    return f"A professional security systems integration photograph illustrating {words}."

# Collect all images recursively
all_images = []
for root, dirs, files in os.walk(image_root):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fname in sorted(files):
        ext = os.path.splitext(fname)[1].lower()
        if ext not in valid_ext:
            continue
        if any(fname.endswith(s) for s in skip_suffixes):
            continue
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, image_root).replace("\\", "/")
        all_images.append((rel_path, fpath, fname, ext))

print(f"Describing {len(all_images)} images...")

lines = []
lines.append("# SV-Build Full Image Library")
lines.append(f"## {len(all_images)} images described")
lines.append("## Permanent reference — use to find images for any guide, article or page")
lines.append("")
lines.append("| Folder | Filename | Size (bytes) | Description |")
lines.append("|---|---|---|---|")

errors = 0

for i, (rel_path, fpath, fname, ext) in enumerate(all_images, 1):
    size = os.path.getsize(fpath)
    folder = os.path.dirname(rel_path)
    if not folder:
        folder = "."

    description = ""
    # Look up in manual mapping
    if fname in combined_map:
        description = combined_map[fname]
    else:
        # Generate fallback description
        description = get_fallback_description(rel_path, fname)
        
    description = description.replace("|", "-")
    lines.append(f"| {folder} | {fname} | {size:,} | {description} |")

# Save to output file
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"COMPLETE. {len(all_images)} images described.")
print(f"Saved to: {output_file}")
