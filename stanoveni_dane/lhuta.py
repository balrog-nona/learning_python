import datetime

class Lhuta:
    """
    Umi spocitat konec lhuty, kdyz uzivatel vi, jak pouzit § 148 a zadane ukony se nemeni.
    Kontroluje zadani ukonu pred a po lhute.
    Neumi drzet v pameti historii ukonu, prepocitat lhutu po zruseni nektereho ukonu, a kvuli tomu neumi kontrolovat
    soubeh ruznych odstavcu.
    """

    def __init__(self, zacatek):
        self.zacatek = self.na_americke_datum(zacatek)
        self.konec = self.zacatek.replace(year=self.zacatek.year + 3)  # normalne dle odst. 1; presne datum
        self.konec = self.kontrola_vikendu(self.konec)  # konec lhuty po pravni strance
        self.maximalni_delka = self.zacatek.replace(year=self.zacatek.year + 10)  # dle odst. 5; presne datum
        self.maximalni_delka = self.kontrola_vikendu(self.maximalni_delka)  # konec lhuty po pravni strance

    def odst2(self, datum):
        ukon = self.na_americke_datum(datum)
        if self.kontrola_pred_zacatkem(datum=ukon) and self.kontrola_po_konci(datum=ukon):
            if self.konec.replace(year=self.konec.year - 1) <= ukon <= self.konec:
                # kdyz nastal v poslednich 12 mesicich, prodluz lhutu o rok
                self.konec = self.konec.replace(year=self.konec.year + 1)
                self.konec = self.kontrola_vikendu(self.konec)
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst3(self, datum):
        ukon = self.na_americke_datum(datum)
        if self.kontrola_pred_zacatkem(datum=ukon) and self.kontrola_po_konci(datum=ukon):
            # nasledujici den po ukonu + 3 roky
            # nelze jen tak zvysit cislo dne o 1, kazdy mesic ma jiny pocet dnu, hrozilo by 31.4.
            # vytvori nasledujici den prirozene podle kalendare
            druhy_den = ukon + datetime.timedelta(days=1)  # vraci datetime object
            druhy_den = self.prevod_data(druhy_den)  # prevod datetime na date object
            self.konec = druhy_den.replace(year=druhy_den.year + 3)
            self.konec = self.kontrola_vikendu(self.konec)
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst4(self, ode_dne, do_dne):
        zacatek_staveni = self.na_americke_datum(ode_dne)
        konec_staveni = self.na_americke_datum(do_dne)

        if self.kontrola_pred_zacatkem(datum=zacatek_staveni) and self.kontrola_po_konci(datum=zacatek_staveni) and \
                self.kontrola_pred_zacatkem(datum=konec_staveni):
            # odcitaci metoda - po konci staveni se pricte, co ze lhuty zbyvalo v dobe zacatku staveni
            # 1 den je treba pricist rucne, aby lhuta nebezela i po oba hranicni dny
            kolik_zbyvalo = (self.konec - zacatek_staveni) + datetime.timedelta(days=1)  # timedelta object
            self.konec = konec_staveni + kolik_zbyvalo  # date object
            self.konec = self.kontrola_vikendu(self.konec)
        if not self.odst5():
            self.konec = self.maximalni_delka

    def odst5(self):
        return self.konec <= self.maximalni_delka  # vraci True/False

    def na_americke_datum(self, datum):  # prevod stringu na date object
        den, mesic, rok = datum.split('.')
        return datetime.date(int(rok), int(mesic), int(den))

    def na_ceske_datum(self, datum):  # prevod date objectu na string v ceske forme
        datum = str(datum)
        rok, mesic, den = datum.split('-')
        return '{}.{}.{}'.format(den, mesic, rok)

    def kontrola_pred_zacatkem(self, datum):
        if datum < self.zacatek:
            raise Exception('Ukon ze dne {} nemuze nastat pred zapocetim behu lhuty dne {}.'.format
                            (self.na_ceske_datum(datum), self.na_ceske_datum(self.zacatek)))
        else:
            return True

    def kontrola_po_konci(self, datum):
        if datum > self.konec:
            raise Exception('Ukon ze dne {} nemuze nastat po konci behu lhuty dne {}.'.format
                            (self.na_ceske_datum(datum), self.na_ceske_datum(self.konec)))
        else:
            return True

    def kontrola_vikendu(self, datum):  # datum je date object; lhuta nesmi skoncit o vikendu
        if datum.isoweekday() == 7:  # nedele - lhuta konci v pondeli, tj. + 1 den
            datum += datetime.timedelta(days=1)  # vraci datetime object
            datum = self.prevod_data(datum)
        elif datum.isoweekday() == 6:  # sobota - lhuta konci v pondeli, tj. + 2 dny
            datum += datetime.timedelta(days=2)
            datum = self.prevod_data(datum)
        return datum  # vraci date object

    def prevod_data(self, datum):  # datum je datetime object; prevede datetime object na date object
        dat = datum.strftime('%d.%m.%Y')  # prevod datetime na string
        return self.na_americke_datum(dat)  # vraci date object

    def vrat_konec(self):
        return self.na_ceske_datum(self.konec)



