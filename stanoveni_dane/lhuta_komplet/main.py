#!/usr/bin/env python3

from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
from funkce import uprava_ukonu_pri_soubehu, uprava_odstavcu4, vytrid_odstavce4, vytrid_ukony


def spocitej_lhutu(seznam_ukonu):
    """
    po uprave ukonu podle toho, jestli byl soubeh s odst. 4 (prioritni uprava),
    nebo s odst. 3 nebo s odst. 2 se na kazdem jedtnolivem ukonu
    spusti metoda konec_lhuty, ktera vraci dateobject s koncem lhuty
    :seznam_ukonu: soubor vsech ukonu; jde do fce srovnany dle data provedeni ukonu
    :return: subjektivni lhuta - komplet vypocet, dateobject
    """

    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0].konec_lhuty()
        seznam_ukonu[0].maximalni_delka()
    # zadani pocatecnich hodnot, od kterych se vyviji nasledny vypocet
    subjektivni_lhuta = seznam_ukonu[0].konec
    objektivni_lhuta = seznam_ukonu[0].maximalni

    # 1. proveri se existence odstavcu 4 mezi vsemi ukony
    odstavce4, seznam_ukonu = vytrid_odstavce4(vsechny_ukony=seznam_ukonu)  # odstavce4 muzou byt prazdne

    # 2. proveri se existence vice odstavcu 4 - moznost soubehu mezi nimi je treba osetrit jako prvni
    if odstavce4 and len(odstavce4) > 1:
        odstavce4 = uprava_odstavcu4(seznam_odstavcu4=odstavce4)

    # 3. roztridi ostatni ukony podle toho, jestli nastaly v dobe odstavce4 nebo ne
    if odstavce4:  # kontroluje pouze, kdyz nejake odstavce4 existuji
        ukony_soubehu, seznam_ukonu = vytrid_ukony(seznam_odstavce4=odstavce4, seznam_ukonu=seznam_ukonu)
        if ukony_soubehu:
            seznam_ukonu = uprava_ukonu_pri_soubehu(odstavce4, ukony_soubehu, seznam_ukonu, subjektivni_lhuta,
                                                objektivni_lhuta)
        else:  # kdyz neni zadny soubeh, tak se odstavce4 vrati do seznamu ukonu
            [seznam_ukonu.append(odstavec) for odstavec in odstavce4 if odstavce4]

    for ukon in seznam_ukonu[1:]:
        ukon.konec_lhuty(datum_zacatku=seznam_ukonu[0].ukon, datum_konce=subjektivni_lhuta,
                      maximalni_delka=objektivni_lhuta)
        subjektivni_lhuta = ukon.konec

    return subjektivni_lhuta




