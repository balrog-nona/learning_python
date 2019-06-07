import sys
import subprocess
import time
import random

class Kostka:
    """
    Trida reprezentuje hraci kostku.
    """

    def __init__(self, pocet_sten):  # metoda konstruktoru
        self.__pocet_sten = pocet_sten  # neverejny/soukromy atribut pomoci __ nelze zvenci modifikovat

    def __repr__(self):
        """
        return: v retezci kod konstruktoru pro fci eval()
        """
        return str("Kostka ({})".format(self.__pocet_sten))

    def __str__(self):
        """
        Vraci textovou reprezentaci kostky.
        Tuto metodu maji vsechny objekty; kdyz se instance potrebuje vypsat nebo s ni pracovat jako s textem.
        """
        return str("Kostka s {} stenami.".format(self.__pocet_sten))

    def vrat_pocet_sten(self):
        return self.__pocet_sten  # atribut je v read-only rezimu; jeho hodnotu zjistime jen zavolanim metody!

    def hod(self):
        """
        Generuje nahodne cislo od 1 do poctu sten kostky a to cislo vrati.
        """
        import random as _random  # vnitrni import modulu
        return _random.randint(1, self.__pocet_sten)


sestistenna = Kostka(pocet_sten=6)  # kostku bez parametru jiz nelze vytvorit
desetistenna = Kostka(pocet_sten=10)
# print(sestistenna.__pocet_sten) hodi AttributeError

print(sestistenna)  # kostka ted automaticky vypisuje __str__ metodu, nikoli odkaz na objekt
for i in range(10):
    print(sestistenna.hod(), end=" ")

print("\n", desetistenna, sep="")  # holy shit! dela se to separatorem
for i in range(10):
    print(desetistenna.hod(), end=" ")

# kopirovani dle teto lekce
jina_sestistenna = eval(repr(sestistenna))
print("\njina sestistenna: ", jina_sestistenna)
print("sestistenna: {}; jina_sestistenna: {}".format(id(sestistenna), id(jina_sestistenna)))
# jednoduse by se dalo pouzit i copy.deepcopy()


class Bojovnik:
    """
    Trida reprezentujici bojovnika do areny.
    Atributy a metody zacinaly na zacatku totirialu jako privatni, ale pak se kvuli dedeni zmenily na vnitrni.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self.__zprava = ""

    def __str__(self):
        return str(self._jmeno)

    def __repr__(self):
        return str(self._jmeno)

    @property  # dekorator - zmenil metodu na vlastnost
    def nazivu(self):
        return self._zivot > 0  # toto vyhodnoti a vrati True nebo False

    def graficky_ukazatel(self, aktualni, maximalni):
        """
        Metoda byla v prubehu prace prepsana tak,aby byla zobecnena a pouzila se jak na zivoty,tak na manu.
        """
        ukazatel_zivota = 20  # delka grafickeho ukazatele zivota
        pocet_dilku = int(aktualni / maximalni * ukazatel_zivota)
        # print(pocet_dilku)
        # na netu to maji nastavene, ze i vstupni zivot 60 se ukazuje jako 100%
        if pocet_dilku == 0 and self.nazivu:
            pocet_dilku = 1
        return "[{}{}]".format("#" * pocet_dilku, " " * (ukazatel_zivota - pocet_dilku))

    def graficky_zivot(self):
        return self.graficky_ukazatel(aktualni=self._zivot, maximalni=self._max_zivot)

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())  # objekt kostka ma k dispozici svoje metody
        if zraneni > 0:
            zprava = "{} utrpel poskozeni {} hp.".format(self._jmeno, zraneni)
            self._zivot -= zraneni
            if self._zivot < 0:
                self._zivot = 0
                zprava = zprava[:-1] + " a zemrel."
        else:
            zprava = "{} odrazil utok.".format(self._jmeno)
        self._nastav_zpravu(zprava=zprava)

    def utoc(self, souper):
        """
        Vyhoda referenci v Pythonu: instance soupere se sem jednoduse prida a vola se na ni metoda, aniz dojde k jejich
        zkopirovani.
        """
        uder = self._utok + self._kostka.hod()
        zprava = "{} utoci uderem za {} hp.".format(self._jmeno, uder)
        self._nastav_zpravu(zprava=zprava)
        souper.bran_se(uder=uder)

    def _nastav_zpravu(self, zprava):
        """
        Pri zacatku psani to byla privatni metoda, ale pak se kvuli dedeni zmenila na vnitrni.
        Celkove je treba pri psani tridy myslet na to, jestli se z ni bude dedit - pokud ano, atributy a metody
        nemuzou byt privatni.
        """
        self.__zprava = zprava

    def vrat_posledni_zpravu(self):
        return self.__zprava

"""
nona = Bojovnik(jmeno="Nona",zivot=100, utok=20, obrana=10, kostka=desetistenna)
print("Zivot: {}".format(nona.graficky_zivot()))
# utok na bojovnika
saruman = Bojovnik(jmeno="Saruman", zivot=60, utok=18, obrana=15, kostka=desetistenna)
saruman.utoc(nona)
print(saruman.vrat_posledni_zpravu())
print(nona.vrat_posledni_zpravu())
print("Zivot: {}".format(nona.graficky_zivot()))
"""


class Mag(Bojovnik):
    """
    Mag pouziva manu k magickemu utoku - ten zpusobi vetsi damage a vycerpa manu na 0.
    V kazdem kole se mana zveda o 10, Mag jinak utoci i beznym utokem.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        """
        Zde konstruktor musi mit vsechny parametry pro predka + nove co ma navic potomel.
        Konstruktor predka se vola pred potomkovym konstruktorem.
        Caste pouziti metody super()
        """
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self.__mana = mana
        self.__max_mana = mana
        self.__magicky_utok = magicky_utok
        self.__zprava = ""

    def utoc(self, souper):
        """
        Tato metoda prepise metodu v superclass.
        """
        # mana neni naplnena a nelze ji proto pouzit
        if self.__mana < self.__max_mana:
            self.__mana += 10
            if self.__mana > self.__max_mana:
                self.__mana = self.__max_mana
            super().utoc(souper=souper)
        # magicky utok s manou
        else:
            uder = self.__magicky_utok + self._kostka.hod()
            zprava = "{} pouzil magii za {} hp.".format(self._jmeno, uder)
            self._nastav_zpravu(zprava=zprava)
            self.__mana = 0
            souper.bran_se(uder=uder)

    def graficka_mana(self):
        return self.graficky_ukazatel(aktualni=self.__mana, maximalni=self.__max_mana)


