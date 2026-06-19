import re

# 1. Update index.html for Actual Image
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS override to the head
css_override = '''
<style>
/* Override Artistic Impression text from S3 style.css */
.gallery-img::after,
.gslide-media.gslide-image::after {
    content: "Actual Image" !important;
}
</style>
'''
if '/* Override Artistic Impression text from S3 style.css */' not in html:
    html = html.replace('</head>', css_override + '</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update thank-you.html to auto-download brochure if form_name has "brochure"
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
if "urlParams.get('form_name')" not in thtml:
    thtml = thtml.replace('</body>', dl_script + '</body>')

with open('thank-you.html', 'w', encoding='utf-8') as f:
    f.write(thtml)
