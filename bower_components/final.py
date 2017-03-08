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


