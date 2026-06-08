import os
import re

files_list = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/sta-inspection-industrial.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
errors = {f"Group {i}": [] for i in range(1, 11)}
files_with_errors = set()

for rel_path in files_list:
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
    body_content = body_match.group(1) if body_match else content

    def report(group, code, msg, line=0):
        errors[f"Group {group}"].append(f"FILE: {rel_path} → {code} {msg} — line {line}")
        files_with_errors.add(rel_path)

    def find_line(pattern):
        m = re.search(pattern, content)
        if m:
            return content.count('\n', 0, m.start()) + 1
        return 0

    slug = os.path.basename(rel_path).replace('.html', '')

    # --- GROUP 1 ---
    if '<nav id="sv-nav"></nav>' not in body_content:
        report(1, "1A", "nav element missing entirely", find_line(r'<nav[^>]*id="sv-nav"'))
    if '<footer id="sv-footer"></footer>' not in body_content:
        report(1, "1B", "footer element missing entirely", find_line(r'<footer[^>]*id="sv-footer"'))
    
    m_nf = re.search(r'<script\s+src="/nav-footer.js"\s*></script>\s*</body>', content)
    if not m_nf:
        report(1, "1C", "nav-footer.js missing or not before </body>", find_line(r'nav-footer.js'))

    m_sc = re.search(r'<head>.*?<script\s+src="/site-config.js"\s*></script>.*?</head>', content, re.DOTALL)
    if not m_sc:
        report(1, "1D", "site-config.js missing or not in head", find_line(r'site-config.js'))

    if re.search(r'<ul\s+class="nav"|<header\s+class="main-nav"', body_content):
        report(1, "1E", "hardcoded nav HTML present", find_line(r'<ul\s+class="nav"|<header\s+class="main-nav"'))

    css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*href="([^"]+)"', content)
    if css_links:
        if "sv-shared.css" not in css_links[0]:
            report(1, "1F", "sv-shared.css is not the first stylesheet loaded", find_line(r'<link[^>]*rel="stylesheet"'))
        try:
            shared_idx = next(i for i, v in enumerate(css_links) if "sv-shared.css" in v)
            if len(css_links) <= shared_idx + 1 or "sv-portfolio.css" not in css_links[shared_idx + 1]:
                report(1, "1G", "sv-portfolio.css missing or not immediately after sv-shared.css", find_line(r'sv-portfolio.css'))
        except StopIteration:
            pass

    if 'class="sv-wa-float"' in body_content:
        report(1, "1H", "sv-wa-float anchor present in body HTML", find_line(r'sv-wa-float'))

    if 'sv-portfolio-block' in body_content and 'portfolio-block.js' not in body_content:
        report(1, "1I", "sv-portfolio-block div present but portfolio-block.js not loaded", find_line(r'sv-portfolio-block'))
        
    if 'sv-systems-block' in body_content and 'systems-block.js' not in body_content:
        report(1, "1J", "sv-systems-block div present but systems-block.js not loaded", find_line(r'sv-systems-block'))


    # --- GROUP 2 ---
    m_title = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title_text = m_title.group(1).strip() if m_title else ""
    if len(title_text) < 50 or len(title_text) > 60 or "Singapore" not in title_text or "Securevision" not in title_text:
        report(2, "2A", "title length under 50 or over 60, or missing keywords", find_line(r'<title>'))

    m_desc = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
    desc_text = m_desc.group(1).strip() if m_desc else ""
    if len(desc_text) < 120 or len(desc_text) > 160:
        report(2, "2B", "description length outside 120-160 range", find_line(r'name="description"'))

    m_canon = re.search(r'<link\s+rel="canonical"\s+href="(.*?)"', content, re.IGNORECASE)
    canon_text = m_canon.group(1) if m_canon else ""
    if not canon_text or not canon_text.startswith("https://www.securevision.com.sg/portfolio/"):
        report(2, "2C", "canonical URL missing or incorrect", find_line(r'rel="canonical"'))

    m_og_title = re.search(r'<meta\s+property="og:title"\s+content="(.*?)"', content, re.IGNORECASE)
    og_title_text = m_og_title.group(1).strip() if m_og_title else ""
    if not og_title_text or og_title_text != title_text:
        report(2, "2D", "og:title missing or does not match title", find_line(r'og:title'))

    m_og_desc = re.search(r'<meta\s+property="og:description"\s+content="(.*?)"', content, re.IGNORECASE)
    og_desc_text = m_og_desc.group(1).strip() if m_og_desc else ""
    if not og_desc_text or og_desc_text != desc_text:
        report(2, "2E", "og:description missing or does not match description", find_line(r'og:description'))

    m_og_url = re.search(r'<meta\s+property="og:url"\s+content="(.*?)"', content, re.IGNORECASE)
    og_url_text = m_og_url.group(1) if m_og_url else ""
    if not og_url_text or og_url_text != canon_text:
        report(2, "2F", "og:url missing or does not match canonical href exactly", find_line(r'og:url'))

    m_og_image = re.search(r'<meta\s+property="og:image"\s+content="(.*?)"', content, re.IGNORECASE)
    og_image_text = m_og_image.group(1) if m_og_image else ""
    if not og_image_text or "og-default" in og_image_text:
        report(2, "2G", "og:image missing or contains og-default", find_line(r'og:image'))

    if re.search(r'&[a-zA-Z0-9#]+;', title_text) or re.search(r'&[a-zA-Z0-9#]+;', desc_text):
        report(2, "2H", "HTML entities present in title or meta description content", find_line(r'<title>|name="description"'))

    # --- GROUP 3 ---
    style_blocks = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
    if len(style_blocks) != 1:
        report(3, "3A", f"{len(style_blocks)} style blocks present", find_line(r'<style>'))
    
    style_content = style_blocks[0] if style_blocks else ""
    if ":root { --page-accent: #0056b3; }" not in style_content and ":root{--page-accent:#0056b3;}" not in style_content.replace(' ', ''):
        report(3, "3B", ":root { --page-accent: #0056b3; } missing", find_line(r'<style>'))

    if not re.search(r'\.hero-' + re.escape(slug) + r'\s*\{[^}]*background-image', style_content):
        report(3, "3C", "no rule targeting .hero-[slug] with background-image outside @media block", find_line(r'<style>'))

    if not re.search(r'@media\s*\(\s*max-width\s*:\s*768px\s*\)[^{]*\{[^}]*\.hero-' + re.escape(slug), style_content):
        report(3, "3D", "no @media (max-width: 768px) block containing .hero-[slug] background-image rule", find_line(r'<style>'))

    if "linear-gradient" in style_content:
        report(3, "3E", "linear-gradient appears anywhere in the style block", find_line(r'linear-gradient'))

    m_hero = re.search(r'<header[^>]*class="[^"]*hero[^"]*"[^>]*>', content)
    if m_hero and 'style=' in m_hero.group(0):
        report(3, "3F", "the <header class=\"hero ...\"> element has a style= attribute", find_line(r'<header[^>]*class="[^"]*hero[^"]*"'))

    rules_count = len(re.findall(r'\{', style_content))
    if rules_count > 4:
        report(3, "3G", "style block contains any rules other than permitted ones", find_line(r'<style>'))


    # --- GROUP 4 ---
    if re.search(r'<section\s+class="hero', content) or re.search(r'<section\s+class="portfolio-hero', content):
        report(4, "4A", "hero opens with <section class=\"hero\" or <section class=\"portfolio-hero\"", find_line(r'<section\s+class="hero|<section\s+class="portfolio-hero'))
    
    if m_hero:
        cls_attr = re.search(r'class="([^"]+)"', m_hero.group(0)).group(1)
        classes = cls_attr.split()
        if "hero" not in classes:
            report(4, "4B", "hero does not include class=\"hero\" standalone", find_line(r'<header[^>]*class="[^"]*hero'))
        if "hero-compact" not in classes:
            report(4, "4C", "hero-compact not present in hero element classes", find_line(r'<header[^>]*class="[^"]*hero'))
        if "hero-high-impact" not in classes:
            report(4, "4D", "hero-high-impact not present in hero element classes", find_line(r'<header[^>]*class="[^"]*hero'))
        if f"hero-{slug}" not in classes:
            report(4, "4E", f"no class matching hero-{slug} present", find_line(r'<header[^>]*class="[^"]*hero'))
    else:
        report(4, "4B", "opening hero tag does not exist", 0)

    hero_inner = re.search(r'<header[^>]*class="[^"]*hero[^"]*"[^>]*>(.*?)</header>', content, re.DOTALL)
    if not hero_inner:
        if re.search(r'<header[^>]*class="[^"]*hero[^"]*"[^>]*>.*?</section>', content, re.DOTALL):
            report(4, "4F", "hero element closes with </section>", find_line(r'<header[^>]*class="[^"]*hero'))
    else:
        h_content = hero_inner.group(1)
        if '<a class="btn"' in h_content or '<button>' in h_content:
            report(4, "4H", "<a class=\"btn\"> or <button> present inside the hero <header>", find_line(r'<a class="btn"|<button>'))
        if 'height' in m_hero.group(0):
            report(4, "4I", "style= attribute on hero element contains height or min-height", find_line(r'<header[^>]*class="[^"]*hero'))
        if '<img class="hero-image"' in h_content:
            report(4, "4J", "<img class=\"hero-image\"> present inside the hero <header>", find_line(r'<img class="hero-image"'))

    h1s = re.findall(r'<h1[^>]*>', content)
    if len(h1s) != 1:
        report(4, "4G", f"{len(h1s)} <h1> elements found", find_line(r'<h1'))

    # --- GROUP 5 ---
    trust_bars = re.findall(r'<div[^>]*class="[^"]*trust-bar[^"]*"[^>]*>', body_content)
    if not trust_bars:
        if 'sv-trust-bar' in body_content:
            report(5, "5A", "outer div uses class sv-trust-bar instead of trust-bar", find_line(r'sv-trust-bar'))
    else:
        tb_match = re.search(r'(<div[^>]*class="[^"]*trust-bar[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>)', body_content, re.DOTALL)
        tb_content = tb_match.group(1) if tb_match else body_content
        if '<div class="container">' not in tb_content:
            report(5, "5B", "<div class=\"container\"> missing inside trust bar outer div", find_line(r'trust-bar'))
        if 'class="trust-inner"' in tb_content and 'trust-bar-inner' not in tb_content:
            report(5, "5C", "inner div uses trust-inner instead of trust-bar-inner", find_line(r'trust-inner'))
        if 'class="divider"' in tb_content and 'trust-divider' not in tb_content:
            report(5, "5D", "dividers use class divider instead of trust-divider", find_line(r'class="divider"'))
        
        items_count = tb_content.count('class="trust-item"')
        if items_count != 3:
            report(5, "5E", f"{items_count} items present (expected 3)", find_line(r'trust-item'))
        
        if "BCA Registered" in tb_content:
            report(5, "5F", "BCA Registered appears inside the trust bar element", find_line(r'BCA Registered'))
        
        if "bizSAFE" in tb_content and 'class="sv-bizsafe"' not in tb_content:
            report(5, "5G", "bizSAFE text is hardcoded plain text", find_line(r'bizSAFE'))
            
        if 'class="sv-sites"' in tb_content:
            if not re.search(r'<strong>\s*<span class="sv-sites">', tb_content):
                report(5, "5H", "sv-sites span is not wrapped in <strong>", find_line(r'sv-sites'))
        else:
            if re.search(r'<strong>[0-9,]+\+?\s*Sites Protected</strong>', tb_content):
                report(5, "5H", "site count is hardcoded number instead of sv-sites span", find_line(r'Sites Protected'))

    # --- GROUP 6 ---
    if '<nav class="sv-breadcrumb" aria-label="Breadcrumb">' not in body_content:
        report(6, "6A", "missing or incorrect class", find_line(r'Breadcrumb'))

    idx_trust = body_content.find('class="trust-bar')
    idx_bread = body_content.find('class="sv-breadcrumb"')
    idx_hero = body_content.find('class="hero')
    idx_footer = body_content.find('<footer')
    idx_cta = body_content.find('class="cta-section')
    
    if idx_trust != -1 and idx_hero != -1 and idx_trust < idx_hero:
        report(7, "7A", "trust bar appears before hero", find_line(r'trust-bar'))
    if idx_bread != -1 and idx_trust != -1 and idx_bread < idx_trust:
        report(7, "7A", "breadcrumb appears before trust bar", find_line(r'sv-breadcrumb'))
    if idx_footer != -1 and idx_cta != -1 and idx_footer < idx_cta:
        report(7, "7A", "footer appears before CTA section", find_line(r'<footer'))

    if idx_trust != -1 and idx_bread != -1:
        between = body_content[idx_trust:idx_bread]
        if '</section>' in between or '<header' in between: 
            report(6, "6B", "other elements appear between trust bar and breadcrumb", find_line(r'sv-breadcrumb'))

    m_bc = re.search(r'<ol[^>]*>(.*?)</ol>', body_content, re.DOTALL)
    if m_bc:
        bc_html = m_bc.group(1)
        lis = re.findall(r'<li[^>]*>(.*?)</li>', bc_html, re.DOTALL)
        if len(lis) != 4:
            if len(lis) == 3:
                report(6, "6G", "only 3 levels present (missing sector level)", find_line(r'sv-breadcrumb'))
            else:
                report(6, "6G", f"{len(lis)} levels present", find_line(r'sv-breadcrumb'))
        if len(lis) > 0 and '<a href="/">' not in lis[0]:
            report(6, "6C", "First breadcrumb item missing or not linked to /", find_line(r'sv-breadcrumb'))
        if len(lis) > 1 and '<a href="/portfolio/">' not in lis[1]:
            report(6, "6D", "Second breadcrumb item missing or not linked to /portfolio/", find_line(r'sv-breadcrumb'))
        if len(lis) > 2:
            if '<a href=' not in lis[2]:
                report(6, "6E", "sector link is not linked (plain text)", find_line(r'sv-breadcrumb'))
            else:
                href = re.search(r'href="([^"]+)"', lis[2]).group(1)
                valid_sectors = ["/portfolio/condominiums/", "/portfolio/commercial/", "/portfolio/industrial/", "/portfolio/institutions/", "/portfolio/residential/", "/portfolio/healthcare/", "/portfolio/managed-living/", "/portfolio/data-centres/"]
                if href not in valid_sectors:
                    report(6, "6E", f"invalid sector href", find_line(r'sv-breadcrumb'))
        if len(lis) > 3:
            if '<a href=' in lis[3]:
                report(6, "6F", "fourth item is wrapped in <a> tag", find_line(r'sv-breadcrumb'))
            
    # --- GROUP 7 ---
    sections = re.findall(r'<section[^>]*class="([^"]*)"[^>]*>', body_content)
    if idx_bread != -1:
        post_bread = body_content[idx_bread:]
        m_sec = re.search(r'<section[^>]*class="([^"]*)"', post_bread)
        if m_sec:
            first_cls = m_sec.group(1)
            if 'sv-section-white' in first_cls:
                report(7, "7B", "first section class is sv-section-white instead", find_line(r'sv-section-white'))

    colors = []
    for cls in sections:
        if 'sv-section-grey' in cls: colors.append('grey')
        elif 'sv-section-white' in cls: colors.append('white')
        elif 'hero' not in cls and 'cta-section' not in cls: colors.append('other')
        
    for i in range(1, len(colors)):
        if colors[i] == colors[i-1] and colors[i] in ['grey', 'white']:
            report(7, "7C", f"two consecutive sections use same class", find_line(r'sv-section-'+colors[i]))

    m_pad = re.findall(r'<section[^>]*style="[^"]*padding[^"]*"', body_content)
    if m_pad:
        report(7, "7D", "any <section> element has style=\"padding:...\"", find_line(r'<section[^>]*style='))

    m_cta = re.search(r'<section[^>]*class="([^"]*cta-section[^"]*)"', body_content)
    if m_cta:
        cls = m_cta.group(1)
        if 'cta-high-impact' not in cls:
            report(7, "7E", "cta-high-impact missing from the final CTA element", find_line(r'cta-section'))
        if not any(x in cls for x in ['cta-property', 'cta-facilities', 'cta-compliance', 'cta-care']):
            report(7, "7J", "CTA section does not include property/facilities/compliance/care class", find_line(r'cta-section'))
    else:
        report(7, "7E", "cta-section missing", 0)
        
    cta_match = re.search(r'<section[^>]*class="[^"]*cta-section[^"]*"[^>]*>(.*?)</section>', body_content, re.DOTALL)
    if cta_match:
        cta_content = cta_match.group(1)
        if '<h2' not in cta_content:
            report(7, "7F", "no <h2> inside the CTA section", find_line(r'cta-section'))
        
        btn_match = re.search(r'<a[^>]*class="[^"]*btn[^"]*"[^>]*>(.*?)</a>', cta_content, re.DOTALL)
        if btn_match:
            lbl = btn_match.group(1).strip()
            if lbl != "Request a Proposal":
                report(7, "7G", "button reads different label", find_line(r'cta-section'))
        else:
            report(7, "7G", "no button found in CTA", find_line(r'cta-section'))
            
        if 'sv-licence' not in cta_content and ('Police' in cta_content or 'Licence' in cta_content or 'trust note' in cta_content):
            report(9, "9E", "CTA section contains a trust note but no sv-licence span", find_line(r'cta-section'))
            
    if '<div class="card"' in body_content or '<a class="card"' in body_content:
        report(7, "7H", "manual portfolio cards present instead of sv-portfolio-block", find_line(r'class="card"'))

    if 'sv-systems-block' not in body_content and ('systems-grid' in body_content or 'portfolio-system-card' in body_content):
        if re.search(r'<div[^>]*class="[^"]*portfolio-system-card', body_content):
            report(7, "7I", "manual system cards present instead of sv-systems-block", find_line(r'portfolio-system-card'))


    # --- GROUP 8 ---
    body_clean = re.sub(r'stat-bar-fill[^>]*style="width:[0-9]+%"', '', body_content)
    body_clean = re.sub(r'<header[^>]*class="[^"]*hero[^"]*"[^>]*>', '', body_clean)
    body_clean = re.sub(r'style="[^"]*line-height:\s*24px[^"]*"', '', body_clean) 
    
    m_style = re.search(r'<([a-zA-Z0-9]+)[^>]*style="([^"]+)"', body_clean)
    if m_style:
        report(8, "8A", f"element <{m_style.group(1)}> has style=\"{m_style.group(2)}\"", find_line(r'style="'))

    # --- GROUP 9 ---
    if re.search(r'L/PS/[0-9]+', body_content):
        report(9, "9A", "L/PS/ appears as plain text", find_line(r'L/PS/'))
    b_match = re.finditer(r'bizSAFE Level 3', body_content)
    for b in b_match:
        prefix = body_content[max(0, b.start()-30):b.start()]
        if 'sv-bizsafe' not in prefix:
            report(9, "9B", "bizSAFE Level 3 appears as plain text", find_line(r'bizSAFE Level 3'))
            break

    s_match = re.finditer(r'2,000\+', body_content)
    for s in s_match:
        prefix = body_content[max(0, s.start()-30):s.start()]
        if 'sv-sites' not in prefix:
            report(9, "9C", "2,000+ appears as plain text", find_line(r'2,000\+'))
            break
            
    sv_sites_iter = re.finditer(r'<span class="sv-sites">', body_content)
    for s in sv_sites_iter:
        prefix = body_content[max(0, s.start()-10):s.start()]
        if not prefix.strip().endswith('<strong>'):
            report(9, "9D", "sv-sites exists but is not wrapped in <strong>", find_line(r'sv-sites'))
            break

    # --- GROUP 10 ---
    hrefs = re.findall(r'href="([^"]+)"', body_content)
    for h in hrefs:
        if h.startswith('./') or h.startswith('../') or not (h.startswith('/') or h.startswith('http') or h.startswith('mailto:') or h.startswith('tel:') or h.startswith('#')):
            report(10, "10A", f"href begins with invalid path: {h}", find_line(re.escape(h)))
            break

    srcs = re.findall(r'src="([^"]+)"', body_content)
    for s in srcs:
        if s.startswith('./') or s.startswith('../') or not (s.startswith('/') or s.startswith('http')):
            report(10, "10B", f"src begins with invalid path: {s}", find_line(re.escape(s)))
            break

    imgs = re.findall(r'<img[^>]*>', body_content)
    for img in imgs:
        alt_match = re.search(r'alt="([^"]*)"', img)
        if not alt_match or not alt_match.group(1).strip() or len(alt_match.group(1).split()) <= 1:
            report(10, "10C", "<img> has alt=\"\" or missing or single word", find_line(r'<img'))
            break

    h_tags = re.findall(r'<h([1-6])[^>]*>', body_content)
    highest_seen = 1
    for h in h_tags:
        lvl = int(h)
        if lvl > highest_seen + 1:
            report(10, "10D", "heading levels are skipped", find_line(r'<h'+h))
            break
        highest_seen = max(highest_seen, lvl)
        
    ids = re.findall(r'id="([^"]+)"', body_content)
    if len(ids) != len(set(ids)):
        report(10, "10E", "duplicate id attributes present", find_line(r'id="'))

    placeholders = ["Lorem ipsum", "TODO", "PLACEHOLDER", "TBC", "Coming soon", "[INSERT", "FIXME"]
    for p in placeholders:
        if p in content:
            report(10, "10F", f"text contains placeholder", find_line(p))
            break

    text_only = re.sub(r'<[^>]+>', ' ', body_content)
    text_only = re.sub(r'License Plate Recognition|LPR', '', text_only)
    text_only = re.sub(r'ColorVu', '', text_only)
    if re.search(r'\bcolor\b', text_only, re.IGNORECASE):
        report(10, "10G", "color appears as a word in visible content", find_line(r'\bcolor\b'))
    if re.search(r'\bcenter\b', text_only, re.IGNORECASE):
        report(10, "10G", "center appears as a word in visible content", find_line(r'\bcenter\b'))
    if re.search(r'\boptimiz(e|ed|ation)\b', text_only, re.IGNORECASE):
        report(10, "10G", "optimize/optimized/optimization appears", find_line(r'\boptimiz(e|ed|ation)\b'))
    if re.search(r'\bauthorization\b', text_only, re.IGNORECASE):
        report(10, "10G", "authorization appears in visible content", find_line(r'\bauthorization\b'))
    if re.search(r'\blicense\b', text_only, re.IGNORECASE):
        report(10, "10G", "license appears as a noun in visible content", find_line(r'\blicense\b'))
    if re.search(r'\banalyz(e|ed)\b', text_only, re.IGNORECASE):
        report(10, "10G", "analyze/analyzed appears in visible content", find_line(r'\banalyz(e|ed)\b'))

