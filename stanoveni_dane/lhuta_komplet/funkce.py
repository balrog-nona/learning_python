#!/bin/python3

from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import types

def konec_lhuty_nove_odst4(self, datum_zacatku, datum_konce, maximalni_delka):
    if super(Odst4, self)._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) and \
            super(Odst4, self)._kontrola_po_konci(datum_ukonu=self._ukon, datum_konce=datum_konce) and \
            super(Odst4, self)._kontrola_pred_zacatkem(datum_ukonu=self._konec_staveni, datum_zacatku=datum_zacatku):
        # odcitaci metoda - po konci staveni se pricte, co ze lhuty zbyvalo v dobe zacatku staveni
        # 1 den je treba pricist rucne, aby lhuta nebezela i po oba hranicni dny
        kolik_zbyvalo = (datum_konce - self._ukon) + datetime.timedelta(days=1)  # timedelta object
        self._konec = self._konec_staveni + kolik_zbyvalo  # date object
        self._konec = self._konec.replace(year=self._konec.year + 1)  # pricteni toho 1 roku za odst. 2
        self._konec = super(Odst4, self)._kontrola_vikendu(self._konec)
    if not super(Odst4, self)._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
        self._konec = maximalni_delka


# 3. roztridim jednotlive soubehy k odstavcum 4 a upravim prislusne hodnoty na objektu
def uprava_ukonu_pri_soubehu(odstavce4, ukony_soubehu, new_list, seznam_ukonu, subjektivni_lhuta, objektivni_lhuta):
    for i in odstavce4:
        odstavec3 = False
        soubeh = list()
        # 1. posbirat vsechny ukony soubehu k jednotlivym odstavcum 4
        for ukon in ukony_soubehu:  # porovnani
            if i._ukon <= ukon._ukon <= i._konec_staveni:
                soubeh.append(ukon)
        if not soubeh:
            new_list.append(i)
        # 2. jednotlive akce pri soubehu s ruznymi ukony
        if soubeh:
            for ukon in soubeh:
                if isinstance(ukon, Odst3):  # soubeh s odst. 3
                    odstavec3 = True
                    ukon.soubeh = True
                    ukon._ukon = ukon._ukon.replace(year=i._konec_staveni.year, month=i._konec_staveni.month,
                                                    day=i._konec_staveni.day)
                    new_list.append(ukon)
                elif isinstance(ukon, Odst2) and not odstavec3:  # soubeh s odst. 2, pokud neni pritomen odst. 3
                    for u in new_list:
                        u.konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                                      maximalni_delka=objektivni_lhuta)
                        subjektivni_lhuta = u._konec
                    prozatimni_konec = subjektivni_lhuta
                    if i._ukon >= prozatimni_konec.replace(year=prozatimni_konec.year - 1):
                        i.konec_lhuty = types.MethodType(konec_lhuty_nove_odst4, i)
                        new_list.append(i)
                    else:
                        new_list.append(i)
    return new_list


def uprava_odstavcu4(seznam_odstavcu):
    nove_odstavce = list()
    porovnavany_objekt = seznam_odstavcu[0]
    delka = len(seznam_odstavcu[1:])
    iterace = 0
    for odstavec in seznam_odstavcu[1:]:
        iterace += 1
        if odstavec._ukon >= porovnavany_objekt._ukon and odstavec._ukon <= porovnavany_objekt._konec_staveni \
                and odstavec._konec_staveni > porovnavany_objekt._konec_staveni:
            porovnavany_objekt._konec_staveni = porovnavany_objekt._konec_staveni.replace(
                year=odstavec._konec_staveni.year,
                month=odstavec._konec_staveni.month,
                day=odstavec._konec_staveni.day)
            if iterace == delka:
                nove_odstavce.append(porovnavany_objekt)
        else:
            if iterace == delka:
                nove_odstavce.extend([porovnavany_objekt, odstavec])
            else:
                nove_odstavce.append(porovnavany_objekt)
            porovnavany_objekt = odstavec
    return nove_odstavce