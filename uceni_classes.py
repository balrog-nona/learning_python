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


class Bojovnik:  # nesoukrome metody se automaticky dedi

    def __init__(self, jmeno, zivot, utok, obrana, hraci_kostka):
        self._jmeno = jmeno  # vnitrni atribut
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = hraci_kostka  # instance kostky - tridy kostka
        self.__zprava = ""  # soukromy atribut

    def __str__(self):
        return str(self._jmeno)

    def __repr__(self):  # k dymanickemu provadeni kodu
        return str(self._jmeno)

    def _nastav_zpravu(self, zprava):  # soukroma metoda s __ by nebzla k dispozici v dedeni; vnitrni metoda _ ano
        self.__zprava = zprava

    def vrat_posledni_zpravu(self):  # nastavovani zprav dle tutorialu - podle me zbytecne slozite
        return self.__zprava

    @property  # dekorator, zde zrejme meni metodu na vlastnost
    def nazivu(self):
        return self._zivot > 0  # posoudi a vrati True nebo False

    def graficky_ukazatel(self, aktualni, maximalni):  # vykresli procentualni vysi zivota
        celkem = 20
        pocet = int(aktualni / maximalni * celkem)
        if pocet == 0 and self.nazivu:
            pocet = 1
        return "[{}{}]".format("#" * pocet, " " * (celkem - pocet))

    def graficky_zivot(self):
        return self.graficky_ukazatel(self._zivot, self._max_zivot)

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())  # objekt kostka ma k dispozici svoje metody
        if zraneni > 0:
            zprava = "{} utrpel poskozeni {} hp.".format(self._jmeno, zraneni)
            self._zivot -= zraneni
            if self._zivot <= 0:
                self._zivot = 0
                zprava = zprava[:-1] + " a zemrel."
        else:
            zprava = "{} odrazil utok.".format(self._jmeno)
        self._nastav_zpravu(zprava)

    def utoc(self, oponent):
        uder = self._utok + self._kostka.hod()
        zprava = "{} utoci s uderem za {} hp.".format(self._jmeno, uder)
        self._nastav_zpravu(zprava)
        oponent.bran_se(uder)




kostka = Kostka(pocet_sten=10)
bojovnik = Bojovnik(jmeno="Zalgoren", zivot=100, utok=20, obrana=10, hraci_kostka=kostka)
print("\nBojovnik: {}".format(bojovnik))  # test __str__
print("Nazivu: {}".format(bojovnik.nazivu))  # test nazivu, tj. nejde to zavolat jako metoda()
print("Zivot: {}".format(bojovnik.graficky_zivot()))  # test graficky_zivot()
souper = Bojovnik(jmeno="Shadow", zivot=60, utok=18, obrana=15, hraci_kostka=kostka)
souper.utoc(bojovnik)
print(souper.vrat_posledni_zpravu())
print(bojovnik.vrat_posledni_zpravu())
print(bojovnik.graficky_zivot())


class Arena:

    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1 = bojovnik1  # vsechny objekty maji k dispozici sve metody a atributy
        self.__bojovnik2 = bojovnik2
        self.__kostka = kostka

    def __vycisti_obrazovku(self):
        import sys as _sys  # prasecina dle tutorialu
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def __vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print("Zivot: {}".format(bojovnik.graficky_zivot()))
        if isinstance(bojovnik, Mag):
            print("Mana: {}".format(bojovnik.graficka_mana()))

    def __vykresli(self):
        self.__vycisti_obrazovku()
        print("--------------ARENA-----------------\n")
        print("Bojovnici: \n")
        self.__vypis_bojovnika(self.__bojovnik1)
        self.__vypis_bojovnika(self.__bojovnik2)
        print("")

    def __vypis_zpravu(self, zprava):
        import time as _time
        print(zprava)
        _time.sleep(1.75)  # uspi vlakno programu na danou dobu v s

    def zapas(self):
        import random as _random
        print("Vitejte v arene!")
        print("Dnes se utkaji {} a {}".format(self.__bojovnik1, self.__bojovnik2))
        print("Zapas muze zacit...", end=" ")
        # prohozeni bojovniku
        if _random.randint(0, 1):  # WOW!
            self.__bojovnik1, self.__bojovnik2 = self.__bojovnik2, self.__bojovnik1
        # cyklus s bojem
        while self.__bojovnik1.nazivu and self.__bojovnik2.nazivu:
            self.__bojovnik1.utoc(oponent=self.__bojovnik2)
            self.__vykresli()
            self.__vypis_zpravu(self.__bojovnik1.vrat_posledni_zpravu())
            self.__vypis_zpravu(self.__bojovnik2.vrat_posledni_zpravu())
            if self.__bojovnik2.nazivu:
                self.__bojovnik2.utoc(oponent=self.__bojovnik1)
                self.__vykresli()
                self.__vypis_zpravu(self.__bojovnik2.vrat_posledni_zpravu())
                self.__vypis_zpravu(self.__bojovnik1.vrat_posledni_zpravu())
            print("")


class Mag(Bojovnik):  # nema pristup k atributum z Bojovnika, ktere jsou soukrome, pouze k vnitrnim

    def __init__(self, jmeno, zivot, utok, obrana, hraci_kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, hraci_kostka)
        self.__mana = mana
        self.__max_mana = mana
        self.__magicky_utok = magicky_utok

    def utoc(self, oponent):  # prekryti metody ze superclass
        # mana neni naplnena
        if self.__mana < self.__max_mana:
            self.__mana += 10
            if self.__mana > self.__max_mana:
                self.__mana = self.__max_mana
            super().utoc(oponent)
        # magicky utok
        else:
            uder = self.__magicky_utok + self._kostka.hod()
            zprava = "{} pouzil magii za {} hp.".format(self._jmeno, uder)
            self._nastav_zpravu(zprava)
            self.__mana = 0
            oponent.bran_se(uder)

    def graficka_mana(self):
        return self.graficky_ukazatel(self.__mana, self.__max_mana)


kostka = Kostka(pocet_sten=10)
zalgoren = Bojovnik(jmeno="Zalgoren", zivot=100, utok=20, obrana=10, hraci_kostka=kostka)
gandalf = Mag(jmeno="Galdalf", zivot=60, utok=15, obrana=12, hraci_kostka=kostka, mana=30, magicky_utok=45)

# funkce s dedenim - vraci True/False
if isinstance(gandalf, Mag):
    print("{} je mag.".format(gandalf))
if issubclass(Mag, Bojovnik):
    print("Mag je subclass Bojovnika.")

arena = Arena(bojovnik1=zalgoren, bojovnik2=gandalf, kostka=kostka)
arena.zapas()