output = []
output.append("### SECTION 1 — SUMMARY TABLE")
output.append("")
output.append("| Check Group | Description | Pages with failures | Total failures |")
output.append("|---|---|---|---|")
descriptions = ["Infrastructure", "Head / SEO / Meta", "Style Block", "Hero", "Trust Bar", "Breadcrumb", "Page Structure and Sections", "Inline Styles", "Dynamic Values", "Content and Links"]
for i in range(1, 11):
    g_errs = errors[f"Group {i}"]
    pages_with_fail = len(set([e.split(' → ')[0] for e in g_errs]))
    output.append(f"| Group {i} | {descriptions[i-1]} | {pages_with_fail} | {len(g_errs)} |")
output.append("")

output.append("### SECTION 2 — DETAILED FINDINGS")
output.append("")
for i in range(1, 11):
    g_errs = errors[f"Group {i}"]
    if g_errs:
        g_errs.sort()
        for e in g_errs:
            output.append(e)
output.append("")

output.append("### SECTION 3 — CLEAN PAGES")
output.append("")
clean_pages = [f for f in files_list if f not in files_with_errors]
if clean_pages:
    for c in sorted(clean_pages):
        output.append(c)
else:
    output.append("No clean pages found.")
output.append("")

output.append("### SECTION 4 — PRIORITY FINDINGS")
output.append("")
failure_pages = {}
for i in range(1, 11):
    for e in errors[f"Group {i}"]:
        file_part, rest = e.split(' → ')
        file_path = file_part.replace('FILE: ', '').strip()
        err_part, line_part = rest.split(' — line ')
        CheckID = err_part.split(' ')[0]
        desc = err_part[len(CheckID):].strip()
        key = f"[{CheckID}] {desc}"
        if key not in failure_pages:
            failure_pages[key] = set()
        failure_pages[key].add(file_path)

counts = [(k, len(v)) for k, v in failure_pages.items()]
counts.sort(key=lambda x: x[1], reverse=True)
for i in range(min(5, len(counts))):
    output.append(f"{counts[i][0]} — affects {counts[i][1]} of 52 pages")

with open(os.path.join(base_dir, r"scratch\audit_52_report.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(output))

