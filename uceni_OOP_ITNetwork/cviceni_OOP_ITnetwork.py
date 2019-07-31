from random import choice
from math import sqrt
from math import degrees, radians

# pri druhem prochazeni tutorialu

# LEKCE 3 - CVICENI
# jednoduchy priklad: clovek a unava
class Clovek:

    def __init__(self, jmeno, unava=0):
        self.jmeno = jmeno
        self.unava = unava

    def __str__(self):
        return "{} ({})".format(self.jmeno, self.unava)

    def beh(self, kms):
        if self.unava >= 20:
            print("Jsem prilis vycerpany.")
        else:
            print("Bezim {} km.".format(kms))
            self.unava += kms

    def spani(self, hod):
        self.unava -= hod * 10
        if self.unava < 0:
            self.unava = 0

karel = Clovek(jmeno="Karel Novy")
print(karel)
karel.beh(10)
karel.beh(10)
karel.beh(10)
karel.spani(1)
print(karel.unava)
karel.beh(10)
print(karel.unava)

# stredne pokrocily priklad: generator nahodnych vet
class Generator:

    def tvorba_slova(self):
        self.jaky = choice(["maly", "opily", "vzdelany", "umanuty", "drzy"])
        self.kdo = choice(["workoholik", "sobec", "kontroverzni podnikatel", "ridic", "serif"])
        self.co = choice(["nakupoval", "prednasel", "exhiboval", "tancil", "vyjednaval"])
        self.jak = choice(["vytrvale", "s nadsenim", "znudene", "sarkasticky", "pitome"])
        self.kde = choice(["u primatora", "v pivovaru", "u nehtarky", "u kartarky", "v zachode"])

    def vypis_vetu(self):
        return "{} {} {} {} {}".format(self.jaky, self.kdo, self.co, self.jak, self.kde)


veta = Generator()
for i in range(10):
    veta.tvorba_slova()
    print(veta.vypis_vetu())

# pokrocily priklad: auto a garaz
class Auto:

    def __init__(self, SPZ, barva):
        self.spz = SPZ
        self.barva = barva

    def __str__(self):
        return "{}".format(self.spz)

    def zaparkuj(self):
        return "V garazi je auto {}.".format(self)

jaguar = Auto(SPZ="123ABC", barva="cerna")
print(jaguar.zaparkuj())

# reseni dle stahnuteho materialu
class Auto:

    def __init__(self, spz, barva):
        self.spz = spz
        self.barva = barva

    def vrat_spz(self):
        return self.spz

    def zaparkuj(self, garaz):  # tady se navazal jiny objekt
        garaz.vloz(self)


class Garaz:

    def vloz(self, auto):
        self.auto = auto  # tady se navazal jiny objekt

    def __str__(self):
        return "V garazi je auto {}.".format(self.auto.vrat_spz())

garaz = Garaz()
corvetta = Auto(spz="567HJK", barva="cervena")
corvetta.zaparkuj(garaz)
print(garaz)

# LEKCE 4 - CVICENI
# jednoduchy priklad: pes a osoba
class Pes:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def zestarni(self):
        self.vek += 1


class Osoba:

    def __init__(self, jmeno, pes):
        self.jmeno = jmeno
        self.pes = pes

pejsek = Pes(jmeno="Azor", vek=1)
print("{} ({} let)".format(pejsek.jmeno, pejsek.vek))
karel = Osoba(jmeno="Karel", pes=pejsek)
lenka = Osoba(jmeno="Lenka", pes=pejsek)
karel.pes.zestarni()
lenka.pes.zestarni()
print("{} ({} let)".format(lenka.pes.jmeno, lenka.pes.vek))


# pokrocily priklad: rodokmen Simpsonu
class Osoba:

    def __init__(self, otec, matka, jmeno):
        self.otec = otec
        self.matka = matka
        self.jmeno = jmeno


