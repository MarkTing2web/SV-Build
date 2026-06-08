from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_pgrid = False
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if attrs_dict.get('id') == 'pGrid':
            self.in_pgrid = True
            
        if self.in_pgrid and tag == 'a':
            classes = attrs_dict.get('class', '').split()
            if 'project-card' in classes:
                if 'href' in attrs_dict:
                    self.hrefs.append(attrs_dict['href'])

parser = MyHTMLParser()
file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    parser.feed(f.read())

for href in sorted(parser.hrefs):
    print(href)
