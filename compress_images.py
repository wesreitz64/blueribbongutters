import os
from PIL import Image

images_to_compress = [
    'split-level.png',
    'work-4.png',
    'work-3.png',
    'hero-ed.png',
    'downspouts-done-right.png',
    'ed-portrait.png',
    'work-2.jpg'
]

for img_file in images_to_compress:
    if not os.path.exists(img_file):
        print(f"Skipping {img_file}, not found")
        continue

    try:
        with Image.open(img_file) as img:
            # Resize image to a more reasonable max dimension, e.g. 1920x1080 bounding box
            img.thumbnail((1200, 1200))
            if img_file.endswith('.png'):
                img.save(img_file, optimize=True)
            else:
                img.save(img_file, "JPEG", optimize=True, quality=80)
        print(f"Compressed {img_file}")
    except Exception as e:
        print(f"Failed to compress {img_file}: {e}")
