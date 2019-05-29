from random import choice

# LEKCE 3 - CVICENI
# jednoduchy priklad: covek a unava
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
class Slovo:

    def __init__(self):
        self.jaky = None
        self.kdo = None
        self.co = None
        self.jak = None
        self.kde = None

generator = Slovo()
generator.jaky = ["maly", "opily", "vzdelany", "umanuty", "drzy"]
generator.kdo = ["workoholik", "sobec", "blbec", "ridic", "serif"]
generator.co = ["varil", "slapal", "mlatil", "tancil", "pral"]
generator.jak = ["vytrvale", "s nadsenim", "znudene", "sarkasticky", "pitome"]
generator.kde = ["u primatora", "v pivovaru", "u nehtarky", "u kartarky", "v zachode"]

for i in range(10):
    print("{} {} {} {} {}".format(random.choice(generator.jaky)))



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

