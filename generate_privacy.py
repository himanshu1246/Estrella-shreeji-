import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header (up to the end of <nav>)
header_match = re.search(r'([\s\S]*?</nav>)', html)
header = header_match.group(1) if header_match else ''

# Extract footer (from <footer> to the end)
footer_match = re.search(r'(<footer[\s\S]*)', html)
footer = footer_match.group(1) if footer_match else ''

# Clean up header to make it suitable for inner page
header = header.replace('html:not(.pg-loaded) #mainSlider{display:block;width:100%;aspect-ratio:768/439;overflow:hidden;}', '')

policy_content = """
<div class="container py-5 mt-5">
    <h1 class="mb-4">Privacy Policy & Terms of Conditions</h1>
    <p>We prioritize your privacy. Our concise Privacy Policy outlines the personal information we collect through our website, including sub-domains and microsites, the purposes of collection we may share it with, and security measures in place. It also informs you about your rights, choices, and how to contact us regarding privacy concerns. We highly recommend reading this Privacy Policy before using services and/or providing personal information.</p>

    <h4 class="mt-4">INTERPRETATIONS AND DEFINITIONS</h4>
    <p>“Data” shall mean personal information, including sensitive personal information and special category personal data about you, which we collect, receive, or otherwise process in connection with your use of our website.</p>
    <p>“User or You” shall mean the natural person who accesses our website.</p>

    <h4 class="mt-4">WEBSITE CONTENT OVERVIEW</h4>
    <p>The contents of this landing page, containing details of properties, property photos, costs, and availability, are provided for informational and illustrative purposes only. This information is subject to change at any time. Users are hereby advised that the actual properties may differ from what is shown in photos and cost on the website and pages, and as such, no claims shall be entertained based on such representations.</p>

    <h4 class="mt-4">TYPES OF DATA COLLECTED</h4>
    <p>While visiting this website, We may ask You to provide Us with certain personally identifiable information that can be used to contact or identify You, including Email address, First name and last name, Phone number, and Address.</p>

    <h4 class="mt-4">RETENTION & DISCLOSURE OF YOUR PERSONAL DATA</h4>
    <p>We shall retain Your Personal Data only for as long as is necessary for the purposes set out in this Privacy Policy. By using the Website and/or by providing information to Us through this Website, the User consents to the collection and use of the information disclosed by the User on the Website in accordance with this Privacy Policy.</p>

    <h4 class="mt-4">COOKIES</h4>
    <p>Cookies are primarily used to enhance your online experience and are not employed to track identifiable visitors' navigational habits. Most internet browsers accept cookies by default, but you can adjust settings or use third-party tools to refuse cookies.</p>

    <h4 class="mt-4">CONTACT US</h4>
    <p>To request to review, update, or delete your personal information or to otherwise reach us, please submit a request by e-mailing us at <a href="mailto:shreejihomes555@gmail.com">shreejihomes555@gmail.com</a>.</p>
</div>
"""

new_html = header + policy_content + footer

# Update links inside the new privacy policy page
new_html = new_html.replace('href="#', 'href="index.html#')
new_html = new_html.replace('privacy-policy.php', 'privacy-policy.html')

with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Update index.html to point to privacy-policy.html
html = html.replace('privacy-policy.php', 'privacy-policy.html')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
