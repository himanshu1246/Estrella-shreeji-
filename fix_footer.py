import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace broken QR code with the new whatsapp QR code
html = re.sub(
    r'<img\s+alt="QR Code.*?class="lazyload"\s+data-src="\./img/qr\.png".*?src="[^"]+".*?>',
    '<img alt="QR Code to Contact Sales Team for ESTRELLA by Shreeji Group" class="lazyload" data-src="./asset/whatsapp_qr.png" height="100" src="./asset/whatsapp_qr.png"/>',
    html,
    flags=re.IGNORECASE | re.DOTALL
)

# Fix old RERA number in the footer
html = html.replace('P51900046567', 'P52000056215')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
