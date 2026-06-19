import os
from PIL import Image
import shutil

src_dir = r'asset\shreeji-actual-photos\photos_cropped'
dst_dir = r'asset\shreeji-actual-photos\photos_final'

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for file in os.listdir(src_dir):
    if file.endswith('.JPG') or file.endswith('.jpg'):
        img_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        
        try:
            with Image.open(img_path) as img:
                # Remove an additional 200 pixels from the bottom to be absolutely safe
                # Note: previously we removed 450 from the original, so this makes it -650 from original
                width, height = img.size
                cropped = img.crop((0, 0, width, height - 200))
                cropped.save(dst_path)
        except Exception as e:
            print(f"Error processing {file}: {e}")