Abraham = Osoba(otec=None, matka=None, jmeno="Abraham Simpson")
Penelope = Osoba(otec=None, matka=None, jmeno="Penelope Olsen")
Bouvier = Osoba(otec=None, matka=None, jmeno="Pan Bouvier")
Jackie = Osoba(otec=None, matka=None, jmeno="Jackie Bouvier")
Homer = Osoba(otec=Abraham, matka=Penelope, jmeno="Homer Simpson")
Marge = Osoba(otec=Bouvier, matka=Jackie, jmeno="Marge Bouvier")
Bart = Osoba(otec=Homer, matka=Marge, jmeno="Bart Simpson")

print("Rodokmen pro osobu Bart Simpson")
print("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(Bart.jmeno, Bart.otec.jmeno, Bart.otec.otec.jmeno,
                                                  Bart.otec.matka.jmeno, Bart.matka.jmeno, Bart.matka.otec.jmeno,
                                                  Bart.matka.matka.jmeno))

print("Rodokmen pro osobu Homer Simpson")
print("{}\n{}\n{}".format(Homer.jmeno, Homer.otec.jmeno, Homer.matka.jmeno))

# sice to funguje, ale je to podstatne krkolomnejsi nez napoprve

# LEKCE 5 - 8
# jednoduche cviceni - ptak a angry ptak

class Ptak:

    def __init__(self):
        self._hlad = 100
        self._vaha = 50

    def __str__(self):
        return "Jsem ptak s vahou {} a hladem {}.".format(self._vaha, self._hlad)

    def snez(self, potrava):
        self._vaha += potrava
        self._hlad -= potrava
        if self._hlad < 0:
            self._hlad = 0


class Angry_ptak(Ptak):

    def __init__(self):
        super().__init__()
        self._vztek = 50

    def __str__(self):
        return "Jsem angry-ptak s vahou {}, hladem {} a mira meho vzteku je {}.".format(self._vaha,
                                                                                        self._hlad, self._vztek)

    def provokuj(self, provokace):
        if self._hlad > 60:
            self._vztek += provokace * 2
        else:
            self._vztek += provokace


ferdik = Ptak()
kane = Angry_ptak()

print(ferdik)
ferdik.snez(potrava=20)
print(ferdik)

print(kane)
kane.provokuj(provokace=5)
print(kane)
kane.snez(potrava=100)
kane.provokuj(provokace=5)
print(kane)


# stredne pokrocily priklad - clovek a Pythonista
class Osoba:

    def __init__(self, jmeno, vek, unava=0):
        """
        Zadany parametr unava jiz nikam nepsat pro dedeni a tvorby objektu.
        """
        self.jmeno = jmeno
        self.vek = vek
        self.unava = unava

    def __str__(self):
        return "{} (vek {}), unaven {}".format(self.jmeno, self.vek, self.unava)

    def beh(self, kms):
        if self.unava + kms <= 20:
            print("Bezim {} km.".format(kms))
            self.unava += kms
        else:
            print("Jsem prilis vycerpany.")

    def spani(self, hod):
        self.unava -= hod * 10
        if self.unava < 0:
            self.unava = 0


class Pythonista(Osoba):

    def __init__(self, jmeno, vek, ide):
        super().__init__(jmeno, vek)
        self.__ide = ide

    def programuj(self, pocet_radku):  # mam to trochu jinou logikou, ale zadani nebylo jednoznacne
        if self.unava > 13:
            print("Jsem prilis unaveny, abych programoval.")
        else:
            self.unava += pocet_radku // 10
            if self.unava > 20:
                self.unava = 20


pythonista = Pythonista(jmeno="Karel Novy",vek=25, ide="pycharm")
print(pythonista)
pythonista.beh(5)
print(pythonista)
pythonista.programuj(25)
print(pythonista)
pythonista.spani(8)
print(pythonista)


# pokrocily priklad - trojuhelniky a obdelnik
class Tvar:

    def __init__(self, barva):
        self.barva = barva


