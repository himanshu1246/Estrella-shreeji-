import re

# 1. Undo index.html changes
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove CSS override
css_override = '''
<style>
/* Override Artistic Impression text from S3 style.css */
.gallery-img::after,
.gslide-media.gslide-image::after {
    content: "Actual Image" !important;
}
</style>
'''
html = html.replace(css_override, '')

# Revert Gallery Blur
old_blur = '''
<div class="slider-container position-relative">
    <div class="bd-img blur" style="cursor: pointer;" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="View Gallery" data-formbtn="Submit" data-formtitle="View Gallery">
        <span class="cta-text" style="z-index: 10;">View Project Gallery</span>
'''
new_unblur = '<div class="slider-container">'
html = html.replace(old_blur, new_unblur)

# Revert the closing div for gallery blur
old_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>\n</div>'
new_end = '<div class="glide__arrows" data-glide-el="controls">\n<button class="glide__arrow glide__arrow--left" data-glide-dir="&lt;"><i class="ri-arrow-left-s-line"></i></button>\n<button class="glide__arrow glide__arrow--right" data-glide-dir="&gt;"><i class="ri-arrow-right-s-line"></i></button>\n</div>\n</div>\n</div>'
html = html.replace(old_end, new_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Undo thank-you.html changes
with open('thank-you.html', 'r', encoding='utf-8') as f:
    thtml = f.read()

dl_script = '''
<script>
window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const formName = urlParams.get('form_name');
    if (formName && formName.toLowerCase().includes('brochure')) {
        const a = document.createElement('a');
        a.href = './asset/SHREEJI_ESTRELLA_BROCHURE.pdf';
        a.download = 'SHREEJI_ESTRELLA_BROCHURE.pdf';
        document.body.appendChild(a);
        a.click();
    }
}
</script>
'''
thtml = thtml.replace(dl_script, '')

with open('thank-you.html', 'w', encoding='utf-8') as f:
    f.write(thtml)
