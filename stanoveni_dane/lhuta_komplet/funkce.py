from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import types


def vytrid_odstavce4(vsechny_ukony):
    """
    fce vytridi ukony odst. 4 - vytvori z nich vlastni seznam a z puvodniho seznamu je vymaze
    puvodni seznam tak zustane plny ukonu, co nejsou odst. 4 a bude mozne tyto porovnat, aby se
    dalo zjistit, jestli je nektery v soubehu s odstavcem 4 a s jakym
    :vsechny_ukony: seznam vsech ukonu tak, jak by do kompetni fce zadan
    :return: seznam ukonu odst. 4 a seznam vsech ostatnich
    """
    odstavce4 = list()
    for ukon in vsechny_ukony[1:]:
        if isinstance(ukon, Odst4):
            odstavce4.append(ukon)
            vsechny_ukony.remove(ukon)
    return odstavce4, vsechny_ukony  # odstavce4 muzou byt prazdne


def uprava_odstavcu4(seznam_odstavcu4):
    """
    fce proveri, jestli nektere ukony odstavce4 nezacaly v ramci jineho odstavce4
    Pokud ano, pak je treba konec ukonu, ktery zacal driv, natahnout az na konec ukonu, ktery se s nim sbiha.
    Sbihajici ukon se timto zpracovanim vyradi.
    :seznam_odstavcu4: seznam ukonu, co jsou odstavce4
    :return: upravene odstavce4 - kompletni jejich seznam
    """
    nove_odstavce4 = list()
    # na zacatku je porovnavanym objektem prvni prvek odstavcu4
    porovnavany_objekt = seznam_odstavcu4[0]
    for i, odstavec4 in enumerate(seznam_odstavcu4[1:], start=1):
        # porovnavaji se prvky nasledujici po porovnavanem objektu
        if porovnavany_objekt.ukon <= odstavec4.ukon <= porovnavany_objekt.konec_staveni \
                and odstavec4.konec_staveni > porovnavany_objekt.konec_staveni:
            """varianta soubehu - odstavec4 zacal v prubehu predchoziho staveni + skoncil pozdeji
            porovnavany objekt dostane nove hodnoty pro koncec staveni - prodlouzi se
            """
            porovnavany_objekt.konec_staveni = porovnavany_objekt.konec_staveni.replace(
                year=odstavec4.konec_staveni.year,
                month=odstavec4.konec_staveni.month,
                day=odstavec4.konec_staveni.day)
            # pri posledni iteraci se do seznamu prida upraveny porovnavany objekt
            if i == len(seznam_odstavcu4[1:]): nove_odstavce4.append(porovnavany_objekt)
        elif porovnavany_objekt.ukon <= odstavec4.ukon <= porovnavany_objekt.konec_staveni \
                and odstavec4.konec_staveni <= porovnavany_objekt.konec_staveni:
            """varianta podmnoziny - odstavec4 zacal v prubehu predchoziho staveni + skoncil v jeho ramci
            porovnavany objekt neni treba menit
            """
            if i == len(seznam_odstavcu4[1:]):
                nove_odstavce4.append(porovnavany_objekt)
            else:
                continue
        else:
            """varianta bez soubehu - odstavec4 nezacal v prubehu predchoziho staveni
            """
            if i == len(seznam_odstavcu4[1:]):
                # pri posledni iteraci se do seznamu prida porovnavany objekt i autonomni odstavec4
                nove_odstavce4.extend([porovnavany_objekt, odstavec4])
            else:
                # prida se porovnavany objekt - jeho hodnoty jsou hotove
                nove_odstavce4.append(porovnavany_objekt)
                # autonomni odstavec4 je novy porovnavany objekt
                porovnavany_objekt = odstavec4
    return nove_odstavce4


