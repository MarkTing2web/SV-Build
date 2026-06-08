from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_pgrid = False
        self.in_fyear = False
        self.pgrid_depth = 0
        self.hrefs = []
        self.years = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'pGrid':
            self.in_pgrid = True
            self.pgrid_depth = 1
        elif self.in_pgrid and tag == 'div':
            self.pgrid_depth += 1
            
        if self.in_pgrid and tag == 'a':
            classes = attrs_dict.get('class', '').split()
            if 'project-card' in classes:
                if 'href' in attrs_dict:
                    self.hrefs.append(attrs_dict['href'])
                    
        if attrs_dict.get('id') == 'fYear':
            self.in_fyear = True
            
        if self.in_fyear and tag == 'option':
            if 'value' in attrs_dict:
                self.years.append(attrs_dict['value'])

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_pgrid:
            self.pgrid_depth -= 1
            if self.pgrid_depth == 0:
                self.in_pgrid = False
        if tag == 'select' and self.in_fyear:
            self.in_fyear = False

parser = MyHTMLParser()
with open(r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html", "r", encoding="utf-8") as f:
    parser.feed(f.read())

print(f"Total cards: {len(parser.hrefs)}")
for i, href in enumerate(parser.hrefs):
    if href == "/portfolio/commercial/scape-commercial.html":
        print(f"After scape-commercial: {parser.hrefs[i+1]}")
    if href == "/portfolio/data-centres/fort-data-centre-access-upgrade.html":
        print(f"After fort-data-centre: {parser.hrefs[i+1]}")
    if href == "/portfolio/commercial/catholic-centre-security-partnership.html":
        print(f"After catholic-centre: {parser.hrefs[i+1]}")
        
print(f"Last card: {parser.hrefs[-1]}")
print(f"Years: {parser.years}")
