import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Gallery Blur & Lock
# We want to wrap the entire slider with a blur class and an overlay button.
# Let's find the gallery slider container.
old_gallery = '<div class="slider-container">'
new_gallery = '''
<div class="slider-container position-relative">
    <div class="bd-img blur" style="cursor: pointer;" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Gallery" data-formbtn="Submit" data-formtitle="View Gallery">
        <span class="cta-text" style="z-index: 10;">View Project Gallery</span>
'''
html = html.replace(old_gallery, new_gallery)

# Close the new div at the end of the slider container.
# The slider container ends with:
# <div class="glide__arrows" data-glide-el="controls">
# <button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>
# <button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>
# </div>
# </div>
# </div>
old_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>'
new_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>\n</div>'
html = html.replace(old_end, new_end)

# Also, update folder from photos_cropped to photos_final to completely bust cache
html = html.replace('photos_cropped', 'photos_final')

# Just in case, let's remove any "Artistic Impression" text completely from the HTML.
html = re.sub(r'<span class="artistic-impression">.*?</span>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
