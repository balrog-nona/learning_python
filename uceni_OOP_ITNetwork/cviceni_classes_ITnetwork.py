import math

# pri prvnim prochazeni tutorialu
# cv. lekce 4:jeden pes pro dva lidi
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


azor = Pes(jmeno='Azor',vek=2)
print("{} ({} let)".format(azor.jmeno, azor.vek))

karel = Osoba(jmeno='Karel', pes=azor)
lenka = Osoba(jmeno='Lenka', pes=azor)

karel.pes.zestarni()
lenka.pes.zestarni()

print('{} ({} let)'.format(karel.pes.jmeno, karel.pes.vek))
print('{} ({} let)'.format(lenka.pes.jmeno, lenka.pes.vek))


# cv. lekce 4: rodokmen Simpsonu
class Rodina:

    def __init__(self, jmeno):
        self.jmeno = jmeno

    def rodice(self, otec, matka):
        self.otec = otec
        self.matka = matka

    def __str__(self):
        return self.jmeno

    def vypis_rodinu(self):
        zprava1 = "Rodokmen pro osobu {}\n".format(self.jmeno)
        try:
            zprava2 = "{}\n{}\n{}\n{}\n{}\n{}".format(self.jmeno, self.otec, self.otec.otec, self.otec.matka,
                                                      self.matka, self.matka.otec, self.matka.matka)
        except AttributeError:
            zprava2 = "{}\n{}\n{}\n".format(self.jmeno, self.otec, self.matka)
        return zprava1 + zprava2



bart = Rodina(jmeno="Bart Simpson")
homer = Rodina(jmeno="Homer Simpson")
marge = Rodina(jmeno="Marge Bouvier")
abraham = Rodina(jmeno="Abraham Simpson")
penelope = Rodina(jmeno="Penelope Olsen")
jackie = Rodina(jmeno="Jackie Bouvier")
bouvier = Rodina(jmeno="Pan Bouvier")

bart.rodice(homer, marge)
homer.rodice(abraham, penelope)
marge.rodice(jackie, bouvier)

print(bart.vypis_rodinu())
print(homer.vypis_rodinu())


# cv. lekce 5 - 8: cviceni s ptakem
class Ptak:

    def __init__(self):
        self.hlad = 100
        self.vaha = 50

    def snez(self, vaha_potravy):
        self.hlad -= vaha_potravy
        self.vaha += vaha_potravy

    def vypis(self):
        print("Jsem ptak s vahou {}g a hladem {}.".format(self.vaha, self.hlad))


class AngryPtak(Ptak):

    def __init__(self):
        self.vztek = 50
        super().__init__()

    def provokuj(self, mira_provokace):
        if self.hlad >= 70:
            self.vztek += mira_provokace * 2
        else:
            self.vztek += mira_provokace

    def vypis(self):
        print("Jsem angry-ptak s vahou {}g, hladem {} a mirou vzteku {}.".format(self.vaha, self.hlad, self.vztek))


ptacek = Ptak()
ptacisko = AngryPtak()
ptacek.vypis()
ptacek.snez(20)
ptacek.vypis()
ptacisko.vypis()
ptacisko.provokuj(5)
ptacisko.vypis()
ptacisko.snez(100)
ptacisko.provokuj(5)
ptacisko.vypis()


# cv. lekce 5 - 8: Clovek a Pythonista
class Clovek:  # tuto tridu jsem jen opsala ze zadani
    # ty kraviny 3 promenne by tu vubec nemusely byt
    jmeno = None  # obsolentni
    vek = None  # obsolentni
    unava = 0  # toto vleze automaticky do self.unava, bo to bude v metode

    # konstruktor
    def __init__(self, jmeno, vek):  # prepisuje defaultni moznost, proto nebere to z promennych vyse
        self.jmeno = jmeno
        self.vek = vek

    # spi danou dobu
    def spi(self, doba):
        self.unava -= doba * 10
        if self.unava < 0:
            self.unava = 0

    # ubehne danou vzdalenost
    def behej(self, vzdalenost):
        if self.unava + vzdalenost < 20:
            self.unava += vzdalenost
        else:
            print("Jsem prilis unaveny.")

    # textova reprezentace cloveka
    def __str__(self):
        return "{} {}".format(self.jmeno, self.vek)


