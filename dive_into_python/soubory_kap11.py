import locale
import io
import gzip
import sys

print(locale.getpreferredencoding())

a_file = open('../../../diveintopython3/examples/chinese.txt', encoding='utf-8')  # vraci objekt typu stream
"""
na Linuxu funguje i bez urceni znakoveho kodovani, protoze Linux pouziva utf-8 jako vychozi nastaveni (viz vyse), 
kazdopadne u nekoho jineho v PC by to pak nefungovalo

soubor muze byt i ve virtualnim souborovem systemu; pokud ho OS vidi jako soubor, i Python k nemu ma pristup
jako k souboru
"""

print(a_file.name)  # ve forme relativni cesty
print(a_file.encoding)  # kdyz se encoding neuvede, tak vraci prave defaultni hodnotu z locale.getpreferredcoding()
print(a_file.mode)  # zatim otevreno v read modu

print(a_file.read())
print('podruhe: ', a_file.read())  # cteni za koncem souboru nevyvola vyjimku, ale vrati prazdny retezec

print(a_file.read())  # stale na konci souboru, stale vraci prazdny retezec
a_file.seek(0)  # presun v souboru na urcenou bajtovou pozici
print(a_file.read(16))  # pocet znaku, ktere se maji nacist - zadan parametr size
print(a_file.read(1))  # jeden znak, ale pocita se z aktualni pozice v souboru
print(a_file.read(1))  # totez
print(a_file.tell())  # vraci cislo bajtu, kde v souboru se program nachazi
"""
aktualne vraci 20, protoze cinsky znak potrebuje vice bajtu
metoda read pocita po znacich, ale seek a tell pracuje po bajtech a ne vzdy se 1 znak rovna 1 bajt 
(u AJ ano, ale u cinstiny ne)
"""
a_file.seek(17)
print(a_file.read(1))
print(a_file.tell())  # ten cinsky znak potrebuje 3 bajty

a_file.seek(18)  # presun na 18. bajt
# print(a_file.read(1))
"""
vyvola UnicodeDecodeError - na 18. bajtu totiz neni znak, nejblizsi znak totiz zacina na 17. bajtu a zabira 3 bajty
pokus o cteni znaku od stredu jeho kodovane posloupnosti vedl k teto chybe
"""
a_file.close()  # soubor je zavreny, ale a_file objekt type stream stale existuje
# print(a_file.read()) vyvola ValueError: I/O operation on closed file
# a_file.seek(0) dtto
# print(a_file.tell()) dtto
a_file.close()  # nevyvola vyjimku, ale je to prazdna operace
print(a_file.closed)  # soubor je opravdu zavreny

# operacni kontext
with open('../../../diveintopython3/examples/chinese.txt', encoding='utf-8') as file:
    file.seek(17)
    character = file.read(1)
    print(character)
    # po konci bloku se VZDY automaticky vola file.close(), i kdyby blok skoncil v dusledku neosetrene vyjimky

"""
objekt typu stream je ve with context manager, tzn. objekt se dozvi, ze vstupuje do operacniho kontextu nebo ze z nej
vystupuje - obejkt typu stream se pak sam zavre, ale toto chovani je suocasti objektu stream a ne v prikazu with
"""

