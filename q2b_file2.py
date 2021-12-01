import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://localhost:8080/')
bs = BeautifulSoup(html, "html.parser")



text = bs.get_text()

#function to count appache lower and uppercase
def count_word(word):
    i = text.count(word.title())
    x = text.count(word)
    print ('total_count_of_words =',i + x)

count_word('apache2')