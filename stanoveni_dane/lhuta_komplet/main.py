from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime

# 1. sesbiram intervaly staveni
odstavce4 = list()
for i in ukony:
    if isinstance(i, Odst4):
        odstavce4.append(i)

# 2. roztridim ukony podle toho, jestli nastaly v intervalu soubehu nebo ne
ukony_soubehu = list()
new_list = list()
for odstavec in odstavce4:
    for i in ukony:
        if odstavec._ukon <= i._ukon <= odstavec._konec_staveni:
            ukony_soubehu.append(i)
        else:
            new_list.append(i)

# 3. roztridim jednotlive soubehy k odstavcum 4 a upravim prislusne hodnoty na objektu
for i in odstavce4:
    odstavec3 = False
    soubeh = list()
    # 1. posbirat vsechny ukony soubehu k jednotlivym odstavcum 4
    for ukon in ukony_soubehu:  # porovnani
        if i._ukon <= ukon <= i._konec_staveni:
            soubeh.append(ukon)
    # 2. jednotlive akce pri soubehu s ruznymi ukony
    for ukon in soubeh:
        if isinstance(ukon, Odst4) and ukon._konec_staveni > i._konec_staveni:  # soubeh s odst. 4
            i._konec_staveni = ukon._konec_staveni
            new_list.append(i)
        elif isinstance(ukon, Odst3):  # soubeh s odst. 3
            odstavec3 = True
            ukon._ukon.replace(year=i._konec_staveni.year + 3)
            new_list.append(ukon)
        elif isinstance(ukon, Odst2) and not odstavec3:  # soubeh s odst. 2, pokud neni pritomen odst. 3
           # pokud staveni zacalo mene nez 12 mesicu pred koncem dosavadni lhuty a v te dobe byl i ukon podle odst. 2,
            # tak se lhuta vypocete tak, ze po pricteni staveni se pricte jeste 12 mesicu




def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0]._konec_lhuty()
        seznam_ukonu[0]._maximalni_delka()
    subjektivni_lhuta = seznam_ukonu[0]._konec
    objektivni_lhuta = seznam_ukonu[0]._maximalni

    for i in seznam_ukonu[1:]:
        i._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta, maximalni_delka=objektivni_lhuta)
        subjektivni_lhuta = i._konec

    return subjektivni_lhuta

"""
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
                    ukony_kopie[index - 1]._konec_staveni = staveni_konec
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
    ukony_staveni = []
    for ukon in ukony:
        if isinstance(ukon, Odst4):
            ukony_staveni.append(ukon)
    return ukony_staveni


def soubeh_odst3(ukony, ukony_odst4):
    indexy = []
    for ukon in ukony:
        print('soubeh 3: ', ukon)
        for i in ukony_odst4:
            konec_staveni = i._konec_staveni
            if i._ukon <= ukon._ukon <= konec_staveni:
                if isinstance(ukon, Odst3):
                    print('isinstance: ', ukon)
                    ukon._ukon = konec_staveni  # pobezi 3 roky po skonceni staveni
                    index = ukony.index(i)
                    indexy.append(index)

    for i in indexy:
        print('i: ', i)
        ukony[i].zadej_konec_staveni(konec_staveni='1.1.2100')
        print(ukony[i]._konec_staveni)

    return ukony
"""

