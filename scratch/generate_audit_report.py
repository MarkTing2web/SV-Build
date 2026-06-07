import json
import datetime

with open('C:/Projects/SV-Build/scratch/audit_results.json', 'r') as f:
    results = json.load(f)

date_str = datetime.datetime.now().strftime("%B %d, %Y")
files_audited = len(results)

report = f"# Systems Section Remaining Audit\n**Date:** {date_str}\n**Files audited:** {files_audited}\n\n---\n\n"

# cross-page summary trackers
seo_fixes_needed = {} # file -> (title_issue, desc_issue)
missing_accents = []
missing_desk_heros = []
missing_mob_heros = []
link_issues_list = []
alt_issues_list = []
neutral_missing_list = []
dyn_issues_list = []
brit_issues_list = []

for filename, data in results.items():
    report += f"## {filename}\n\n"
    
    # SEO
    report += "### SEO Metadata\n"
    report += "| Tag | Content | Chars | Status | Action needed |\n"
    report += "|---|---|---|---|---|\n"
    
    seo = data['seo']
    
    # Title
    t_text = seo['title']
    t_chars = len(t_text)
    t_status = "GOOD"
    if t_chars < 50: t_status = "SHORT"
    elif t_chars > 60: t_status = "LONG"
    
    t_action = "none"
    if t_status != "GOOD" or "Singapore" not in t_text:
        # suggestion
        suggested = t_text
        if "Singapore" not in suggested: suggested += " | Singapore"
        if len(suggested) > 60: suggested = suggested[:57] + "..."
        t_action = f"suggested fix: {suggested}"
        
    report += f"| title | {t_text} | {t_chars} | {t_status} | {t_action} |\n"
    
    # Desc
    d_text = seo['desc']
    d_chars = len(d_text)
    d_status = "GOOD"
    if d_chars < 120: d_status = "SHORT"
    elif d_chars > 160: d_status = "LONG"
    
    d_action = "none"
    # check benefit led
    d_lower = d_text.lower()
    ben_led = True
    for p in ["we provide", "we are", "this is a", "our product", "securevision is", "securevision provides", "a system", "systems for"]:
        if d_lower.startswith(p): ben_led = False
        
    if not ben_led: d_action = "Make it benefit-led"
    if d_status != "GOOD": 
        if d_action == "none": d_action = f"Adjust length to 120-160 chars"
        else: d_action += ", adjust length"
        
    report += f"| description | {d_text} | {d_chars} | {d_status} | {d_action} |\n"
    
    # Canonical
    c_text = seo['canonical']
    c_flag = "OK"
    if not c_text.startswith("https://www.securevision.com.sg"): c_flag = "FLAG"
    report += f"| canonical | {c_text} | — | {c_flag} | — |\n"
    
    # OG tags
    for tag in ['og:title', 'og:description', 'og:image', 'og:url']:
        key = tag.replace(':', '_')
        if key == 'og_description': key = 'og_desc'
        val = seo[key]
        status = "OK"
        if val == "MISSING": status = "MISSING"
        elif tag in ['og:image', 'og:url'] and val.startswith('/'): status = "RELATIVE"
        report += f"| {tag} | {val} | — | {status} | — |\n"
        
    report += "\n"
    
    # Track for summary
    t_issue = None
    if t_status != "GOOD" or "Singapore" not in t_text: t_issue = f"{t_status}{' (No Singapore)' if 'Singapore' not in t_text else ''}"
    d_issue = None
    if d_status != "GOOD" or not ben_led: d_issue = f"{d_status}{' (Not Benefit-Led)' if not ben_led else ''}"
    
    if t_issue or d_issue:
        seo_fixes_needed[filename] = (t_issue or "OK", d_issue or "OK")
        
    # STYLE BLOCK
    report += "### Style Block\n"
    report += "| Rule | Status | Value |\n"
    report += "|---|---|---|\n"
    
    style = data['style']
    acc_status = "PRESENT" if style['accent'] != "MISSING" else "MISSING"
    dh_status = "PRESENT" if style['desk_hero'] != "MISSING" else "MISSING"
    mh_status = "PRESENT" if style['mob_hero'] != "MISSING" else "MISSING"
    
    report += f"| --page-accent | {acc_status} | {style['accent'] if acc_status == 'PRESENT' else '—'} |\n"
    report += f"| Desktop hero image | {dh_status} | {style['desk_hero'] if dh_status == 'PRESENT' else '—'} |\n"
    report += f"| Mobile hero @media | {mh_status} | {style['mob_hero'] if mh_status == 'PRESENT' else '—'} |\n"
    report += f"| Extra CSS in block | {style['other_css']} | {'—'} |\n\n"
    
    if acc_status == "MISSING": missing_accents.append(filename)
    if dh_status == "MISSING": missing_desk_heros.append(filename)
    if mh_status == "MISSING": missing_mob_heros.append(filename)
    
    # INTERNAL LINKS
    report += "### Internal Links — Flagged Only\n"
    links = data['links']
    if not links:
        report += "[none if clean]\n\n"
    else:
        report += "| Line | href | Issue |\n|---|---|---|\n"
        for l in links:
            report += f"| {l['line']} | {l['href']} | {l['issue']} |\n"
            link_issues_list.append(f"{filename} (Line {l['line']}): {l['issue']}")
        report += "\n"
            
    # ALTS
    report += "### Image Alt Text — Flagged Only\n"
    alts = data['alts']
    if not alts:
        report += "[none if clean]\n\n"
    else:
        report += "| Line | src (truncated) | Issue |\n|---|---|---|\n"
        for a in alts:
            report += f"| {a['line']} | {a['src']} | {a['issue']} |\n"
            alt_issues_list.append(f"{filename} (Line {a['line']}): {a['issue']}")
        report += "\n"
            
    # FEATURE CARD
    if filename != "index.html":
        report += "### Feature Card Neutral (detail pages only)\n"
        fc = data['feature_cards']
        pos = fc['pos'] if fc['pos'] else "MISSING"
        neg = fc['neg'] if fc['neg'] else "MISSING"
        neg_status = "has feature-card--neutral" if "feature-card--neutral" in neg else "MISSING feature-card--neutral"
        if neg_status == "MISSING feature-card--neutral": neutral_missing_list.append(filename)
        
        report += f"- Positive card: {pos}\n"
        report += f"- Negative card: {neg} — {neg_status}\n\n"
        
    # DYNAMIC VALUES
    report += "### Dynamic Values — Flagged Only\n"
    dyns = data['dyn']
    if not dyns:
        report += "[none if clean]\n\n"
    else:
        report += "| Line | Text found | Should use |\n|---|---|---|\n"
        for d in dyns:
            report += f"| {d['line']} | {d['text']} | {d['should']} |\n"
            dyn_issues_list.append(f"{filename} (Line {d['line']}): {d['text']} -> {d['should']}")
        report += "\n"
        
    # BRITISH ENGLISH
    report += "### British English — Flagged Only\n"
    brits = data['brit']
    if not brits:
        report += "[none if clean]\n\n---\n\n"
    else:
        report += "| Line | Text found | Correction |\n|---|---|---|\n"
        for b in brits:
            report += f"| {b['line']} | {b['text']} | {b['corr']} |\n"
            brit_issues_list.append(f"{filename} (Line {b['line']}): {b['text']} -> {b['corr']}")
        report += "\n---\n\n"

