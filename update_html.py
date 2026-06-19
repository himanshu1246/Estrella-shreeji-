from bs4 import BeautifulSoup
import re
import os
import glob

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Global text replacements
replacements = {
    "LODHA BELLEVUE": "ESTRELLA by Shreeji Group",
    "Lodha Bellevue": "Estrella",
    "Lodha Group": "Shreeji Group",
    "Mahalaxmi, Mumbai": "Kharghar City, Navi Mumbai",
    "Mahalaxmi": "Kharghar",
    "RERA : P51900046567": "Maha RERA No.: P52000056215",
    "Upcoming Mahalaxmi Metro : 3 mins": "🚇 Kharghar Village Metro Station : 2 Mins Walk (300 meters)",
    "Mahalaxmi Race Course : 10 mins": "🛤️ Kharghar Railway Station : 5 Mins Drive",
    "Palladium & High Street Phoenix : 15 mins": "🛣️ Sion-Panvel / Pune Highway : 3 Mins Drive",
    "Haji Ali : 15 mins": "✈️ Navi Mumbai Intl. Airport : 15 Mins Drive",
    "Bandra-Worli Sea Link : 20 mins": "⛳ Valley Golf Course & Central Park : 5-7 Mins Drive",
    "Domestic & International Airports : 35 mins": "🏫 Ryan Intl. & NIFT Educational Hub : 3-5 Mins Drive"
}
for k, v in replacements.items():
    html = html.replace(k, v)

# Use BeautifulSoup for structural changes
soup = BeautifulSoup(html, "lxml")

# 2. Update Logo
# Find img with class containing 'logo'
for img in soup.find_all('img'):
    classes = img.get('class', [])
    if any('logo' in c.lower() for c in classes):
        img['src'] = "./asset/Shreeji Group Logo.jpeg"
        if img.has_attr('data-src'): img['data-src'] = "./asset/Shreeji Group Logo.jpeg"
        if img.has_attr('data-srcset'): img['data-srcset'] = "./asset/Shreeji Group Logo.jpeg"

# 3. Update Hero Image
for img in soup.select('.banner img, #mainSlider img'):
    img['src'] = "./asset/building photo.png"
    if img.has_attr('data-src'): img['data-src'] = "./asset/building photo.png"
    if img.has_attr('data-srcset'): img['data-srcset'] = "./asset/building photo.png"
for source in soup.select('.banner source, #mainSlider source'):
    if source.has_attr('data-srcset'): source['data-srcset'] = "./asset/building photo.png"
    if source.has_attr('srcset'): source['srcset'] = "./asset/building photo.png"

# Update Location Map (iframe and map image)
for iframe in soup.select('#location iframe'):
    iframe['src'] = "https://share.google/bCbI2L8dcmdszGseg"
    if iframe.has_attr('data-src'): iframe['data-src'] = "https://share.google/bCbI2L8dcmdszGseg"
for img in soup.select('#location img'):
    img['src'] = "https://share.google/bCbI2L8dcmdszGseg" # We map it or just use the location image
    if img.has_attr('data-src'): img['data-src'] = "./asset/location.png"
    if img.has_attr('data-srcset'): img['data-srcset'] = "./asset/location.png"
for source in soup.select('#location source'):
    if source.has_attr('data-srcset'): source['data-srcset'] = "./asset/location.png"
    if source.has_attr('srcset'): source['srcset'] = "./asset/location.png"

# Update About Info Tagline
for h2 in soup.find_all(["h2", "h3"]):
    if "About Estrella" in h2.text:
        parent = h2.find_parent("div")
        if parent:
            new_p = soup.new_tag("p")
            new_p.string = "REDEFINING DESIGN IN NAVI MUMBAI, INSPIRED BY TIMELESS SPANISH ARCHITECTURE. Project Highlights: CIDCO tender plot, G+19 storied, 3 & 4 BHK flats, Earthquake-resistant RCC structure."
            # Append before the last text paragraph to look nice
            parent.insert(len(parent.contents), new_p)

