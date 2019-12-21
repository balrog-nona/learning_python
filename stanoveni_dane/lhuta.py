import datetime
import calendar

class Lhuta:

    def __init__(self, zacatek):
        self.zacatek = self.na_americke_datum(zacatek)
        self.konec = self.zacatek.replace(year=self.zacatek.year + 3)
        self.maximalni_delka = self.zacatek.replace(year=self.zacatek.year + 10)

    def odst2(self, datum):
        ukon = self.na_americke_datum(datum)
        if self.konec.replace(year=self.konec.year - 1) <= ukon <= self.konec:
            self.konec = self.konec.replace(year=self.konec.year + 1)
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst3(self, datum):
        ukon = self.na_americke_datum(datum)
        if ukon <= self.konec:
            self.konec = self.konec.replace(year=self.konec.year + 3)
        else:
            raise Exception("Ukon ze dne {} zacal az po skonceni lhuty.".format(datum))
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst4(self, ode_dne, do_dne):
        zacatek_staveni = self.na_americke_datum(ode_dne)
        konec_staveni = self.na_americke_datum(do_dne)
        kolik_zbyvalo = (self.konec - zacatek_staveni) + datetime.timedelta(days=1)
        self.konec = konec_staveni + kolik_zbyvalo
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst5(self):
        return self.konec <= self.maximalni_delka

    def na_americke_datum(self, datum):
        den, mesic, rok = datum.split('.')
        return datetime.date(int(rok), int(mesic), int(den))

    def na_ceske_datum(self, datum):
        datum = str(datum)
        rok, mesic, den = datum.split("-")
        return "{}.{}.{}".format(den, mesic, rok)

    def vrat_konec(self):
        return self.na_ceske_datum(self.konec)



