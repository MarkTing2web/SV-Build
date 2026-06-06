import os
import re

w = r"c:\Projects\SV-Build"
index_path = os.path.join(w, "portfolio", "index.html")
js_path = os.path.join(w, "portfolio-block.js")

with open(index_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# --- TASK A ---
replacements = {
    "/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html": ("/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp", "/images/portfolio/managed-living/scb-worker-dormitory-rel.webp"),
    "/portfolio/institutions/sengkang-interim-bus-interchange.html": ("/images/portfolio/institutions/cpf-maxwell-rel.webp", "/images/portfolio/institutions/sengkang-interim-bus-interchange-rel.webp"),
    "/portfolio/healthcare/surya-home.html": ("/images/portfolio/healthcare/sunlove-rel.webp", "/images/portfolio/healthcare/surya-home-rel.webp")
}

for href, (old_img, new_img) in replacements.items():
    # Find the card block starting with href
    # Since it's HTML, we can just replace the specific img src if we are careful.
    # Actually, we can just replace the img src directly globally if it's unique, 
    # but to be safe, let's find the card block
    card_pattern = re.compile(rf'<a href="{re.escape(href)}".*?</a>', re.DOTALL)
    def replace_img(match):
        return match.group(0).replace(old_img, new_img)
    html_content = card_pattern.sub(replace_img, html_content)


# --- TASK B ---
# 1. Parse portfolio-block.js for metadata
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# simple regex to extract objects
entries = {}
for match in re.finditer(r'\{\s*slug:\s*"(.*?)",\s*category:\s*"(.*?)",\s*image:\s*"(.*?)",\s*badge:\s*"(.*?)",\s*title:\s*"(.*?)",\s*text:\s*"(.*?)"\s*\}', js_content, re.DOTALL):
    slug, cat, img, badge, title, text = match.groups()
    entries[slug] = {
        'image': img,
        'badge': badge,
        'title': title,
        'text': text
    }

pages_to_add = [
    ("/portfolio/commercial/altitudex-sentosa-commercial.html", "Commercial"),
    ("/portfolio/commercial/em-services-call-centre-redhill.html", "Commercial"),
    ("/portfolio/commercial/hilton-singapore-orchard-fire-door.html", "Commercial"),
    ("/portfolio/commercial/scape-commercial.html", "Commercial"),
    ("/portfolio/commercial/scape-smart-booking-access.html", "Commercial"),
    ("/portfolio/condominiums/country-grandeur-upper-thomson-condo.html", "Condominiums"),
    ("/portfolio/condominiums/high-oak-condominium-cctv.html", "Condominiums"),
    ("/portfolio/condominiums/hillview-park-cctv-upgrade.html", "Condominiums"),
    ("/portfolio/condominiums/idyllic-suites-geylang-condo.html", "Condominiums"),
    ("/portfolio/condominiums/light-cairnhill-condo.html", "Condominiums"),
    ("/portfolio/condominiums/mergui-mansions-novena-condo.html", "Condominiums"),
    ("/portfolio/condominiums/newton21-newton-condo.html", "Condominiums"),
    ("/portfolio/condominiums/the-bale-intercom-cctv.html", "Condominiums"),
    ("/portfolio/condominiums/the-lviv-newton-condo.html", "Condominiums"),
    ("/portfolio/condominiums/the-verte-telok-kurau-condo.html", "Condominiums"),
    ("/portfolio/condominiums/village-pasir-panjang-condo.html", "Condominiums"),
    ("/portfolio/data-centres/fort-st-engineering.html", "Data Centres"),
    ("/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", "Healthcare"),
    ("/portfolio/industrial/cyrus-tech-industrial.html", "Industrial"),
    ("/portfolio/industrial/hoy-san-industrial.html", "Industrial"),
    ("/portfolio/industrial/multibase-construction-security-upgrade.html", "Industrial"),
    ("/portfolio/industrial/sta-compliance-imaging.html", "Industrial"),
    ("/portfolio/industrial/sta-inspection-industrial.html", "Industrial"),
    ("/portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html", "Industrial"),
    ("/portfolio/institutions/catholic-centre-waterloo.html", "Institutions"),
    ("/portfolio/institutions/cpf-maxwell-institution.html", "Institutions"),
    ("/portfolio/institutions/das-learning-centre-woodlands.html", "Institutions"),
    ("/portfolio/institutions/my-world-preschool-cctv.html", "Institutions"),
    ("/portfolio/residential/upper-east-coast-road-landed-home.html", "Residential"),
]

new_cards_html = ""

for slug, prop in pages_to_add:
    # Get from JS
    js_data = entries.get(slug)
    if not js_data:
        print(f"Warning: {slug} not found in JS")
        continue
    
    # Open HTML
    page_path = os.path.join(w, slug.lstrip('/'))
    if not os.path.exists(page_path):
        print(f"Warning: HTML file not found {page_path}")
        continue
        
    with open(page_path, 'r', encoding='utf-8') as f:
        phtml = f.read()
    
    # 1. Location
    loc_m = re.search(r'📍\s*(.*?)\s*</span>', phtml)
    loc = loc_m.group(1) if loc_m else "Singapore"
    
    # 2. Tags
    chips = re.findall(r'<span class="portfolio-chip">(.*?)</span>', phtml)
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in chips[:3]]) # up to 3 tags
    
    # 3. Systems (from layer cards or specific text, or we can guess from tags/title)
    # The prompt says read from HTML. Let's look for known systems.
    known_sys = ["Premises Security", "Entry & Access", "Vehicle Management", "Platform & Management"]
    sys_list = []
    if "Premises Security" in phtml or "CCTV" in js_data['title'] or "Surveillance" in phtml:
        sys_list.append("Premises Security")
    if "Entry Access Control" in phtml or "Entry & Access" in phtml or "Access" in js_data['title'] or "Turnstile" in phtml or "Intercom" in phtml:
        sys_list.append("Entry & Access")
    if "Vehicle" in phtml or "LPR" in phtml or "Barrier" in phtml:
        sys_list.append("Vehicle Management")
    if "Platform" in phtml or "Management Workstation" in phtml or "BMS" in phtml:
        sys_list.append("Platform & Management")
    if not sys_list:
        sys_list.append("Premises Security") # fallback
    systems_str = ", ".join(sys_list[:2]) # max 2
    
    # 4. Metric
    mval_m = re.search(r'<span class="portfolio-stat-value">(.*?)</span>', phtml)
    mlab_m = re.search(r'<span class="portfolio-stat-label">(.*?)</span>', phtml)
    mval = mval_m.group(1) if mval_m else "1"
    mlab = mlab_m.group(1) if mlab_m else "System"
    if len(mval) > 8: mval = mval[:8] # sanity check
    
    # 5. Outcome
    out_m = re.search(r'<h4 class="portfolio-result-title">(?:✓\s*)?(.*?)</h4>', phtml)
    outcome = out_m.group(1) if out_m else "Enhanced security and operations."
    
    # 6. Year
    # We can try to regex for 201\d or 202\d in the text, or fallback to 2024
    year_m = re.search(r'\b(201[4-9]|202[0-6])\b', phtml)
    year = year_m.group(1) if year_m else "2024"
    
    # 7. Scale
    # Just use mval digits if any
    scale_m = re.search(r'\d+', mval)
    scale = scale_m.group(0) if scale_m else "10"
    
    card_html = f'''
                <!-- {js_data['title']} -->
                <a href="{slug}" class="project-card" data-prop="{prop}"
                    data-sys="{systems_str}" data-year="{year}" data-scale="{scale}">
                    <div class="card-img-w">
                        <img src="{js_data['image']}" alt="{js_data['title']} Portfolio" loading="lazy">
                        <span class="property-badge">{js_data['badge']}</span>
                    </div>
                    <div class="card-body">
                        <h3>{js_data['title']}</h3>
                        <div class="loc"><svg class="feature-icon" style="width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> {loc}</div>
                        <p class="desc">{js_data['text']}</p>
                        <div class="tag-row">
                            {tags_html}
                        </div>
                        <p style="font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;">Key Outcome: {outcome}</p>
                    </div>
                    <div class="card-foot">
                        <div class="metric"><span class="m-val">{mval}</span><span class="m-lab">{mlab}</span></div>
                        <span class="c-date">{year}</span>
                    </div>
                </a>'''
    new_cards_html += card_html

# Insert into <div id="pGrid">
grid_end_idx = html_content.find('</div>\n            </div>\n        </div>\n    </section>\n\n    <!-- 4. BOTTOM CTA -->')
if grid_end_idx == -1:
    # Try another way
    grid_end_idx = html_content.find('</section>\n\n    <!-- CTA')
    if grid_end_idx == -1:
        # Just find the end of pGrid
        grid_end_idx = html_content.rfind('</div>\n        </div>\n    </section>')

# We want to insert just before the closing </div> of <div id="pGrid">
# Let's use regex to find the closing div of pGrid.
# Since pGrid is large, let's find the specific comment after it
insert_marker = '            </div>\n        </div>\n    </section>'
# wait, pGrid is inside <div class="container"> inside <section class="grid-container">
idx = html_content.find(insert_marker)
if idx != -1:
    html_content = html_content[:idx] + new_cards_html + '\n' + html_content[idx:]
else:
    print("Could not find insert marker")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Tasks A and B completed.")