class Obdelnik(Tvar):

    def __init__(self, barva, sirka, delka):
        super().__init__(barva)
        self.sirka = sirka
        self.delka = delka

    def spocti_obsah(self):
        return self.sirka * self.delka


class Trojuhelnik(Tvar):

    def __init__(self, barva, a, b, c):
        super().__init__(barva)
        self.a = a
        self.b = b
        self.c = c

    def spocti_obsah(self):
        """
        Dle zadani pouzit Heronuv vzorec.
        """
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


obdelnik = Obdelnik(barva="hneda", sirka=3, delka=26)
trojuhelnik = Trojuhelnik(barva="zelena", a=25, b=15, c=15)

print("Obsah stromu je {} cm^2".format(4 * trojuhelnik.spocti_obsah() + obdelnik.spocti_obsah()))


# lekce 9
# jednoduchy priklad - prevod stupnu na radiany
class Prevodnik():

    @staticmethod
    def na_radiany(stupen):
        return "{} stupnu na radiany: {}".format(stupen, radians(stupen))

    @staticmethod
    def na_stupne(radian):
        return "{} radianu na stupne: {}".format(radian, degrees(radian))


print(Prevodnik.na_stupne(6.28))
print(Prevodnik.na_radiany(90))


# priklad 2 - tovarna na cukrovi
# dle zadani se mel pouzit navrhovy vzor Factory

class Cukrarna:

    def __init__(self, barva, tvar, vaha):
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha

    @staticmethod
    def bananove():
        return Cukrarna(barva="zluta", tvar="kulaty", vaha=20)

    @staticmethod
    def jahodove():
        return Cukrarna(barva="cervena", tvar="kulaty", vaha=15)

    @staticmethod
    def cokoladove():
        return Cukrarna(barva="hneda", tvar="hranaty", vaha=25)

    def __str__(self):
        return "Cukrovi barvy {}, tvaru {} a vahy {}g.".format(self.barva, self.tvar, self.vaha)


cukrovi = []

for i in range(4):
    cukrovi.append(Cukrarna.bananove())

for i in range(7):
    cukrovi.append(Cukrarna.jahodove())

for i in range(11):
    cukrovi.append(Cukrarna.cokoladove())

for kus in cukrovi:
    print(kus, id(kus))

"""
Pokyn o vytvoreni instance jsem sice pochopila, ale ty instance se nemusely ukladat! stacilo dat:
for i in range(4):
    a = Cukrarna.cokoladove()
    print(a)
Pri kazde iteraci by se promenna a normalne prepsala!

Spravne reseni nechalo ve tride Cukrovi pouze __init__ a textovou reprezentaci cukrovi. Na vyrobu cukrovi se vytvorila
samostatna trida Tovarna_na_cukrovi(), kde byly static metody na vyrobu jednotlivych druhu tak, jak to mam ja!

Reseni vypadalo takto:
class Cukrovi:

    def __init__(self, barva, tvar, vaha):
        jak to mam ja
    def __str__(self):
        jak to mam ja

class Tovarna_na_cukrovi:
    @staticmethod
    def vytvor_bananove():
        return Cukrovi("zluta", "kulaty", 20)

    ... a dalsi typy


Takze principem je nemit jednu tridu s hafo static metodama, ale jen se spolecnym kodem, a jednu, kde jsou definovane 
vsechny mozne druhy toho defaultniho originalu.
"""

# pokrocily priklad - databaze
# dle zadani se ma pouzit vzor Singleton
# reseni dle ITNetwork bo z toho zadani se to nedalo pochopit
class Databaze:

    # Instance, ktera se bude vracet
    __instance = None

    jmeno = None

    """
    toto jsem nasla na netu a trochu upravila, ale nefungovalo mi to spravne dle zadani pro a, b i c
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Vytvarim instanci.")
            self.jmeno = "SQLite"
            cls._instance = object.__new__(cls, *args, **kwargs)
        else:
            print("Instance uz existuje.")
        return cls._instance
    """

    def __new__(self):
        if Databaze.__instance:
            print("Instance uz existuje")
        else:
            print("Tvorim instanci")
            self.jmeno = 'SQLite'
            Databaze.__instance = self
        return Databaze.__instance


