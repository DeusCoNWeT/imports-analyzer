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
        urlacortada = url[1:]
        return urlacortada
    if url.startswith("../../"):
        urlacortada = url[5:]
        return urlacortada
    if url.startswith("../"):
        urlacortada = url[2:]
        return urlacortada
    return  url

def removeDups(inputfile, outputfile):
    count=1
    lines=open(inputfile, 'r').readlines()
    lines_set = set(lines)
    out=open(outputfile, 'w')
    for line in lines_set:
        out.write(str(count)+': '+line)
        count=count+1

def funcionRecursiva(dirrel):
    dirajust = removerPuntoPunto(dirrel)
    fileopen= open (dirajust)
    soup2= BeautifulSoup(fileopen,"html.parser")
    with open("importsTotales.txt", "a") as myfile:
        for link in soup2.find_all(rel="import"):
            myfile.write(dirajust+'\n')
            print('Import number:' + dirajust)
            if(link.get('href'))=='':
                break
            else:
                auxi = str(link.get('href'))
                if(auxi.startswith("./")):
                    #print("Empieza con ./:   "+auxi + '\n')
                    #print("El resultado de removerPuntoPunto es: " + removerPuntoPunto(auxi))
                    auxi=str(Path(dirajust).parent) + removerPuntoPunto(auxi)
                    funcionRecursiva(auxi)
                if(auxi.startswith("../../")):
                    auxi2=str(Path(dirajust).parent.parent.parent)
                    auxi= auxi2 + removerPuntoPunto(auxi)
                    #print("Empieza con ../../:  "+auxi+'\n')
                if auxi.startswith("../"):
                    auxi2=str(Path(dirajust).parent.parent)
                    auxi= auxi2 + removerPuntoPunto(auxi)
                    #print("Empieza con ../:  "+auxi+'\n')
                    funcionRecursiva(auxi)
                elif auxi.startswith("/"):
                    #print("Empieza con /:   "+auxi + '\n')
                    funcionRecursiva(auxi)
                else:
                    #print("Import a tratar:  " + auxi + '\n')
                    auxi =  str(Path(dirajust).parent) + '/' + auxi 
                    funcionRecursiva(auxi)
       
funcionRecursiva('/home/gcarrerat/proyectos/pythonparser/index.html')
removeDups('importsTotales.txt', 'importsCribados.txt')




