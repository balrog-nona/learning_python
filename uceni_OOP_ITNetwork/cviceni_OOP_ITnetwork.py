from random import choice

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