import collections


# creating a dictionary using zip function and two lists
names = ["girl", "boy"]
hobbies = ["fitness", "reading"]
d = dict(zip(names, hobbies))
print(d)


# counting with dictionaries
colors = ["red", "green", "red", "blue", "green", "red"]
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

print(d)


# grouping with dictionaries
names = ["charlie", "will", "stephen", "roxanne", "yoko", "ted", "raymond"]
s = {}
for name in names:  # logicky spravne, ale neidiomaticke + nejpomalejsi
    key = len(name)
    if key not in s:
        s[key] = []
    s[key].append(name)

print(s)

r = {}
for name in names:
    key = len(name)
    r.setdefault(key, []).append(name)  # ne az tak moderni verze + o neco pomalejsi nez defaultdict

print(r)
"""
Setdefault returns a value of a key if the key is in the dictionary. If not, it inserts key with a default value to the 
dictionary.
setdefault method returns: 
- the value of the key, if the key is in dictionary
- None, if key is not in the dictionary and the default value is not specified
- default value if key is not in the dictionary and default value is specified (second parameter)
"""


dict_q = collections.defaultdict(list)  # nejmodernejsi a nejrychlejsi verze
for name in names:
    key = len(name)
    dict_q[key].append(name)

print(dict_q)


"""
Poznamky ruzne:
1. Ve fcich je dobre pro vetsi citelnost psat do argumentu keywords, aby tam nebyly jen nejake hausnumera nebo slova,
ktere budou s postupem casu neprehledne.
2. Vyuzivej moznosti updatovat vice promennych naraz, viz updating multiple state variables - eliminuje to chyby typu
hodnota promenne se zmenila + umoznuje to high level thinking - chunking.
3. pure function - returns the same value every time you call it
4. caching - dela asi neco s funkcema, asi je stabilizije?
"""


# unpacking sequences
k = "bill", "gates", 54, "bill@microsoft.com"
fname, sname, age, email = k  # nepsat 4 liny se 4 promennyma a indexovat k

letters = "abc"
first, second, third = letters

seznam = ["ovoce", "lusteniny", "drogerie"]
polozka1, polozka2, polozka3 = seznam

print(fname, sname, age, email, first, second, third, polozka1, polozka2, polozka3)


# updating multiple state variables
x, y = 0, 1  # fibonacciho posloupnost
for i in range(4):
    print(x)
    x, y = y, x + y
"""
wow, toto prestane fungovat, kdyz je to na dvou radcich! promenne se zde musi menit zaroven! Kdyz se to napise na dva
radky, tak to nefunguje, bo hodnota x se zmeni a je pak brana do vypoctu.
"""

# unpacking a list of strings
v = names[:]
v = ", ".join(v)
print(v, type(v))

# unpacking tuple
for x, y in[(10, 20), (50,60)]:
    print(x, y)  # vysledkem neni tuple, ale jeji obsah!


"""
zajimava knihovna collections - deque kolekce napr.
variable_name = deque(iterable) - provides methods like del, append, pop, but it is much more quick!
besides, there are special methods: popleft(), appendleft()
video pana 39:21 + dokumentace
"""


# factor-out temporary contexts
"""
idiom pro:
try:
    os.remove("somefile.tmp")
except OSError:
    pass
    
je:
with ignored(OSError):
    os.remove("somefile.tmp")
"""

# list comprehensions and generator expressions - tvorba seznamu
print(sum([i ** 2 for i in range(10)]))
# funguje i verze bez [] a je to rychlejsi a nezere tolik pameti tvourbou listu
"""
rozdil se da chapat tak, ze pokud je to rozepsane na hafo radku a postupne apendovane do seznamu, tak to rika spis
JAK se to ma udelat, zatimco ve verzi comprehension to rika, CO to ma udelat.
"""
"""
da se tu pouzit seznam vznikly jakumkoli zpusobem, napr. i vysledek volani glob.glob - to vrati seznam, cili jde provest
[os.path.realpath(f) for f in glob.glob("../*.xml")]
"""
filtrace = [i for i in range(15) if i ** 2 % 5 == 0]  # pri tomto lze i filtorvat podminkou!
print(filtrace)
"""
cela konstrukce muze byt libovolne slozita:
[f for f in glob.glob("*.py") if os.stat(f).st_size > 6000] - na principu se nic nemeni
[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob("*.xml")] - najde vsechno .xml, pak zjisti velikost 
kazdeho z nich a pak k nemu vytvori absolutni cestu. Vrati seznam n-tic.
"""


