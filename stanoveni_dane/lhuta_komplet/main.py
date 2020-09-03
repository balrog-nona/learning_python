from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import types

def konec_lhuty_nove(self, datum_zacatku, datum_konce, maximalni_delka):
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
                for u in new_list:
                    u.konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                                  maximalni_delka=objektivni_lhuta)
                    subjektivni_lhuta = i._konec
                prozatimni_konec = subjektivni_lhuta
                print(prozatimni_konec)
                print(prozatimni_konec.replace(year=prozatimni_konec.year - 1))
                if i._ukon >= prozatimni_konec.replace(year=prozatimni_konec.year - 1):
                    i.konec_lhuty = types.MethodType(konec_lhuty_nove, i)
                    new_list.append(i)
                else:
                    new_list.append(i)
    return new_list


def spocitej_lhutu(seznam_ukonu):  # seznam ukonu jde do fce srovnany dle data provedeni ukonu
    if not isinstance(seznam_ukonu[0], Odst1):
        raise Exception('Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.')
    else:
        seznam_ukonu[0].konec_lhuty()
        seznam_ukonu[0]._maximalni_delka()
    subjektivni_lhuta = seznam_ukonu[0]._konec
    objektivni_lhuta = seznam_ukonu[0]._maximalni

    # 1. sesbiram intervaly staveni, tj. vsechny objekty odst4
    odstavce4 = list()
    for i in seznam_ukonu[1:]:
        if isinstance(i, Odst4):
            odstavce4.append(i)
            seznam_ukonu.remove(i)  # odstraneni vsech objektu odst4

    # 2. roztridim ukony podle toho, jestli nastaly v intervalu soubehu nebo ne
    ukony_soubehu = list()
    new_list = list()
    for odstavec in odstavce4:
        for ukon in seznam_ukonu[1:]:  # iterace ukonama uz bez objektu odst4
            if odstavec._ukon <= ukon._ukon <= odstavec._konec_staveni:
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
            i.konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                          maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = i._konec
    else:
        for i in seznam_ukonu[1:]:
            i.konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                          maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = i._konec

    return subjektivni_lhuta




