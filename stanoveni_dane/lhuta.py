import datetime

class Lhuta:
    """
    Umi spocitat konec lhuty, kdyz uzivatel vi, jak pouzit § 148 a zadane ukony se nemeni.
    Kontroluje zadani ukonu pred a po lhute.
    Neumi drzet v pameti historii ukonu, prepocitat lhutu po zruseni nektereho ukonu, a kvuli tomu neumi kontrolovat
    soubeh ruznych odstavcu.
    Chybi kontrola vikendu.
    """

    def __init__(self, zacatek):
        self.zacatek = self.na_americke_datum(zacatek)
        self.konec = self.zacatek.replace(year=self.zacatek.year + 3)
        self.maximalni_delka = self.zacatek.replace(year=self.zacatek.year + 10)

    def odst2(self, datum):
        ukon = self.na_americke_datum(datum)
        if ukon < self.zacatek:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (datum, self.na_ceske_datum(self.zacatek)))
        elif ukon > self.konec:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (datum, self.na_ceske_datum(self.konec)))
        elif self.konec.replace(year=self.konec.year - 1) <= ukon <= self.konec:
            self.konec = self.konec.replace(year=self.konec.year + 1)

        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst3(self, datum):
        ukon = self.na_americke_datum(datum)
        if ukon < self.zacatek:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (datum, self.na_ceske_datum(self.zacatek)))
        elif ukon > self.konec:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (datum, self.na_ceske_datum(self.konec)))
        else:
            self.konec = self.konec.replace(year=self.konec.year + 3)

        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst4(self, ode_dne, do_dne):
        zacatek_staveni = self.na_americke_datum(ode_dne)
        konec_staveni = self.na_americke_datum(do_dne)

        if zacatek_staveni < self.zacatek:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (ode_dne, self.na_ceske_datum(self.zacatek)))
        elif zacatek_staveni > self.konec:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (ode_dne, self.na_ceske_datum(self.konec)))

        if konec_staveni < self.zacatek:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (do_dne, self.na_ceske_datum(self.zacatek)))

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



