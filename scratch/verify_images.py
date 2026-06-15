import urllib.request
import urllib.error
import os
import re

files = [
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\rackmount-nvr.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\security-upgrade-condo-agm.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\mcst-legal-obligations-security.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\standalone-door-access.html",
    r"d:\Ler Wee Meng\Project-Web\SV-Build\insights\reduce-false-alarms.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
base_url = "http://localhost:3000"

for filepath in files:
    slug = os.path.basename(filepath).replace(".html", "")
    print(f"--- Article: {slug} ---")
    
    if not os.path.exists(filepath):
        print("File not found")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image tags
    img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    
    for src in img_tags:
        filename = os.path.basename(src)
        
        # 1. Check localhost
        url = base_url + src
        status = "Unknown"
        try:
            req = urllib.request.Request(url, method="HEAD")
            with urllib.request.urlopen(req) as response:
                status = str(response.status)
        except urllib.error.HTTPError as e:
            status = str(e.code)
        except urllib.error.URLError as e:
            status = "Connection Failed"

        # 2. Check disk
        local_path = os.path.join(base_dir, src.lstrip('/\\').replace('/', '\\'))
        disk_status = "EXISTS" if os.path.exists(local_path) else "MISSING"
        size_info = ""
        if disk_status == "EXISTS":
            size_info = f" ({os.path.getsize(local_path)} bytes)"
            
        if status != "200" or disk_status == "MISSING" or (disk_status == "EXISTS" and os.path.getsize(local_path) == 0):
            print(f"- {filename} [Status: {status}] [Disk: {disk_status}{size_info}]")
    
    print("")

