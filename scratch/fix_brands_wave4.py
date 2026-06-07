import os
import re
from bs4 import BeautifulSoup

base_dir = "C:/Projects/SV-Build"
brands_dir = os.path.join(base_dir, "brands")

files_in_scope = [
    "aiphone-intercom.html", "ajax-alarms.html", "akuvox-access.html", "akuvox-intercom.html",
    "apollo-access.html", "dahua-cctv.html", "dormer-autogate.html", "dsc-alarms.html",
    "ebelco-locks.html", "entrypass-entry-access.html", "faac-autogate.html", "fanvil-intercom.html",
    "fanvil-ip-phone.html", "gantrygo.html", "ge-caddx-alarms.html", "hanwha-cctv.html",
    "hid-entry-access.html", "hikcentral.html", "hikvision-access.html", "hikvision-cctv.html",
    "hikvision-intercom.html", "hrui-network.html", "kocom-intercom.html", "mag-autogate.html",
    "microengine-entry-access.html", "milesight-cctv.html", "omada-network.html", "paradox-alarms.html",
    "risco-alarms.html", "ruijie-reyee-network.html", "suprema-entry-access.html", "uniview-cctv.html",
    "vesta.html", "viro-locks.html", "yealink-ip-phone.html", "yeastar-ippbx.html",
    "zkteco-cvsecurity.html", "zkteco-entry-access.html"
]

fixD_files = [
    "aiphone-intercom.html", "akuvox-access.html", "akuvox-intercom.html", "apollo-access.html",
    "dahua-cctv.html", "dormer-autogate.html", "ebelco-locks.html", "entrypass-entry-access.html",
    "faac-autogate.html", "fanvil-intercom.html", "fanvil-ip-phone.html", "gantrygo.html",
    "hid-entry-access.html", "hikcentral.html", "hikvision-access.html", "hikvision-intercom.html",
    "hrui-network.html", "kocom-intercom.html", "mag-autogate.html", "microengine-entry-access.html",
    "omada-network.html", "ruijie-reyee-network.html", "suprema-entry-access.html", "vesta.html",
    "viro-locks.html", "yealink-ip-phone.html", "yeastar-ippbx.html", "zkteco-cvsecurity.html",
    "zkteco-entry-access.html"
]

fixG_lines = {
    "akuvox-intercom.html": 431,
    "dahua-cctv.html": 183,
    "dormer-autogate.html": 134,
    "kocom-intercom.html": 179,
    "mag-autogate.html": 150,
    "suprema-entry-access.html": 323,
    "viro-locks.html": 161,
    "yealink-ip-phone.html": 177,
    "yeastar-ippbx.html": 0, # Will search for it
    "zkteco-cvsecurity.html": 186,
    "zkteco-entry-access.html": 368
}

stats = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'modified': 0
}

for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig_html = html
    
    # FIX A: H1 hero-title-main
    def h1_repl(m):
        attrs = m.group(1)
        if 'class="' in attrs:
            if 'hero-title-main' not in attrs:
                return f'<h1{re.sub(r"class=\"([^\"]*)\"", r"class=\"\1 hero-title-main\"", attrs)}>'
            return m.group(0)
        else:
            return f'<h1 class="hero-title-main"{attrs}>'
            
    # Apply only to first <h1> which is in hero
    html_new, n = re.subn(r'<h1([^>]*)>', h1_repl, html, count=1)
    if html_new != html:
        stats['A'] += 1
        html = html_new

    # FIX B: Hero subtitle hero-subtitle-main
    # The paragraph immediately after H1
    def p_repl(m):
        p_attrs = m.group(2)
        if 'class="' in p_attrs:
            if 'hero-subtitle-main' not in p_attrs:
                new_p = f'<p{re.sub(r"class=\"([^\"]*)\"", r"class=\"\1 hero-subtitle-main\"", p_attrs)}>'
            else:
                new_p = f'<p{p_attrs}>'
        else:
            new_p = f'<p class="hero-subtitle-main"{p_attrs}>'
        return f'</h1>{m.group(1)}{new_p}'
        
    html_new, n = re.subn(r'</h1>(\s*)<p([^>]*)>', p_repl, html, count=1)
    if html_new != html:
        stats['B'] += 1
        html = html_new

    # FIX C: sv-sites inside strong
    # Replace <span class="sv-sites"></span> with <strong class="sv-sites"></strong>
    # or <span class="sv-sites"> with <strong class="sv-sites"> and </span> with </strong>
    def site_repl(m):
        return f'<strong class="sv-sites">{m.group(1)}</strong>'
    html_new, n = re.subn(r'<span class="sv-sites">(.*?)</span>', site_repl, html)
    if html_new != html:
        stats['C'] += 1
        html = html_new

    # FIX D: eyebrow class
    if filename in fixD_files:
        # replace first occurrence of <span class="eyebrow"> with <span class="eyebrow-light">
        html_new, n = re.subn(r'<span class="eyebrow">', r'<span class="eyebrow-light">', html, count=1)
        if html_new != html:
            stats['D'] += 1
            html = html_new

    # FIX E: wrong CTA button labels
    cta_map = {
        "entrypass-entry-access.html": ("Discuss Your EntryPass System", "Request a Proposal"),
        "gantrygo.html": ("Request a Demo", "Request a Proposal"),
        "kocom-intercom.html": ("Service Enquiry", "Request a Proposal"),
        "microengine-entry-access.html": ("Discuss Your MicroEngine System", "Request a Proposal")
    }
    if filename in cta_map:
        old_val, new_val = cta_map[filename]
        # Only replace inside the final cta-section
        # Let's just do string replacement since it's unique
        html_new = html.replace(f">{old_val}<", f">{new_val}<")
        if html_new != html:
            stats['E'] += 1
            html = html_new

    # FIX F: British English spelling
    if filename == "hikcentral.html":
        # Replace "What We License" with "What We Licence"
        html_new = html.replace("What We License", "What We Licence")
        if html_new != html:
            stats['F'] += 1
            html = html_new

    # FIX G: Section alternation
    if filename in fixG_lines:
        soup = BeautifulSoup(html, 'html.parser')
        main = soup.find('main')
        if main:
            sections = main.find_all('section', recursive=False)
            prev_bg = None
            for s in sections:
                c = s.get('class', [])
                bg = 'grey' if 'sv-section-grey' in c else 'white' if 'sv-section-white' in c else None
                if bg:
                    if prev_bg == bg:
                        # Found collision
                        old_class = 'sv-section-grey' if bg == 'grey' else 'sv-section-white'
                        new_class = 'sv-section-white' if bg == 'grey' else 'sv-section-grey'
                        # To preserve spacing and exact formatting, let's find the exact section tag in raw HTML
                        # Since line numbers can shift slightly, we just search for consecutive identical backgrounds
                        pass
                    prev_bg = bg
        
        # Actually a safer way is to regex search all sections in <main> and enforce grey/white/grey/white
        # But we only need to flip the second one of a collision.
        # A simple state machine over the HTML string
        lines = html.split('\n')
        bg_state = None
        modified_g = False
        for i, line in enumerate(lines):
            if '<section class="sv-section' in line:
                if 'sv-section-grey' in line:
                    if bg_state == 'grey':
                        lines[i] = line.replace('sv-section-grey', 'sv-section-white')
                        modified_g = True
                        bg_state = 'white'
                    else:
                        bg_state = 'grey'
                elif 'sv-section-white' in line:
                    if bg_state == 'white':
                        lines[i] = line.replace('sv-section-white', 'sv-section-grey')
                        modified_g = True
                        bg_state = 'grey'
                    else:
                        bg_state = 'white'
        html_new = '\n'.join(lines)
        if modified_g:
            stats['G'] += 1
            html = html_new

    if html != orig_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        stats['modified'] += 1

