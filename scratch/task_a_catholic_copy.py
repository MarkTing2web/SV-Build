import shutil
import os

base = r"c:\Projects\SV-Build\images\portfolio"
src_hero = os.path.join(base, "commercial", "catholic-centre-hero.webp")
src_mobile = os.path.join(base, "commercial", "catholic-centre-mobile.webp")
src_rel = os.path.join(base, "commercial", "catholic-centre-rel.webp")

dest_hero = os.path.join(base, "institutions", "catholic-centre-waterloo-hero.webp")
dest_mobile = os.path.join(base, "institutions", "catholic-centre-waterloo-mobile.webp")
dest_rel = os.path.join(base, "institutions", "catholic-centre-waterloo-rel.webp")

shutil.copy(src_hero, dest_hero)
shutil.copy(src_mobile, dest_mobile)
shutil.copy(src_rel, dest_rel)

print(f"Hero exists: {os.path.exists(dest_hero)}")
print(f"Mobile exists: {os.path.exists(dest_mobile)}")
print(f"Rel exists: {os.path.exists(dest_rel)}")
