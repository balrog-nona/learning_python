from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4


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
    pokud ano, vlozi se do ukony_soubehu a vyradi ze seznamu ukonu
    pokud ne - nic se nestane a ukony_soubehu muzou byt prazdne
    :seznam_odstavce4: vytridene a upravene odstavce4
    :seznam_ukonu: celkovy seznam ukonu uz bez vytridenych odstavcu4
    :return: ukony_soubehu
    """
    ukony_soubehu = list()
    for odstavec4 in seznam_odstavce4:
        for ukon in seznam_ukonu[1:]:
            # iterace od 2. prvku, protoze prvni je odst.1, uz zpracovany
            if odstavec4.ukon <= ukon.ukon <= odstavec4.konec_staveni:  # vycleneni ukonu ze soubehu
                ukony_soubehu.append(ukon)
                seznam_ukonu.remove(ukon)
    return ukony_soubehu, seznam_ukonu  # ukony soubehu muzou byt prazdne


def uprava_ukonu_pri_soubehu(odstavce4, ukony_soubehu, seznam_ukonu, subjektivni_lhuta, objektivni_lhuta):
    """
    ukony v soubehu se musi priradit konkretne k urcitemu odstavci4 - az potom lze posoudit vliv na delku lhuty
    :odstavce4: sezbirane odstavce4
    :ukony_soubehu: sezbirane ukony v soubehu
    :seznam_ukonu: ukony zadane v pripadu uz bez odstavcu4 a ukonu v soubehu
    :param subjektivni_lhuta: subjektivni lhuta v pripadu dle odst. 1
    :param objektivni_lhuta: objektivni lhuta v pripadu dle odst. 1
    :return: seznam ukonu doplneny o zpracovane ukony - osetreny vsechny soubehy
    """
    for odstavec4 in odstavce4:
        """kazda iterace je pro jednotlivy odstavec4 - vuci nemu se posuzuje soubeh
        """
        odstavec3 = False
        soubeh = list()

        # 1. posbirat vsechny ukony soubehu k aktualnimu odstavci4
        for ukon in ukony_soubehu:
            if odstavec4.ukon <= ukon.ukon <= odstavec4.konec_staveni:
                # soubeh obsahuje vsechny ukony v soubehu s aktualne porovnavanym odstavcem4
                soubeh.append(ukon)
        if not soubeh:
            # zadny ukon neni v soubehu s aktualnim odstavcem4 - prida se do celkoveho seznamu
            seznam_ukonu.append(odstavec4)

        # 2. jednotlive akce pri soubehu - varianty s ruznymi ukony
        if soubeh:
            for ukon in soubeh:
                # iteruje se vsemi ukony, ktere jsou v soubehu s aktualne porovnavanym odtavcem4
                if isinstance(ukon, Odst3):
                    """soubeh s odst. 3 - toto posouzeni ma prioritu, a to i pokud je v soubehu
                    zaroven s odstavcem2 - odstavec2 a odstavec4 jsou irelevantni
                    uprava: zmeni se, kdy odstavec3 nastal = konec staveni odstavce4 + ten je pak irelevantni
                    """
                    # kontrola na existenci odstavce3 v soubehu - prednost posouzeni
                    odstavec3 = True
                    # nastaveni atributu na odstavci3 - jiny zpusob vypoctu konce lhuty (metoda konec_lhuty)
                    ukon.soubeh = True
                    # prepsani zacatku odstavce3
                    ukon.ukon = ukon.ukon.replace(year=odstavec4.konec_staveni.year,
                                                  month=odstavec4.konec_staveni.month,
                                                    day=odstavec4.konec_staveni.day)
                    # do celkoveho vypoctu se prida jen odstavec3
                    seznam_ukonu.append(ukon)
                elif isinstance(ukon, Odst2) and not odstavec3:
                    """soubeh s odst. 2, pokud neni pritomen odst. 3
                    musi se spocitat dosavadni konec lhuty - pokud odstavec4 zacal drive nez v poslednich
                    12 mesicich pred koncem lhuty -> po ukonceni staveni se lhuta normalne prodlouzi
                    dle staveni + rok prida
                    pokud odstavec4 nezacal drive nez v poslednich 12 mesicich pred koncem lhuty 
                    -> nic se nemeni, ale odstavec2 je irelevantni
                    """
                    for u in seznam_ukonu[1:]:
                        u.konec_lhuty(datum_zacatku=seznam_ukonu[0].ukon, datum_konce=subjektivni_lhuta,
                                      maximalni_delka=objektivni_lhuta)
                        subjektivni_lhuta = u.konec
                    # prozatimni konec lhuty pro porovnani, jestli odstavec4 nastal drive nez
                    # v poslednich 12 mesicich pred koncem
                    if odstavec4.ukon >= subjektivni_lhuta.replace(year=subjektivni_lhuta.year - 1):
                        odstavec4.soubeh = True
                        # do celkoveho seznamu se prida odstavec4 s atributem na modifikaci konec_lhuty
                        seznam_ukonu.append(odstavec4)
                    else:
                        # do celkoveho seznamu se prida odstavec4 bez atributu na modifikaci konec_lhuty
                        seznam_ukonu.append(odstavec4)
    return seznam_ukonu


