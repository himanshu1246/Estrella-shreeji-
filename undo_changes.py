import re
import shutil

# 1. Revert index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Revert photos_final to photos_cropped
html = html.replace('photos_final', 'photos_cropped')

# Revert Gallery Blur
old_blur = '''
<div class="slider-container position-relative">
    <div class="bd-img blur" style="cursor: pointer;" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Gallery" data-formbtn="Submit" data-formtitle="View Gallery">
        <span class="cta-text" style="z-index: 10;">View Project Gallery</span>
'''
new_unblur = '<div class="slider-container">'
html = html.replace(old_blur, new_unblur)

# Revert the closing div
old_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>\n</div>'
new_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>'
html = html.replace(old_end, new_end)

# Revert Spelling
html = html.replace('Terms and Conditions', 'Terms of Conditions')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Revert privacy-policy.html
with open('privacy-policy.html', 'r', encoding='utf-8') as f:
    pp_html = f.read()
pp_html = pp_html.replace('Terms and Conditions', 'Terms of Conditions')
with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(pp_html)

# 3. We can optionally delete the photos_final directory since it's no longer used
import os
dst_dir = r'asset\shreeji-actual-photos\photos_final'
if os.path.exists(dst_dir):
    shutil.rmtree(dst_dir)
