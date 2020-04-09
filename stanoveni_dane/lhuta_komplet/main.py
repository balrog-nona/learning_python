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

    for ukon in seznam_ukonu[1:]:
        print('velky for cyklus:', ukon)
        if isinstance(ukon, Odst4) and not ukon._konec_staveni:
            raise Exception('Lhutu nelze spocitat, dokud neskoncilo staveni.')

        if isinstance(ukon, Odst4):  # je treba prozkoumat nasledujici prvky seznamu
            print('isinstance ', ukon)
            print(ukon in seznam_ukonu)
            odstavce4 = []
            index_ukonu = seznam_ukonu.index(ukon)
            print('index ukonu:', index_ukonu)
            for item in seznam_ukonu[index_ukonu + 1:]:
                print('ve for cyklu')
                if isinstance(item, Odst4):  # nutno posbirat vsechny odst4 pro zkoumani soubehu
                    print('mala isinstance: ', item)
                    odstavce4.append(item)
                    print('odstavce4: ', odstavce4)

            if odstavce4:  # kontrola soubehu prvku tridy Odst4
                """Vsechny nasledujici objekty tridy Odst4 se posoudi, jestli bezi uvnitr jineho. Pokud ano, posune se
                lhuta konce staveni prvniho z nich a takovy objekt se vzradi. Pokud ne, nic se nemeni a objekt neni
                vyrazen.
                """
                print('v if odstavce4')
                for i in odstavce4:
                    if i._ukon <= ukon._konec_staveni: # ukon je prvni prvek tridy Odst4 v seznam_ukonu
                        if i._konec_staveni >= ukon._konec_staveni:  # druhe staveni je delsi nez prvni
                            ukon._konec_staveni = i._konec_staveni
                        else:  # druhe skoncilo v ramci prvniho
                            pass
                    seznam_ukonu.remove(i)  # seznam_ukonu upraven, sbihajici objekty Odst4 odstraneny

            ukon._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                              maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = ukon._konec

        else:  # pro objekty,co nejsou instance Odst4 neni treba kontrolovat dalsi prvky seznamu
            ukon._konec_lhuty(datum_zacatku=seznam_ukonu[0]._ukon, datum_konce=subjektivni_lhuta,
                              maximalni_delka=objektivni_lhuta)
            subjektivni_lhuta = ukon._konec


    return subjektivni_lhuta


