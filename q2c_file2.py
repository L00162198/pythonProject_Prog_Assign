#program to print list content using beautiful soup
import urllib.request
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://localhost:8080/')
bs = BeautifulSoup(html, "html.parser")

html = bs.find("ul")
ulist = bs.find('ul')
items = ulist.find_all("li")
#loop through list and return list text content only
for item in items:
    print(item.get_text())