import os

repo_root = r"c:\Projects\SV-Build"

updates = {
    "solutions/automate-vehicle-access.html": [
        ("url('/images/solutions/automate-vehicle-access-hero-mobile.png')", "url('/images/solutions/hero-solutions/automate-vehicle-access-hero-mobile.webp')")
    ],
    "solutions/commercial/hotel.html": [
        (
            """    @media (max-width: 768px) {
      .hero-hotel { background-position: 70% center; }
    }""",
            """    @media (max-width: 768px) {
      .hero-hotel {
        background-image: linear-gradient(rgba(14, 26, 43, 0.72), rgba(14, 26, 43, 0.72)), url('/images/solutions/hero-solutions/solution-commercial-hotel-hero-mobile.webp');
        background-position: 70% center;
      }
    }"""
        )
    ],
    "solutions/commercial/office.html": [
        (
            """.hero-office {
      background: linear-gradient(rgba(14, 26, 43, 0.72), rgba(14, 26, 43, 0.72)), url('/images/solutions/hero-solutions/solution-commercial-office-hero.webp') no-repeat center/cover;
    }""",
            """.hero-office {
      background: linear-gradient(rgba(14, 26, 43, 0.72), rgba(14, 26, 43, 0.72)), url('/images/solutions/hero-solutions/solution-commercial-office-hero.webp') no-repeat center/cover;
    }
    @media (max-width: 768px) {
      .hero-office {
        background-image: linear-gradient(rgba(14, 26, 43, 0.72), rgba(14, 26, 43, 0.72)), url('/images/solutions/hero-solutions/solution-commercial-office-hero-mobile.webp');
      }
    }"""
        )
    ],
    "solutions/commercial/retail.html": [
        (
            """    @media (max-width: 768px) {
      .hero-retail { background-position: 70% center; }
    }""",
            """    @media (max-width: 768px) {
      .hero-retail {
        background-image: linear-gradient(rgba(14, 26, 43, 0.72), rgba(14, 26, 43, 0.72)), url('/images/solutions/hero-solutions/solution-commercial-retail-hero-mobile.webp');
        background-position: 70% center;
      }
    }"""
        )
    ],
    "solutions/improve-cctv-visibility.html": [
        ("url('/images/solutions/solution-improve-cctv-visibility-hero-mobile.png')", "url('/images/solutions/hero-solutions/solution-improve-cctv-visibility-hero-mobile.webp')")
    ],
    "solutions/improve-visitor-management.html": [
        ("url('/images/solutions/improve-visitor-management-hero-mobile.png')", "url('/images/solutions/hero-solutions/improve-visitor-management-hero-mobile.webp')")
    ],
    "solutions/reduce-guard-manpower.html": [
        ("url('/images/solutions/reduce-manpower-with-technology-mobile.png')", "url('/images/solutions/hero-solutions/reduce-manpower-with-technology-mobile.webp')")
    ],
    "solutions/upgrade-intercom-system.html": [
        ("url('/images/solutions/intercom-upgrade-hero-mobile.png')", "url('/images/solutions/hero-solutions/intercom-upgrade-hero-mobile.webp')")
    ]
}

for rel_path, replacements in updates.items():
    filepath = os.path.join(repo_root, rel_path)
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {rel_path}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    updated = False
    for target, replacement in replacements:
        # Normalize line endings for reliable matching on Windows
        target_norm = target.replace('\r\n', '\n').strip()
        content_norm = content.replace('\r\n', '\n')
        
        if target_norm in content_norm:
            content_norm = content_norm.replace(target_norm, replacement.replace('\r\n', '\n').strip())
            content = content_norm # keep normalized content
            updated = True
        else:
            # Let's try matching with space/newline normalization or simple substring if not matched
            print(f"WARNING: Target not matched exactly in {rel_path}.")
            # Print a snippet of the file to see why
            # print("File content snippet around style:")
            
    if updated:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"SUCCESS: Updated {rel_path}")
        # Print what was added
        for target, replacement in replacements:
            print(f"  Added:\n{replacement}\n")
    else:
        print(f"FAILED: No changes made to {rel_path}")
