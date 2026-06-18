import re

with open("solutions/data-centres.html", encoding="utf-8") as fh:
    content = fh.read()

faq_list   = "faq-list" in content
faq_grid   = "faq-grid faq-grid--single" in content
details    = "<details>" in content
faq_items  = len(re.findall(r'class="faq-item"', content))

print(f"faq-list present:              {faq_list}   (expected: False)")
print(f"faq-grid--single present:      {faq_grid}  (expected: True)")
print(f"<details> present:             {details}   (expected: False)")
print(f"faq-item count:                {faq_items}    (expected: 6)")
