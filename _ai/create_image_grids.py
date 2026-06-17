import os
from PIL import Image, ImageDraw, ImageFont

image_root = r"c:\Projects\SV-Build\images"
grid_dir = r"c:\Projects\SV-Build\_ai\grids"
os.makedirs(grid_dir, exist_ok=True)

skip_suffixes = ("-mobile.webp", "-rel.webp")
valid_ext = {".webp", ".jpg", ".jpeg", ".png"}

# Collect all images recursively
all_images = []
for root, dirs, files in os.walk(image_root):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for fname in sorted(files):
        ext = os.path.splitext(fname)[1].lower()
        if ext not in valid_ext:
            continue
        if any(fname.endswith(s) for s in skip_suffixes):
            continue
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, image_root).replace("\\", "/")
        all_images.append((rel_path, fpath))

print(f"Total images found: {len(all_images)}")

# Grid configuration
cell_width = 400
cell_height = 400
cols = 5
rows = 5
grid_size = cols * rows

# Create grids
for grid_idx in range((len(all_images) + grid_size - 1) // grid_size):
    grid_img = Image.new("RGB", (cell_width * cols, cell_height * rows), (240, 240, 240))
    draw = ImageDraw.Draw(grid_img)
    
    # Try to load a default font
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    start_idx = grid_idx * grid_size
    end_idx = min(start_idx + grid_size, len(all_images))
    group = all_images[start_idx:end_idx]
    
    for idx, (rel_path, fpath) in enumerate(group):
        c = idx % cols
        r = idx // cols
        x = c * cell_width
        y = r * cell_height
        
        try:
            with Image.open(fpath) as img:
                # Resize keeping aspect ratio
                img.thumbnail((cell_width - 20, cell_height - 60))
                # Center the image in the cell
                img_x = x + (cell_width - img.width) // 2
                img_y = y + 10 + (cell_height - 60 - img.height) // 2
                
                # Paste
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new("RGB", img.size, (240, 240, 240))
                    background.paste(img, mask=img.split()[-1])
                    grid_img.paste(background, (img_x, img_y))
                else:
                    grid_img.paste(img, (img_x, img_y))
        except Exception as e:
            draw.text((x + 10, y + 100), f"ERROR LOADING", fill=(255, 0, 0), font=font)
            print(f"Error reading {fpath}: {e}")
            
        # Draw filename and index
        short_name = f"{start_idx + idx + 1}: {rel_path}"
        # Split text to fit
        if len(short_name) > 45:
            short_name = short_name[:42] + "..."
        draw.text((x + 10, y + cell_height - 40), short_name, fill=(0, 0, 0), font=font)
        draw.rectangle([x, y, x + cell_width, y + cell_height], outline=(200, 200, 200), width=1)
        
    grid_path = os.path.join(grid_dir, f"grid_{grid_idx + 1}.png")
    grid_img.save(grid_path)
    print(f"Saved grid {grid_idx + 1} to {grid_path}")