a = Databaze()
b = Databaze()
c = Databaze()

print(id(a) == id(b) == id(c))  # je to jeden a tentyz objekt

print("Jméno databáze a {0} b {1} c {2}".format(a.jmeno, b.jmeno, c.jmeno))
print("Je a instance Databaze?", a is Databaze)
print("Je b instance Databaze?", b is Databaze)
print("Je c instance Databaze?", c is Databaze)
print(isinstance(a, Databaze))  # what the hell
print(isinstance(b, Databaze))
print(isinstance(c, Databaze))
"""
a, b, c jsou stejny objekt - jak to, ze nejsou stejna instance tridy? proc mi tu haze False
a is Databaze znamena, ze se to rovna tomu objektu Tridy??
jaka je tady za tim logika?
"""


# lekce 10-13
# jednoduchy priklad - MujList
class MujList:

    def __init__(self, seznam):
        self.list = seznam

    def __add__(self, other):  # metoda se vola pri pouziti operatoru +
        if isinstance(other, MujList):
            new_list = []
            for cislo1, cislo2 in zip(self.list, other.list):
                new_list.append(cislo1 + cislo2)
            return new_list
        raise NotImplemented

    def __sub__(self, other):  # metoda se vola pri pouziti operatoru -
        if isinstance(other, MujList):
            new_list = []
            for cislo1, cislo2 in zip(self.list, other.list):
                new_list.append(cislo1 - cislo2)
            return new_list
        raise NotImplemented

    def __mul__(self, other):  # metoda se vola pri pouziti operatoru *
        if isinstance(other, MujList):
            new_list = []
            for cislo1, cislo2 in zip(self.list, other.list):
                new_list.append(cislo1 * cislo2)
            return new_list
        raise NotImplemented

    def __truediv__(self, other):  # metoda se vola pri pouziti operatoru /
        if isinstance(other, MujList):
            new_list = []
            for cislo1, cislo2 in zip(self.list, other.list):
                new_list.append(cislo1 / cislo2)
            return new_list
        raise NotImplemented

    def __str__(self):
        return '{}'.format(self.list)  # return str(self.list)


a = MujList([1, 2, 3, 4, 5])
b = MujList([5, 4, 3, 2, 1])
print(str(a), ' + ', str(b), " = ", b + a)
print(str(a), ' - ', str(b), " = ", a - b)
print(str(a), ' * ', str(b), " = ", b * a)
print(str(a), ' / ', str(b), " = ", a / b)
# jiny zapis: print('{} + {} = {}'.format(a, b, a + b))
c = [5, 4, 3, 2, 1]
# print(a + c) vyjimka NotImplemeted funguje


# stredni priklad - Dum s byty
class Dum:

    """
    Stejneho vysledku by se dalo dosahnout i tim, ze by existovala metoda
    def obyvatel(self, podlazi, majitel) - ktera by normalne nastavila majitele self.byty[0] = majitel
    a pak dalsi metoda, ktera by majitele vracela.
    """

    def __init__(self, n):
        self.byty = [None] * n

    def __setitem__(self, podlazi, majitel):
        print('setting...')
        self.byty[podlazi] = majitel

    def __getitem__(self, podlazi):
        """
        Is used to implement calls like self[key]
        """
        print('getting...')
        return self.byty[podlazi]

    def __str__(self):
        """
        Moje reseni zbytecne dela radek navic + __str__ by asi nemel sam nic tisknout... stacilo si vytvorit
        promennou - string, kde by byly vsechny ty vety a metoda by pak vracela toto.
        """
        for i in range(len(self.byty)):
            if self.byty[i]:
                print('V byte cislo {} je {}.'.format(i, self.byty[i]))
            else:
                print('Byt cislo {} je na prodej.'.format(i))
        return ''


