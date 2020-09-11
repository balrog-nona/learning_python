#!/bin/python3

from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
from funkce import konec_lhuty_nove_odst4, uprava_ukonu_pri_soubehu, uprava_odstavcu4


def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0].konec_lhuty()
        seznam_ukonu[0].maximalni_delka()
    subjektivni_lhuta = seznam_ukonu[0].konec
    objektivni_lhuta = seznam_ukonu[0].maximalni

    # 1. sesbiram intervaly staveni, tj. vsechny objekty odst4
    odstavce4 = list()
    for i in seznam_ukonu[1:]:
        if isinstance(i, Odst4):
            odstavce4.append(i)
            seznam_ukonu.remove(i)  # odstraneni vsech objektu odst4

    if odstavce4 and len(odstavce4) > 1:
        odstavce4 = uprava_odstavcu4(odstavce4)

    # 2. roztridim ukony podle toho, jestli nastaly v intervalu soubehu nebo ne
    ukony_soubehu = list()
    new_list = list()
    for odstavec in odstavce4:
        for ukon in seznam_ukonu[1:]:  # iterace ukonama uz bez objektu odst4
            if odstavec.ukon <= ukon.ukon <= odstavec.konec_staveni:
                ukony_soubehu.append(ukon)
            else:
                new_list.append(ukon)

    if not ukony_soubehu:
        [new_list.append(odstavec) for odstavec in odstavce4]
    else:
        new_list = uprava_ukonu_pri_soubehu(odstavce4, ukony_soubehu, new_list, seznam_ukonu, subjektivni_lhuta,
                                        objektivni_lhuta)

    if new_list:
        for i in new_list:
            i.konec_lhuty(datum_zacatku=seznam_ukonu[0].ukon, datum_konce=subjektivni_lhuta,
                          maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = i.konec
    else:
        for i in seznam_ukonu[1:]:
            i.konec_lhuty(datum_zacatku=seznam_ukonu[0].ukon, datum_konce=subjektivni_lhuta,
                          maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = i.konec

    return subjektivni_lhuta




