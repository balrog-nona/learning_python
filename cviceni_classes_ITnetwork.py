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



