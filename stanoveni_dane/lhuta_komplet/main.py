from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime

def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
    # chybi ochrana soubehu staveni a preruseni/prodlouzeni lhuty
    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0]._konec_lhuty()
        seznam_ukonu[0]._maximalni_delka()
    subjektivni_lhuta = seznam_ukonu[0]._konec
    objektivni_lhuta = seznam_ukonu[0]._maximalni_delka

    for i in seznam_ukonu[1:]:
        if isinstance(i, Odst4) and not i._konec_staveni:
            raise Exception('Lhutu nelze spocitat, dokud neskoncilo staveni.')

        i._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta, maximalni_delka=objektivni_lhuta)
        subjektivni_lhuta = i._konec

    return subjektivni_lhuta


