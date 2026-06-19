import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add cache buster ?v=2 to all JPG image paths
html = re.sub(r'(\.JPG)(?![\w=?])', r'\1?v=2', html, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