class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self.__bojovnik_1 = bojovnik_1
        self.__bojovnik_2 = bojovnik_2
        self.__kostka = kostka

    def __vykresli(self):
        self.__vycisti_obrazovku()
        print("------------Arena-----------------\n")
        print("Bojovnici: \n")
        self.__vypis_bojovnika(bojovnik=self.__bojovnik_1)
        self.__vypis_bojovnika(bojovnik=self.__bojovnik_2)

    def __vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print("Zivot: {}".format(bojovnik.graficky_zivot()))
        if isinstance(bojovnik, Mag):
            print("Mana: {}".format(bojovnik.graficka_mana()))

    def __vycisti_obrazovku(self):
        if sys.platform.startswith("win"):
            subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            subprocess.call(["clear"])

    def __vypis_zpravu(self, zprava):
        print(zprava)
        time.sleep(1.5)  # uspi vlakno programu na tuto dobu v s

    def zapas(self):
        """
        Je to neprehledne, protoze graficky zivot reaguje az na text, ktery se teprve vypise. Az pochopim,
        proc se mi neprovadi prvni dva printy, prepsat si to do vlastni logicke verze, kde je nejdriv text a az
        po nem grafika.
        """
        print("Vitejte v arene!\nDnes se utkaji {} s {}!".format(self.__bojovnik_1,self.__bojovnik_2))
        print("Zapas muze zacit...")
        # self.__vykresli() proc to neprovede predchozi prikazy?
        if random.randint(0, 1):
            (self.__bojovnik_1, self.__bojovnik_2) = (self.__bojovnik_2, self.__bojovnik_1)
        while self.__bojovnik_1.nazivu and self.__bojovnik_2.nazivu:
            self.__bojovnik_1.utoc(self.__bojovnik_2)
            self.__vykresli() # tohle taky neprovede predchozi printy
            self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())  # nejdriv dostaneme info o utoku
            self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
            if self.__bojovnik_2.nazivu:
                self.__bojovnik_2.utoc(self.__bojovnik_1)
                self.__vykresli()
                self.__vypis_zpravu(self.__bojovnik_2.vrat_posledni_zpravu())
                self.__vypis_zpravu(self.__bojovnik_1.vrat_posledni_zpravu())


# print(nona._Bojovnik__jmeno)

nona = Bojovnik(jmeno="Nona", zivot=100, utok=20, obrana=10, kostka=desetistenna)
saruman = Mag(jmeno="Saruman", zivot=60, utok=15, obrana=12, kostka=desetistenna, mana=30, magicky_utok=45)

arena = Arena(bojovnik_1=nona, bojovnik_2=saruman, kostka=desetistenna)
arena.zapas()

