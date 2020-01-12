import datetime

class Lhuta148:

    def _na_americke_datum(self, datum):  # prevod stringu na date object
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

    def _vrat_konec(self):
        return self._na_ceske_datum(self._konec)


class Odst1(Lhuta148):

    def __init__(self, datum):
        self._ukon = super()._na_americke_datum(datum)

    def _konec_lhuty(self):
        self._konec = self._ukon.replace(year=self._ukon.year + 3)  # normalne dle odst. 1; presne datum
        self._konec = super()._kontrola_vikendu(self._konec)

    def _maximalni_delka(self):
        self._maximalni_delka = self._ukon.replace(year=self._ukon.year + 10)  # dle odst. 5; presne datum
        self._maximalni_delka = super()._kontrola_vikendu(self._maximalni_delka)  # konec lhuty po pravni strance
        self._maximalni_delka = super()._na_ceske_datum(self._maximalni_delka)


class Odst2(Lhuta148):

    def __init__(self, datum):
        self._ukon = super()._na_americke_datum(datum)

    def _konec_lhuty(self):
        pass