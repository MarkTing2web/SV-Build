import os
import glob
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def fix_founder_card(soup, changed):
    fc = soup.find(class_="founder-card")
    if fc:
        # Check if it has sv-years-experience
        if not fc.find(class_=re.compile(r"sv-years-experience")):
            # It usually has text like: 37+ Years
            # Let's just find the text node and replace it.
            for el in fc.find_all(["p", "span", "div"]):
                if "37+ Years" in el.get_text():
                    # Need to replace the text carefully
                    new_html = str(el).replace("37+ Years", "<span class=\"sv-years-experience\"></span> Years")
                    # parse it and replace
                    new_tag = BeautifulSoup(new_html, "html.parser").contents[0]
                    el.replace_with(new_tag)
                    changed[0] = True

def update_seo(soup, title, desc):
    # Update <title>
    title_tag = soup.find("title")
    if title_tag:
        title_tag.string = title
    else:
        new_title = soup.new_tag("title")
        new_title.string = title
        soup.head.append(new_title)

    # Update meta description
    desc_tag = soup.find("meta", {"name": "description"})
    if not desc_tag:
        desc_tag = soup.find("meta", {"name": "Description"})
    if desc_tag:
        desc_tag["content"] = desc

    # Update og:title
    og_title = soup.find("meta", {"property": "og:title"})
    if og_title:
        og_title["content"] = title

    # Update og:description
    og_desc = soup.find("meta", {"property": "og:description"})
    if og_desc:
        og_desc["content"] = desc

def process_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    changed = [False]
    fix_founder_card(soup, changed)

    filename = os.path.basename(fpath)
    if filename == "lpr-vs-rfid-vehicle-access-singapore.html":
        update_seo(soup, 
                   "LPR vs RFID Vehicle Access in Singapore | Securevision", 
                   "Compare LPR and RFID vehicle access control systems for Singapore condos and offices. Learn about costs, reliability, and security benefits.")
        changed[0] = True
    elif filename == "pdpa-cctv-singapore.html":
        update_seo(soup, 
                   "PDPA & CCTV Guidelines for Singapore | Securevision", 
                   "Understand PDPA requirements for CCTV installation in Singapore properties. Learn about legal obligations, signage, and data protection rules.")
        changed[0] = True
    elif filename == "video-analytics-retail-singapore.html":
        update_seo(soup, 
                   "Video Analytics for Singapore Retailers | Securevision", 
                   "Discover how retail video analytics can boost sales, reduce shrinkage, and provide customer insights for your Singapore business.")
        changed[0] = True

    if changed[0]:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))

if __name__ == "__main__":
    for fpath in glob.glob(os.path.join(INSIGHTS_DIR, "*.html")):
        process_file(fpath)
    print("Phase 6 SEO fixes and sv-years batch fix applied.")
