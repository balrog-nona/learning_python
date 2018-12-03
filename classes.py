# print(type("a") == str)

class Kotatko:
    def __init__(self, jmeno):  # zavola se automaticky pri tvorbe noveho objektu
        self.jmeno = jmeno

    def __str__(self):
        return "Kotatko jmenem {}.".format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mnau, mnau, {} mi chutna!".format(self.jmeno, jidlo))

"""
kotatko = Kotatko()  # tvorba noveho objektu/nove instance zavolanim tridy
# kotatko.zamnoukej()  # volani metody

mourek = Kotatko()
mourek.jmeno = "Mourek"  # atribut - uschova dat

micka = Kotatko()
micka.jmeno = "Micka"
# micka.zamnoukej = 12345  # timto by se vytvoril atribut a ztratil pristup k metode
# micka.zamnoukej()  # int object is not callable

mourek.zamnoukej()
micka.zamnoukej()
mourek.snez("tofu")
"""

barnecek = Kotatko(jmeno="Barnecek")
barnecek.zamnoukej()
print(barnecek)


class Kocka:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zivoty = 9

    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))

    def je_ziva(self):  # ev. return self.zivoty > 0 - vrati True nebo False
        if self.zivoty > 0:
            print("{}: Ano, jsem ziva. Mam {} zivotu.".format(self.jmeno, self.zivoty))
        else:
            print("{}: Bohuzel, jsem mrtva.".format(self.jmeno))

    def uber_zivot(self):  # ev. if not self.je_ziva() - nezabijes mrtvou kocku; else self.zivoty -= 1
        if 1 <= self.zivoty <= 9:
            self.zivoty -= 1
            print("Prisla jsem o zivot, mam jich ted jen {}.".format(self.zivoty))

    def snez(self, jidlo):
        if jidlo == "ryba" and 1 < self.zivoty < 8:
            self.zivoty += 1
        if self.zivoty > 0:
            print("{}: Mnam, to mi moc chutnalo!".format(self.jmeno))


dafne = Kocka(jmeno="Dafne")
dafne.zamnoukej()
dafne.je_ziva()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.snez("tofu")
dafne.snez("ryba")
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.uber_zivot()
dafne.je_ziva()
dafne.snez("ryba")
dafne.uber_zivot()
dafne.uber_zivot()
dafne.je_ziva()