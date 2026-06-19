import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the top nav brochure link
old_nav_brochure = r'<a class="nav-link" download="SHREEJI_ESTRELLA_BROCHURE\.pdf" href="\./asset/SHREEJI_ESTRELLA_BROCHURE\.pdf" onclick="window\.location\.href=\'\./asset/SHREEJI_ESTRELLA_BROCHURE\.pdf\'; return false;" target="_blank">'
new_nav_brochure = '<a class="nav-link" href="javascript:void(0);" data-brochure-popup="yes" data-bs-target="#enqPopup" data-bs-toggle="modal" data-form-name="Download Brochure - Top" data-formbtn="Submit" data-formtitle="Download Brochure">'
html = re.sub(old_nav_brochure, new_nav_brochure, html)

# 2. Fix privacy policy links to open in a new tab
html = html.replace('<a href="privacy-policy.html" target="_self">', '<a href="privacy-policy.html" target="_blank">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
