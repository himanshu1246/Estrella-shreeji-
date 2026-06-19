from bs4 import BeautifulSoup
import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

# Task 1: Update "Artistic Impression" to "Actual Image" in Gallery
gallery_section = soup.select_one('#gallery')
if gallery_section:
    for span in gallery_section.find_all('span', string=re.compile(r'Artistic Impression', re.IGNORECASE)):
        span.string = span.string.replace("Artistic Impression", "Actual Image")

# Task 2: Change Banner Brochure button to trigger popup
# The banner usually is #home or similar. Let's find any a tag that says Brochure or Download Brochure and doesn't look like navbar
for a in soup.find_all('a'):
    text = a.get_text().lower()
    if 'brochure' in text and not 'nav-link' in a.get('class', []):
        # This is likely the banner or about section brochure button
        # Let's revert it to trigger the popup
        if a.has_attr('download'):
            del a['download']
        if a.has_attr('onclick'):
            del a['onclick']
        a['href'] = "#"
        a['data-bs-toggle'] = "modal"
        a['data-bs-target'] = "#enqPopup"
        # Restore form triggers if they were deleted
        a['data-form-name'] = "Download Brochure"

# Task 3: Lock Gallery Images
if gallery_section:
    for a in gallery_section.find_all('a', class_='glightbox'):
        # Remove glightbox so it doesn't open
        classes = a.get('class', [])
        if 'glightbox' in classes:
            classes.remove('glightbox')
            classes.append('locked-gallery')
            a['class'] = classes
            
            # Save the original href and remove it so it doesn't navigate
            orig_href = a.get('href', '')
            a['data-original-href'] = orig_href
            a['href'] = "javascript:void(0);"
            
            # Make it open the enquire popup
            a['data-bs-toggle'] = "modal"
            a['data-bs-target'] = "#enqPopup"

# Task 4 & 5: About Section Content & Button
about_heading = soup.find(string=lambda t: t and "About Estrella" in t)
if about_heading:
    col_div = about_heading.find_parent("div")
    if col_div:
        # Create the new paragraph
        p = soup.new_tag("p")
        p.string = "Estrella by Shreeji Group is an upcoming uptown address in Navi Mumbai, located in the beautifully-built node of Kharghar. Expanding its space to nature and its wonders, Estrella offers the best of both worlds where golf meets tranquility. Inspired by timeless Spanish architecture, Estrella redefines design and offers a luxurious lifestyle. Step into royalty and live in luxury with spacious balconies, grand reception lounges, and world-class amenities."
        p['class'] = 'mt-3 mb-4' # Add some spacing
        
        # Insert it after the heading (or after the horizontal line if there is one)
        h_tag = about_heading.find_parent(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if h_tag:
            # Let's find the brochure button that was "beside the heading"
            brochure_btn = None
            # Sometimes it's a sibling or in a wrapper next to it.
            # Actually, the user says "right now it is beside the heading".
            # We will find the closest button/a tag containing 'Brochure' within the same parent row/div and move it.
            parent_row = h_tag.find_parent('.row') or h_tag.find_parent('div')
            for a in parent_row.find_all('a'):
                if 'brochure' in a.get_text().lower():
                    brochure_btn = a.extract() # Remove it from its current place
                    break
            
            h_tag.insert_after(p)
            
            if brochure_btn:
                # Wrap it in a div if needed and put it after the paragraph
                btn_wrapper = soup.new_tag("div")
                btn_wrapper['class'] = 'mt-3'
                btn_wrapper.append(brochure_btn)
                p.insert_after(btn_wrapper)

# Task 6: Add RERA info to footer/RERA section
# Look for MahaRERA or similar text
rera_found = False
for p in soup.find_all(['p', 'span', 'div']):
    if p.string and ('maharera' in p.string.lower() or 'rera' in p.string.lower()):
        # Let's just append the new RERA text
        if 'P52000056215' not in p.text:
            p.append(soup.new_string(" | Maha RERA No.: P52000056215 | Site / Office Address: Estrella, Plot No. 109, Sector - 11, Kharghar, Navi Mumbai - 410 210."))
            rera_found = True
            break

if not rera_found:
    # Append to footer
    footer = soup.find('footer')
    if footer:
        rera_p = soup.new_tag("p")
        rera_p['class'] = 'text-center text-white mt-3'
        rera_p.string = "Maha RERA No.: P52000056215 | Site / Office Address: Estrella, Plot No. 109, Sector - 11, Kharghar, Navi Mumbai - 410 210."
        footer.append(rera_p)

# Add unlocking script
script_tag = soup.new_tag("script")
script_tag.string = """
document.addEventListener('DOMContentLoaded', function() {
    // Attempt to hook into any form submissions
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            setTimeout(function() {
                var locked = document.querySelectorAll('.locked-gallery');
                locked.forEach(function(a) {
                    a.classList.remove('locked-gallery');
                    a.classList.add('glightbox');
                    a.removeAttribute('data-bs-toggle');
                    a.removeAttribute('data-bs-target');
                    a.setAttribute('href', a.getAttribute('data-original-href'));
                });
                if (typeof GLightbox !== 'undefined') {
                    GLightbox({ selector: '.glightbox' });
                }
            }, 1500); // 1.5 second delay assuming success
        });
    });
});
"""
if soup.body:
    soup.body.append(script_tag)


with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Execution complete!")
