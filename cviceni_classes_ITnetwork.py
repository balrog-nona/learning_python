import math

# jeden pes pro dva lidi
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


# rodokmen Simpsonu
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


# cviceni s ptakem
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


# Clovek a Pythonista
class Clovek:  # tuto tridu jsem jen opsala ze zadani

    jmeno = None  # nechapu, nedovoli mi to vytvorit cloveka bez jmena...
    vek = None
    unava = 0  # toto vleze automaticky do self.unava?

    # konstruktor
    def __init__(self, jmeno, vek):
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


# geometricke tvary
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