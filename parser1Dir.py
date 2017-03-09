
import os
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]+'index.html'
fileop= open (url)
soup= BeautifulSoup(fileop,"html.parser")



def funcionRecursiva(dirrel):
    if dirrel.startswith(".."):
        dirajust = dirrel.replace(dirrel[:2],'bower_components')
    else:
        dirajust= sys.argv[1]+dirrel
    fileopen= open (dirajust)
    soup2= BeautifulSoup(fileopen,"html.parser")
    for links in soup2.find_all('link'):
        if(links.get('href'))=='':
            break
        else:
            if not link.get('href').startswith("bower_components"):
                print(links.get('href'))
                auxi = ''
                auxi =  str(link.get('href')) 
                #print 'Auxi= ' + auxi
                #print 'DirAjust= ' + dirajust
                
                funcionRecursiva(auxi)
            else:
                print(links.get('href'))
                funcionRecursiva(dirajust)


print '\n' + 'En la Dir:' + '\n' + '\n' + url  + ' existen los siguientes imports:' +'\n'
for link in soup.find_all('link'):
    print(link.get('href'))
    funcionRecursiva('note-app.html')


