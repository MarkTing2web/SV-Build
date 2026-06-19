from PIL import Image

img_path = r"C:\Users\Ler Wee Meng\.gemini\antigravity\brain\797eb192-249a-4a9f-8875-9042f23c9a60\aged_care_hero_base_1781846498473.png"

img = Image.open(img_path)

w, h = img.size
desktop_h = int(w * 9 / 16)
top = (h - desktop_h) // 2
desktop_crop = img.crop((0, top, w, top + desktop_h))
desktop_resized = desktop_crop.resize((1920, 1080), Image.Resampling.LANCZOS)
desktop_resized.save("images/solutions/hero-solutions/solution-healthcare-aged-care-hero.webp", format="WEBP")

mobile_w = int(h * 9 / 16)
left = (w - mobile_w) // 2
mobile_crop = img.crop((left, 0, left + mobile_w, h))
mobile_resized = mobile_crop.resize((1080, 1920), Image.Resampling.LANCZOS)
mobile_resized.save("images/solutions/hero-solutions/solution-healthcare-aged-care-hero-mobile.webp", format="WEBP")

print("Images resized and saved.")
