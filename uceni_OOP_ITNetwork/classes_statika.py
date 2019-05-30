"""
v tomto tutorialu jsem nedodelavala zapouzdreni - privatni a vnitrni promenne, atributy a metody
"""


class Uzivatel:

    minimalni_delka_hesla = 6
    dalsi_id = 1  # kdyby tu nebyla tridni promenna, musel by se pocet instanci hlidat zvenci

    def __init__(self, jmeno, heslo):
        self.jmeno = jmeno
        self.heslo = heslo
        self.prihlaseny = False
        self.id = Uzivatel.dalsi_id
        Uzivatel.dalsi_id += 1  # trida si sama uklada, jake bude id dalsi instance

    def prihlas_se(self, zadane_heslo):
        if self.heslo == zadane_heslo:
            self.prihlaseny = True
            return True
        else:
            self.prihlaseny = False
            return False

    @staticmethod  # staticka metoda; nemuze pristupvat k zadnym instancnim promennym
    def zvaliduj_heslo(heslo):
        if len(heslo) >= Uzivatel.minimalni_delka_hesla:
            return True
        else:
            return False

    @classmethod  # tridni metoda; hodi se, kdyz se bude trida dedit a v potomkovi ma byt jina hodnota tridni promenne
    def nove_zvaliduj_heslo(cls, heslo):  # prvni parametr - odkaz na tridu,dle konveci cls
        if len(heslo) >= cls.minimalni_delka_hesla:  # pomoci cls. se volajitridni promenne
            return True
        else:
            return False


print(Uzivatel.minimalni_delka_hesla)
"""
pristup k promenne primo pres tridu, nikoli instanci
promenna nalezi tride a muzeme se na ni ptat, aniz bychom meli vytvoreneho uzivatele
tato promenna bude ale i na instanci
"""
u = Uzivatel(jmeno="Tomas", heslo="hesloveslo")
print(u.minimalni_delka_hesla)

u.minimalni_delka_hesla = 2  # zmena probehla jen na instanci
print(Uzivatel.minimalni_delka_hesla)

print(Uzivatel.zvaliduj_heslo("hesloveslo"))  # metodu muzu zavolat na tride

v = Uzivatel(jmeno="Ondra", heslo="testo")

print("ID prvniho uzivatele je ", u.id)
print("ID druheho uzivatele je ", v.id)
print("Minimalni delka hesla uzivatele je: ", Uzivatel.minimalni_delka_hesla)
print("Validnost hesla 'testo' je:" , Uzivatel.zvaliduj_heslo("testo"))


# i normalni funkce jde slucovat do trid
class Trida:  # vypada to podobne, jakoby byly obsazene v nejakem modulu

    def nejaka_fce():  # POZOR - neni tu self, jsou to totiz fce a ne metody
        print("Tato fce je ve tride.")

    def jina_fce(text):
        print("Tahle fce je taky ve tride.")
        print("Text je: ", text)


Trida.nejaka_fce()
Trida.jina_fce(text="parametr")