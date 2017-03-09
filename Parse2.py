import os
import sys
import fnmatch
from termcolor import colored
from bs4 import BeautifulSoup


if len(sys.argv) < 2:
    cwd = os.getcwd()
    print colored(' => Error!!', 'red') + " Introducir directorio a analizar como primer argumento"
    print " Se utilizara el directorio actual: "+ colored(cwd, 'yellow', 'on_cyan')
else:
    cwd = sys.argv[1]

#Abrir archivo para borrar el contenido en caso de que no sea la primera ejecucion
open("importsTotales.txt", "w")
pass


for dirpath, dirs, files in os.walk(cwd):
    for filename in fnmatch.filter(files, '*.html'):
        with open(os.path.join(dirpath, filename)) as infile:
            with open("importsTotales.txt", "a") as myfile:
                myfile.write('\n' + 'En la Dir:' + '\n' + '\n' + dirpath
                             + '/'+filename+'\n' +' existen los siguientes imports:' +'\n')
                #print('\n' + 'En la Dir:' + '\n' + '\n' + dirpath
                # +filename+'\n' +' existen los siguientes imports:' +'\n')
                soup = BeautifulSoup(infile, "html.parser")
                for link in soup.find_all('link'):
                    aus = link.get('href')
                    if aus.startswith("../"):
                        if aus.startswith("../../"):
                            dirajust = aus.replace(aus[:6], '')
                        dirajust = aus.replace(aus[:2], '')
                        #print(dirpath + '' + dirajust + '\n')
                        myfile.write(dirpath + '' + dirajust + '\n')
                    else:
                        #print(dirpath + ''+ link.get('href') + '\n')
                        myfile.write(dirpath + ''+ link.get('href') + '\n')

print(colored(' => Archivo creado como file.txt \n','green'))


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


#print '\n' + 'En la Dir:' + '\n' + '\n' +   + ' existen los siguientes imports:' +'\n'
for link in soup.find_all('link'):
    print(link.get('href'))
    #funcionRecursiva('note-app.html')

