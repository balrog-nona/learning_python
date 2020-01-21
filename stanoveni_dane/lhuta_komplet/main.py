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

    poradi_prvku = 1
    for ukon in seznam_ukonu[1:]:
        if isinstance(ukon, Odst4) and not ukon._konec_staveni:
            raise Exception('Lhutu nelze spocitat, dokud neskoncilo staveni.')

        if isinstance(ukon, Odst4):  # je treba prozkoumat nasledujici prvky seznamu
            for item in seznam_ukonu[poradi_prvku:]:
                odstavce2 = []
                odstavce3 = []
                odstavce4 = []
                if isinstance(item, Odst4):  # nutno posbirat vsechny odst4 pro zkoumani soubehu
                    odstavce4.append(item)
                if ukon._ukon <= item._ukon <= ukon._konec_staveni:  # jiny ukon nastal v dobe staveni
                    if isinstance(item, Odst2):
                        odstavce2.append(item)
                    elif isinstance(item, Odst3):
                        odstavce3.append(item)

                if odstavce4:  # zjisteni teto lhuty ma prioritu - je vychozi pro vypocet dle dalsich odstavcu
                    # prodlouzeni lhuty, jestli je tam soubeh, a to i vicekrat
                if odstavce3 or (odstavce3 and odstavce2):
                    # prodlouzeni lhuty
                elif odstavce2:
                    # prodlouzeni lhuty
                else:  # zadny ukon nenastal v dobe staveni
                    ukon._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                                      maximalni_delka=objektivni_lhuta)
                    subjektivni_lhuta = ukon._konec
        else:  # pro objekty,co nejsou instance Odst4 neni treba kontrolovat dalsi prvky seznamu
            ukon._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                              maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = ukon._konec

        poradi_prvku += 1

    return subjektivni_lhuta


