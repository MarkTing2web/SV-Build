import sys

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\site-config.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    # 1. access-control-upgrade-drivers-singapore
    ('title: "Access Control Upgrade Drivers in Singapore"', 'title: "Three Reasons Singapore Organisations Should Review Their Access Control System Now"'),
    ('category: "Access & Intercom"', 'category: "Security Planning"'),
    ('date: "2026-06-15"', 'date: "2026-06-14"'),
    ('image: "access-control-upgrade-drivers-feature.webp"', 'image: "access-control-upgrade-drivers-singapore-feature.webp"'),

    # 2. alarm-communication-paths
    ('title: "How Your Alarm Communicates With the Monitoring Centre"', 'title: "Why Banks Use Multiple Communication Paths"'),
    ('date: "2026-03-12"', 'date: "2026-05-10"'),

    # 3. alarm-internet-cut
    ('title: "What Happens to My Alarm If the Internet Is Cut?"', 'title: "What Happens If a Burglar Cuts the Internet?"'),
    ('date: "2026-04-02"', 'date: "2026-05-31"'),

    # 4. alarm-monitoring-history
    ('title: "How Alarm Monitoring Evolved in Singapore"', 'title: "How Alarm Monitoring Worked Before the Internet"'),
    ('date: "2026-03-06"', 'date: "2026-05-04"'),

    # 5. alarm-panel
    ('title: "What Does an Alarm Panel Actually Do?"', 'title: "The Brain Behind Your Burglar Alarm"'),
    ('date: "2026-04-08"', 'date: "2026-04-07"'),

    # 6. alarm-panel-polling
    ('title: "What Is Alarm Panel Polling and Why Does It Matter?"', 'title: "Why Alarm Panels Used to Call Home Every Seven Days"'),
    ('date: "2026-03-09"', 'date: "2026-05-07"'),

    # 7. alarm-power-cut
    ('title: "What Happens to My Alarm During a Power Cut?"', 'title: "What Happens If a Burglar Cuts the Power?"'),
    ('date: "2026-04-05"', 'date: "2026-06-03"'),

    # 8. alarm-response
    ('date: "2026-02-13"', 'date: "2026-04-13"'),

    # 9. alarm-siren
    ('date: "2026-02-22"', 'date: "2026-04-22"'),

    # 10. alarm-system-lifespan
    ('date: "2026-03-27"', 'date: "2026-05-25"'),

    # 11. alarm-upgrade-or-replace
    ('title: "Should I Upgrade or Replace My Burglar Alarm System?"', 'title: "Should I Upgrade or Replace My Alarm System?"'),
    ('date: "2026-03-24"', 'date: "2026-05-22"'),

    # 12. alarm-usage-habits
    ('title: "Bad Alarm Habits That Undermine Your Security"', 'title: "Most Alarm Systems Are Installed Correctly But Used Incorrectly"'),

    # 13. alarm-wiring-reuse
    ('title: "Can I Reuse My Existing Alarm Wiring When Upgrading?"', 'title: "Can I Reuse My Existing Alarm Wiring?"'),
    ('date: "2026-03-21"', 'date: "2026-05-19"'),

    # 14. auto-gate-motor
    ('title: "Choosing the Right Auto Gate Motor for Your Property"', 'title: "How to Choose the Right Auto Gate Motor"'),

    # 15. break-in-nearby-security-review
    ('title: "There Has Been a Break-In Nearby. What Should You Do?"', 'title: "A Break-In Nearby Prompted This Security Review"'),
    ('date: "2026-04-14"', 'date: "2026-06-12"'),
    ('image: "break-in-nearby-feature.webp"', 'image: "break-in-nearby-security-review-feature.webp"'),

    # 16. burglar-alarm-design
    ('title: "How to Design a Burglar Alarm System"', 'title: "Protection Starts With Good Design"'),
    ('category: "Alarm & Intrusion"', 'category: "Alarm & Intrusion", date: "2026-04-01"'),

    # 17. burglar-alarm-detectors-sensors
    # Note: wait, for 16 and 17, replacing category: "Alarm & Intrusion" will replace ALL instances of it in the file!
    # I should write custom replacements for those that are too generic.
]

