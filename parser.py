import os
import sys
from bs4 import BeautifulSoup

url = os.getcwd()+'index.html'
#fileop= open (url)
#soup= BeautifulSoup(fileop,"html.parser")
soup=BeautifulSoup(open("index.html"))
for link in soup.find_all(rel="import"):
    print(link.get('href'))

