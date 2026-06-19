import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the "Exclusive Tower 3 Launch" status tag
html = html.replace('Exclusive Tower 3 Launch', 'Premium Project Launch')

# Replace the table rows
html = re.sub(
    r'<td class="heading2">Land Parcel</td>\s*<td class="heading1">[^<]+</td>',
    '<td class="heading2">Project Type</td>\n<td class="heading1">&nbsp; Residential-cum-Commercial</td>',
    html
)
html = re.sub(
    r'<td class="heading2">Towers</td>\s*<td class="heading1">[^<]+</td>',
    '<td class="heading2">Elevation</td>\n<td class="heading1">&nbsp; G+19 Storied</td>',
    html
)
html = re.sub(
    r'<td class="heading2">Possession </td>\s*<td class="heading1">[^<]+</td>',
    '<td class="heading2">Plot Details</td>\n<td class="heading1">&nbsp; CIDCO Tender Plot</td>',
    html
)

# Replace the offers
html = html.replace('<li>Avail Limited Period Offer</li>', '<li>Timeless Spanish Architecture</li>')
html = html.replace('<li>Free Stamp Duty Charges</li>', '<li>Aesthetically Designed 3 &amp; 4 BHK</li>')
html = html.replace('<li>Exclusive 25:75 Payment Plan</li>', '<li>3-Tier Security System</li>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
