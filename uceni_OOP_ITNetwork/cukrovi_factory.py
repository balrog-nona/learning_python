# lekce 9, priklad 2
# dle zadani se mel pouzit navrhovy vzor Factory

class Cukrarna:

    def __init__(self, barva, tvar, vaha):
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha

    @staticmethod
    def bananove():

        return Cukrarna(barva="zluta", tvar="kulaty", vaha=20)

    @staticmethod
    def jahodove():

        return Cukrarna(barva="cervena", tvar="kulaty", vaha=15)

    @staticmethod
    def cokoladove():

        return Cukrarna(barva="hneda", tvar="hranaty", vaha=25)

    def __str__(self):

        return "Cukrovi barvy {}, tvaru {} a vahy {}g.".format(self.barva, self.tvar, self.vaha)


cukrovi = []

for i in range(4):
    cukrovi.append(Cukrarna.bananove())

for i in range(7):
    cukrovi.append(Cukrarna.jahodove())

for i in range(11):
    cukrovi.append(Cukrarna.cokoladove())

for kus in cukrovi:
    print(kus, id(kus))

"""
Pokyn o vytvoreni instance jsem sice pochopila, ale tyinstance se nemusely ukladat! stacilo dat:
for i in range(4):
    a = Cukrarna.cokoladove()
    print(a)
Pri kazde iteraci by se promenna a normalne prepsala!

Spravne reseni nechalo ve tride Cukrovi pouze __init__ a textovou reprezentaci cukrovi. Na vyrobu cukrovi se vytvorila
samostatna trida Tovarna_na_cukrovi(), kde byly static metody na vyrobu jednotlivych druhu tak, jak to mam ja!

Reseni vypadalo takto:
class Cukrovi:

    def __init__(self, barva, tvar, vaha):
        jak to mam ja
    def __str__(self):
        jak to mam ja
        
class Tovarna_na_cukrovi:
    @staticmethod
    def vytvor_bananove():
        return Cukrovi("zluta", "kulaty", 20)
    
    ... a dalsi typy


Takze principem je nemit jednu tridu s hafo static metodama, ale jen se spolecnym kodem, a jednu, kde jsou definovane 
vsechny mozne druhy toho defaultniho originalu.
"""