# 4. Update Area & Pricing
price_slider = soup.select_one('#price-slider .glide__slides')
if price_slider:
    slides = price_slider.find_all('li', recursive=False)
    if len(slides) > 0:
        for s in slides[3:]:
            s.decompose()
        slides = price_slider.find_all('li', recursive=False)
        data = [
            {"title": "3 BHK", "price": "₹3.35 Cr*"},
            {"title": "4 BHK", "price": "OFFER PRICE"},
            {"title": "4.5 BHK", "price": "OFFER PRICE"},
        ]
        for i, slide in enumerate(slides):
            if i < len(data):
                h4 = slide.find('h4')
                h5 = slide.find('h5')
                h6 = slide.find('h6')
                if h4: h4.string = data[i]["title"]
                if h5: h5.string = "" # Remove area
                if h6: h6.string = data[i]["price"]

# 5. Amenities
amenity_images = [
    "./asset/aminities/Gym.png",
    "./asset/aminities/Yoga.png",
    "./asset/aminities/banqute hall.png",
    "./asset/aminities/children playzone.png",
    "./asset/aminities/garden.png",
    "./asset/aminities/indoor games.jpeg",
    "./asset/aminities/mini theatre.png",
    "./asset/aminities/swimming pool.png"
]
amenity_section = soup.select_one('#amenities')
if amenity_section:
    images = amenity_section.find_all('img')
    for i, img in enumerate(images):
        idx = i % len(amenity_images)
        img['src'] = amenity_images[idx]
        if img.has_attr('data-src'): img['data-src'] = amenity_images[idx]
        if img.has_attr('data-srcset'): img['data-srcset'] = amenity_images[idx]
    sources = amenity_section.find_all('source')
    for i, source in enumerate(sources):
        idx = i % len(amenity_images)
        if source.has_attr('data-srcset'): source['data-srcset'] = amenity_images[idx]
        if source.has_attr('srcset'): source['srcset'] = amenity_images[idx]

# 6. Floor Plans
floor_plan_images = ["./asset/floor plan/floor-plan-1.png", "./asset/floor plan/floor-plan.png"]
fp_section = soup.select_one('#sitefloorplan')
if fp_section:
    images = fp_section.find_all('img')
    for i, img in enumerate(images):
        idx = i % len(floor_plan_images)
        img['src'] = floor_plan_images[idx]
        if img.has_attr('data-src'): img['data-src'] = floor_plan_images[idx]
        if img.has_attr('data-srcset'): img['data-srcset'] = floor_plan_images[idx]
    sources = fp_section.find_all('source')
    for i, source in enumerate(sources):
        idx = i % len(floor_plan_images)
        if source.has_attr('data-srcset'): source['data-srcset'] = floor_plan_images[idx]
        if source.has_attr('srcset'): source['srcset'] = floor_plan_images[idx]

# 7. Gallery
gallery_files = glob.glob("asset/shreeji-actual-photos/photos/*")
gallery_images = ["./" + p.replace('\\', '/') for p in gallery_files]
gallery_section = soup.select_one('#gallery')
if gallery_section and gallery_images:
    images = gallery_section.find_all('img')
    for i, img in enumerate(images):
        idx = i % len(gallery_images)
        img['src'] = gallery_images[idx]
        if img.has_attr('data-src'): img['data-src'] = gallery_images[idx]
        if img.has_attr('data-srcset'): img['data-srcset'] = gallery_images[idx]
    anchors = gallery_section.find_all('a', class_='glightbox')
    for i, a in enumerate(anchors):
        idx = i % len(gallery_images)
        a['href'] = gallery_images[idx]

# 8. Brochure
for a in soup.find_all('a'):
    href = a.get('href', '')
    text = a.text.lower()
    if ('brochure' in href.lower() or 'brochure' in text or 'download' in text) and not href.startswith('#'):
        a['href'] = "./asset/SHREEJI ESTRELLA BROCHURE.pdf"
        a['target'] = "_blank"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
