import os

images_dir = r"C:\Projects\SV-Build\images\insights"

files_to_delete = [
    "10-tips-motion-light.webp",
    "10-tips-visible-camera.webp",
    "access-control-fire-doors-breakglass.webp",
    "access-control-fire-doors-feature.webp",
    "access-control-fire-doors-maglock.webp",
    "after-install-service-visit.webp",
    "ai-hikvision-nvr-analytics.webp",
    "alarm-detectors-pir.webp",
    "alarm-maintain-battery.webp",
    "alarm-maintain-pir-clean.webp",
    "alarm-using-app.webp",
    "alarm-using-keypad.webp",
    "alarm-using-partial-arm.webp",
    "auto-gate-sliding-motor.webp",
    "auto-gate-swing-arm.webp",
    "burglar-alarm-design-feature-sm.webp",
    "burglar-alarm-design-signoff.webp",
    "condo-agm-proposal-document.webp",
    "condo-intercom-aged-system.webp",
    "condo-intercom-ip-doorstation.webp",
    "condo-proposal-existing-system.webp",
    "condo-quotes-contractor-meeting.webp",
    "condo-quotes-site-assessment.webp",
    "condo-timeline-access-cards.webp",
    "home-cost-quote-document.webp",
    "intercom-home-card-reader.webp",
    "intercom-home-mobile-app.webp",
    "ip-cctv-layout-plan.webp",
    "lpr-vs-rfid-vehicle-access-singapore-hero.webp",
    "lpr-vs-rfid-vehicle-access-singapore-mobile.webp",
    "maintenance-contract-report.webp",
    "class-zoning-placeholder.webp", # just in case
    "multi-door-access-credentials.webp",
    "multi-door-access-zoning.webp",
    "pdpa-cctv-singapore-mobile.webp",
    "property-types-condo-lobby.webp",
    "property-types-hdb-door.webp",
    "rackmount-nvr-cable-management.webp",
    "securevision-insights-mobile.webp",
    "security-refresh-site-survey.webp",
    "standalone-access-admin.webp",
    "standalone-access-lock.webp",
    "standalone-access-reader.webp",
    "system-check-alarm-panel.webp",
    "system-check-intercom-test.webp",
    "upgrade-existing-assessment.webp",
    "upgrade-existing-wored-detectors.webp",
    "upgrade-repair-assessment.webp",
    "video-analytics-retail-singapore-hero.webp",
    "video-analytics-retail-singapore-mobile.webp",
    "wifi-gate-keyfob-comparison.webp",
    "wifi-gate-mobile-app.webp"
]

deleted_count = 0
not_found_count = 0

for filename in files_to_delete:
    path = os.path.join(images_dir, filename)
    if os.path.exists(path):
        try:
            os.remove(path)
            deleted_count += 1
            print(f"Deleted: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
    else:
        not_found_count += 1
        print(f"File not found (already deleted?): {filename}")

print()
print(f"Total files deleted: {deleted_count}")
print(f"Files not found:     {not_found_count}")
