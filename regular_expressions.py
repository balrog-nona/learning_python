import re

print("NAHRAZOVANI ADRESY")
# priklady z ucebnice - nahrazovani slova ROAD zkratkou RD.
s = "100 NORTH MAIN ROAD"
s = s.replace("ROAD", "RD.")
print(s, 1)

s = "100 NORTH BROAD ROAD"
s = s.replace("ROAD", "RD.")
print(s, 2)

s = "100 NORTH BROAD ROAD"
s = s[:-4] + s[-4:].replace("ROAD", "RD.")  # do -4 ponecha s jak je a replace se uskutecni jen na -4 do konce
print(s, 3)

s = re.sub("ROAD$", "RD.", s)  # $ je konec retezce
print(s, 4)  # funguje

s = "100 BROAD"
s = re.sub("ROAD$", "RD.", s)  # zmenilo to nazev ulice, coz se nechtelo
print(s, 5)

s = "100 BROAD"
s = re.sub("\\bROAD$", "RD.", s)  # \b znamena boundary - musi to byt samostatne slovo
# \\ je 2x, aby se zamezilo interpretaci jako escape character, \ se pouziva pro zapis zvlastnich posloupnosti: \n \t
print(s, 6)
s = re.sub(r'\bROAD$', "RD.", s)  # r znamena raw string a ze ve stringu nebudou zvlastni znaky, proto \ jen jednou
print(s, 7)

s = "100 BROAD ROAD APT. 3"
s = re.sub(r'\bROAD$', "RD.", s)  # zde neni road na konci retezce, cili to nefunguje
print(s, 8)
s = re.sub(r'\bROAD\b', "RD.", s)  # opustena podminka s koncem retezce a zalozena na hranicich slova
print(s, 9)  # vyhleda samostatne slovo ROAD a zmeni ho

print("ANALYZA RIMSKYCH CISLIC")
# hrani s overovanim rimskych cislic
pattern = "^M?M?M?$"  # toto je regularni vyraz
"""
^ zajisti vazbu na zacatek retezce a $ na konec - tj. spolecne znamenaji, ze vzorek musi odpovidat celemu retezci
M? znamena nepovinny vyskyt znaku M, opakuje se 3x tj. odpovida vyskytu 0-3 znaku M za sebou
"""
a = re.search(pattern, "M")
print(a, 1)
"""
fce search() bere regularni vyraz a retezec a zkusi, jestli k soe pasuji. Pokud najde shodu, vrati objekt, ktery nabizi
ruzne metody k popisu vysledku
zde retezec M odpovida regularnimu vyrazu, protoze prvni nepovinny znak sedi a dalsi dva se ignorujou
"""
b = re.search(pattern, "MM")
print(b, 2)  # vyhovuje, bo prvni dva nepovinne znaky sedi a treti se ignoruje
c = re.search(pattern, "MMM")
print(c, 3)  # vsechny tri znaky pasuji
d = re.search(pattern, "MMMM")
print(d, 4)
"""
zde ke shode nedoslo, fce search() vraci None
tri znaky M pasuji, ale pak vyraz trva na tom, ze ma koncit (predepsano znakem $). Tady retezec nekonci, obsahuje jeste
jedno M, takze vraceno None
"""
e = re.search(pattern, "")  # prazdny retezec vyhovuje, bo vsechny znaky M z regularniho vyrazu jsou nepovinne
print(e, 5)

pattern = "^M?M?M?(CM|CD|D?C?C?C?)$"  # pridana kontrola pro stovky
s = re.search(pattern, "MCM")
print(s, 5)
r = re.search(pattern, "MD")
print(r, 6)
d = re.search(pattern, "MMMCCC")
print(d, 7)
w = re.search(pattern, "MCMC")
print(w, 8)
e = re.search(pattern, "")  # shoda protoze:
print(e, 9)  # vsechny M jsou nepovinne a "" odpovida posledni moznosti ze zavorky, kde je D a vsechny C nepovinne

pattern = "^M{0,3}$"  # alternativa zapisu M?M?M?- M zopakovane 0 az 3x
# opet najde shodu s prazdnym retezcem, s M, MM, MMM, ale uz ne s MMMM

pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$"  # prodana kontrola desitek
# najde shodu napr. s MCMXL, MCML, MCMLX, MCMLXXX, ale uz ne treba s MCMLXXXX

pattern = "^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"  # neboli:
pattern = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# oboji zapis najde shodu s jakymkoli platne zadanym rimskym cislem od 1 I do 3888 MMMDCCCLXXXVIII

# viceslovne regularni vyrazy - verbose regular expressions
"""
Bile znaky se ignoruji. Pokud chci predepsat shodu s mezerou, musim pred ni napsat zpetne lomitko.
Komentare se ignoruji - tvar bezneho komentare. Je to komentar uvnitr viceradkoveho retezce ne uvnitr zdrojoveho kodu,
ale funguji stejne.
"""

pattern = """
^                                  # zacatek retezce
M{0,3}                             # tisice - 0 az 3 M
(CM|CD|D?C{0,3})                   # stovky - 900 CM, 400 CD, 0-300 (0 az 3 C),
                                   #    nebo 500-800 (D nasledovane 0 az 3 C)
(XC|XL|L?X{0,3})                   # desitky - 90 XC, 40 XL, 0-30 (0 az 3 X),
                                   #    nebo 50-80 (L nasledovane 0 az 3 X)
(IX|IV|V?I{0,3})                   # jednotky - 9 IX, 4 IV, 0-3 (0 az 3 I),
                                   #    nebo 5-8 (V nasledovane 0 az 3 I)
$                                  # konec retezce                                     
"""

g = re.search(pattern, "M", re.VERBOSE)
print(g, 77)
q = re.search(pattern, "MCMLXXXIX", re.VERBOSE)
print(q, 99)
t = re.search(pattern,"MMMDCCCLXXXVIII", re.VERBOSE)
print(t, 55)
r = re.search(pattern, "M")  # shoda nenalezena, chybi urceni,ze je to viceslovny regularni vyraz
print(r, 100)
"""
u viceslovneh vyrazu je treba pridat jeden argument - re.VERBOSE, protoze jinak python automaticky povazuje vyraz za
kompaktni a vnima vsechny bile znaky. Musi se proto vyslovne stanovit, ze je vicelosvny. 
"""

print("ANALYZA TELEFONNICH CISEL")
phone_Pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phone_Pattern.search("800-555-1212").groups())
"""
metoda groups() vraci tolikaclennou n-tici, kolik skupin bylo v regularnim vyrazu definovano
ke skupinam, ktere se vytvorily behem analyzy, se da prispupovat metodou groups() objektu, ktery vratila metoda search()
"""
# print(phone_Pattern.search("800-555-1212-1234").groups()) nebude fungovat, bo regularni vyraz nemysli na klapku

phone_Pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phone_Pattern.search("800-555-1212-1234").groups())
# print(phone_Pattern.search("800 555 1212 1234").groups()) vyraz nepocita s tim, ze by cisla byly oddelene jinak nez -
# print(phone_Pattern.search("800-555-1212").groups())  vyraz vyzaduje cislo i s klapkou
