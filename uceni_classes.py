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

maxx = Stenatko(jmeno="Max")
maxx.snez("susenka")
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


# z IT NETWORK, kap. objektove orientovane programovani
class Kostka:

    def __init__(self, pocet_sten):  # metoda konstruktoru
        self.__pocet_sten = pocet_sten  # neverejny/soukromy atribut pomoci __

    def __str__(self):
        """
        Vraci textovou reprezentaci kostky.
        Tuto metodu maji vsechny objekty; kdyz se instance potrebuje vypsat nebo s ni pracovat jako s textem.
        """
        return str("Kostka s {} stenami.".format(self.__pocet_sten))

    def vrat_pocet_sten(self):
        return self.__pocet_sten

    def hod(self):
        """
        Generuje nahodne cislo od 1 do poctu sten kostky a to cislo vrati.
        """
        import random as _random  # vnitrni import modulu
        return _random.randint(1, self.__pocet_sten)


sestistenna = Kostka(pocet_sten=6)  # kostku bez parametru jiz nelze vytvorit
desetistenna = Kostka(pocet_sten=10)

print(sestistenna)  # kostka ted automaticky vypisuje __str__ metodu, nikoli odkaz na objekt
for i in range(10):
    print(sestistenna.hod(), end=" ")

print("\n", desetistenna, sep="")  # holy shit! dela se to separatorem
for i in range(10):
    print(desetistenna.hod(), end=" ")


class Bojovnik:

    def __init__(self, jmeno, zivot, utok, obrana, hraci_kostka):
        self.__jmeno = jmeno  # atributy jsou neverejne
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = hraci_kostka  # instance kostky - tridy kostka

    def __str__(self):
        return str(self.__jmeno)

    def __repr__(self):  # k dymanickemu provadeni kodu
        return str(self.__jmeno)

    @property  # dekorator, meni metodu na vlastnost??
    def nazivu(self):
        return self.__zivot > 0  # posoudi a vrati True nebo False

    def graficky_zivot(self):  # vykresli procentualni vysi zivota
        celkem = 20
        pocet = int(self.__zivot / self.__max_zivot * celkem)
        if pocet == 0 and self.nazivu:
            pocet = 1
        return "[{}{}]".format("#" * pocet, " " * (celkem - pocet))

    def bran_se(self, uder):
        zraneni = uder - (self.__obrana + self.__kostka_hod())
        if zraneni > 0:
            self.__zivot -= zraneni
            if self.__zivot < 0:
                self.__zivot = 0


kostka = Kostka(pocet_sten=10)
bojovnik = Bojovnik(jmeno="Zalgoren", zivot=100, utok=20, obrana=10, hraci_kostka=kostka)
print("\nBojovnik: {}".format(bojovnik))  # test __str__
print("Nazivu: {}".format(bojovnik.nazivu))  # test nazivu, tj. nejde to zavolat jako metoda()
print("Zivot: {}".format(bojovnik.graficky_zivot()))  # test graficky_zivot()
