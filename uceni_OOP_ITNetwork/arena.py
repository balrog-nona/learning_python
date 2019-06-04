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
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__max_zivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self.__kostka = kostka
        self.__zprava = ""

    def __str__(self):
        return str(self.__jmeno)

    def __repr__(self):
        return str(self.__jmeno)

    @property  # dekorator - zmenil metodu na vlastnost
    def nazivu(self):
        return self.__zivot > 0  # toto vyhodnoti a vrati True nebo False

    def graficky_zivot(self):
        ukazatel_zivota = 20  # delka grafickeho ukazatele zivota
        pocet_dilku = int(self.__zivot / self.__max_zivot * ukazatel_zivota)
        # print(pocet_dilku)
        # na netu to maji nastavene, ze i vstupni zivot 60 se ukazuje jako 100%
        if pocet_dilku == 0 and self.nazivu:
            pocet_dilku = 1
        return "[{}{}]".format("#" * pocet_dilku, " " * (ukazatel_zivota - pocet_dilku))

    def bran_se(self, uder):
        zraneni = uder - (self.__obrana + self.__kostka.hod())  # objekt kostka ma k dispozici svoje metody
        if zraneni > 0:
            zprava = "{} utrpel poskozeni {} hp.".format(self.__jmeno, zraneni)
            self.__zivot -= zraneni
            if self.__zivot < 0:
                self.__zivot = 0
                zprava = zprava[:-1] + " a zemrel."
        else:
            zprava = "{} odrazil utok.".format(self.__jmeno)
        self.__nastav_zpravu(zprava=zprava)

    def utoc(self, souper):
        """
        Vyhoda referenci v Pythonu: instance soupere se sem jednoduse prida a vola se na ni metoda, aniz dojde k jejich
        zkopirovani.
        """
        uder = self.__utok + self.__kostka.hod()
        zprava = "{} utoci uderem za {} hp.".format(self.__jmeno, uder)
        self.__nastav_zpravu(zprava=zprava)
        souper.bran_se(uder)

    def __nastav_zpravu(self, zprava):  # soukroma/privatni metoda
        """
        Pro vnitrni ucel tridy - nastavi zpravu do privatni promenne.
        """
        self.__zprava = zprava

    def vrat_posledni_zpravu(self):
        return self.__zprava


Nona = Bojovnik(jmeno="Nona",zivot=100, utok=20, obrana=10, kostka=desetistenna)
print("Zivot: {}".format(Nona.graficky_zivot()))
# utok na bojovnika
Saruman = Bojovnik(jmeno="Saruman", zivot=60, utok=18, obrana=15, kostka=desetistenna)
Saruman.utoc(Nona)
print(Saruman.vrat_posledni_zpravu())
print(Nona.vrat_posledni_zpravu())
print("Zivot: {}".format(Nona.graficky_zivot()))