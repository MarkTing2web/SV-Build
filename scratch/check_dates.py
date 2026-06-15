import os
import re
import glob

insights_dir = r"C:\Projects\SV-Build\insights"

html_files = glob.glob(os.path.join(insights_dir, '*.html'))

for filepath in sorted(html_files):
    slug = os.path.basename(filepath).replace('.html', '')
    if slug == 'index':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract published_time
    m1 = re.search(r'property=["\']article:published_time["\'][^>]*content=["\']([^"\']+)["\']', content)
    if not m1:
        m1 = re.search(r'content=["\']([^"\']+)["\'][^>]*property=["\']article:published_time["\']', content)
        
    # Extract datePublished
    m2 = re.search(r'"datePublished":\s*"([^"]+)"', content)
    
    # Extract byline date
    m3 = re.search(r'hero-byline-role[^>]*>(.*?)(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4})(.*?</p>)', content, re.DOTALL)
    
    published_time = m1.group(1) if m1 else "MISSING"
    date_published = m2.group(1) if m2 else "MISSING"
    byline_date = m3.group(2) if m3 else "MISSING"
    
    print(f"{slug}: pub_time={published_time}, ld={date_published}, byline={byline_date}")
