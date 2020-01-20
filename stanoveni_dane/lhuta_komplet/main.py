from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime

def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
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

        # sem prijde soubeh staveni + soubeh staveni s necim dalsim

        i._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta, maximalni_delka=objektivni_lhuta)
        subjektivni_lhuta = i._konec

    return subjektivni_lhuta


# ukazat Petrovi, co to delalo, kdyz jsem mela 2x assert v jedne fci
# zeptat se na soukrome a verejne metody/atributy
"""
def soubeh_staveni(i, seznam_ukonu):
    if isinstance(i, Odst4):
        for item in seznam_ukonu[iterace:]:
            if i._ukon <= item._ukon =< i._konec_staveni:
                if isinstance(item, Odst2):
                    # co se stane
                elif isinstance(item, Odst3):  # po konci staveni, ten druhy den + 3 roky
                    item._konec_lhuty(datum_zacatku='')
                elif isinstance(item, Odst4):
                    # co se stane
            else:
                # co??
"""