import os

base_dir = 'C:/Projects/SV-Build/'

files = [
    'systems/index.html',
    'systems/premises-security.html',
    'systems/entry-access-control.html',
    'systems/vehicle-lpr-management.html',
    'systems/ip-phone-communications.html',
    'systems/security-management-platform.html',
    'systems/network-infrastructure.html'
]

# CHANGES DICTIONARY
# format: { filename: [ (find_string, replace_string, change_letter, allow_multiple), ... ] }

changes = {f: [] for f in files}

# CHANGE A: Trust bar
trust_bar_find = """<div class="sv-trust-bar">
  <div class="container">
    <div class="trust-flex-inline">
      <span>Police Licensed</span>
      <span class="sep">|</span>
      <span class="sv-bizsafe"></span>
      <span class="sep">|</span>
      <span>BCA Registered</span>
      <span class="sep">|</span>
      <span><span class="sv-sites"></span> Sites Protected</span>
    </div>
  </div>
</div>"""

trust_bar_replace = """<div class="trust-bar">
  <div class="container">
    <div class="trust-bar-inner">
      <span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>
    </div>
  </div>
</div>"""

for f in files[:-1]:
    changes[f].append((trust_bar_find, trust_bar_replace, 'A', False))

trust_bar_net_find = """    <div class="sv-trust-bar">
      <div class="container">
        <div class="trust-bar-inner">
          <span>Police Licensed</span>
          <span class="divider">|</span>
          <span class="sv-bizsafe"></span>
          <span class="divider">|</span>
          <span>BCA Registered</span>
          <span class="divider">|</span>
          <span><span class="sv-sites"></span> Sites Protected</span>
        </div>
      </div>
    </div>"""

trust_bar_net_replace = """    <div class="trust-bar">
      <div class="container">
        <div class="trust-bar-inner">
          <span>Police Licensed</span>
          <span class="trust-divider">|</span>
          <span class="sv-bizsafe"></span>
          <span class="trust-divider">|</span>
          <span><strong class="sv-sites"></strong> Sites Protected</span>
        </div>
      </div>
    </div>"""

changes['systems/network-infrastructure.html'].append((trust_bar_net_find, trust_bar_net_replace, 'A', False))

# CHANGE B: Hero class addition
hero_data = {
    'systems/index.html': ('class="hero-high-impact hero-systems"', 'class="hero-high-impact hero-standard hero-systems"'),
    'systems/entry-access-control.html': ('class="hero-high-impact hero-access"', 'class="hero-high-impact hero-standard hero-access"'),
    'systems/vehicle-lpr-management.html': ('class="hero-high-impact hero-vehicle"', 'class="hero-high-impact hero-standard hero-vehicle"'),
    'systems/ip-phone-communications.html': ('class="hero-high-impact hero-comms"', 'class="hero-high-impact hero-standard hero-comms"'),
    'systems/security-management-platform.html': ('class="hero-high-impact hero-platform"', 'class="hero-high-impact hero-standard hero-platform"'),
    'systems/network-infrastructure.html': ('class="hero-high-impact hero-network"', 'class="hero-high-impact hero-standard hero-network"')
}
for f, (find_str, rep_str) in hero_data.items():
    changes[f].append((find_str, rep_str, 'B', False))

# DETAIL PAGES C-G
detail_pages = [
    'systems/premises-security.html',
    'systems/entry-access-control.html',
    'systems/vehicle-lpr-management.html',
    'systems/ip-phone-communications.html',
    'systems/security-management-platform.html'
]

c_find = '<div class="grid-2" style="gap:48px;">'
c_rep = '<div class="grid-2 sys-grid-wide">'

d_find = '<div class="feature-card feature-card--full" style="margin-top: 64px; padding: 24px;">'
d_rep = '<div class="feature-card feature-card--full sys-integration-panel">'

e_find = '<div class="grid-2" style="gap:32px; margin-bottom:48px;">'
e_rep = '<div class="grid-2 sys-grid-who">'

f_find = '<div class="callout-box" style="margin-top:24px;">'
f_rep = '<div class="callout-box mt-24">'

g_find = '<div class="grid-2" style="gap:48px; align-items:start;">'
g_rep = '<div class="grid-2 sys-grid-process">'

for f in detail_pages:
    changes[f].extend([
        (c_find, c_rep, 'C', False),
        (d_find, d_rep, 'D', False),
        (e_find, e_rep, 'E', False),
        (f_find, f_rep, 'F', True), # appears twice
        (g_find, g_rep, 'G', False),
    ])

# INDEX ONLY H-K
idx = 'systems/index.html'
changes[idx].extend([
    ('<div class="group-accent-bar" style="background:#0056b3;"></div>', '<div class="group-accent-bar"></div>', 'H', False),
    ('<div class="callout-box" style="margin-top:24px;">', '<div class="callout-box mt-24">', 'I', False),
    ('<div class="grid-2" style="gap:48px; align-items:start;">', '<div class="grid-2 sys-grid-process">', 'J', False),
    ('<li>bizSAFE Level 3</li>', '<li><span class="sv-bizsafe"></span></li>', 'K', False)
])