def vytrid_ukony(seznam_odstavce4, seznam_ukonu):
    """
    kompletne pripravene odstavce4 se porovnaji s tim, jestli nejake ukony ze seznamu_ukonu nastaly
    v dobe staveni:
    pokud ano, vlozi se do ukony_soubehu
    pokud ne, vlozi se do finalniho seznamu new_list - tam se prirazuji uz finalni ukony ke konecnemu
    vypoctu
    :seznam_odstavce4: vytridene a upravene odstavce4 nebo prazdny seznam
    :seznam_ukonu: celkovy seznam ukonu uz bez vytridenych odstavcu4
    :return: ukony_soubehu a new_list (finalni seznam ukonu k vypoctu)
    """
    ukony_soubehu = list()
    new_list = list()
    for odstavec4 in seznam_odstavce4:  # seznam_odstavce4 muze byt prazdny - logika upravena TO DO
        for ukon in seznam_ukonu[1:]:
            # iterace od 2. prvku, protoze prvni je odst.1, uz zpracovany
            if odstavec4.ukon <= ukon.ukon <= odstavec4.konec_staveni:  # vycleneni ukonu ze soubehu
                ukony_soubehu.append(ukon)
            else:
                new_list.append(ukon)
    return ukony_soubehu, new_list  # ukony soubehu muzou byt prazdne


def konec_lhuty_nove_odst4(self, datum_zacatku, datum_konce, maximalni_delka):
    if super(Odst4, self)._kontrola_pred_zacatkem(datum_ukonu=self.ukon, datum_zacatku=datum_zacatku) and \
            super(Odst4, self)._kontrola_po_konci(datum_ukonu=self.ukon, datum_konce=datum_konce) and \
            super(Odst4, self)._kontrola_pred_zacatkem(datum_ukonu=self.konec_staveni, datum_zacatku=datum_zacatku):
        # odcitaci metoda - po konci staveni se pricte, co ze lhuty zbyvalo v dobe zacatku staveni
        # 1 den je treba pricist rucne, aby lhuta nebezela i po oba hranicni dny
        kolik_zbyvalo = (datum_konce - self.ukon) + datetime.timedelta(days=1)  # timedelta object
        self.konec = self.konec_staveni + kolik_zbyvalo  # date object
        self.konec = self.konec.replace(year=self.konec.year + 1)  # pricteni toho 1 roku za odst. 2
        self.konec = super(Odst4, self)._kontrola_vikendu(self.konec)
    if not super(Odst4, self)._kontrola_odst5(konec=self.konec, maximalni_delka=maximalni_delka):
        self.konec = maximalni_delka


# 3. roztridim jednotlive soubehy k odstavcum 4 a upravim prislusne hodnoty na objektu - TO DO!
def uprava_ukonu_pri_soubehu(odstavce4, ukony_soubehu, new_list, seznam_ukonu, subjektivni_lhuta, objektivni_lhuta):
    for i in odstavce4:
        odstavec3 = False
        soubeh = list()
        # 1. posbirat vsechny ukony soubehu k jednotlivym odstavcum 4
        for ukon in ukony_soubehu:  # porovnani
            if i.ukon <= ukon.ukon <= i.konec_staveni:
                soubeh.append(ukon)
        if not soubeh:
            new_list.append(i)
        # 2. jednotlive akce pri soubehu s ruznymi ukony
        if soubeh:
            for ukon in soubeh:
                if isinstance(ukon, Odst3):  # soubeh s odst. 3
                    odstavec3 = True
                    ukon.soubeh = True
                    ukon.ukon = ukon.ukon.replace(year=i.konec_staveni.year, month=i.konec_staveni.month,
                                                    day=i.konec_staveni.day)
                    new_list.append(ukon)
                elif isinstance(ukon, Odst2) and not odstavec3:  # soubeh s odst. 2, pokud neni pritomen odst. 3
                    for u in new_list:
                        u.konec_lhuty(datum_zacatku=seznam_ukonu[0].ukon, datum_konce=subjektivni_lhuta,
                                      maximalni_delka=objektivni_lhuta)
                        subjektivni_lhuta = u.konec
                    prozatimni_konec = subjektivni_lhuta
                    if i.ukon >= prozatimni_konec.replace(year=prozatimni_konec.year - 1):
                        i.konec_lhuty = types.MethodType(konec_lhuty_nove_odst4, i)
                        new_list.append(i)
                    else:
                        new_list.append(i)
    return new_list


