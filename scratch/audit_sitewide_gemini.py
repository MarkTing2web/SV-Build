import os
import re
import json
from collections import defaultdict
from bs4 import BeautifulSoup, Comment

base_dir = r"c:\Projects\SV-Build"
out_dir = os.path.join(base_dir, "_ai")
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# Define all the pages requested in the sitemap
sitemap = {
    "root": ["index.html", "about.html", "contact.html", "contact-gateway.html", "request-site-assessment-singapore.html", "privacy.html", "terms.html", "sitemap.html"],
    "solutions": [
        "solutions/index.html", "solutions/residential.html", "solutions/condominiums.html", "solutions/commercial.html", "solutions/industrial.html", "solutions/institutions.html", "solutions/healthcare.html", "solutions/managed-living.html", "solutions/data-centres.html",
        "solutions/automate-vehicle-access.html", "solutions/improve-cctv-visibility.html", "solutions/improve-visitor-management.html", "solutions/reduce-guard-manpower.html", "solutions/upgrade-intercom-system.html",
        "solutions/commercial/commercial-security-systems.html", "solutions/commercial/hotel.html", "solutions/commercial/office.html", "solutions/commercial/retail.html",
        "solutions/condominiums/condominium-security-systems.html", "solutions/condominiums/managing-agents.html", "solutions/condominiums/mcst.html", "solutions/condominiums/security-contractors.html",
        "solutions/data-centres/data-centre-security-systems.html",
        "solutions/healthcare/aged-care.html", "solutions/healthcare/day-care.html", "solutions/healthcare/healthcare-security-systems.html",
        "solutions/industrial/industrial-security-systems.html", "solutions/industrial/logistics.html", "solutions/industrial/manufacturing.html", "solutions/industrial/tech-park.html",
        "solutions/institutions/community.html", "solutions/institutions/govt-office.html", "solutions/institutions/institutions-security-systems.html", "solutions/institutions/schools.html",
        "solutions/managed-living/co-living.html", "solutions/managed-living/dormitories.html", "solutions/managed-living/hostels.html", "solutions/managed-living/managed-living-security-systems.html",
        "solutions/residential/architects-and-designers.html", "solutions/residential/home-upgrade.html", "solutions/residential/landed-home-security-systems.html", "solutions/residential/new-build.html"
    ],
    "systems": [
        "systems/index.html", "systems/premises-security.html", "systems/entry-access-control.html", "systems/vehicle-lpr-management.html", "systems/ip-phone-communications.html", "systems/network-infrastructure.html", "systems/security-management-platform.html"
    ],
    "brands": [
        "brands/index.html", "brands/ajax-alarms.html", "brands/risco-alarms.html", "brands/dsc-alarms.html", "brands/paradox-alarms.html", "brands/ge-caddx-alarms.html", "brands/hikvision-cctv.html", "brands/dahua-cctv.html", "brands/hanwha-cctv.html", "brands/milesight-cctv.html", "brands/uniview-cctv.html", "brands/hikvision-access.html", "brands/akuvox-access.html", "brands/apollo-access.html", "brands/hid-entry-access.html", "brands/suprema-entry-access.html", "brands/entrypass-entry-access.html", "brands/microengine-entry-access.html", "brands/zkteco-entry-access.html", "brands/ebelco-locks.html", "brands/viro-locks.html", "brands/aiphone-intercom.html", "brands/akuvox-intercom.html", "brands/hikvision-intercom.html", "brands/fanvil-intercom.html", "brands/kocom-intercom.html", "brands/dormer-autogate.html", "brands/faac-autogate.html", "brands/mag-autogate.html", "brands/gantrygo.html", "brands/zkteco-cvsecurity.html", "brands/fanvil-ip-phone.html", "brands/yealink-ip-phone.html", "brands/yeastar-ippbx.html", "brands/omada-network.html", "brands/ruijie-reyee-network.html", "brands/hrui-network.html", "brands/hikcentral.html", "brands/vesta.html"
    ],
    "portfolio": [
        "portfolio/index.html",
        "portfolio/commercial/altitudex-sentosa-commercial.html", "portfolio/commercial/catholic-centre-security-partnership.html", "portfolio/commercial/em-services-call-centre-redhill.html", "portfolio/commercial/hilton-singapore-orchard-fire-door.html", "portfolio/commercial/scape-commercial.html", "portfolio/commercial/scape-smart-booking-access.html", "portfolio/commercial/st-engineering-mobility-cctv.html",
        "portfolio/condominiums/clearwater-access-salto-partnership.html", "portfolio/condominiums/clearwater-cctv-upgrade.html", "portfolio/condominiums/country-grandeur-upper-thomson-condo.html", "portfolio/condominiums/d-elias-pasir-ris-condo.html", "portfolio/condominiums/high-oak-condominium-cctv.html", "portfolio/condominiums/hillview-park-cctv-upgrade.html", "portfolio/condominiums/idyllic-suites-geylang-condo.html", "portfolio/condominiums/light-cairnhill-condo.html", "portfolio/condominiums/mergui-mansions-novena-condo.html", "portfolio/condominiums/newton21-newton-condo.html", "portfolio/condominiums/rezi-3two-condo.html", "portfolio/condominiums/suites-cairnhill-intercom-lpr.html", "portfolio/condominiums/the-bale-intercom-cctv.html", "portfolio/condominiums/the-lviv-newton-condo.html", "portfolio/condominiums/the-verte-telok-kurau-condo.html", "portfolio/condominiums/village-pasir-panjang-condo.html",
        "portfolio/data-centres/fort-data-centre-access-upgrade.html", "portfolio/data-centres/fort-st-engineering.html",
        "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", "portfolio/healthcare/surya-home.html",
        "portfolio/industrial/cogent-logistics-hub-cctv.html", "portfolio/industrial/cyrus-tech-industrial.html", "portfolio/industrial/hoy-san-industrial.html", "portfolio/industrial/mitsubishi-elevator-face-access-bms.html", "portfolio/industrial/multibase-construction-security-upgrade.html", "portfolio/industrial/smartflex-tampines.html", "portfolio/industrial/sta-compliance-imaging.html", "portfolio/industrial/sta-inspection-industrial.html", "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
        "portfolio/institutions/catholic-centre-waterloo.html", "portfolio/institutions/changi-airport-lpr-barriers.html", "portfolio/institutions/cpf-maxwell-institution.html", "portfolio/institutions/das-learning-centre-woodlands.html", "portfolio/institutions/my-world-preschool-cctv.html", "portfolio/institutions/sengkang-interim-bus-interchange.html", "portfolio/institutions/sfx-retreat-centre-punggol.html",
        "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html", "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
        "portfolio/residential/dunbar-walk-landed-home.html", "portfolio/residential/dyson-8-residences-landed-home.html", "portfolio/residential/lengkok-mariam-landed-home.html", "portfolio/residential/merryn-road-landed-home.html", "portfolio/residential/shelford-landed-home.html", "portfolio/residential/siglap-bank-landed-home.html", "portfolio/residential/upper-east-coast-road-landed-home.html"
    ],
    "insights": [
        "insights/index.html", "insights/10-tips-securing-your-premises.html", "insights/after-security-installation-support.html", "insights/ai-analytics-hikvision.html", "insights/analogue-to-ip-migration.html", "insights/architect-id-guide-security.html", "insights/burglar-alarm-design.html", "insights/burglar-alarm-detectors-sensors.html", "insights/choose-intercom-for-home.html", "insights/compare-security-integrators.html", "insights/condo-security-upgrade-proposal.html", "insights/condo-security-upgrade-quotes.html", "insights/condo-security-upgrade-timeline.html", "insights/hdb-landed-condo-security-differences.html", "insights/home-security-system-cost-singapore.html", "insights/how-burglar-alarm-works.html", "insights/how-card-access-works.html", "insights/how-intercom-systems-work.html", "insights/how-ip-cctv-works.html", "insights/how-technology-makes-your-guarding-team-more-competitive.html", "insights/how-to-choose-auto-gate-motor.html", "insights/how-to-choose-cctv.html", "insights/how-to-choose-multi-door-access.html", "insights/is-my-security-system-still-working.html", "insights/lpr-vs-rfid-vehicle-access-singapore.html", "insights/maintain-burglar-alarm.html", "insights/maintenance-contract.html", "insights/managing-agents-guide-estate-security-systems.html", "insights/managing-multiple-estates-with-vesta.html", "insights/mcst-legal-obligations-security.html", "insights/pdpa-cctv-singapore.html", "insights/rackmount-nvr.html", "insights/reduce-false-alarms.html", "insights/security-system-refresh.html", "insights/security-upgrade-condo-agm.html", "insights/standalone-door-access.html", "insights/upgrade-condo-intercom.html", "insights/upgrade-existing-security-system.html", "insights/upgrade-or-repair.html", "insights/using-your-burglar-alarm.html", "insights/video-analytics-retail-singapore.html", "insights/why-mechanical-locks-not-enough.html", "insights/why-security-needs-managed-network.html", "insights/wifi-remote-control-auto-gate.html"
    ],
    "resources": [
        "resources/index.html", "resources/guides.html", "resources/checklists.html", "resources/calculators.html", "resources/library.html", "resources/training-videos.html", "resources/faq.html",
        "resources/guides/auto-gate-guide.html", "resources/guides/burglar-alarm-guide.html", "resources/guides/cctv-guide.html", "resources/guides/door-access-guide.html", "resources/guides/how-to-evaluate-security-contractor.html", "resources/guides/intercom-guide.html", "resources/guides/office-telephone-guide.html", "resources/guides/security-renovation-guide.html", "resources/guides/wifi-network-guide.html",
        "resources/checklists/care-facility-checklist.html", "resources/checklists/commercial-security-checklist.html", "resources/checklists/dormitory-checklist.html", "resources/checklists/institutional-security-checklist.html", "resources/checklists/intercom-checklist.html", "resources/checklists/mcst-checklist.html",
        "resources/calculators/access-control-cost-calculator.html", "resources/calculators/cctv-camera-coverage-calculator.html", "resources/calculators/cctv-storage-bandwidth-calculator.html", "resources/calculators/cctv-system-cost-calculator.html",
        "resources/library/access-control.html", "resources/library/burglar-alarm.html", "resources/library/cctv.html", "resources/library/intercom.html", "resources/library/ip-telephony.html", "resources/library/network.html", "resources/library/platform.html", "resources/library/vehicle.html"
    ]
}

