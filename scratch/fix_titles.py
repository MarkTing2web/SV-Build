import os

files_to_fix = {
    "why-mechanical-locks-not-enough.html": (
        "Why Mechanical Locks Are Not Enough for Security in Singapore",
        "Why Mechanical Locks Are Insufficient in Singapore"
    ),
    "how-to-choose-multi-door-access.html": (
        "How to Choose a Multi-Door Access Control System in Singapore",
        "How to Select a Multi-Door Access System in Singapore"
    ),
    "how-ip-cctv-works.html": (
        "How IP CCTV Works: A Practical Guide for Singapore Properties",
        "How IP CCTV Works: A Practical Guide for Singapore"
    ),
    "choose-intercom-for-home.html": (
        "Choosing the Right Intercom System for Your Home in Singapore",
        "Choosing the Right Home Intercom System in Singapore"
    ),
    "after-security-installation-support.html": (
        "Security System Support and Warranty in Singapore",
        "Security System Support and Warranties in Singapore"
    )
}

insights_dir = r"C:\Projects\SV-Build\insights"

for filename, (old_title, new_title) in files_to_fix.items():
    filepath = os.path.join(insights_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace in <title>
    content = content.replace(f"<title>{old_title}</title>", f"<title>{new_title}</title>")
    # Replace in og:title
    content = content.replace(f'content="{old_title}" property="og:title"', f'content="{new_title}" property="og:title"')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated {filename}")