# dictionary comprehension - misto seznamu popisuje vytvoreni slovniku(pomoci iteratoru)
new_dict = {i:i ** 2 for i in [2, 3, 4, 5]}
print(new_dict)
"""
jinak to lze navazat i na slozitejsi konstrukce, muze to vypadat i totalne hardcore, jako treba v Dive into Python 3,
lekce 3.4: (pri spusteni glob.glob z adresare, kde se nachazeji ty soubory)
metadata_dict = {f:os.stat(f) for f in glob.glob("*test*.py")}  - pred : je klic, pak hodnota

humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) for f, meta in metadata_dict.items()
                                                                                    if meta.st_size > 6000}

vysvetleni k tomuto: metadata_dict je slovnik vytvoreny ze vsech souboru ve slozce, ktere maji v nazvu test
nasledne se vytvoril humansize_dict tak, ze klicem je nazev souboru bez pripony (bo os.path.splitext() vraci tuple,
kde je nazev zvlast a pripona zvlast) a hodnota velikost spocitana podle fce, ktera se v te ucebnici pouziva na vice
mistech. Iteruje se skrz metadata_dict.items(), kde jsou klice nazvy souboru a hodnoty objekty vytvorene pomoci
os.stat(). meta pak odkazuje prave na objekt vytvoreny timto zpusobem a .st_size je metoda na tomto objektu, pomoci
ktere se taky zjistuje, jestli je naplnena podminka velikosti vetsi nez 6000.
"""

uvodni_dict = {"a": 1, "b": 2, "c": 3}
sranda_dict = {value:key for key, value in uvodni_dict.items()}  # obraceni hodnot na klice a naopak
print(sranda_dict)


# set comprehensions - tvorba mnoziny
a_set = set(range(10))
print({x ** 2 for x in a_set})  # zde je vstupem set
print({x for x in a_set if x % 2 == 0})  # opet lze zaroven filtrovat
print({2 ** x for x in range(10)})  # zde je vstupem iterable


# string formatting
slovnik = {"jmeno": "Lucka", "povolani": "drticka odpadu", "zajmy": "kresleni"}
print("{jmeno} pracuje jako {povolani} a ma rada {zajmy}.".format(**slovnik))

seznam = ["Marek", "Matous", "Lukas", "Jan"]
print("{0}, {1}, {2} a {3} si sedli a napsali knizku.".format(*seznam))

surname = ["Novak", "Vokoun", "Jagr", "Novakova", "Vokounova", "Jagrova"]
print("pan {0[2]} + pani {0[5]}".format(surname))  # argumentem je seznam a do neho se da normalne pristupovat

"""
da se formatovat i pomoci slovniku a klicu; modulu a promennych/fci; tridy a vlastnosti/metod; a kombinaci vseho, pr.:
import humansize
import sys
vypis = "1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}".format(sys)
vysvetleni tohoto je v Dive into python v kap 4.4.1.

+
FORMAT SPECIFIER
"{0:.1f} {1}".format(698.24, "GB")
:.1f upresnuje, jak ma byt dosazovana hodnota formatovana. Dovoli pridat vycpavku z 0 nebo mezer, ridit pocet dese-
tinnych mist i konvertovat cisla do jine soustavy (sestnactkove apod.)
: je zacatek specifikatoru a .1 je specifikator - zaokrouhli na nejblizsi desetiny, tj. zobrazi 1 desetinne misto
f znamena cislo s pevnou radovou carkou
tento kod vypise misto 698.24 jen 698.2
"""

# yield/generators
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygenerator = create_generator()  # creates a generator
print(mygenerator)
for i in mygenerator:
    print(i)

"""
Pri volani fce kod z tela fce neprobehne - fce pouze vrati generator object. Ten kod probehne pokazde, kdyz for cyklus
pouzije ten generator object.
Poprve, kdyz for cyklus zavola generator object, probehne kod v tele fce od zacatku, az dokud neprijde k yield a pak 
vrati prvni hodnotu z cyklu. Pak pokazde pri volani fce probehne for cyklus z te fce a vrati dalsi hodnotu, az neni uz
zadna hodnota k vraceni.
Generator je povazovan za prazdny, kdyz uz kod nedosahne na yield - napr. kdyz cyklus dojde ke konci nebo uz se
nenaplnuje podminka.
Fce, ktere maji yield jsou generator functions.
modul itertools - manipulates iterables
"""
