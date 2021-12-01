#code to find headers on page

import urllib.request

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://localhost:8080/')
bs = BeautifulSoup(html, "html.parser")
#when searching on the apache web page there is only one header contained in a head tag not h1,h2 etc.
headers = bs.find('title').get_text()
print('List all the header tags :', headers, sep='\n\n')