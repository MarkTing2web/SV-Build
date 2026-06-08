from bs4 import BeautifulSoup

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
pgrid = soup.find(id="pGrid")

if pgrid:
    links = pgrid.find_all("a", class_="project-card", recursive=False)
    print(f"Total cards strictly inside #pGrid: {len(links)}")
    
    for i, link in enumerate(links):
        href = link.get('href')
        if href == "/portfolio/commercial/scape-commercial.html":
            print(f"After scape-commercial: {links[i+1].get('href')}")
        if href == "/portfolio/data-centres/fort-data-centre-access-upgrade.html":
            print(f"After fort-data-centre: {links[i+1].get('href')}")
        if href == "/portfolio/commercial/catholic-centre-security-partnership.html":
            print(f"After catholic-centre: {links[i+1].get('href')}")
            
    print(f"Last card: {links[-1].get('href')}")

fyear = soup.find(id="fYear")
if fyear:
    opts = [opt.get('value') for opt in fyear.find_all('option')]
    print(f"Years: {opts}")