# Let's handle them carefully. I'll read line by line, or match specifically per slug, to avoid catastrophic global replacements.
# Because the instructions literally say `content.replace(old, new)`, but things like `category: "Alarm & Intrusion"` appear many times!
# But the user's brief is extremely strict. Let's look closely.
# "Use Python string replacement: content.replace(old, new) — do NOT use str_replace or line-number edits."
# Wait, if I do `content.replace('category: "Alarm & Intrusion"', 'category: "Alarm & Intrusion", date: "2026-04-01"')`, it will replace ALL of them.
# So I should only apply the replacements within the specific entry for that slug to be safe.

import re

# Parse file into entries
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

def replace_in_slug(slug, find_str, replace_str):
    for i, line in enumerate(lines):
        if f'slug: "{slug}"' in line:
            if find_str in line:
                lines[i] = line.replace(find_str, replace_str)
                print(f"Replaced in {slug}: {find_str[:30]}...")
            else:
                print(f"WARNING: Could not find '{find_str}' in slug {slug}")
            return
    print(f"WARNING: Could not find slug {slug}")

changes = {
    'access-control-upgrade-drivers-singapore': [
        ('title: "Access Control Upgrade Drivers in Singapore"', 'title: "Three Reasons Singapore Organisations Should Review Their Access Control System Now"'),
        ('category: "Access & Intercom"', 'category: "Security Planning"'),
        ('date: "2026-06-15"', 'date: "2026-06-14"'),
        ('image: "access-control-upgrade-drivers-feature.webp"', 'image: "access-control-upgrade-drivers-singapore-feature.webp"')
    ],
    'alarm-communication-paths': [
        ('title: "How Your Alarm Communicates With the Monitoring Centre"', 'title: "Why Banks Use Multiple Communication Paths"'),
        ('date: "2026-03-12"', 'date: "2026-05-10"')
    ],
    'alarm-internet-cut': [
        ('title: "What Happens to My Alarm If the Internet Is Cut?"', 'title: "What Happens If a Burglar Cuts the Internet?"'),
        ('date: "2026-04-02"', 'date: "2026-05-31"')
    ],
    'alarm-monitoring-history': [
        ('title: "How Alarm Monitoring Evolved in Singapore"', 'title: "How Alarm Monitoring Worked Before the Internet"'),
        ('date: "2026-03-06"', 'date: "2026-05-04"')
    ],
    'alarm-panel': [
        ('title: "What Does an Alarm Panel Actually Do?"', 'title: "The Brain Behind Your Burglar Alarm"'),
        ('date: "2026-04-08"', 'date: "2026-04-07"')
    ],
    'alarm-panel-polling': [
        ('title: "What Is Alarm Panel Polling and Why Does It Matter?"', 'title: "Why Alarm Panels Used to Call Home Every Seven Days"'),
        ('date: "2026-03-09"', 'date: "2026-05-07"')
    ],
    'alarm-power-cut': [
        ('title: "What Happens to My Alarm During a Power Cut?"', 'title: "What Happens If a Burglar Cuts the Power?"'),
        ('date: "2026-04-05"', 'date: "2026-06-03"')
    ],
    'alarm-response': [
        ('date: "2026-02-13"', 'date: "2026-04-13"')
    ],
    'alarm-siren': [
        ('date: "2026-02-22"', 'date: "2026-04-22"')
    ],
    'alarm-system-lifespan': [
        ('date: "2026-03-27"', 'date: "2026-05-25"')
    ],
    'alarm-upgrade-or-replace': [
        ('title: "Should I Upgrade or Replace My Burglar Alarm System?"', 'title: "Should I Upgrade or Replace My Alarm System?"'),
        ('date: "2026-03-24"', 'date: "2026-05-22"')
    ],
    'alarm-usage-habits': [
        ('title: "Bad Alarm Habits That Undermine Your Security"', 'title: "Most Alarm Systems Are Installed Correctly But Used Incorrectly"')
    ],
    'alarm-wiring-reuse': [
        ('title: "Can I Reuse My Existing Alarm Wiring When Upgrading?"', 'title: "Can I Reuse My Existing Alarm Wiring?"'),
        ('date: "2026-03-21"', 'date: "2026-05-19"')
    ],
    'auto-gate-motor': [
        ('title: "Choosing the Right Auto Gate Motor for Your Property"', 'title: "How to Choose the Right Auto Gate Motor"')
    ],
    'break-in-nearby-security-review': [
        ('title: "There Has Been a Break-In Nearby. What Should You Do?"', 'title: "A Break-In Nearby Prompted This Security Review"'),
        ('date: "2026-04-14"', 'date: "2026-06-12"'),
        ('image: "break-in-nearby-feature.webp"', 'image: "break-in-nearby-security-review-feature.webp"')
    ],
    'burglar-alarm-design': [
        ('title: "How to Design a Burglar Alarm System"', 'title: "Protection Starts With Good Design"'),
        ('category: "Alarm & Intrusion"', 'category: "Alarm & Intrusion", date: "2026-04-01"')
    ],
    'burglar-alarm-detectors-sensors': [
        ('category: "Alarm & Intrusion"', 'category: "Alarm & Intrusion", date: "2026-04-04"')
    ],
    'cctv-pdpa-compliance': [
        ('title: "CCTV and PDPA — What Singapore Property Owners Need to Know"', 'title: "Is My CCTV System PDPA Compliant?"')
    ],
    'cctv-system-components': [
        ('title: "The Four Components That Make Up a CCTV System"', 'title: "Most People Think CCTV Is Just Cameras. It Isn\'t."')
    ],
    'cctv-vs-alarm': [
        ('title: "CCTV vs Burglar Alarm — Do You Need Both?"', 'title: "Do I Still Need a Burglar Alarm If I Have CCTV?"'),
        ('date: "2026-03-30"', 'date: "2026-05-28"')
    ],
    'choose-intercom-for-home': [
        ('title: "How to Choose an Intercom for Your Home"', 'title: "How to Choose the Right Intercom for Your Home"'),
        ('category: "Access & Intercom"', 'category: "Security Planning"'),
        ('category: "Access & Intercom"', 'category: "Access & Intercom", date: "2026-04-29"'), # Wait, if I replace it first, the second one might fail!
        # Ah, in the prompt: category is changed twice. Wait, the prompt says:
        # CATEGORY: Find: category: "Access & Intercom" Replace: category: "Security Planning"
        # DATE: Find: category: "Access & Intercom" Replace: category: "Access & Intercom", date: "2026-04-29"
        # Since they act on the same thing, I need to chain them manually or adjust!
        # Actually, let's just do the exact replacements in the order they are listed.
    ],
    'compare-security-integrators': [
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-06-07"'),
        ('tags: ["integrator","tender","selection","singapore","contractor","comparison"] }', 'tags: ["integrator","tender","selection","singapore","contractor","comparison"], image: "compare-security-integrators-feature.webp" }')
    ],
    'condo-intercom-upgrade': [
        ('title: "Upgrading Your Condominium Intercom System — What Councils Need to Know"', 'title: "Condominium Intercom Upgrade — When Should Your Estate Start Planning?"')
    ],
    'condo-security-upgrade-timeline': [
        ('title: "Realistic Timeline and Disruption Plan for Condo Security Upgrade"', 'title: "Condominium Security Upgrade in Singapore — What MCST Councils Should Expect"'),
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-01"'),
        ('tags: ["condo","mcst","upgrade","timeline","residents"] }', 'tags: ["condo","mcst","upgrade","timeline","residents"], image: "condo-security-upgrade-timeline-feature.webp" }')
    ],
    'false-alarm-causes': [
        ('title: "The Most Common Causes of False Alarms — and How to Prevent Them"', 'title: "The Most Common Causes of False Alarms"'),
        ('date: "2026-02-25"', 'date: "2026-04-25"')
    ],
    'false-alarms': [
        ('title: "Why False Alarms Matter More Than You Think"', 'title: "Why False Alarms Matter"'),
        ('date: "2026-02-19"', 'date: "2026-04-19"')
    ],
    'gate-remote-smartphone': [
        ('title: "Controlling Your Gate With a Smartphone — What You Need to Know"', 'title: "Do You Still Need a Gate Remote?"')
    ],
    'guarding-technology-singapore': [
        ('category: "Platform & Integration"', 'category: "Security Planning"'),
        ('date: "2026-06-15"', 'date: "2026-04-01"'),
        ('image: "guarding-technology-feature.webp"', 'image: "guarding-technology-singapore-feature.webp"')
    ],
    'hdb-landed-condo-security-differences': [
        ('title: "HDB, Landed, or Condo — How Security Requirements Differ"', 'title: "HDB, Condominium or Landed Home — What Security System Do You Actually Need?"'),
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-01"'),
        ('tags: ["residential","hdb","landed","condo","singapore"] }', 'tags: ["residential","hdb","landed","condo","singapore"], image: "hdb-landed-condo-security-differences-feature.webp" }')
    ],
    'home-security-system-cost-singapore': [
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-01"'),
        ('tags: ["cost","residential","singapore","homeowner","budget"] }', 'tags: ["cost","residential","singapore","homeowner","budget"], image: "home-security-system-cost-singapore-feature.webp" }')
    ],
    'how-alarm-works': [
        ('title: "How a Burglar Alarm System Actually Works — From Trigger to Response"', 'title: "How Does a Burglar Alarm System Work?"'),
        ('date: "2026-04-08"', 'date: "2026-06-06"')
    ],
    'how-card-access-works': [
        ('title: "How Card Access Control Actually Works"', 'title: "What Actually Happens When You Tap Your Access Card?"'),
        # Same chaining issue:
        # CATEGORY Find: category: "Access & Intercom" Replace: category: "Security Planning"
        # DATE Find: category: "Access & Intercom" Replace: category: "Access & Intercom", date: "2026-04-01"
    ],
    'how-to-choose-cctv': [
        # Same chaining issue
    ],
    'installer-leaves': [
        ('title: "What to Do When Your Security Installer Leaves the Job"', 'title: "The Real Test Begins After the Installer Leaves"'),
        ('date: "2026-04-17"', 'date: "2026-06-15"')
    ],
    'intercom-system-evolution-singapore': [
        ('title: "How Intercom Systems Have Evolved in Singapore"', 'title: "IP Intercom vs Traditional Intercom — What Changed and Why It Matters for Your Property"'),
        ('category: "Access & Intercom"', 'category: "Security Planning"'),
        ('date: "2026-06-15"', 'date: "2026-04-01"'),
        ('image: "intercom-system-evolution-feature.webp"', 'image: "intercom-system-evolution-singapore-feature.webp"')
    ],
    'is-my-security-system-still-working': [
        ('title: "Is Your Security System Actually Still Working?"', 'title: "Is Your Security System Still Working?"'),
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-12"'),
        ('tags: ["maintenance","health-check","cctv","burglar-alarm"] }', 'tags: ["maintenance","health-check","cctv","burglar-alarm"], image: "is-my-security-system-still-working-feature.webp" }')
    ],
    'lpr-vs-rfid-condo': [
        ('title: "LPR vs RFID: Which Vehicle Access System Is Better for Your Condominium?"', 'title: "LPR vs RFID: Which Vehicle Access System Is Better For Your Condo?"')
    ],
    'maintain-burglar-alarm': [
        ('category: "Alarm & Intrusion"', 'category: "Alarm & Intrusion", date: "2026-04-01"'),
        ('tags: ["burglar-alarm","maintenance","battery","walk-test"] }', 'tags: ["burglar-alarm","maintenance","battery","walk-test"], image: "maintain-burglar-alarm-feature.webp" }')
    ],
    'maintenance-contract': [
        ('title: "Do You Need a Security System Maintenance Contract?"', 'title: "What Should a Security System Maintenance Contract Include?"'),
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-01"'),
        ('tags: ["maintenance","contract","sla","service"] }', 'tags: ["maintenance","contract","sla","service"], image: "maintenance-contract-feature.webp" }')
    ],
    'managing-agents-guide-estate-security-systems': [
        ('category: "Security Planning"', 'category: "Security Planning", date: "2026-04-01"'),
        ('tags: ["managing-agent","estate","mcst","systems"] }', 'tags: ["managing-agent","estate","mcst","systems"], image: "managing-agents-guide-estate-security-systems-feature.webp" }')
    ],
    'managing-multiple-estates-with-vesta': [
        ('title: "Managing Multiple Estates with VESTA"', 'title: "Managing Multiple Estates With VESTA — What It Does Today and Where It Is Heading"'),
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'mcst-legal-obligations-security': [
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'modern-detectors': [
        ('date: "2026-02-28"', 'date: "2026-04-28"')
    ],
    'monitoring-station': [
        ('title: "What Happens at a Security Monitoring Centre When Your Alarm Goes Off?"', 'title: "Inside a Central Monitoring Station"'),
        ('date: "2026-02-10"', 'date: "2026-04-10"')
    ],
    'network-security-systems': [
        ('title: "Why Your Security System Is Only as Good as Your Network"', 'title: "The Cameras Were Fine. The Network Was the Problem."'),
        ('date: "2026-04-20"', 'date: "2026-06-18"')
    ],
    'pstn-to-ip': [
        ('title: "From PSTN to IP Monitoring — Why the Phone Line Is No Longer Enough"', 'title: "From PSTN to IP Monitoring"'),
        ('date: "2026-03-15"', 'date: "2026-05-13"')
    ],
    'rackmount-nvr': [
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'reduce-false-alarms': [
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'security-assessment-10-things': [
        ('title: "10 Things a Security Assessment Should Tell You"', 'title: "10 Things I Look For When Assessing a Property\'s Security"'),
        ('date: "2026-04-11"', 'date: "2026-06-09"')
    ],
    'security-upgrade-condo-agm': [
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'self-monitoring-vs-cms': [
        ('date: "2026-03-18"', 'date: "2026-05-16"')
    ],
    'singapore-licensing': [
        ('date: "2026-03-03"', 'date: "2026-05-01"')
    ],
    'standalone-door-access': [
        ('title: "How to Choose a Standalone Door Access System"', 'title: "Standalone Door Access Control: When to Use It and What to Get Right"'),
        ('date: "2026-06-15"', 'date: "2026-04-01"')
    ],
    'system-repair-or-replace': [
        ('title: "Repair or Replace? How to Decide What to Do With an Ageing Security System"', 'title: "My System Is 10 Years Old. Should I Repair It or Replace It?"')
    ],
    'video-verification': [
        ('title: "Video Verification — Seeing the Alarm Before Responding"', 'title: "Video Verification: The Technology That Changed Alarm Monitoring"'),
        ('date: "2026-02-16"', 'date: "2026-04-16"')
    ]
}

# Fix chaining issues manually for specific slugs
changes['choose-intercom-for-home'] = [
    ('title: "How to Choose an Intercom for Your Home"', 'title: "How to Choose the Right Intercom for Your Home"'),
    ('category: "Access & Intercom"', 'category: "Security Planning", date: "2026-04-29"'),
    ('tags: ["intercom","residential","homeowner","video-intercom"] }', 'tags: ["intercom","residential","homeowner","video-intercom"], image: "choose-intercom-for-home-feature.webp" }')
]

changes['how-card-access-works'] = [
    ('title: "How Card Access Control Actually Works"', 'title: "What Actually Happens When You Tap Your Access Card?"'),
    ('category: "Access & Intercom"', 'category: "Security Planning", date: "2026-04-01"'),
    ('tags: ["access-control","how-it-works","card","controller"] }', 'tags: ["access-control","how-it-works","card","controller"], image: "how-card-access-works-feature.webp" }')
]

changes['how-to-choose-cctv'] = [
    ('category: "CCTV & Surveillance"', 'category: "Security Planning", date: "2026-04-01"'),
    ('tags: ["cctv","selection","homeowner","commercial","singapore"] }', 'tags: ["cctv","selection","homeowner","commercial","singapore"], image: "how-to-choose-cctv-feature.webp" }')
]

# Wait, the instructions said:
# For choose-intercom-for-home:
# CATEGORY: Find: category: "Access & Intercom" Replace: category: "Security Planning"
# DATE: Find: category: "Access & Intercom" Replace: category: "Access & Intercom", date: "2026-04-29"
# This implies the final output should have category: "Security Planning", date: "2026-04-29".
# So combining them directly into `category: "Security Planning", date: "2026-04-29"` is exactly what's needed.

# Execute replacements per slug
for slug, replacements in changes.items():
    for f, r in replacements:
        replace_in_slug(slug, f, r)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Updates applied to site-config.js.")