report_data = {sec: [] for sec in sitemap.keys()}
global_stats = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
issue_frequency = defaultdict(int)

def determine_page_type(path):
    if path == "index.html": return "homepage", "Book a Site Assessment"
    if path == "brands/index.html": return "brands index", "Book a Site Assessment"
    if path.startswith("brands/"): return "brand", "Request a Proposal"
    if path.startswith("systems/"): return "systems", "Book a Site Assessment"
    if path.startswith("insights/"): return "insights", "Request a Proposal"
    if path.startswith("portfolio/"): return "portfolio", "Request a Proposal"
    if path.startswith("resources/guides/"): return "resource guide", "Request a Proposal"
    if path.startswith("resources/checklists/"): return "resource checklist", "Request a Proposal"
    if path.startswith("resources/calculators/"): return "resource calculator", "Request a Proposal"
    if path.startswith("resources/library/"): return "resource library", "Request a Proposal"
    
    # Solutions Hubs
    hubs = ["solutions/residential.html", "solutions/condominiums.html", "solutions/commercial.html", "solutions/industrial.html", "solutions/institutions.html", "solutions/healthcare.html", "solutions/managed-living.html", "solutions/data-centres.html"]
    prob_hubs = ["solutions/automate-vehicle-access.html", "solutions/improve-cctv-visibility.html", "solutions/improve-visitor-management.html", "solutions/reduce-guard-manpower.html", "solutions/upgrade-intercom-system.html"]
    
    if path in hubs or path in prob_hubs or path == "solutions/index.html": return "sector hub", "Book a Site Assessment"
    if "-security-systems.html" in path and path.count("/") == 2: return "sector deep-dive", "Book a Site Assessment"
    if path.startswith("solutions/"): return "persona sub-page", "Request a Proposal"
    
    return "general", "Request a Proposal" # fallback

