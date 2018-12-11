class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: Mnam, {} mi chutna.".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Mnau.".format(self.jmeno))

    def snez(self, jidlo):
        print("{} na {} chvili fascinovane kouka.".format(self.jmeno, jidlo))
        super().snez(jidlo)


class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Haf.".format(self.jmeno))


barnecek = Kotatko(jmeno="Barnecek")
barnecek.snez("tofu")
# barnecek.zamnoukej()

max = Stenatko(jmeno="Max")
max.snez("susenka")
# max.zastekej()


class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace("s", "sss")
        jmeno = jmeno.replace("S", "SSS")
        super().__init__(jmeno)

standa = Hadatko(jmeno="Stanislav")
print(standa.jmeno)
standa.snez("mys")

zviratka = [Kotatko(jmeno="Mandy"), Stenatko(jmeno="Bak")]
for zviratko in zviratka:
    zviratko.udelej_zvuk()
    zviratko.snez("flakota")

"""
V ramci generalizace byly metody zamnkoukej a zastekej prepsane na udelej zvuk, aby se to dalo pouzit v cyklu.
"""






