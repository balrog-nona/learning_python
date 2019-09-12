import os
import glob
import time
import humansize

# kapitola 3 Dive into Python
# prace se soubory a adresari
# generatorove notace

# 1. modul os - zkratka pro operacni system
"""
vzdy ecistuje aktualni pracovni adresar - Python si ho neustale udrzuje v pameti
"""
print(os.getcwd())  # get current working directory
os.chdir('/home/balrog/Documents/Programovani/diveintopython3/examples')  # change directory
print(os.getcwd())  # funguje

# os.path - manipulace se jmeny souboru a adresaru
print(os.path.join('/home/balrog/Documents/Programovani/diveintopython3/examples/', 'humansize.py'))
# sestavi cestu z jedne nebo vice casti - tady jen spojil retezce
print(os.path.join('/home/balrog/Documents/Programovani/diveintopython3/examples', 'humansize.py'))
# Python sam prida spravne lomitko
print(os.path.expanduser('~'))  # cesta k domovskemu adresari uzivatele
print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))
# vytvorilo zcela novou cestu podle zadani! os.path.join() bere libovolne mnozstvi argumentu

print('ODDELOVANI')
pathname = '/home/balrog/Documents/Programovani/diveintopython3/examples/humansize.py'
print(os.path.split(pathname))  # vraci tuple s cestou a jmenem souboru zvlast
dirname, filename = os.path.split(pathname)
print(dirname)
print(filename)
shortname, extension = os.path.splitext(filename)  # vraci nazev souboru a priponu zvlast
print(shortname)
print(extension)

# modul glob - pouziva wildcards
print('GLOB')
print(os.getcwd())
os.chdir('/home/balrog/Documents/Programovani/diveintopython3/')
print(glob.glob('examples/*.xml'))  # vraci seznam s relativni cestou k xml souborum ve slozce examples
os.chdir('examples/')  # lze pouzit i relativni cestu
# pozor! tento prikaz zajistil, ze nasledujici glob.glob fungujou
print(glob.glob('*test*.py'))

# pristup k metadatum
metadata = os.stat('feed.xml')  # vraci objekt obsahujici metadata o souboru
print(metadata.st_mtime)  # cas posledni modifikace ve tvaru poctu sekund od Epochy (1. 1. 1970)
# modul time obsahuje fce pro prevod mezi ruznymi reprezentacemi casu, formatovaci, casove zony...
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)  # braci v bajtech

# absolutni cesta
print(os.getcwd())  # jsem ve slozce examples
print(os.path.realpath('feed.xml'))  # vraci absolutni cestu

# generatorova notace seznamu - list comprehension
print('GENERATOROVA NOTACE SEZNAMU')
a_list = [1, 9, 8, 4]
print([elem * 2 for elem in a_list])
print(a_list)  # je nezmenen
a_list = [elem * 2 for elem in a_list]
# nejdrive se vytvori seznamv pameti a po ukonceni generovani je prirazen do promenne
print(a_list)

# v generatorove notaci lze pouzit jakykoli vyraz
print(glob.glob('*.xml'))
print([os.path.realpath(f) for f in glob.glob('*.xml')])  # tranformace se seznam jmen s plnou cestou
print([f for f in glob.glob('*.py') if os.stat(f).st_size > 6000])  # lze pripojit i podminku

# lze mit i slozite vyrazy
print([(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.xml')])

# generatorova notace slovniku
print('GENERATOROVA NOTACE SLOVNIKU')
metadata = [(f, os.stat(f)) for f in glob.glob('*test*.py')]  # chceme nazev souboru a jeho metadata
print(metadata[0])
metadata_dict = {f: os.stat(f) for f in glob.glob('*test*.py')}
print(type(metadata_dict))
print(list(metadata_dict.keys()))  # klicem jsou jmena souboru
print(metadata_dict['alphameticstest.py'].st_size)

metadata_dict = {f: os.stat(f) for f in glob.glob('*')}  # file a metadata pro vsechny soubory z current working dir
humansize_dict = {os.path.splitext(f)[0]: humansize.approximate_size(meta.st_size)
                  for f, meta in metadata_dict.items() if meta.st_size > 6000}
# nazev souboru bez pripony jako klic, velikost jako hodnota for file a metadata object in items() if velikost > 6000
print(list(humansize_dict.keys()))  # je jich 6 jako vyse
print(humansize_dict['romantest9'])  # vrati hodnotu velikosti zpracovanou fci approximate_size

# zamena klicu a hodnot ve slovniku
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value: key for key, value in a_dict.items()})
# jde to ale delatjen u immutable data types
a_dict = {'a': [1, 2, 3], 'b': 4, 'c': 5}
# print({value:key for key, value in a_dict.items()}) vyvola TypeError unhashable type list

# generatorova notace mnozin
print('GENERATOROVA NOTACE MNOZIN')
a_set = set(range(10))
print(a_set)
print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2 ** x for x in range(10)})  # vstupem muze byt jakakoli posloupnost