# Helper to find line numbers for errors based on a search string
def get_line(html_text, search_str):
    if not search_str: return "—"
    try:
        idx = html_text.find(search_str)
        if idx == -1: return "—"
        return str(html_text.count('\n', 0, idx) + 1)
    except:
        return "—"

for section, files in sitemap.items():
    for rel_path in files:
        full_path = os.path.join(base_dir, rel_path.replace('/', '\\'))
        issues = []
        page_type, correct_cta = determine_page_type(rel_path)
        
        if not os.path.exists(full_path):
            issues.append(("SYSTEM", "CRITICAL", f"File not found: {rel_path}", "—"))
            report_data[section].append({"path": rel_path, "type": page_type, "issues": issues})
            continue
            
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
            
        soup = BeautifulSoup(html, "html.parser")
        
        def add_issue(rule, severity, desc, line_str=None):
            l = get_line(html, line_str) if line_str else "—"
            issues.append((rule, severity, desc, l))
            global_stats[severity] += 1
            issue_frequency[f"{rule} - {desc}"] += 1

        # PART 1: NAV-FOOTER HARDCODED
        nav = soup.find("nav", id="sv-nav")
        if not nav: add_issue("PART 1", "CRITICAL", "Missing <nav id=\"sv-nav\"></nav>")
        elif nav.contents: add_issue("PART 1", "CRITICAL", "Hardcoded <nav> contents instead of empty placeholder")
        
        footer = soup.find("footer", id="sv-footer")
        if not footer: add_issue("PART 1", "CRITICAL", "Missing <footer id=\"sv-footer\"></footer>")
        elif footer.contents: add_issue("PART 1", "CRITICAL", "Hardcoded <footer> contents instead of empty placeholder")

        # RULE 1: CSS LOAD ORDER
        links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]
        scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
        
        if "/sv-shared.css" not in links: add_issue("RULE 1", "CRITICAL", "sv-shared.css missing")
        if "/site-config.js" not in scripts: add_issue("RULE 1", "CRITICAL", "site-config.js missing")
        
        req_css = None
        if "solutions" in rel_path: req_css = "/sv-solutions.css"
        elif "systems" in rel_path: req_css = "/sv-systems.css"
        elif "brands" in rel_path: req_css = "/sv-brands.css"
        elif "portfolio" in rel_path: req_css = "/sv-portfolio.css"
        elif "insights" in rel_path: req_css = "/sv-insights.css"
        elif "resources" in rel_path: req_css = "/sv-resources.css"
        
        if req_css and req_css not in links:
            add_issue("RULE 1", "HIGH", f"Required section CSS {req_css} missing")
            
        # Check cross-pollution
        for css in ["/sv-solutions.css", "/sv-systems.css", "/sv-brands.css", "/sv-portfolio.css", "/sv-insights.css", "/sv-resources.css"]:
            if css in links and css != req_css:
                add_issue("RULE 1", "HIGH", f"Wrong section CSS {css} loaded on {page_type}")
                
        has_form = soup.find("form")
        if has_form and "/sv-forms.css" not in links:
            add_issue("RULE 1", "HIGH", "sv-forms.css missing on page with form")
        elif not has_form and "/sv-forms.css" in links:
            add_issue("RULE 1", "HIGH", "sv-forms.css loaded on page without form")

        # RULE 2: INLINE STYLES
        for el in soup.find_all(style=True):
            s = el.get("style").strip()
            if el.name in ["header", "div"] and s.startswith("background-image"):
                continue # Hero allowed
            if "display:grid" in s and el.get("class") and "footer-grid" in el.get("class"):
                continue # Footer exception
            # Add issue
            add_issue("RULE 2", "HIGH", f"Inline style found on <{el.name}>: {s}", s[:30])

        # RULE 3: <style> BLOCK
        style_blocks = soup.find_all("style")
        if len(style_blocks) > 1:
            add_issue("RULE 3", "HIGH", f"Multiple <style> blocks ({len(style_blocks)}) found")
        if style_blocks:
            for sb in style_blocks:
                if sb.parent.name != "head":
                    add_issue("RULE 3", "HIGH", "<style> block placed outside <head>")
                text = sb.string or ""
                if "--page-accent" not in text:
                    add_issue("RULE 3", "HIGH", "Missing :root { --page-accent } in style block")
                if "@media" not in text or "max-width: 768px" not in text:
                    add_issue("RULE 3", "MEDIUM", "Missing @media mobile hero override in <style> block")
                # Very basic check for extraneous rules
                rules = text.split("}")
                for r in rules:
                    if r.strip() and not any(x in r for x in [":root", "hero-", "@media"]):
                        add_issue("RULE 3", "HIGH", f"Extraneous CSS in style block: {r.strip()[:30]}...")
                        break

        # RULE 4: HERO CLASSES
        hero = soup.find("header") or soup.find(class_=re.compile("hero-"))
        if hero:
            hclass = hero.get("class", [])
            has_valid = False
            for c in ["hero-full", "hero-standard", "hero-compact"]:
                if c in hclass: has_valid = True
            if not has_valid:
                add_issue("RULE 4", "HIGH", "No recognised hero height class present")
            elif page_type == "homepage" and "hero-full" not in hclass:
                add_issue("RULE 4", "HIGH", f"Wrong hero class for homepage (found {hclass})")
            elif page_type in ["sector hub", "sector deep-dive", "systems", "brands index"] and "hero-standard" not in hclass:
                add_issue("RULE 4", "HIGH", f"Wrong hero class for {page_type} (expected hero-standard)")
            elif page_type not in ["homepage", "sector hub", "sector deep-dive", "systems", "brands index"] and "hero-compact" not in hclass:
                add_issue("RULE 4", "HIGH", f"Wrong hero class for {page_type} (expected hero-compact)")
        else:
            add_issue("RULE 4", "HIGH", "Hero section missing entirely")

        # RULE 5: TRUST BAR
        trust_bar = soup.find(class_=re.compile("trust-bar"))
        if page_type == "insights":
            if trust_bar: add_issue("RULE 5", "CRITICAL", "Trust bar present on insights page")
        else:
            if not trust_bar: add_issue("RULE 5", "CRITICAL", "Trust bar missing")
            else:
                tb_text = trust_bar.get_text()
                if "sv-licence" not in str(trust_bar): add_issue("RULE 5", "CRITICAL", "Hardcoded licence in trust bar or missing .sv-licence")
                if "sv-sites" not in str(trust_bar): add_issue("RULE 5", "CRITICAL", "Hardcoded sites count in trust bar or missing .sv-sites")
                if "Police Licensed" not in tb_text or "bizSAFE" not in tb_text or "BCA" not in tb_text:
                    add_issue("RULE 5", "HIGH", "Trust bar text deviating from canonical format")

        # RULE 6: BREADCRUMB
        bc = soup.find(class_="breadcrumb") or soup.find(class_="sv-breadcrumb")
        if page_type == "homepage":
            if bc: add_issue("RULE 6", "HIGH", "Breadcrumb present on homepage")
        else:
            if not bc: add_issue("RULE 6", "CRITICAL", "Breadcrumb missing")
            else:
                links = bc.find_all("a")
                if not links or links[0].get_text(strip=True) != "Home":
                    add_issue("RULE 6", "HIGH", "First breadcrumb item is not Home")
                # Current page has a link?
                last_li = bc.find_all("li")
                if last_li and last_li[-1].find("a"):
                    add_issue("RULE 6", "HIGH", "Current page (last item) in breadcrumb has a link")

        # RULE 7: ONE H1
        h1s = soup.find_all("h1")
        if len(h1s) == 0: add_issue("RULE 7", "CRITICAL", "Zero H1s on page")
        elif len(h1s) > 1: add_issue("RULE 7", "CRITICAL", f"Multiple H1s ({len(h1s)}) on page")

        # RULE 8: HEADING HIERARCHY
        headings = soup.find_all(re.compile(r"^h[1-6]$"))
        h_levels = [int(h.name[1]) for h in headings]
        max_h = 1
        for level in h_levels:
            if level > max_h + 1:
                add_issue("RULE 8", "HIGH", f"Skipped heading level: h{level} used without preceding h{level-1}")
                break
            max_h = max(max_h, level)

        # RULE 9: CTA ARCHITECTURE
        buttons = soup.select(".btn")
        # Just checking any primary-looking CTA or finding the wrong label
        for btn in buttons:
            label = btn.get_text(strip=True)
            if label and label not in [correct_cta, "Submit", "Read More"]:
                if "Book" in label or "Request" in label or "WhatsApp" in label:
                    if label != correct_cta and label not in ["💬 WhatsApp", "💬 WhatsApp an Engineer", "💬 Discuss a Similar Project"]:
                        add_issue("RULE 9", "HIGH", f'CTA label is "{label}" — should be "{correct_cta}" (or is non-canonical)', label)

        # RULE 10: ABSOLUTE PATHS
        for tag, attr in [("a", "href"), ("img", "src"), ("link", "href"), ("script", "src")]:
            for el in soup.find_all(tag):
                val = el.get(attr)
                if val:
                    if val.startswith("../") or val.startswith("./") or (not val.startswith("/") and not val.startswith("http") and not val.startswith("mailto") and not val.startswith("tel") and not val.startswith("#")):
                        add_issue("RULE 10", "HIGH", f"Relative path found: {val}", val)
                    elif val.startswith("//"):
                        add_issue("RULE 10", "HIGH", f"Protocol-relative URL found: {val}", val)

        # RULE 11: BRITISH ENGLISH
        text_content = soup.get_text()
        for us, uk in [("authorization", "authorisation"), ("optimize", "optimise"), ("center", "centre"), ("license", "licence"), ("color", "colour"), ("recognize", "recognise"), ("analyze", "analyse")]:
            # ignore inside tags/classes handled by just checking text nodes
            # A simple regex bounded by word boundaries
            if re.search(r'\b' + us + r'\b', text_content, re.IGNORECASE):
                add_issue("RULE 11", "LOW", f'American spelling "{us}" found (should be "{uk}")')

        # RULE 12: SEO METADATA
        title = soup.find("title")
        if not title: add_issue("RULE 12", "CRITICAL", "Missing <title>")
        else:
            tt = title.get_text(strip=True)
            if len(tt) < 50 or len(tt) > 60: add_issue("RULE 12", "MEDIUM", f"<title> length is {len(tt)} (should be 50-60)")
            if "Singapore" not in tt: add_issue("RULE 12", "MEDIUM", "<title> missing 'Singapore'")
            
        desc = soup.find("meta", {"name": "description"})
        if not desc: add_issue("RULE 12", "CRITICAL", "Missing <meta name=\"description\">")
        else:
            dlen = len(desc.get("content", ""))
            if dlen < 120 or dlen > 160: add_issue("RULE 12", "MEDIUM", f"Meta description length is {dlen} (should be 120-160)")
            
        canon = soup.find("link", {"rel": "canonical"})
        if not canon: add_issue("RULE 12", "CRITICAL", "Missing <link rel=\"canonical\">")
        elif not canon.get("href", "").startswith("https://www.securevision.com.sg/"):
            add_issue("RULE 12", "HIGH", f"Canonical URL relative or wrong domain: {canon.get('href')}")
            
        for og in ["og:title", "og:description", "og:image", "og:url"]:
            if not soup.find("meta", {"property": og}): add_issue("RULE 12", "HIGH", f"Missing {og}")

        og_img = soup.find("meta", {"property": "og:image"})
        if og_img and not og_img.get("content", "").startswith("http"):
            add_issue("RULE 12", "HIGH", "og:image uses relative path instead of absolute URL")

        # RULE 13: IMAGE ALT TEXT
        for img in soup.find_all("img"):
            alt = img.get("alt")
            if alt is None: add_issue("RULE 13", "HIGH", "<img> missing alt attribute")
            elif alt.strip() == "" and not ("icon" in img.get("class", []) or "svg" in img.get("src", "")):
                add_issue("RULE 13", "HIGH", "<img alt=\"\"> on content image")
            elif alt.lower().strip() in ["image", "photo", "banner", "logo", "hero"]:
                add_issue("RULE 13", "LOW", f"Generic alt text used: '{alt}'")

        # RULE 14: SECTION ALTERNATION
        sections = soup.find_all("section")
        bg_classes = []
        for s in sections:
            cls = s.get("class", [])
            if "sv-section-white" in cls: bg_classes.append("white")
            elif "sv-section-grey" in cls: bg_classes.append("grey")
            elif "bg-light" in cls: bg_classes.append("grey")
        
        consecutive = 1
        for i in range(1, len(bg_classes)):
            if bg_classes[i] == bg_classes[i-1]: consecutive += 1
            else: consecutive = 1
            if consecutive >= 3:
                add_issue("RULE 14", "MEDIUM", "3 or more consecutive sections share the same background class")
                break

        # RULE 15: PLACEHOLDERS
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            if any(x in c.upper() for x in ["TODO", "FIXME", "PLACEHOLDER", "UPDATE"]):
                add_issue("RULE 15", "HIGH", f"Placeholder HTML comment found: {c.strip()[:30]}")
        
        for p in ["[INSERT]", "[PLACEHOLDER]", "[Sector]", "[Brand Name]", "[PRIMARY CTA LABEL]", "[page-class]", "[slug]", "[CLIENT NAME]", "[PROJECT NAME]"]:
            if p in text_content: add_issue("RULE 15", "HIGH", f"Placeholder text found: {p}")

        # RULE 16: DYNAMIC VALUES
        for hc, correct in [("2,000+", ".sv-sites"), ("2025", ".sv-current-year"), ("2026", ".sv-current-year"), ("bizSAFE Level 3", ".sv-bizsafe"), ("L/PS/001568/2026P", ".sv-licence")]:
            if hc in html and correct not in html:
                add_issue("RULE 16", "HIGH", f"Hardcoded '{hc}' found instead of dynamic class {correct}")

        # PART 3: SECTION COMPLETENESS BY PAGE TYPE
        page_text = text_content.lower()
        if page_type == "sector hub":
            if "who this is for" not in page_text: add_issue("PART 3", "HIGH", "Missing 'Who This Is For' section")
            if not soup.find(class_=re.compile("sv-systems-block")): add_issue("PART 3", "HIGH", "Missing .sv-systems-block")
            if not soup.find(class_=re.compile("sv-portfolio-block")) and not "portfolio" in page_text: add_issue("PART 3", "HIGH", "Missing portfolio proof (.sv-portfolio-block)")
        elif page_type == "sector deep-dive" or page_type == "persona sub-page" or page_type == "systems":
            if "who this is for" not in page_text: add_issue("PART 3", "HIGH", "Missing 'Who This Is For' section")
        elif page_type == "portfolio":
            if not soup.find(class_=re.compile("stat-strip")) and not soup.find(class_=re.compile("portfolio-stat")): add_issue("PART 3", "HIGH", "Missing 4-stat strip")
            h = soup.find("header")
            if h and h.find(class_="btn"): add_issue("PART 3", "HIGH", "CTA button found inside hero section")
            if not soup.find(class_=re.compile("sv-portfolio-block")) and not soup.find(class_="related-projects"): add_issue("PART 3", "HIGH", "Missing related portfolio section")
        elif page_type == "insights":
            if not soup.find(class_=re.compile("author-bio")) and "ler wee meng" not in page_text and "SECUREVISION.authorName" not in html: add_issue("PART 3", "HIGH", "Author bio strip missing")
            if not soup.find(id="related-insights-grid"): add_issue("PART 3", "HIGH", "Missing <div id=\"related-insights-grid\"></div>")
            body = soup.find("body")
            if body:
                art = body.get("data-article")
                slug = os.path.basename(rel_path).replace(".html", "")
                if not art: add_issue("PART 3", "HIGH", "<body> missing data-article attribute")
                elif art != slug: add_issue("PART 3", "HIGH", f"data-article '{art}' does not match filename '{slug}'")
        elif page_type == "brand":
            if not "Request a Proposal" in html: add_issue("PART 3", "HIGH", "Primary CTA is not 'Request a Proposal'")
        elif page_type == "resource guide":
            if not soup.find(class_="layout-with-sidebar"): add_issue("PART 3", "HIGH", "Missing .layout-with-sidebar")
            if not soup.find(class_="sticky-toc"): add_issue("PART 3", "HIGH", "Missing .sticky-toc sidebar")

        report_data[section].append({"path": rel_path, "type": page_type, "issues": issues})

