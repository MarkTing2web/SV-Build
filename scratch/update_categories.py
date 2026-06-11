import re

updates = {
    'burglar-alarm-design': 'Alarm & Intrusion',
    'how-burglar-alarm-works': 'Alarm & Intrusion',
    'burglar-alarm-detectors-sensors': 'Alarm & Intrusion',
    'maintain-burglar-alarm': 'Alarm & Intrusion',
    'reduce-false-alarms': 'Alarm & Intrusion',
    'using-your-burglar-alarm': 'Alarm & Intrusion',

    'how-to-choose-cctv': 'CCTV & Surveillance',
    'how-ip-cctv-works': 'CCTV & Surveillance',
    'rackmount-nvr': 'CCTV & Surveillance',
    'analogue-to-ip-migration': 'CCTV & Surveillance',
    'ai-analytics-hikvision': 'CCTV & Surveillance',
    'pdpa-cctv-singapore': 'CCTV & Surveillance',
    'video-analytics-retail-singapore': 'CCTV & Surveillance',

    'how-card-access-works': 'Access & Intercom',
    'how-to-choose-multi-door-access': 'Access & Intercom',
    'standalone-door-access': 'Access & Intercom',
    'how-intercom-systems-work': 'Access & Intercom',
    'choose-intercom-for-home': 'Access & Intercom',
    'upgrade-condo-intercom': 'Access & Intercom',
    'why-mechanical-locks-not-enough': 'Access & Intercom',

    'how-to-choose-auto-gate-motor': 'Vehicle & Gates',
    'wifi-remote-control-auto-gate': 'Vehicle & Gates',
    'lpr-vs-rfid-vehicle-access-singapore': 'Vehicle & Gates',

    'architect-id-guide-security': 'Security Planning',
    'hdb-landed-condo-security-differences': 'Security Planning',
    'home-security-system-cost-singapore': 'Security Planning',
    'compare-security-integrators': 'Security Planning',
    '10-tips-securing-your-premises': 'Security Planning',
    'is-my-security-system-still-working': 'Security Planning',
    'security-system-refresh': 'Security Planning',
    'upgrade-existing-security-system': 'Security Planning',
    'upgrade-or-repair': 'Security Planning',
    'mcst-legal-obligations-security': 'Security Planning',
    'security-upgrade-condo-agm': 'Security Planning',
    'condo-security-upgrade-quotes': 'Security Planning',
    'condo-security-upgrade-timeline': 'Security Planning',
    'condo-security-upgrade-proposal': 'Security Planning',
    'after-security-installation-support': 'Security Planning',
    'maintenance-contract': 'Security Planning',

    'managing-agents-guide-estate-security-systems': 'Platform & Integration',
    'managing-multiple-estates-with-vesta': 'Platform & Integration',
    'how-technology-makes-your-guarding-team-more-competitive': 'Platform & Integration',
}

with open(r'd:\Ler Wee Meng\Project-Web\SV-Build\site-config.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'slug:' in line and 'category:' in line:
        slug_match = re.search(r'slug:\s*"([^"]+)"', line)
        if slug_match:
            slug = slug_match.group(1)
            if slug in updates:
                new_cat = updates[slug]
                # calculate padding so that tags align roughly?
                # or just simple replace
                # It's better to preserve the existing spacing if possible, but let's just do simple string replace of the category value
                old_cat_match = re.search(r'(category:\s*")([^"]+)(")', line)
                if old_cat_match:
                    old_cat = old_cat_match.group(2)
                    new_line = line[:old_cat_match.start(2)] + new_cat + line[old_cat_match.end(2):]
                    
                    # Also let's re-pad the comma after category to align tags
                    # Let's see the old padding
                    # line format: ... category: "Old",         tags: ...
                    # If new_cat is longer or shorter, we can adjust spaces.
                    
                    # For now just simple replace:
                    lines[i] = new_line
            else:
                print(f"Warning: slug {slug} not found in updates dict.")

with open(r'd:\Ler Wee Meng\Project-Web\SV-Build\site-config.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done")
