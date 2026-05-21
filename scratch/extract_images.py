import os
import re
from pathlib import Path

base_dir = Path(r"d:\Ler Wee Meng\Project-Web\SV-Build\resources")

image_patterns = [
    r'<img[^>]+src=["\'](.*?)["\']',
    r'<source[^>]+srcset=["\'](.*?)["\']',
    r'background-image:\s*url\([\'"]?(.*?)[\'"]?\)',
    r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']',
    r'<meta[^>]+name=["\']og:image["\'][^>]+content=["\'](.*?)["\']',
    r'<meta[^>]+content=["\'](.*?)["\'][^>]+property=["\']og:image["\']',
    r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']og:image["\']',
    r'data-src=["\'](.*?)["\']'
]

results = {}
all_images = set()

exclude_image = "/images/ler-wee-meng-bio.webp"
domain = "https://www.securevision.com.sg"

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = Path(root) / file
            rel_path = filepath.relative_to(base_dir.parent).as_posix()
            
            try:
                content = filepath.read_text(encoding='utf-8')
            except Exception:
                continue
            
            file_images = []
            
            for pattern in image_patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    url = match.group(1).strip()
                    if url.startswith(domain):
                        url = url[len(domain):]
                    
                    urls = []
                    if 'srcset' in pattern:
                        for part in url.split(','):
                            part = part.strip()
                            if part:
                                urls.append(part.split(' ')[0])
                    else:
                        urls.append(url)
                        
                    for u in urls:
                        if not u.startswith('/images/'):
                            continue
                        if u == exclude_image:
                            continue
                        file_images.append(u)
                        all_images.add(u)
            
            if file_images:
                results[rel_path] = sorted(list(set(file_images)))

for rel_path in sorted(results.keys()):
    print(f"FILE: {rel_path}")
    for img in results[rel_path]:
        print(f"  {img}")

print("\n--- UNIQUE IMAGES ---")
sorted_all = sorted(list(all_images))
for img in sorted_all:
    print(img)
print(f"Total count: {len(sorted_all)}")
