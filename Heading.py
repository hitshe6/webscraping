from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://businessdatascience.nl/summer-school/ ')
Heading = BeautifulSoup(html.read(),'html.parser')
print (Heading.p['class'])