# Generate Markdown Reports
import datetime
date_str = datetime.datetime.now().strftime("%B %d, %Y")

# Summary
summary = f"""# Securevision Full Site Audit — Executive Summary
**Date:** {date_str}
**Audited by:** Gemini Antigravity
**Total pages audited:** {sum(len(v) for v in report_data.values())}
**Total issues found:** {sum(global_stats.values())} — Critical: {global_stats['CRITICAL']} | High: {global_stats['HIGH']} | Medium: {global_stats['MEDIUM']} | Low: {global_stats['LOW']}

---

## Top Systemic Issues
"""
top_issues = sorted(issue_frequency.items(), key=lambda x: x[1], reverse=True)[:10]
for issue, count in top_issues:
    summary += f"- **{issue}** (Found on {count} pages)\n"

summary += """
---

## Issues by Section

| Section | Pages | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|---|
"""
for section, pages in report_data.items():
    s_crit, s_high, s_med, s_low = 0, 0, 0, 0
    for p in pages:
        for i in p["issues"]:
            if i[1] == "CRITICAL": s_crit += 1
            elif i[1] == "HIGH": s_high += 1
            elif i[1] == "MEDIUM": s_med += 1
            elif i[1] == "LOW": s_low += 1
    total = s_crit + s_high + s_med + s_low
    summary += f"| {section.capitalize()} | {len(pages)} | {s_crit} | {s_high} | {s_med} | {s_low} | {total} |\n"

