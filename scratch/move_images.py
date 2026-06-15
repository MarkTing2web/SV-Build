from PIL import Image

paths = [
  (r'C:\Users\Ler Wee Meng\.gemini\antigravity\brain\635f98ec-bdc7-4acd-9b6c-5a970a607d09\cctv_cable_upgrade_1781521830241.png', r'd:\Ler Wee Meng\Project-Web\SV-Build\images\insights\cctv-cable-upgrade-feature.webp'),
  (r'C:\Users\Ler Wee Meng\.gemini\antigravity\brain\635f98ec-bdc7-4acd-9b6c-5a970a607d09\cctv_cable_hybrid_1781521842469.png', r'd:\Ler Wee Meng\Project-Web\SV-Build\images\insights\cctv-cable-upgrade-hybrid.webp'),
  (r'C:\Users\Ler Wee Meng\.gemini\antigravity\brain\635f98ec-bdc7-4acd-9b6c-5a970a607d09\cctv_pdpa_compliance_1781521879726.png', r'd:\Ler Wee Meng\Project-Web\SV-Build\images\insights\cctv-pdpa-compliance-placement.webp'),
  (r'C:\Users\Ler Wee Meng\.gemini\antigravity\brain\635f98ec-bdc7-4acd-9b6c-5a970a607d09\cctv_vs_alarm_1781521892193.png', r'd:\Ler Wee Meng\Project-Web\SV-Build\images\insights\cctv-vs-alarm-feature.webp')
]

for src, dst in paths:
  Image.open(src).save(dst, 'WEBP', quality=85)

print('Images successfully converted and moved!')
