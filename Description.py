from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://businessdatascience.nl/summer-school/ ')
Description = BeautifulSoup(html.read(),'html.parser')

print(Description.p)