# cteni po radcich
line_number = 0
with open('../../../diveintopython3/examples/favorite-people.txt', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        print('{:>4} {}'.format(line_number, line.rstrip()))
        # zarovnani doprava na sirku 4 pozic; rstrip odstrani znaky konce radku

"""
objekt typu stream je taky iteratorem, ktery vraci radek pokazde, kdyz je pozadan
Python zpracovava konce radku automaticky, bez ohledu na to, jaky znak noveho radku je v souboru pouzit - jestli 
carriage return nebo line feed nebo oba dva
"""

# zapisovani do souboru - mode w jako write, mode a jako append
# pokud soubor pri techto rezimech jeste neexistuje, bude vytvoren
"""
with open('test.log', encoding='utf-8', mode='w') as file:  # kdyby soubor existoval, obsah bude prepsan
    file.write('test succeeded')

with open('test.log', encoding='utf-8') as file:
    print(file.read())

with open('test.log', encoding='utf-8', mode='a') as file:  # neznici existujici obsah
    file.write('ang again')

with open('test.log', encoding='utf-8') as file:
    print(file.read())
"""


# binarni soubory
image = open('../../../diveintopython3/examples/beauregard.jpg', mode='rb')  # read a binarni rezim
print(image.mode)  # opet objekt typu stream
print(image.name)
# print(image.encoding) vyvola AttributeError
"""
binarni objekty typu stream nemaji encoding - ctou a zapisuji se retezce, z binarniho souboru se dostane presne to,
co je do nej vlozeno, Python tedy nemusi delat zadnou konverzi
"""
print(image.tell())
data = image.read(3)  # ctou se bajty, ne retezce
# pri otevreni v binarnim rezimu bere metoda read jako argument pocet bajtu a ne pocet znaku
print(data)
print(type(data))
print(image.tell())  # proto nedojde k nesouladu mezi metodou read a tell
image.seek(0)
data = image.read()
print(len(data))

# OBJEKTY TYPU STREAM
"""
v nejjednodussim pripade je to vsechno, co ma metodu read(), ktera ma nepovinny parametr size a vraci retezec
pokud je read() zavolana bez size, mela by ze zdroje precist vsechna zbyvajici data a vratit je jako jednu hodnotu
pokud je read() zavolana se size, precte ze zdroje pozadovane mnozstvi dat a vrati je. pokud je volana znovu,
pokracuje od mista, kde prestala a vraci dalsi cast

nemusi se omezovat na skutecne soubory - zdrojem informaci, ze ktereho se cte, muze byt cokoli: webova stranka,
retezec v pameti, vystup z jineho programu

io.StringIO umozni chovat se k retezci jako k textovemu souboru
io.BytesIO umozni chovat se k poli bajtu jako k binarnimu souboru
"""
a_string = 'PapayaWhip is the new black.'
a_file = io.StringIO(a_string)  # prevod na objekt typu stream
# pomoci io.StringIO() se dosahne toho, aby se string choval v pameti jako soubor
print(a_file.read())  # funguje normalne, precte cely 'soubor'
print(a_file.read())  # vraci prazdny retezec jako normalne
a_file.seek(0)  # metoda seek taky funguje
print(a_file.read(10))  # zadani parametru size, precte 10 znaku
print(a_file.tell())
a_file.seek(18)
print(a_file.read())


# komprimovane soubory
with gzip.open('out.log.gz', mode='wb') as file:  # soubory zabalene gzip by se mely otvirat v rezimu binary
    file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
# dekomprimace v prikazove radce pomoci prikazu gunzip out.log.gz - soubor rozbali jako out.log


# STANDARDNI VSTUP, VYSTUP, CHYBOVY VYSTUP
for i in range(3):
    print('PapayaWhip')

for i in range(3):
    h = sys.stdout.write('is the')  # strout je obejkt typu stream a je definovat v modulu sys

for i in range(3):  # toto nedela, co je v ucebnici
    f = sys.stderr.write('new black')  # do strout a strerr se da pouze zapisovat, ne z nich cist

# print(sys.stdout.read()) vyvola vyjimku not readable

"""
bezne je vystup stdout a stderr smerovan do stejneho mista - bud IDE nebo terminalu 

stdout a stderr jsou objekty typu stream, ale nejsou konstatni - lze do nich priradit jinou hodnotu (jiny objekt typu
stream) a presmerovat je
"""
class RedirectStdoutTo:  # trida je spravcem kontextu - ma metody enter a exit
    def __init__(self, new_out):
        """
        prebira 1 parametr - objekt typu stream, ktery se bude po dobu zivotnosti kontextu pouzivat jako standardni
        vystup
        """
        self.new_out = new_out  # sem bude smerovat stdout

    def __enter__(self):
        """
        enter se vola v okamziku vstupu do kontextu, tj. na zacatku prikazu with
        """
        self.out_old = sys.stdout  # ulozeni hodnoty pro pozdejsi pouziti pri vraceni veci na sve misto
        sys.stdout = self.new_out  # presmerovani standardniho vystupu

    def __exit__(self, *args):  # volane pri opousteni kontextu, tj. na konci prikazu with
        sys.stdout = self.out_old  # obnoveni puvodniho nasmerovani standardniho vystupu

print('A')  # strout smeruje do IDE/terminalu
with open('out.log', mode='w', encoding='utf-8') as file, RedirectStdoutTo(file):  # carkou oddeleny seznam kontextu
    print('B')  # provede zapis do souboru out.log - tam je smerovat strout

"""
seznam kontextu se chova jako vnorene prikazy with - prvni kontext je vnejsi blok, druhy kontext je vnitrni blok;
prvni otvira soubor, druhy presmerovava stdout tak, jak je definovano ve tride RedirectStroutTo

ekvivalentem je tento zapis:
with open('out.log', mode='w', encoding='utf-8') as file:
    with RedirectStroudTo(file):  - tady se neprirazuje kontext prikazu with do nejake promenne
        print('B')

pri ukonceni kontextu Python sdeli obema spravcum kontextu, ze maji udelat to, co pri opousteni kontextu - druhy spravce
zmenil sys.stdout zpet na puvodni hodnotu, prvni spravce pak zavrel soubor
"""

print('C')  # stdout opet funkcne smeruje do IDE/terminalu

# s chybovym vystupem se zachazi uplne stejne, akorat se pouziva sys.stderr