# NETWORK INFRASTRUCTURE ONLY L-W
net = 'systems/network-infrastructure.html'
changes[net].extend([
    ('class="card card-clickable" style="align-self:start"', 'class="card card-clickable card-align-start"', 'L', True), # appears twice
    ('<div class="mt-32" style="background:var(--white); border:1px solid var(--border-light); border-radius:12px; padding:32px 40px; text-align:center;">', '<div class="mt-32 sys-info-panel">', 'M', False),
    ('<p style="font-family:\'Inter\',sans-serif; color:var(--text-gray); max-width:640px; margin:0 auto 20px;">', '<p class="sys-info-panel-intro">', 'N', False),
    ('<div class="mt-32" style="background:var(--white); border-radius:12px; padding:32px 40px;">', '<div class="mt-32 sys-lifecycle-panel">', 'O', False),
    ('<p style="font-family:\'Montserrat\',sans-serif; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-light); margin-bottom:24px;">The Securevision Support Lifecycle</p>', '<p class="sys-lifecycle-label">The Securevision Support Lifecycle</p>', 'P', False),
    ('<div style="text-align:center;">', '<div class="sys-lifecycle-step">', 'Q', True), # 4 times
    ('<div style="font-size:28px; margin-bottom:10px;">📋</div>', '<span class="sys-lifecycle-icon">📋</span>', 'R', False),
    ('<div style="font-size:28px; margin-bottom:10px;">🔧</div>', '<span class="sys-lifecycle-icon">🔧</span>', 'R', False),
    ('<div style="font-size:28px; margin-bottom:10px;">📡</div>', '<span class="sys-lifecycle-icon">📡</span>', 'R', False),
    ('<div style="font-size:28px; margin-bottom:10px;">🔄</div>', '<span class="sys-lifecycle-icon">🔄</span>', 'R', False),
    ('<p style="font-family:\'Montserrat\',sans-serif; font-size:13px; font-weight:700; color:var(--text-dark); margin-bottom:6px;">Site Assessment</p>', '<p class="sys-lifecycle-title">Site Assessment</p>', 'S', False),
    ('<p style="font-family:\'Montserrat\',sans-serif; font-size:13px; font-weight:700; color:var(--text-dark); margin-bottom:6px;">Installation</p>', '<p class="sys-lifecycle-title">Installation</p>', 'S', False),
    ('<p style="font-family:\'Montserrat\',sans-serif; font-size:13px; font-weight:700; color:var(--text-dark); margin-bottom:6px;">Remote Diagnostics</p>', '<p class="sys-lifecycle-title">Remote Diagnostics</p>', 'S', False),
    ('<p style="font-family:\'Montserrat\',sans-serif; font-size:13px; font-weight:700; color:var(--text-dark); margin-bottom:6px;">Ongoing Support</p>', '<p class="sys-lifecycle-title">Ongoing Support</p>', 'S', False),
    ('<p style="font-size:13px; color:var(--text-gray);">Device count, cable routes, switch placement, VLAN design, remote access requirements</p>', '<p class="sys-lifecycle-desc">Device count, cable routes, switch placement, VLAN design, remote access requirements</p>', 'T', False),
    ('<p style="font-size:13px; color:var(--text-gray);">Switch mounting, patching, VLAN configuration, AP placement and full commissioning</p>', '<p class="sys-lifecycle-desc">Switch mounting, patching, VLAN configuration, AP placement and full commissioning</p>', 'T', False),
    ('<p style="font-size:13px; color:var(--text-gray);">Switch health monitoring, port status, firmware updates via Omada or Ruijie Cloud</p>', '<p class="sys-lifecycle-desc">Switch health monitoring, port status, firmware updates via Omada or Ruijie Cloud</p>', 'T', False),
    ('<p style="font-size:13px; color:var(--text-gray);">Port reconfiguration, device additions, VLAN changes as your system grows</p>', '<p class="sys-lifecycle-desc">Port reconfiguration, device additions, VLAN changes as your system grows</p>', 'T', False),
    ('<div style="font-size:32px; margin-bottom:16px;">🔧</div>', '<span class="sys-card-icon">🔧</span>', 'U', False),
    ('<div style="font-size:32px; margin-bottom:16px;">🏗️</div>', '<span class="sys-card-icon">🏗️</span>', 'U', False),
    ('<div style="font-size:32px; margin-bottom:16px;">📡</div>', '<span class="sys-card-icon">📡</span>', 'U', False),
    ('<section class="sv-section-grey" style="padding: 64px 0;">', '<section class="sv-section-grey sys-section-compact">', 'V', False),
    ('<div class="grid-2" style="gap:32px; margin-bottom:48px;">', '<div class="grid-2 sys-grid-who">', 'W', False),
    ('<div class="grid-2" style="gap:48px; align-items:start;">', '<div class="grid-2 sys-grid-process">', 'W', False),
    ('<div class="callout-box" style="margin-top:24px;">', '<div class="callout-box mt-24">', 'W', True) # network page callout box, appears potentially multiple times
])


import re

report_applied = {f: [] for f in files}
report_missing = []

for f in files:
    full_path = os.path.join(base_dir, f)
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified_content = content
    
    for find_str, rep_str, letter, allow_multiple in changes[f]:
        count = modified_content.count(find_str)
        if count == 0:
            report_missing.append(f"- {f}: {letter} — Searched for: {find_str!r}")
        else:
            if not allow_multiple and count > 1:
                # Prompt says exact replacements. If it's more than 1 and not flagged, we might have an issue, but let's just replace all since they are exact.
                pass
            modified_content = modified_content.replace(find_str, rep_str)
            if letter not in report_applied[f]:
                report_applied[f].append(letter)
                
    # inline style check
    inline_styles = re.findall(r'style="[^"]*"', modified_content)
    
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
        
    print(f"Processed {f}")

print("\n--- REPORT DATA ---")
for f in files:
    print(f"{f} applied: {', '.join(report_applied[f])}")

print("\nMissing strings:")
for m in report_missing:
    print(m)

