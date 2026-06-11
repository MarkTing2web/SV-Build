import sys
from PIL import Image
import os

def process_image(src, dest, target_size):
    try:
        img = Image.open(src)
        src_w, src_h = img.size
        target_w, target_h = target_size
        
        source_ar = src_w / src_h
        target_ar = target_w / target_h
        
        if source_ar > target_ar:
            # Crop width
            new_w = int(src_h * target_ar)
            left = (src_w - new_w) / 2
            right = left + new_w
            img = img.crop((left, 0, right, src_h))
        elif source_ar < target_ar:
            # Crop height
            new_h = int(src_w / target_ar)
            top = (src_h - new_h) / 2
            bottom = top + new_h
            img = img.crop((0, top, src_w, bottom))
            
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        img.save(dest, "WEBP", quality=85)
        print(f"Saved {dest}")
    except Exception as e:
        print(f"Error processing {src}: {e}")

alarm_panel_images = [
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\alarm_panel_feature_1781171199145.png", 
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-panel-feature.webp", (640, 360)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\alarm_panel_zones_v2_1781171460224.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-panel-zones.webp", (320, 240)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\alarm_panel_wired_wireless_1781171512856.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-panel-wired-wireless.webp", (320, 240)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\alarm_panel_mobile_app_1781171676226.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\alarm-panel-mobile-app.webp", (320, 240))
]

print("Processing alarm panel images...")
for src, dest, size in alarm_panel_images:
    process_image(src, dest, size)

burglar_alarm_images = [
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\burglar_alarm_feature_v2_1781169032414.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\burglar-alarm-detectors-sensors-feature.webp", (640, 360)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\burglar_alarm_door_contact_v5_1781169532807.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\burglar-alarm-detectors-sensors-door-contact.webp", (320, 240)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\burglar_alarm_glass_break_v2_1781169806252.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\burglar-alarm-detectors-sensors-glass-break.webp", (320, 240)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\burglar_alarm_pir_1781169915043.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\burglar-alarm-detectors-sensors-pir.webp", (320, 240)),
    (r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\9b85bbd2-912e-473c-8a9a-c036aacc1e6c\burglar_alarm_photobeam_v2_1781170121097.png",
     r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights\burglar-alarm-detectors-sensors-photobeam.webp", (320, 240))
]

print("Processing burglar alarm images...")
for src, dest, size in burglar_alarm_images:
    process_image(src, dest, size)
