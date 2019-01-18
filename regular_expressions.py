import re

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

s = re.sub("ROAD$", "RD.", s)  # $ je konec radku
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
s = re.sub(r'\bROAD$', "RD.", s)  # zde neni road na konci radku, cili to nefunguje
print(s, 8)
s = re.sub(r'\bROAD\b', "RD.", s)  # opustena podminka s koncem radku a zalozena na hranicich slova
print(s, 9)  # vyhleda samostatne slovo ROAD a zmeni ho

# hrani s overovanim rimskych cislic
pattern = "^M?M?M?$"  # toto je regularni vyraz
"""
^ zajisti vazbu na zacatek radku a $ na konec - tj. spolecne znamenaji, ze vzorek musi odpovidat celemu retezci
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
