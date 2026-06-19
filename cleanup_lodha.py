import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix WhatsApp number
html = html.replace('phone=918369125062', 'phone=919075060900')

# Fix WhatsApp text
html = html.replace('LODHA+BELLEVUE+by+Lodha+Group', 'Estrella+by+Shreeji+Group')
html = html.replace('LODHA BELLEVUE', 'Estrella Kharghar')
html = html.replace('Lodha Group', 'Shreeji Group')
html = html.replace('Lodha-4bhk', 'Estrella-Kharghar')
html = html.replace('Lodha', 'Shreeji')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