dum = Dum(5)
dum[0] = 'Tonda Novak'  # prirazeni jako do seznamu
dum[4] = 'Jan Novy'
print(dum[2])  # pristup jako k seznamu, zapoji se __getitem__
print(dum.byty[4])  # __getitem__ se nezapoji
print(dum)
"""
Pouziti techto metod je zavisle na tom, jak chce clovek tridu a jeji data pouzivat.
"""

# pokrocily priklad: Mag a Kouzlo
class Kouzlo:

    def __init__(self, nazev, typ):
        self.nazev = nazev
        self.typ = typ


ohniva_koule = Kouzlo(nazev='Ohniva koule', typ='ohnive')
kletba_smrti = Kouzlo(nazev='Kletba smrti', typ='temne')
absolutni_nula = Kouzlo(nazev='Ansolutni nula', typ='vodni')
manipulace_energie = Kouzlo(nazev='Manipulace energie', typ='cista')


class Mag:

    iterace = 0

    def __init__(self, jmeno, specializace):
        self.__jmeno = jmeno
        self.specializace = specializace  # vyvola setter

    @property
    def specializace(self):
        return self.__specializace

    @specializace.setter
    def specializace(self, nova_specializace):
        """
        Nemusela jsem tu prirazovat primo jednotlive intance kouzel, ale priradit do setu typ jako ohnive, temne,
        ciste, vodni a pak v pouzij_kouzlo pristoupit pomoci if kouzlo.typ self.__typy_kouzel
        Takhle to funguje jen pro konkretni instance kouzel, ale ne na jine instance!!
        """
        self.__specializace = nova_specializace
        self.__typy_kouzel = set()
        if nova_specializace == 'voda':
            self.__typy_kouzel.update({absolutni_nula, ohniva_koule})
        elif nova_specializace == 'ohen':
            self.__typy_kouzel.update({ohniva_koule, kletba_smrti})
        elif nova_specializace == 'temna':
            self.__typy_kouzel.add(kletba_smrti)
        elif nova_specializace == 'cista':
            self.__typy_kouzel.add(manipulace_energie)
        if self.iterace > 0:
            print('{} se nyni specializuje na {}.'.format(self.__jmeno, self.__specializace))
        self.iterace += 1

    def pouzij_kouzlo(self, kouzlo):
        if kouzlo in self.__typy_kouzel:
            print('{} pouzil kouzlo {}.'.format(self.__jmeno, kouzlo.nazev))
        else:
            print('{} nemuze pouzit {} s typem poskozeni {}.'.format(self.__jmeno, kouzlo.nazev, kouzlo.typ))

    def __str__(self):
        return '{} je mag se specializaci na {}.'.format(self.__jmeno, self.__specializace)


gandalf = Mag(jmeno='Gandalf', specializace='voda')
print(gandalf.specializace)  # opravdu se nastavi
print(gandalf)
gandalf.pouzij_kouzlo(absolutni_nula)
gandalf.pouzij_kouzlo(kletba_smrti)
gandalf.specializace = 'temna'
gandalf.pouzij_kouzlo(kletba_smrti)
gandalf.pouzij_kouzlo(manipulace_energie)
gandalf.specializace = 'ohen'
gandalf.pouzij_kouzlo(ohniva_koule)



# jak funguji settery
class Person:

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        #self.fullname = jmeno + prijmeni vyvolava akci setteru

    @property
    def fullname(self):
        print('jsem ve vlastnosti')
        return '{} {}'.format(self.jmeno, self.prijmeni)

    @fullname.setter
    def fullname(self, name):
        print('jdu do setteru...')
        jmeno, prijmeni = name.split(' ')
        self.jmeno = jmeno
        self.prijmeni = prijmeni

mirek = Person("Mirek", 'Dusin')
mirek.fullname = 'Marek Holy'
print(mirek.fullname)
"""
Nelze mit atribut, vlastnost a setter stejneho jmena! Prirazeni do atributu vyvola akci setteru a do vlastnosti taky.
"""

