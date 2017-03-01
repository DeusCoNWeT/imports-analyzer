import os
import sys
from bs4 import BeautifulSoup
import fnmatch

for dirpath, dirs, files in os.walk(sys.argv[1]):
    for filename in fnmatch.filter(files, '*.html'):
        
        with open(os.path.join(dirpath, filename)) as infile:
            soup= BeautifulSoup(infile,"html.parser")
            
            for link in soup.find_all('link'):
                print '\n' + 'En la Dir:' + '\n' + '\n' + dirpath +'\n' +' existen los siguientes imports:' +'\n'
                print(link.get('href'))
                aus= link.get('href')
                with open("file.txt", "a") as myfile:
                    if aus.startswith(".."):
                        dirajust = aus.replace(aus[:2],'')
                        myfile.write(dirpath + '/' + dirajust + '\n')
                        if aus.startswith("../../"):
                            dirajust = aus.replace(aus[:5],'')    
                    else:
                        myfile.write(dirpath + '/'+ link.get('href') + '\n')
