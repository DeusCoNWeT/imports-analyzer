import os
import sys
import fnmatch
from pathlib import Path

from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    cwd = os.path.dirname(os.path.abspath(__file__)) + '/index.html'
    print  ("Error!! Introducir directorio a analizar como primer argumento")
    print (" Se utilizara el directorio actual: " + cwd + "\n\n")
else:
    cwd = sys.argv[1]


def removerPuntoPunto(url):
    if url.startswith("./"):
        urlacortada = url.replace(url[:1], "")
        return urlacortada
    if url.startswith("../"):
        urlacortada = url.replace(url[:2], "")
        return urlacortada
    else:
        if url.startswith("../../"):
            urlacortada = url.replace(url[:6], "")
            return urlacortada
    return  url



def funcionRecursiva(dirrel):
    dirajust = removerPuntoPunto(dirrel)
    fileopen= open (dirajust)
    soup2= BeautifulSoup(fileopen,"html.parser")
    print('PADRE:'+dirajust)
    for link in soup2.find_all('link'):
        
        if(link.get('href'))=='':
            break
        else:
           auxi = str(link.get('href'))
           if auxi.startswith("../"):
               auxi2=str(Path(dirajust).parent.parent)
               auxi= auxi2 + removerPuntoPunto(auxi)
               funcionRecursiva(auxi)
           elif auxi.startswith("/"):
                funcionRecursiva(auxi)
           else:
               print("AUXI VALE:" + auxi + '\n')
               auxi =  str(Path(dirajust).parent) + '/' + auxi 
               funcionRecursiva(auxi)
       
           






funcionRecursiva('/home/gcarrerat/proyectos/pythonparser/note-app.html')




