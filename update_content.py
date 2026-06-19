import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace phone numbers globally
html = html.replace('+91 9606970804', '+91 90750 60900')
html = html.replace('919606970804', '919075060900') # For whatsapp links
html = html.replace('+919606970804', '+919075060900') # For tel links
html = html.replace('9606970804', '9075060900') # Any other naked occurrence

soup = BeautifulSoup(html, 'lxml')

# Task 1: Update overview image
overview_img = soup.select_one('#overview picture img')
if overview_img:
    overview_img['src'] = './asset/grand-lobby.png'
    overview_img['data-srcset'] = './asset/grand-lobby.png'
    overview_img['alt'] = 'Grand Lobby of Estrella Kharghar'

overview_source = soup.select_one('#overview picture source')
if overview_source:
    overview_source['data-srcset'] = './asset/grand-lobby.png'
    overview_source['srcset'] = './asset/grand-lobby.png'
    if 'type' in overview_source.attrs:
        del overview_source['type']

# Task 3: Update highlights image
highlights_img = soup.select_one('#highlights picture img')
if highlights_img:
    highlights_img['src'] = './asset/sunset-view-from-balcony.png'
    highlights_img['data-srcset'] = './asset/sunset-view-from-balcony.png'
    highlights_img['alt'] = 'Sunset View from Balcony - Estrella Kharghar'

highlights_source = soup.select_one('#highlights picture source')
if highlights_source:
    highlights_source['data-srcset'] = './asset/sunset-view-from-balcony.png'
    highlights_source['srcset'] = './asset/sunset-view-from-balcony.png'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
