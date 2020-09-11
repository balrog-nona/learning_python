"""
Uprava vypoctu behu prekluzivni lhuty pro stanoveni dane dle § 148
danoveho radu ve zneni do 31. 12. 2020.

Trida Lhuta148 s obecnyma metodama pro pouziti ve vsech podtridach.

Definovana vlastni podtrida pro kazdy odstavec § 148 zvlast, krome odst. 5,
ktery se definovany jako jedina metoda kontrolujici maximalni delku lhuty
v rodicovske tride Lhuta148.

Podtridy dedi obecne metody prevodu mezi stringem a dateobjectem a naopak, kontrolu vikendu,
kontrolu pred zacatkem a po konci, kontrolu maximalni delky dle odst. 5
a metodu na vraceni konce.
Podtridy maji vlastni metody na vypocet behu lhuty.

Vypocet behu lhuty: je treba vytvorit tolik objektu, kolik je v pripadu relevantnich ukonu
Tyto objekty musi byt odpovidajici tridy a musi obsahovat datum sveho zacatku.
Nasledne se vsechny objekty vlozi do seznamu, a ten se musi
setridit chronologicky dle toho, kdy jednotlive ukony nastaly, tzn.
setridit vsechny objekty podle atributu ukon.
V realnem vypoctu behu lhuty musi vzdy mezi objekty existovat odst. 1
a musi nastat najdrive ze vsech ostatnich objektu. Kontrola, jestli je nejdrivejsi ukon
opravdu odst. 1 je v hlavni fci v modulu main.py
"""

import datetime

class Lhuta148:
    """
    definice obecnych metod, ktere se budou dedit v podtridach + kontrola odst. 5
    """

    @classmethod
    def _na_americke_datum(cls, datum):
        """prevod stringu na date object"""
        den, mesic, rok = datum.split('.')
        return datetime.date(int(rok), int(mesic), int(den))

    @classmethod
    def _na_ceske_datum(cls, datum):
        """prevod date objectu na string v ceske forme"""
        datum = str(datum)
        rok, mesic, den = datum.split('-')
        return '{}.{}.{}'.format(den, mesic, rok)

    def _prevod_data(self, datum):
        """
        datum je datetime object
        prevede datetime object na date object
        """
        dat = datum.strftime('%d.%m.%Y')  # prevod datetime na string
        return self._na_americke_datum(dat)  # vraci date object

    def _kontrola_vikendu(self, datum):
        """
        datum je date object
        lhuta nesmi skoncit o vikendu
        """
        if datum.isoweekday() == 7:  # nedele - lhuta konci v pondeli, tj. + 1 den
            datum += datetime.timedelta(days=1)  # vraci datetime object
            datum = self._prevod_data(datum)
        elif datum.isoweekday() == 6:  # sobota - lhuta konci v pondeli, tj. + 2 dny
            datum += datetime.timedelta(days=2)
            datum = self._prevod_data(datum)
        return datum  # vraci date object

    def _kontrola_pred_zacatkem(self, datum_ukonu, datum_zacatku):
        """
        po vytvoreni konecne fce main se tato podminka testuje jeste i ve fci,
        cili nize uvedeny kod neprobehne
        oba parametry jsou date object
        :datum_ukonu: datum provedeni ukonu, self._ukon
        :datum_zacatku: datum zacatku behu lhuty
        :return: bolean
        """
        if datum_ukonu < datum_zacatku:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (self._na_ceske_datum(datum_ukonu),
                             self._na_ceske_datum(datum_zacatku)))

        return True

    def _kontrola_po_konci(self, datum_ukonu, datum_konce):
        """oba parametry jsou date object"""
        if datum_ukonu > datum_konce:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (self._na_ceske_datum(datum_ukonu), self._na_ceske_datum(datum_konce)))
        return True

    @classmethod
    def _kontrola_odst5(cls, konec, maximalni_delka):
        """oba parametry jsou date object"""
        return konec <= maximalni_delka

    def _vrat_konec(self, datum):
        """
        datum je date object
        vraci string
        """
        return self._na_ceske_datum(datum)


class Odst1(Lhuta148):
    """
    vypocet behu lhuty podle § 148 odst. 1
    """

    def __init__(self, datum):
        """datum je string"""
        self._ukon = super()._na_americke_datum(datum=datum)
        self._konec = None  # vypocita se az v ramci metody na vypocet
        self._maximalni = None  # vypocita se az v ramci metody na vypocet

    def konec_lhuty(self):
        """
        metoda pro vypocet subjektivni lhuty
        normalne dle odst. 1; presne datum
        """
        self._konec = self._ukon.replace(year=self._ukon.year + 3)
        self._konec = super()._kontrola_vikendu(self._konec)

    def _maximalni_delka(self):
        """
        metoda pro vypocet objektivni lhuty dle odst. 5 na
        presne datum
        """
        self._maximalni = self._ukon.replace(year=self._ukon.year + 10)
        # konec lhuty po pravni strance
        self._maximalni = super()._kontrola_vikendu(self._maximalni)


