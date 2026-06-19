from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html", encoding="utf-8"), "lxml")
with open("dump_gallery2.txt", "w", encoding="utf-8") as f:
    f.write(soup.select_one('#gallery').prettify() if soup.select_one('#gallery') else "none")
