import re

with open("solutions/improve-cctv-visibility.html", encoding="utf-8") as fh:
    content = fh.read()

old_cards  = len(re.findall(r'class="rel-card"', content))
has_block  = 'class="sv-solutions-block"' in content
has_all    = 'data-solutions="all"' in content
has_cols4  = 'data-cols="4"' in content
has_script = "solutions-block.js" in content

print(f"Old rel-cards remaining: {old_cards}   (expected: 0)")
print(f"sv-solutions-block:      {has_block}  (expected: True)")
print(f"data-solutions=all:      {has_all}  (expected: True)")
print(f"data-cols=4:             {has_cols4}  (expected: True)")
print(f"solutions-block.js:      {has_script}  (expected: True)")
