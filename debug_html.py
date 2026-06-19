from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

with open("debug_output.txt", "w", encoding="utf-8") as out:
    out.write("--- PRICING ---\n")
    for el in soup.find_all(string=lambda t: "Area & Pricing" in t if t else False):
        parent = el.find_parent("section") or el.find_parent("div")
        if parent:
            out.write(parent.prettify()[:2000])
            break

    out.write("\n--- LOCATION ---\n")
    for el in soup.find_all(string=lambda t: "Location Advantage" in t if t else False):
        parent = el.find_parent("section") or el.find_parent("div")
        if parent:
            out.write(parent.prettify()[:2000])
            break

    out.write("\n--- AMENITIES ---\n")
    for el in soup.find_all(string=lambda t: "Amenities" in t if t else False):
        parent = el.find_parent("section") or el.find_parent("div")
        if parent:
            out.write(parent.prettify()[:2000])
            break

    out.write("\n--- GALLERY ---\n")
    for el in soup.find_all(string=lambda t: "Gallery" in t if t else False):
        parent = el.find_parent("section") or el.find_parent("div")
        if parent:
            out.write(parent.prettify()[:2000])
            break
