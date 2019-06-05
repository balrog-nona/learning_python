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

# lekce 4 - reference, garbage collector
class Uzivatel:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return str(self.jmeno)


u = Uzivatel(jmeno="Jan Novak", vek=28)
v = Uzivatel(jmeno="Josef Novy", vek=32)
print("u: {}\nv: {}".format(u, v))
print("u: {}\nv: {}".format(id(u), id(v)))

u = v  # zkopiruje se odkaz na objekt pod referenci v, ale objekt mame jen jeden; k objektu u ted nevede zadna reference
# mam ted 2 reference na stejny objekt (Josefa Noveho)
print("u: {}\nv: {}".format(u, v))
print("u: {}\nv: {}".format(id(u), id(v)))
# objekt u (Jana Novaka) sezral garbage collector
# vice k moznostem spravy pameti na webu ITNetwork

v.jmeno = "John Doe"
print("u: {}\nv: {}".format(u, v))
print("u: {}\nv: {}".format(id(u), id(v)))
v = None  # reference na objekt zrusena
print("u: {}\nv: {}".format(u, v))
print("u: {}\nv: {}".format(id(u), id(v)))
# zrusila se reference v na Noveho, ale stale k nemu vede reference u


# LEKCE 7 - DEDENI

"""
PRIVATNI metody a atributy
- pri vytvareni privatnich metod a atributu python pouziva name mangling, tzn. nasledujici:
ma-li class Foo atribut self.__a nelze k nemu pristoupit takto Foo.__a musi se pouzit toto
Foo._Foo__a
to plati pro atributy i metody. Python pouziva __ a name mangling k tomu, aby nedochazelo ke konfliktum pri dedeni, 
kdyby existovaly atributy a metody stejneho jmena. __ by se melo pouzivat prave k tomuto ucelu.

pristup ze zdedene tridy by vypadal takto:
self._Parentclass__private()
podle konvenci by ale toto nemela byt bezna praxe
"""

class Zamestnanec:

    def __init__(self, jmeno, heslo, vek):  # vnitrni atributy misto privatnich
        self._jmeno = jmeno
        self._heslo = heslo
        self._vek = vek
        self.__prava = "zadna"

    def prihlasit(self):
        return "prihlasen {}".format(self._heslo)

    def odhlasit(self):
        return "odhlasen {}".format(self._heslo)

    def nastav_vahu(self, zvire):
        return zvire.vaha


class Administrator(Zamestnanec):

    def __init__(self, jmeno, heslo, vek, telefon):
        super().__init__(jmeno, heslo, vek)
        self.__telefon = telefon

    def pridej_zvire(self, zvire):
        return zvire

    def vymaz_zvire(self, zvire):
        return zvire


zamestnanec = Zamestnanec(jmeno="nona", heslo="1234", vek=32)
print("informace o zamestnanci:\n{} {} {}".format(zamestnanec._jmeno, zamestnanec._heslo, zamestnanec._vek))
# print(zamestnanec.__prava) vyhodi AttributeError
print(zamestnanec._Zamestnanec__prava)  # toto by se ale moc nemelo delat

admin = Administrator(jmeno="paul", heslo=444, vek=55, telefon=732999)
print("info o adminovi:\n{} {} {}".format(admin._jmeno, admin._heslo, admin._vek))
# print(admin.__prava)  oboje AttributeError
# print(admin.__telefon)
print(admin._Zamestnanec__prava)  # toto by se ale nemelo moc delat
print(admin._Administrator__telefon)  # dtto

print(zamestnanec.prihlasit())
print(admin.prihlasit())
print(admin.pridej_zvire(zvire="had"))


# testovani typu tridy
a = 1
# 1. pomoci fce type()
print(type(a) == type(1))
print(type(a) == type("python"))
print(type(a) == int)
print(type(a) == str)

# 2. beznejsi je pomoci fce isinstance(),issubclass()
print(isinstance(a, int))
print(isinstance(a, str))

print(a.__class__.__base__)
print(a.__class__.__bases__)
# vsechny objekty (a v pythonu je objektem vsechno) dedi ze tridy objekt