class Odst2(Lhuta148):
    """
    vypocet behu lhuty s modifikaci podle odst. 2
    """

    def __init__(self, datum):
        """datum je string"""
        self._ukon = super()._na_americke_datum(datum=datum)
        self._konec = None  # vypocita se az v ramci metody na vypocet

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):
        """
        parametry jsou date object
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) \
                and super()._kontrola_po_konci(datum_ukonu=self._ukon,
                                               datum_konce=datum_konce):
            if datum_konce.replace(year=datum_konce.year - 1) <= self._ukon <= datum_konce:
                # kdyz nastal v poslednich 12 mesicich, prodluz lhutu o rok
                self._konec = datum_konce.replace(year=datum_konce.year + 1)
                self._konec = super()._kontrola_vikendu(self._konec)
            else:
                self._konec = datum_konce
        if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
            self._konec = maximalni_delka


class Odst3(Lhuta148):
    """
    vypocet behu lhuty s modifikaci podle odst. 3
    Z duvodu mechaniky vypoctu lhuty pro soubehu odst. 3 a odst. 4
    jsou definovany dve ruzne metody pro vypocet konce lhuty,
    ktere se lisi jen tim, ze v pripade soubehu se nekontroluje,
    jestli ukon podle odst. 3 nenastal po konci behu lhuty
    """

    def __init__(self, datum):
        """datum je string"""
        self._ukon = super()._na_americke_datum(datum=datum)
        self._konec = None  # vypocita se az v ramci metody na vypocet
        self.soubeh = False  # atribut pro urceni soubehu s odst. 4

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):
        """
        parametry jsou date object
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if not self.soubeh:  # vypocet pro pripad neexistence soubehu s odst. 4
            if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) \
                    and super()._kontrola_po_konci(datum_ukonu=self._ukon,
                                                   datum_konce=datum_konce):
                # nasledujici den po ukonu + 3 roky
                # nelze jen tak zvysit cislo dne o 1, kazdy mesic ma jiny pocet dnu, hrozilo by 31.4.
                # vytvori nasledujici den prirozene podle kalendare
                druhy_den = self._ukon + datetime.timedelta(days=1)  # vraci datetime object
                druhy_den = super()._prevod_data(datum=druhy_den)  # prevod datetime na date object
                self._konec = druhy_den.replace(year=druhy_den.year + 3)
                self._konec = super()._kontrola_vikendu(self._konec)
            if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
                self._konec = maximalni_delka
        else:  # vypocet pro pripad soubehu s odst. 4 - nepouziva kontrolu po konci
            if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku):
                # nasledujici den po ukonu + 3 roky
                # nelze jen tak zvysit cislo dne o 1, kazdy mesic ma jiny pocet dnu, hrozilo by 31.4.
                # vytvori nasledujici den prirozene podle kalendare
                druhy_den = self._ukon + datetime.timedelta(days=1)  # vraci datetime object
                druhy_den = super()._prevod_data(datum=druhy_den)  # prevod datetime na date object
                self._konec = druhy_den.replace(year=druhy_den.year + 3)
                self._konec = super()._kontrola_vikendu(self._konec)
            if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
                self._konec = maximalni_delka


class Odst4(Lhuta148):
    """
    vypocet behu lhuty s modifikaci podle odst. 4
    Soubehy s ostatnimi odstavci jsou reseny separatne v ramci modulu main.py a funkce.py
    """

    def __init__(self, datum):
        """
        datum je zacatek staveni - string
        konec_lhuty je aktualni konec lhuty pred zacatkem staveni
        """
        self._ukon = super()._na_americke_datum(datum=datum)
        self._konec_staveni = None  # zada se az pozdeji v ramci metody
        self._konec = None  # vypocita se az v ramci metody na vypocet

    def zadej_konec_staveni(self, konec_staveni):
        """
        nastavuje konec staveni a prevede ho na dateobject
        konec staveni se zada az touto metodou, protoze nejcasteji se vi,
        ze staveni zaclo, a ceka se na jeho konec - konec staveni se tak
        jen prida k jich existujicimu objektu
        :konec_staveni: string
        """
        self._konec_staveni = super()._na_americke_datum(datum=konec_staveni)

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):
        """
        parametry jsou date object
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) and \
                super()._kontrola_po_konci(datum_ukonu=self._ukon, datum_konce=datum_konce) and \
                super()._kontrola_pred_zacatkem(datum_ukonu=self._konec_staveni,
                                                datum_zacatku=datum_zacatku):
            # odcitaci metoda - po konci staveni se pricte, co ze lhuty zbyvalo v dobe zacatku staveni
            # 1 den je treba pricist rucne, aby lhuta nebezela i po oba hranicni dny
            kolik_zbyvalo = (datum_konce - self._ukon) + datetime.timedelta(days=1)  # timedelta object
            self._konec = self._konec_staveni + kolik_zbyvalo  # date object
            self._konec = super()._kontrola_vikendu(self._konec)
        if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
            self._konec = maximalni_delka