summary += f"| **TOTAL** | {sum(len(v) for v in report_data.values())} | {global_stats['CRITICAL']} | {global_stats['HIGH']} | {global_stats['MEDIUM']} | {global_stats['LOW']} | {sum(global_stats.values())} |\n"

summary += """
---

## Recommended Fix Order
1. Fix CRITICAL layout script dependencies (missing/hardcoded nav/footer placeholders).
2. Fix CRITICAL SEO issues (missing titles, canonicals).
3. Standardise RULE 2 Inline Styles across Brands pages.
4. Normalise CSS Load Order (RULE 1) across all sections.
5. Standardise CTA labels across section hubs and portfolio pages.
"""

with open(os.path.join(out_dir, "audit-00-summary.md"), "w", encoding="utf-8") as f:
    f.write(summary)

section_idx = 1
for section, pages in report_data.items():
    md = ""
    for p in pages:
        if len(p["issues"]) == 0:
            md += f"## {p['path']} ✓\n**Page type:** {p['type']}\n**Issues found:** 0 — No issues found.\n\n---\n\n"
        else:
            md += f"## {p['path']}\n**Page type:** {p['type']}\n**Issues found:** {len(p['issues'])}\n\n"
            md += "| # | Rule | Severity | Issue | Line |\n|---|---|---|---|---|\n"
            for idx, iss in enumerate(p["issues"], 1):
                md += f"| {idx} | {iss[0]} | {iss[1]} | {iss[2]} | {iss[3]} |\n"
            md += "\n---\n\n"
            
    filename = f"audit-0{section_idx}-{section}.md"
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(md)
    section_idx += 1

print("Audit complete! Reports generated in _ai/")
