import re, os, glob

files = sorted(glob.glob("solutions/**/*.html", recursive=True))
files = [f for f in files if f.count(os.sep) > 1 or f.count("/") > 1]

subtitles = {
    "commercial/commercial-security-systems.html": "A retail shop, office, hotel, shopping mall, and commercial building each present a different security brief. We address all of them.",
    "commercial/hotel.html": "Integrated security for Singapore hotels — managing guest movement, staff access, and back-of-house protection without affecting the guest experience.",
    "condominiums/condominium-security-systems.html": "From estate CCTV and mobile intercom to LPR vehicle management and centralised monitoring — how condominium security systems work together.",
    "condominiums/managing-agents.html": "Integrated solutions that help Managing Agents reduce friction, improve visibility, and consolidate estate security operations across Singapore.",
    "condominiums/security-contractors.html": "Integrated systems that help security companies improve site visibility, reduce repetitive tasks, and deliver better outcomes for MCST clients.",
    "data-centres/data-centre-security-systems.html": "Data centre certifications require documented, auditable physical access control. We design systems that produce that documentation automatically.",
    "healthcare/day-care.html": "Senior day care, autism, and cerebral palsy centres need security that protects without restraining — built around care team workflows.",
    "healthcare/healthcare-security-systems.html": "Nursing homes and day care centres need security that prevents wandering, manages visitors, and supports MOH compliance — without harshness.",
    "industrial/industrial-security-systems.html": "Factories, logistics hubs, and tech parks need security that supports throughput, compliance, and safety — not systems that slow operations down.",
    "industrial/logistics.html": "High-volume logistics operations need gantry systems that process vehicles in seconds and loading bay surveillance covering every dock.",
    "industrial/manufacturing.html": "Manufacturing security means AI surveillance for PPE compliance on live production floors and WSH documentation — without stopping the line.",
    "industrial/tech-park.html": "Tech park managers need centralised security across tenants — perimeter control, multi-tenant access, and unified estate visibility.",
    "institutions/community.html": "Churches, mosques, temples, and community centres need security that protects people at gatherings without turning open spaces into controlled ones.",
    "institutions/govt-office.html": "Government offices and statutory boards operate under compliance and uptime requirements that standard commercial security does not address.",
    "institutions/institutions-security-systems.html": "Government offices, schools, and places of worship carry a duty of care — and a security obligation that must not create unnecessary barriers.",
    "institutions/schools.html": "Singapore schools and childcare centres need access control, visitor management, and CCTV that supports safeguarding without institutional harshness.",
    "managed-living/co-living.html": "Co-living properties need access control, visitor management, and shared space monitoring that scales with high resident turnover.",
    "managed-living/managed-living-security-systems.html": "Dormitory, co-living, or managed hostel — the brief is the same: know who is in your property at all times and prove it with compliance records.",
    "residential/architects-and-designers.html": "Reliable security sub-contracting for Singapore residential projects — pre-wiring schedules, clean installations, and zero callbacks for your clients."
}

def get_hero_class(content):
    m = re.search(r'<header[^>]*class="([^"]+)"', content)
    if not m: return None
    classes = m.group(1).split()
    for c in classes:
        if c.startswith('hero-') and c not in ['hero-high-impact', 'hero-compact', 'hero-standard', 'hero-vehicle-access', 'hero-title-main', 'hero-subtitle-main']:
            return c
    return None

for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    # Find the hero class
    hero_cls = get_hero_class(content)
    if not hero_cls:
        m2 = re.search(r'\.(hero-[a-z-]+)\s*\{', content)
        if m2:
            hero_cls = m2.group(1)
        else:
            continue
            
    # Remove hero-standard from header
    content = re.sub(r'(<header[^>]*class="[^"]*?)\bhero-standard\b\s*([^"]*?")', r'\1\2', content)
    content = re.sub(r'class="\s+', 'class="', content)
    content = re.sub(r'\s+"', '"', content)

    # Move background image
    bg_pattern = r'\.' + hero_cls + r'\s*\{\s*background-image:\s*(url\([^)]+\));\s*\}'
    bg_m = re.search(bg_pattern, content)
    if bg_m:
        bg_url = bg_m.group(1)
        content = re.sub(bg_pattern, '', content)
        
        if 'style="' not in re.search(r'<header[^>]*>', content).group(0):
            # some paths might be missing a quote or something, just insert it
            header_str = re.search(r'<header[^>]*>', content).group(0)
            new_header_str = header_str[:-1] + f' style="background: linear-gradient(to right, rgba(0,0,0,0.80) 0%, rgba(0,0,0,0.50) 55%, rgba(0,0,0,0.15) 100%), {bg_url} center/cover no-repeat;">'
            content = content.replace(header_str, new_header_str, 1)
            
    # remove mobile media query if present
    content = re.sub(r'@media\s*\([^)]+\)\s*\{\s*\.' + hero_cls + r'\s*\{\s*background-image:\s*url\([^)]+\);\s*\}\s*\}', '', content)

    # Add the CSS block
    if "min-height: 45vh" not in content:
        css_block = f"""
    /* Tier 4 subpage hero — 45vh */
    .hero-high-impact.{hero_cls} {{
      min-height: 45vh !important;
      padding: 72px 0 56px !important;
    }}
    .{hero_cls} .hero-title-main {{
      font-size: clamp(26px, 3.5vw, 42px) !important;
      margin-bottom: 16px !important;
    }}
    .{hero_cls} .hero-subtitle-main {{
      font-size: clamp(14px, 1.1vw, 17px) !important;
      margin-bottom: 28px !important;
    }}"""
        if ':root' in content:
            content = re.sub(r'(:root\s*\{[^}]+\})', r'\1\n' + css_block, content, count=1)
        else:
            content = re.sub(r'(</style>)', css_block + r'\n  \1', content)

    # Task 2: Update subtitle
    rel_path = path.replace("\\", "/").split("solutions/", 1)[-1]
    if rel_path in subtitles:
        new_sub = subtitles[rel_path]
        content = re.sub(r'(<p class="hero-subtitle-main">).*?(</p>)', rf'\1{new_sub}\2', content, flags=re.S)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)

print("Edits complete.")
