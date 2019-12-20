import datetime
import calendar

class Lhuta:

    def __init__(self, zacatek):
        self.zacatek = self.na_americke_datum(zacatek)
        self.konec = self.zacatek.replace(year=self.zacatek.year + 3)

    def odst2(self, datum):
        ukon = self.na_americke_datum(datum)
        if self.konec.replace(year=self.konec.year - 1) <= ukon <= self.konec:
            self.konec = self.konec.replace(year=self.konec.year + 1)

    def odst3(self, datum):
        ukon = self.na_americke_datum(datum)
        if ukon <= self.konec:
            self.konec = self.konec.replace(year=self.konec.year + 3)
        else:
            raise Exception("Ukon ze dne {} zacal az po skonceni lhuty.".format(datum))


    def na_americke_datum(self, datum):
        den, mesic, rok = datum.split('.')
        return datetime.date(int(rok), int(mesic), int(den))

    def na_ceske_datum(self, datum):
        datum = str(datum)
        rok, mesic, den = datum.split("-")
        return "{}.{}.{}".format(den, mesic, rok)

    def vrat_konec(self):
        return self.na_ceske_datum(self.konec)