# SUMMARY
report += "## Cross-Page Summary\n\n"

report += "### SEO fixes needed:\n"
report += "| File | Title issue | Description issue |\n|---|---|---|\n"
for f, (ti, di) in seo_fixes_needed.items():
    report += f"| {f} | {ti} | {di} |\n"
if not seo_fixes_needed:
    report += "| - | - | - |\n"
    
report += "\n### Style block fixes needed:\n"
report += "| File | Missing --page-accent | Missing desktop hero | Missing mobile hero |\n|---|---|---|---|\n"
style_files = set(missing_accents + missing_desk_heros + missing_mob_heros)
for f in style_files:
    ma = "YES" if f in missing_accents else "NO"
    md = "YES" if f in missing_desk_heros else "NO"
    mm = "YES" if f in missing_mob_heros else "NO"
    report += f"| {f} | {ma} | {md} | {mm} |\n"
if not style_files:
    report += "| - | - | - | - |\n"

report += "\n### Internal links to fix:\n"
if link_issues_list:
    for l in link_issues_list: report += f"- {l}\n"
else:
    report += "None\n"
    
report += "\n### Alt text to fix:\n"
if alt_issues_list:
    for a in alt_issues_list: report += f"- {a}\n"
else:
    report += "None\n"
    
report += "\n### Feature card--neutral missing:\n"
if neutral_missing_list:
    for n in neutral_missing_list: report += f"- {n}\n"
else:
    report += "None\n"
    
report += "\n### Dynamic value violations:\n"
if dyn_issues_list:
    for d in dyn_issues_list: report += f"- {d}\n"
else:
    report += "None\n"
    
report += "\n### British English corrections:\n"
if brit_issues_list:
    for b in brit_issues_list: report += f"- {b}\n"
else:
    report += "None\n"
    
report += "\n### Overall status:\n"
report += f"{len(seo_fixes_needed)} files need SEO fixes\n"
report += f"{len(style_files)} files need style block fixes\n"
report += f"{len(link_issues_list)} internal link issues\n"
report += f"{len(alt_issues_list)} alt text issues\n"
report += f"{len(neutral_missing_list)} feature-card--neutral missing\n"
report += f"{len(dyn_issues_list)} dynamic value violations\n"
report += f"{len(brit_issues_list)} British English corrections\n"

with open("C:/Projects/SV-Build/_ai/audit-systems-remaining.md", "w", encoding='utf-8') as f:
    f.write(report)

print("Report generation complete.")
