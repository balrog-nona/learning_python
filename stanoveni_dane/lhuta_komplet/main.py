from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime

def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0]._konec_lhuty()
        seznam_ukonu[0]._maximalni_delka()
    subjektivni_lhuta = seznam_ukonu[0]._konec
    objektivni_lhuta = seznam_ukonu[0]._maximalni

    ukony = soubeh_odst4(seznam_ukonu)  # sjednoceni ukonu soubehu i Odst4
    zacatky_konce = odstavce4(ukony)  # posbirani zacatku a konce vsech staveni
    ukony_soubehu = []

    for ukon in seznam_ukonu[1:]:  # 1. krok - zpracovani seznamu ukonu
        #print('velky for cyklus:', ukon)
        if isinstance(ukon, Odst4) and not ukon._konec_staveni:
            raise Exception('Lhutu nelze spocitat, dokud neskoncilo staveni.')
        """
        for prvek in zacatky_konce:  # pokud jsou zacatky_konce prazdne, nic se nestane
            if ukon._ukon <= prvek[1]:
                ukony_soubehu.append(ukon)
        """

        ukon._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                              maximalni_delka=objektivni_lhuta)
        subjektivni_lhuta = ukon._konec


    return subjektivni_lhuta


def soubeh_odst4(ukony):
    ukony_kopie = ukony
    odstavce4 = []
    for ukon in ukony[1:]:  # posouzeni az po prvnim prvku, ktery je vzdy Odst1
        """Vsechny nasledujici objekty tridy Odst4 se posoudi, jestli zacaly bezet uvnitr jineho. Pokud ano, posune se
        lhuta konce staveni prvniho z nich a takovy objekt se vyradi. Pokud ne, nic se nemeni a objekt neni
        vyrazen.
        """
        if isinstance(ukon, Odst4):
            odstavce4.append(ukon)
    #print('odstavce 4:', odstavce4)
    if odstavce4:
        staveni_konec = odstavce4[0]._konec_staveni
        iterace = 1
        for i in odstavce4[1:]:
            print('i', i)
            index = ukony_kopie.index(i)
            print('index', index)
            if i._ukon <= staveni_konec:  # je soubeh
                if i._konec_staveni >= staveni_konec:  # druhe staveni je delsi nez prvni
                    staveni_konec = i._konec_staveni
                    print('staveni konec ', staveni_konec)
                    ukony_kopie[index - 1]._konec_staveni = staveni_konec  # PROMITNOUT DO UKONY
                    print('ukony_kopie[index]._koenc_staveni', staveni_konec)
                else:  # druhe skoncilo v ramci prvniho
                    pass
                del ukony_kopie[index]  # DELETOVAT UKON co nastaly v ramci staveni
            elif i._ukon > staveni_konec:  # neni soubeh
                staveni_konec = i._konec_staveni
                #print('neni soubeh: ', staveni_konec)
            iterace += 1

    for ukon in ukony_kopie:
        if isinstance(ukon, Odst4):
            print(ukon._ukon, ukon._konec_staveni)
        else:
            print(ukon._ukon)
        print('-' * 35)

    return ukony_kopie

def odstavce4(ukony):
    zacatky_konce = []
    for ukon in ukony:
        if isinstance(ukon, Odst4):
            zacatky_konce.append((ukon._ukon, ukon._konec_staveni))
    return zacatky_konce

