import os

files = [
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open(os.path.join(base_dir, "scratch/tail_files.txt"), "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            out.write(f"### {fpath}\n")
            for line in lines[-15:]:
                out.write(line)
            out.write("\n\n")
        else:
            out.write(f"### {fpath}\nFILE NOT FOUND\n\n")
