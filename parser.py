import os
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]+'index.html'
#fileop= open (url)
#soup= BeautifulSoup(fileop,"html.parser")






def funcionSort(dirrel):
    dirajust = ''
    if dirrel.startswith(".."):
        dirajust = dirrel.replace(dirrel[:2],'bower_components')
    else:
        dirajust = ''
    url2 = dirrel+dirajust
    file = open(url2)
    soup= BeautifulSoup(file,"html.parser")

    print '\n' + 'En la Dir:' + '\n' + '\n' + url2  + ' existen los siguientes imports:' +'\n'
    for link in soup.find_all('link'):
        print(link.get('href'))
        if(link.get('href'))=='':
            break
        else:
            funcionSort(link.get('href')) 
    return

funcionSort(url)

#print soup.prettify()


#for link in soup.find_all('link'):
#    if link.get('test') == "":
#        print 'Funcion vacia'
#    print(link.get('href'))

print '__________________________________________________________' + '\n'


