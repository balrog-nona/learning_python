"""
staticke (neboli tridni) promenne a metody jsou promenne/metody definovane na tride a jsou nezavisle na instanci
ITNetwork je doporucuje vubec nepouzivat... ale kdo vi. Pry je to jako globalni promenne a umoznuje to psat spatny kod.

Staticke prvky patri tride a ne instanci - data v nich ulozena lze cist bez ohledu na to, jestli nejaka instance
existuje.

Staticke metody se volaji na tride, hlavne pomocne metody, ktere se budou casto pouzivat a nevyplati se vytvorit
instanci.

Tridni metody dostavaji jakoprvni parametr tridu. Hodi se, kdyz budu tridu dedit a chci mit v potomkovi jinou hodnou
tridni promenne. Jinak je lepsi pouzit statickou metodu.

Ignorovala jsem zapouzdreni. Normalne by ty vypisy na konci vyzadovaly vlastni metody na vraceni privatnich promennych.
"""

class Uzivatel:

    # Ve chvili, kdy uzivatele registruju, jeste nemam k dispozici jeho instanci.
    """Pri registraci uzivatele potrebuju znat minimalni delku hesla jeste pred jeho vytvorenim + taky heslo
    zkontrolovat."""

    minimalni_delka_hesla = 6
    dalsi_id = 1

    def __init__(self, jmeno, heslo):
        self.jmeno = jmeno
        self.heslo = heslo
        self.prihlaseny = False
        # prakticke vyuziti tridnich promennych pro cislovani uzivatelu
        self.id = Uzivatel.dalsi_id
        Uzivatel.dalsi_id += 1

    def prihlas_se(self,zadane_heslo):
        if self.heslo == zadane_heslo:
            self.prihlaseny = True
            return True
        else:
            self.prihlaseny = False
            return False

    @staticmethod
    def zvaliduj_heslo(heslo):
        """
        Staticka metoda nema pristup k zadnym instancnim promennym - tyto promenne totiz neexitujv kontextu tridy, ale
        instance.
        """
        if len(heslo) >= Uzivatel.minimalni_delka_hesla:
            # print(self.jmeno)
            return True
        else:
            return False

    @classmethod
    def zvaliduj_heslo_class(cls, heslo):
        if len(heslo) >= cls.minimalni_delka_hesla:
            return True
        else:
            return False


print(Uzivatel.minimalni_delka_hesla)  # da se na to ptat primo pres tridu

u = Uzivatel(jmeno="Tomas Marny", heslo="tik")
print(u.minimalni_delka_hesla)  # tady je ta promenna taky

# zmena tridni promenne pres instanci zmeni hodnotu jen pro tu instanci
u.minimalni_delka_hesla = 90
print(Uzivatel.minimalni_delka_hesla)
print(u.minimalni_delka_hesla)

print(Uzivatel.zvaliduj_heslo("hesloveslo"))
print(u.zvaliduj_heslo(u.heslo))

v = Uzivatel(jmeno="Rosta", heslo="6666666")

print("ID prvniho uzivatele je {}".format(u.id))
print("ID druheho uzivatele je {}".format(v.id))
print("Minimalni delka hesla uzivatele je {}".format(Uzivatel.minimalni_delka_hesla))
print("Validnost hesla 'heslo' je: {}".format(Uzivatel.zvaliduj_heslo("heslo")))

"""
Do trid lze slucovat i normalni fce - kazda fce by byla vlastne metoda. Pak to vypada podobne jakoby byly obsazene v
nejakem modulu.
"""

class Trida:

    def scitani():  # je to opravdu fce - neobsahuje self ani nic
        print("fce scitani")

    def odcitani(a):
        print("fce odcitani {}".format(a))


Trida.scitani()
Trida.odcitani(a=6)