# Audit
rem_A = []
rem_B = []
rem_C = []
rem_D = []
rem_E = []
rem_F = []

for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    hero = soup.find('header', class_=lambda c: c and 'hero' in c)
    if hero:
        h1 = hero.find('h1')
        if h1 and 'hero-title-main' not in h1.get('class', []):
            rem_A.append(filename)
            
        p = hero.find('p')
        if p and 'hero-subtitle-main' not in p.get('class', []):
            rem_B.append(filename)
            
        eyebrow = hero.find('span', class_='eyebrow')
        if eyebrow:
            rem_D.append(filename)
            
    if soup.find('span', class_='sv-sites'):
        rem_C.append(filename)
        
    cta = soup.body.find_all('section')[-1] if soup.body and soup.body.find_all('section') else None
    if cta:
        btn = cta.find('a', class_=lambda c: c and 'btn' in c)
        if btn:
            bt = btn.text.strip()
            if filename != 'vesta.html' and bt != 'Request a Proposal':
                rem_E.append(filename)
                
    if filename == "hikcentral.html":
        # check if noun license remains
        if "What We License" in html:
            rem_F.append(filename)

clean_count = 38 - len(set(rem_A + rem_B + rem_C + rem_D + rem_E + rem_F))

out = []
out.append("BRANDS SECTION FIX — WAVE 4 COMPLETION REPORT")
out.append("Files processed: 38")
out.append(f"Files modified: {stats['modified']}\n")
out.append(f"FIX A — H1 hero-title-main class added: {stats['A']} pages updated")
out.append(f"FIX B — Hero subtitle hero-subtitle-main class added: {stats['B']} pages updated")
out.append(f"FIX C — sv-sites wrapped in strong: {stats['C']} pages updated")
out.append(f"FIX D — Hero eyebrow class corrected to eyebrow-light: {stats['D']} pages updated")
out.append(f"FIX E — CTA button labels corrected: {stats['E']} pages updated")
out.append(f"FIX F — British English spelling corrected: {stats['F']} pages updated")
out.append(f"FIX G — Section alternation corrected: {stats['G']} pages updated\n")
out.append("AUDIT FINDINGS:")
out.append(f"A. Remaining H1 without hero-title-main: {', '.join([f.replace('.html', '') for f in rem_A]) if rem_A else 'None'}")
out.append(f"B. Remaining subtitles without hero-subtitle-main: {', '.join([f.replace('.html', '') for f in rem_B]) if rem_B else 'None'}")
out.append(f"C. Remaining sv-sites not in strong: {', '.join([f.replace('.html', '') for f in rem_C]) if rem_C else 'None'}")
out.append(f"D. Remaining eyebrow class issues: {', '.join([f.replace('.html', '') for f in rem_D]) if rem_D else 'None'}")
out.append(f"E. Remaining non-canonical CTA labels: {', '.join([f.replace('.html', '') for f in rem_E]) if rem_E else 'None'}")
out.append(f"F. Remaining British English issues: {', '.join([f.replace('.html', '') for f in rem_F]) if rem_F else 'None'}\n")
out.append(f"Pages with no remaining issues: {clean_count} / 38")

report_path = os.path.join(base_dir, '_ai/audit-brands-wave4-completion.md')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("Wave 4 fix and audit complete.")
