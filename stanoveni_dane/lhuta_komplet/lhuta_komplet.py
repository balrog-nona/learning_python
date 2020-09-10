import datetime


class Lhuta148:

    def _na_americke_datum(self, datum):  # prevod stringu na date object
        if datum:
            den, mesic, rok = datum.split('.')
            return datetime.date(int(rok), int(mesic), int(den))

    def _na_ceske_datum(self, datum):  # prevod date objectu na string v ceske forme
        datum = str(datum)
        rok, mesic, den = datum.split('-')
        return '{}.{}.{}'.format(den, mesic, rok)

    def _prevod_data(self, datum):  # datum je datetime object; prevede datetime object na date object
        dat = datum.strftime('%d.%m.%Y')  # prevod datetime na string
        return self._na_americke_datum(dat)  # vraci date object

    def _kontrola_vikendu(self, datum):  # datum je date object; lhuta nesmi skoncit o vikendu
        if datum.isoweekday() == 7:  # nedele - lhuta konci v pondeli, tj. + 1 den
            datum += datetime.timedelta(days=1)  # vraci datetime object
            datum = self._prevod_data(datum)
        elif datum.isoweekday() == 6:  # sobota - lhuta konci v pondeli, tj. + 2 dny
            datum += datetime.timedelta(days=2)
            datum = self._prevod_data(datum)
        return datum  # vraci date object

    def _kontrola_pred_zacatkem(self, datum_ukonu, datum_zacatku):  # oba parametry jsou date object
        """
        po vytvoreni konecne fce main se tato podminka testuje jeste i ve fci, cili nize uvedeny kod neprobehne
        :datum_ukonu: datum provedeni ukonu, self._ukon
        :datum_zacatku: datum zacatku behu lhuty
        :return: bolean
        """
        if datum_ukonu < datum_zacatku:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (self._na_ceske_datum(datum_ukonu), self._na_ceske_datum(datum_zacatku)))
        else:
            return True

    def _kontrola_po_konci(self, datum_ukonu, datum_konce):  # oba parametry jsou date object
        if datum_ukonu > datum_konce:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (self._na_ceske_datum(datum_ukonu), self._na_ceske_datum(datum_konce)))
        else:
            return True

    def _kontrola_odst5(self, konec, maximalni_delka): # oba parametry jsou date object
        return konec <= maximalni_delka

    def _vrat_konec(self, datum):  # datum je date object
        return self._na_ceske_datum(datum)  # vraci string


class Odst1(Lhuta148):

    def __init__(self, datum):  # datum je string
        self._ukon = super()._na_americke_datum(datum)

    def konec_lhuty(self):  # metoda pro vypocet subjektivni lhuty
        self._konec = self._ukon.replace(year=self._ukon.year + 3)  # normalne dle odst. 1; presne datum
        self._konec = super()._kontrola_vikendu(self._konec)

    def _maximalni_delka(self):  # metoda pro vypocet objektivni lhuty
        self._maximalni = self._ukon.replace(year=self._ukon.year + 10)  # dle odst. 5; presne datum
        self._maximalni = super()._kontrola_vikendu(self._maximalni)  # konec lhuty po pravni strance


class Odst2(Lhuta148):

    def __init__(self, datum):  # datum je string
        self._ukon = super()._na_americke_datum(datum)

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):  # parametry jsou date object
        """
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) and \
                super()._kontrola_po_konci(datum_ukonu=self._ukon, datum_konce=datum_konce):
            if datum_konce.replace(year=datum_konce.year - 1) <= self._ukon <= datum_konce:
                # kdyz nastal v poslednich 12 mesicich, prodluz lhutu o rok
                self._konec = datum_konce.replace(year=datum_konce.year + 1)
                self._konec = super()._kontrola_vikendu(self._konec)
            else:
                self._konec = datum_konce
        if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
            self._konec = maximalni_delka


class Odst3(Lhuta148):

    def __init__(self, datum):  # datum je string
        self._ukon = super()._na_americke_datum(datum)
        self.soubeh = False  # atribut pro urceni soubehu s odst. 4

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):  # parametry jsou date object
        """
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if not self.soubeh:  # vypocet pro pripad neexistence soubehu s odst. 4
            if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) and \
                    super()._kontrola_po_konci(datum_ukonu=self._ukon, datum_konce=datum_konce):
                # nasledujici den po ukonu + 3 roky
                # nelze jen tak zvysit cislo dne o 1, kazdy mesic ma jiny pocet dnu, hrozilo by 31.4.
                # vytvori nasledujici den prirozene podle kalendare
                druhy_den = self._ukon + datetime.timedelta(days=1)  # vraci datetime object
                druhy_den = super()._prevod_data(datum=druhy_den)  # prevod datetime na date object
                self._konec = druhy_den.replace(year=druhy_den.year + 3)
                self._konec = super()._kontrola_vikendu(self._konec)
            if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
                self._konec = maximalni_delka
        else:  # vypocet pro pripad soubehu s odst. 4 - nutne odstranit kontrolu po konci
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

class Odst4(Lhuta148):  # datum je string

    def __init__(self, datum):  # zacatek_staveni je string
        # datum je zacatek staveni
        # konec_lhuty je aktualni konec lhuty pred zacatkem staveni
        self._ukon = super()._na_americke_datum(datum)
        self._konec_staveni = None

    def zadej_konec_staveni(self, konec_staveni):  # konec staveni je string
        self._konec_staveni = super()._na_americke_datum(konec_staveni)

    def konec_lhuty(self, datum_zacatku, datum_konce, maximalni_delka):  # parametry jsou date object
        """
        :datum_zacatku: 1. den zacatku behu lhuty
        :datum_konce: prozatimni den konce subjektivni lhuty
        :maximalni_delka: objektivni lhuta
        :return: date object
        """
        if super()._kontrola_pred_zacatkem(datum_ukonu=self._ukon, datum_zacatku=datum_zacatku) and \
                super()._kontrola_po_konci(datum_ukonu=self._ukon, datum_konce=datum_konce) and \
                super()._kontrola_pred_zacatkem(datum_ukonu=self._konec_staveni, datum_zacatku=datum_zacatku):
            # odcitaci metoda - po konci staveni se pricte, co ze lhuty zbyvalo v dobe zacatku staveni
            # 1 den je treba pricist rucne, aby lhuta nebezela i po oba hranicni dny
            kolik_zbyvalo = (datum_konce - self._ukon) + datetime.timedelta(days=1)  # timedelta object
            self._konec = self._konec_staveni + kolik_zbyvalo  # date object
            self._konec = super()._kontrola_vikendu(self._konec)
        if not super()._kontrola_odst5(konec=self._konec, maximalni_delka=maximalni_delka):
            self._konec = maximalni_delka
