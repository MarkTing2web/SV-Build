import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

def insert_after_card(html, href_match, insert_content):
    start_idx = html.find(f'href="{href_match}"')
    if start_idx == -1:
        print(f"Error: Could not find card with href: {href_match}")
        return html
    
    end_idx = html.find('</a>', start_idx)
    if end_idx == -1:
        print(f"Error: Could not find </a> after {href_match}")
        return html
    
    insertion_point = end_idx + 4
    return html[:insertion_point] + "\n\n                " + insert_content.strip() + html[insertion_point:]

c1 = """<a href="/portfolio/commercial/scape-smart-booking-access.html" class="project-card" data-prop="Commercial"
                    data-sys="Entry & Access" data-year="2024" data-scale="0">
                    <div class="card-img-w">
                        <img src="/images/portfolio/commercial/scape-rel.webp" alt="SCAPE Smart Booking and Access Integration Portfolio">
                        <span class="property-badge">Booking-to-Access Automation</span>
                    </div>
                    <div class="card-body">
                        <h3>SCAPE Singapore — Smart Booking & Access</h3>
                        <div class="loc"><svg class="feature-icon" style="width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Orchard Road, Singapore</div>
                        <p class="desc">Custom middleware connecting Salesforce bookings to ZKTeco QR access readers — confirmed reservations automatically generate time-bound entry credentials without any staff intervention.</p>
                        <div class="tag-row">
                            <span class="tag">ZKTeco QR</span>
                            <span class="tag">Salesforce Integration</span>
                            <span class="tag">Custom Middleware</span>
                        </div>
                        <p style="font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;">Key Outcome: Zero manual check-ins at entry.</p>
                    </div>
                    <div class="card-foot">
                        <div class="metric"><span class="m-val">100%</span><span class="m-lab">Automated</span></div>
                        <span class="c-date">2024</span>
                    </div>
                </a>"""

content = insert_after_card(content, "/portfolio/commercial/scape-commercial.html", c1)

c2 = """<a href="/portfolio/data-centres/fort-st-engineering.html" class="project-card" data-prop="Data Centres"
                    data-sys="Premises Security, Entry & Access" data-year="2023" data-scale="92">
                    <div class="card-img-w">
                        <img src="/images/portfolio/data-centres/fort-st-engineering-rel.webp" alt="FORT Data Centre ST Engineering Portfolio">
                        <span class="property-badge">Live-Environment Upgrade</span>
                    </div>
                    <div class="card-body">
                        <h3>FORT Data Centre — ST Engineering</h3>
                        <div class="loc"><svg class="feature-icon" style="width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Singapore</div>
                        <p class="desc">Non-disruptive camera fleet expansion to 92 IP cameras across two 128-channel NVRs, plus fingerprint access renewal with zero credential discontinuity in a live data centre environment.</p>
                        <div class="tag-row">
                            <span class="tag">Hikvision CCTV</span>
                            <span class="tag">ZKTeco Fingerprint</span>
                            <span class="tag">128ch NVR</span>
                        </div>
                        <p style="font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;">Key Outcome: Zero downtime during live upgrade.</p>
                    </div>
                    <div class="card-foot">
                        <div class="metric"><span class="m-val">92</span><span class="m-lab">Cameras</span></div>
                        <span class="c-date">2023</span>
                    </div>
                </a>"""

content = insert_after_card(content, "/portfolio/data-centres/fort-data-centre-access-upgrade.html", c2)

c3 = """<a href="/portfolio/institutions/catholic-centre-waterloo.html" class="project-card" data-prop="Institutions"
                    data-sys="Premises Security" data-year="2022" data-scale="58">
                    <div class="card-img-w">
                        <img src="/images/portfolio/institutions/catholic-centre-waterloo-rel.webp" alt="Catholic Centre Waterloo Street CCTV Portfolio">
                        <span class="property-badge">Analogue to IP Migration</span>
                    </div>
                    <div class="card-body">
                        <h3>Catholic Centre Waterloo Street</h3>
                        <div class="loc"><svg class="feature-icon" style="width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Waterloo Street, Singapore</div>
                        <p class="desc">Modernising a nine-year-old analogue system into 58 IP cameras — including 12 super-wide 180° units for wide corridors — with floor-level PoE switches enabling future expansion without recabling.</p>
                        <div class="tag-row">
                            <span class="tag">180° Super-Wide</span>
                            <span class="tag">IP Migration</span>
                            <span class="tag">PoE Infrastructure</span>
                        </div>
                        <p style="font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;">Key Outcome: Future-ready without central cabling runs.</p>
                    </div>
                    <div class="card-foot">
                        <div class="metric"><span class="m-val">58</span><span class="m-lab">Cameras</span></div>
                        <span class="c-date">2022</span>
                    </div>
                </a>"""

content = insert_after_card(content, "/portfolio/commercial/catholic-centre-security-partnership.html", c3)

c4 = """<a href="/portfolio/residential/upper-east-coast-road-landed-home.html" class="project-card" data-prop="Residential"
                    data-sys="Premises Security, Entry & Access" data-year="2026" data-scale="4">
                    <div class="card-img-w">
                        <img src="/images/portfolio/residential/upper-east-coast-landed-upgrade-rel.webp" alt="Upper East Coast Road Landed Home Security Portfolio">
                        <span class="property-badge">Decade of Upgrades</span>
                    </div>
                    <div class="card-body">
                        <h3>Upper East Coast Road</h3>
                        <div class="loc"><svg class="feature-icon" style="width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Upper East Coast Road, Singapore</div>
                        <p class="desc">Ten years of phased security improvements across CCTV, intercom, and gate automation — keeping a landed property current without wholesale replacement at each stage.</p>
                        <div class="tag-row">
                            <span class="tag">IP CCTV</span>
                            <span class="tag">Gate Automation</span>
                            <span class="tag">Phased Upgrades</span>
                        </div>
                        <p style="font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px;">Key Outcome: 10-year security lifecycle without rip-and-replace.</p>
                    </div>
                    <div class="card-foot">
                        <div class="metric"><span class="m-val">4</span><span class="m-lab">Upgrade Phases</span></div>
                        <span class="c-date">2026</span>
                    </div>
                </a>"""

# To insert c4 at the end of #pGrid
# We find where #pGrid ends. Usually it's followed by </div> then </section>
grid_start = content.find('id="pGrid"')
if grid_start != -1:
    # Find the next </div> that closes pGrid. Since there are many divs inside, we can just find the end of the last </a> before </div>
    # Let's find the closing tag of #pGrid by counting div depth or just using regex.
    # Actually, we know that all cards are <a> tags.
    # So we can find the last </a> after #pGrid and before the next section.
    section_end = content.find('</section>', grid_start)
    last_a_end = content.rfind('</a>', grid_start, section_end)
    if last_a_end != -1:
        insertion_point = last_a_end + 4
        content = content[:insertion_point] + "\n\n                " + c4.strip() + content[insertion_point:]
    else:
        print("Error: Could not find last </a> in #pGrid")
else:
    print("Error: Could not find #pGrid")


# Update the year filter
new_filter = """<select id="fYear" onchange="filterP()">
                        <option value="all">All Years</option>
                        <option value="2026">2026</option>
                        <option value="2025">2025</option>
                        <option value="2024">2024</option>
                        <option value="2023">2023</option>
                        <option value="2022">2022</option>
                        <option value="2021">2021</option>
                        <option value="2019">2019</option>
                        <option value="2017">2017</option>
                    </select>"""

content = re.sub(r'<select id="fYear"[^>]*>.*?</select>', new_filter, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updates complete.")