class Pythonista(Clovek):

    def __init__(self, jmeno, vek, ide):
        super().__init__(jmeno, vek)  # novejsi zpusob syntaxe nez v reseni
        self.ide = ide

    def programuj(self, pocet_radku):
        self.unava += pocet_radku // 10
        if self.unava > 20:
            self.unava = 20
            print("Jsem prilis unaveny, nez abych programoval.")


#nekdo = Clovek()  nedovoli vytvorit cloveka bez jmena a veku, ackoli vychozi jsou None
#print(nekdo)

programator = Pythonista(jmeno="Nona",vek=32, ide="Pycharm")
print(programator)
programator.programuj(250)
print(programator.unava)
programator.behej(2)
print(programator.unava)
programator.spi(1)
print(programator.unava)
programator.programuj(15)
print(programator.unava)


# cv. lekce 5 - 8: geometricke tvary
class Tvar:

    def __init__(self, barva):
        self.barva = barva


class Obdelnik(Tvar):

    def __init__(self, barva, sirka, vyska):
        super().__init__(barva)
        self.sirka = sirka
        self.vyska = vyska

    def obsah(self):
        self.obsah = self.sirka * self.vyska


class Trojuhelnik(Tvar):

    def __init__(self, barva, a, b, c):
        super().__init__(barva)
        self.strana_a = a
        self.strana_b = b
        self.strana_c = c

    def obsah(self):
        s = (self.strana_a + self.strana_b + self.strana_c) / 2
        self.obsah = math.sqrt(s * (s - self.strana_a) * (s - self.strana_b) * (s - self.strana_c))



obdelnik = Obdelnik(barva="cervena", sirka=3, vyska=26)
obdelnik.obsah()
trojuhelnik = Trojuhelnik(barva="modra", a=15, b=15, c=25)
trojuhelnik.obsah()

obsah_stromu = obdelnik.obsah + (4 * trojuhelnik.obsah)
print("Obsah stromu je {} cm^2.".format(obsah_stromu))


# LEKCE 9
# prevod stupne a radiany mezi sebou - cviceni ke statice
class Prevod:

    @staticmethod
    def na_stupne(radian):  # stacilo math.degrees()
        return radian * (180 / math.pi)


    @staticmethod
    def na_radian(stupne):  # stacilo math.radians()
        return stupne * (math.pi / 180)


print("6.28 radianu na stupne {}".format(Prevod.na_stupne(6.28)))
print("90 stupnu na radiany {}".format(Prevod.na_radian(90)))


# tovarna na cukrovi
class Cukrarna:

    @staticmethod
    def bananove():
        barva = "zluta"
        tvar = "kulaty"
        vaha = 20
        return barva, tvar, vaha

    @staticmethod
    def jahodove():
        barva = "cervena"
        tvar = "kulaty"
        vaha = 15
        return barva, tvar,vaha

    @staticmethod
    def cokoladove():
        barva = "hneda"
        tvar = "hranaty"
        vaha =25
        return barva, tvar, vaha

for i in range(4):
    print("Cukrovi barvy {}, tvaru {} a vahy {}g".format(*Cukrarna.bananove()))
for i in range(4):
    print("Cukrovi barvy {}, tvaru {} a vahy {}g".format(*Cukrarna.jahodove()))
for i in range(4):
    print("Cukrovi barvy {}, tvaru {} a vahy {}g".format(*Cukrarna.cokoladove()))
"""
v jejich reseni je to jinak poskladane, bo to mel byt priklad na navrhovy vzor Factory, coz me se vubec 
nepovedlo implementovat
"""


# navrhovy vzor Singleton
class Databaze:

    # instance, ktera se bude vracet
    __instance = None
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

    def __new__(self):  # tohle je opsane dle spravneho reseni
        if not Databaze.__instance:
            print("Vytvarim instanci.")
            self.jmeno = "SQLite"
            Databaze.__instance = self
        else:
            print("Instance jiz existuje.")
        return Databaze.__instance


a = Databaze()  # jak to,ze to neni instance?
b = Databaze()  # proc mi to dole haze, ze se to rovna tride a ne ze je to instance??
c = Databaze()


print("Jmeno databaze a {}, b {}, c {}".format(a.jmeno, b.jmeno, c.jmeno))
print("Je a instance Databaze? ", isinstance(a, Databaze))  # what the hell
print("Je b instance Databaze? ", isinstance(b, Databaze))
print("Je c instance Databaze? ", c is Databaze)