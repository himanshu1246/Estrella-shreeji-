import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update image paths to point to the newly renamed directory
html = html.replace('asset/shreeji-actual-photos/photos', 'asset/shreeji-actual-photos/photos_cropped')

# Also remove the broken CSS hack properly
html = re.sub(r'<style>\s*/\*\s*Hide Artistic Impression watermark\s*\*/.*?</style>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
