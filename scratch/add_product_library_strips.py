import os
import re

workspace_dir = r"c:\Projects\SV-Build"

categories = {
    "Burglar Alarm": {
        "url": "/resources/library/burglar-alarm.html",
        "label": "burglar alarm",
        "files": [
            "brands/risco-alarms.html",
            "brands/ajax-alarms.html",
            "brands/paradox-alarms.html",
            "brands/dsc-alarms.html",
            "brands/ge-caddx-alarms.html",
        ]
    },
    "CCTV & Surveillance": {
        "url": "/resources/library/cctv.html",
        "label": "CCTV",
        "files": [
            "brands/hikvision-cctv.html",
            "brands/milesight-cctv.html",
            "brands/hanwha-cctv.html",
            "brands/uniview-cctv.html",
            "brands/dahua-cctv.html",
        ]
    },
    "Entry & Access Control": {
        "url": "/resources/library/access-control.html",
        "label": "access control",
        "files": [
            "brands/zkteco-entry-access.html",
            "brands/suprema-entry-access.html",
            "brands/hid-entry-access.html",
            "brands/entrypass-entry-access.html",
            "brands/microengine-entry-access.html",
            "brands/hikvision-access.html",
            "brands/akuvox-access.html",
            "brands/apollo-access.html",
        ]
    },
    "Intercom & Video Entry": {
        "url": "/resources/library/intercom.html",
        "label": "intercom",
        "files": [
            "brands/akuvox-intercom.html",
            "brands/hikvision-intercom.html",
            "brands/aiphone-intercom.html",
            "brands/fanvil-intercom.html",
            "brands/kocom-intercom.html",
        ]
    },
    "Vehicle Management": {
        "url": "/resources/library/vehicle.html",
        "label": "vehicle management",
        "files": [
            "brands/gantrygo.html",
            "brands/faac-autogate.html",
            "brands/mag-autogate.html",
            "brands/dormer-autogate.html",
            "brands/ebelco-locks.html",
            "brands/viro-locks.html",
        ]
    },
    "IP Telephony": {
        "url": "/resources/library/ip-telephony.html",
        "label": "IP telephony",
        "files": [
            "brands/yeastar-ippbx.html",
            "brands/fanvil-ip-phone.html",
            "brands/yealink-ip-phone.html",
        ]
    },
    "Network Infrastructure": {
        "url": "/resources/library/network.html",
        "label": "network infrastructure",
        "files": [
            "brands/omada-network.html",
            "brands/ruijie-reyee-network.html",
            "brands/hrui-network.html",
        ]
    },
    "Platform & Management": {
        "url": "/resources/library/platform.html",
        "label": "platform and management",
        "files": [
            "brands/vesta.html",
            "brands/hikcentral.html",
            "brands/zkteco-cvsecurity.html",
        ]
    }
}

strip_template = """<!-- ── Product Library link ── -->
<section class="{section_class}" style="padding: 32px 0;">
  <div class="container">
    <div style="display:flex; align-items:center; gap:20px; flex-wrap:wrap; background:#fff; border:1.5px solid #CBD5E0; border-left:4px solid var(--primary-blue); border-radius:10px; padding:20px 24px;">
      <span style="font-size:24px; flex-shrink:0;">📂</span>
      <div style="flex:1; min-width:200px;">
        <p style="font-family:'Montserrat',sans-serif; font-size:13px; font-weight:700; color:var(--text-dark); margin:0 0 4px;">Looking for datasheets and manuals?</p>
        <p style="font-family:'Inter',sans-serif; font-size:13px; color:var(--text-light); margin:0;">Specifications, installation manuals, and product videos for every {category_label} brand we carry.</p>
      </div>
      <a href="{library_url}" class="btn btn-outline-dark" style="white-space:nowrap; flex-shrink:0;">Browse Product Library →</a>
    </div>
  </div>
</section>
"""

def modify_file(file_path, url, label):
    abs_path = os.path.join(workspace_dir, file_path)
    if not os.path.exists(abs_path):
        print(f"File not found: {abs_path}")
        return
    
    with open(abs_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "<!-- ── Product Library link ── -->" in content:
        print(f"Already added to {file_path}")
        return
        
    main_end_match = re.search(r'</main>', content)
    if not main_end_match:
        print(f"</main> not found in {file_path}")
        return
        
    main_end_idx = main_end_match.start()
    
    # Check what the previous section class is.
    prev_content = content[:main_end_idx]
    last_section_match = list(re.finditer(r'class="[^"]*(sv-section-(?:grey|white))[^"]*"', prev_content))
    
    section_class = "sv-section-grey"
    if last_section_match:
        last_class = last_section_match[-1].group(1)
        if last_class == "sv-section-grey":
            section_class = "sv-section-white"
            
    strip_html = strip_template.format(
        section_class=section_class,
        category_label=label,
        library_url=url
    )
    
    new_content = content[:main_end_idx] + strip_html + content[main_end_idx:]
    
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path} with {section_class}")

for cat_name, cat_data in categories.items():
    for f in cat_data['files']:
        modify_file(f, cat_data['url'], cat_data['label'])
