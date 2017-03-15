# Guillermo Carrera Trasobares 2017
import os, sys, fnmatch, argparse
from pathlib import Path
from bs4 import BeautifulSoup

parser= argparse.ArgumentParser()
parser.add_argument('-u','--url',help="" )
parser.parse_args()
if



if len(sys.argv) < 2:
    cwd = os.getcwd() + '/index.html'
    print  ("Error!! Introducir directorio a analizar como primer argumento")
    print (" Se utilizara el directorio actual: " + cwd + "\n\n")
else:
    cwd = sys.argv[1]


def removeDups(inputfile, outputfile):
    count=1
    lines=open(inputfile, 'r').readlines()
    lines_set = set(lines)
    out=open(outputfile, 'w')
    for line in lines_set:
        out.write(str(count)+': '+line)
        count=count+1

def listAllFiles(dirrel):
    count=1
    for subdir, dirs, files in os.walk(dirrel):
        for file in files:
            print(str(count) + ': '+ os.path.join(subdir, file))
            count=count+1

def listAllImports(dirrel):
    return


def funcionRecursiva(dirrel):
    dirajust = dirrel
    fileopen = open(dirajust)
    soup2 = BeautifulSoup(fileopen, "html.parser")
    with open("importsTotales.txt", "a") as myfile:
        for link in soup2.find_all(rel="import"):
            #print('Import number:' + dirajust)
            if link.get('href') == '':
                break
            else:
                auxi = str(link.get('href'))
                if auxi.startswith("./"):
                    #print("Empieza con ./:   "+auxi + '\n')
                    #print("El resultado de removerPuntoPunto es: " + removerPuntoPunto(auxi))
                    auxi = str(Path(dirajust).parent) + auxi[1:]
                    myfile.write(auxi+'\n')
                    funcionRecursiva(auxi)
                if auxi.startswith("../../"):
                    auxi2 = str(Path(dirajust).parent.parent.parent)
                    auxi = auxi2 + auxi[5:]
                    #print("Empieza con ../../:  "+auxi+'\n')
                    myfile.write(auxi+'\n')
                    funcionRecursiva(auxi)
                if auxi.startswith("../"):
                    auxi2 = str(Path(dirajust).parent.parent)
                    auxi = auxi2 + auxi[2:]
                    #print("Empieza con ../:  "+auxi+'\n')
                    myfile.write(auxi+'\n')
                    funcionRecursiva(auxi)
                elif auxi.startswith("/"):
                    #print("Empieza con /:   "+auxi + '\n')
                    funcionRecursiva(auxi)
                else:
                    #print("Import a tratar:  " + auxi + '\n')
                    auxi = str(Path(dirajust).parent) + '/' + auxi
                    myfile.write(auxi+'\n')
                    funcionRecursiva(auxi)

funcionRecursiva('/home/gcarrerat/proyectos/TestPolymer/index.html')
#listAllFiles('/home/gcarrerat/proyectos/pythonparser/')
removeDups('importsTotales.txt', 'importsCribados.txt')




