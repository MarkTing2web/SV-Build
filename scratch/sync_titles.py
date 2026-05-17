import os
import re

repo_root = r"c:\Projects\SV-Build"
insights_dir = os.path.join(repo_root, "insights")

exclude_files = ["index.html", "index-od1.html", "index-od2.html"]

count = 0

for filename in os.listdir(insights_dir):
    if not filename.endswith(".html") or filename in exclude_files:
        continue
        
    filepath = os.path.join(insights_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    h1_match = re.search(r'<h1 class="insights-header-title">(.*?)</h1>', content)
    if h1_match:
        h1_title = h1_match.group(1).strip()
        new_title = f"{h1_title} | Securevision Insights"
        
        # update <title>
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, count=1, flags=re.DOTALL)
        
        # update og:title
        content = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{new_title}">', content, count=1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Synced titles in {count} insight files.")
