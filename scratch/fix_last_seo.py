import os
from bs4 import BeautifulSoup

RESOURCES_DIR = r"C:\Projects\SV-Build\resources"

SEO_DATA = {
    "faq.html": {
        "title": "Security System FAQ For Singapore | Securevision SG",
    },
    "library.html": {
        "title": "Security System Product Library Singapore | Securevision",
    },
    "intercom-guide.html": {
        "title": "Intercom & Video Entry Guide Singapore | Securevision",
    }
}

for root, dirs, files in os.walk(RESOURCES_DIR):
    for fname in files:
        if fname in SEO_DATA:
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
            
            title = SEO_DATA[fname]['title']
            if soup.title:
                soup.title.string = title
            
            og_title = soup.find("meta", attrs={"property": "og:title"})
            if og_title:
                og_title["content"] = title
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

print("Fixed the last 3 SEO lengths.")
