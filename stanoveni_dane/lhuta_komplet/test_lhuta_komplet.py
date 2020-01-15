from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import pytest


def test_odst1():
    odst1 = Odst1(datum='1.4.2019')
    odst1._konec_lhuty()
    odst1._maximalni_delka()
    assert odst1._vrat_konec(datum=odst1._konec) == '01.04.2022'
    assert odst1._maximalni_delka == datetime.date(2029, 4, 2)
    assert odst1._vrat_konec(datum=odst1._maximalni_delka) == '02.04.2029'

    odst1 = Odst1(datum='1.4.2020')
    odst1._konec_lhuty()
    odst1._maximalni_delka()
    assert odst1._vrat_konec(datum=odst1._konec) == '03.04.2023'
    assert odst1._maximalni_delka == datetime.date(2030, 4, 1)
    assert odst1._vrat_konec(datum=odst1._maximalni_delka) == '01.04.2030'


odst1 = Odst1(datum='1.4.2020')
odst1._konec_lhuty()
odst1._maximalni_delka()


def test_odst1():
    lhuta = Lhuta148()
    assert lhuta._na_americke_datum(datum='13.6.2021') == datetime.date(2021, 6, 13)
    assert lhuta._na_ceske_datum(datum=datetime.date(2021, 11, 2)) == '02.11.2021'
    assert lhuta._prevod_data(datum=datetime.datetime(2009, 10, 23)) == datetime.date(2009, 10, 23)
    assert lhuta._kontrola_vikendu(datum=datetime.date(2020, 1, 18)) == datetime.date(2020, 1, 20)
    assert lhuta._kontrola_vikendu(datum=datetime.date(2020, 1, 17)) == datetime.date(2020, 1, 17)
    assert lhuta._kontrola_pred_zacatkem(datum_ukonu=datetime.date(2019, 7, 23),
                                         datum_zacatku=datetime.date(2019, 7, 23)) == True
    with pytest.raises(Exception):
        lhuta._kontrola_pred_zacatkem(datum_ukonu=datetime.date(2019, 7, 22), datum_zacatku=datetime.date(2019, 7, 23))
        assert 'Ukon ze dne 22.7.2019 nemuze nastat pred zapocetim behu lhuty dne 23.7.2019.' == str(error.value)

    assert lhuta._kontrola_po_konci(datum_ukonu=datetime.date(2020, 6, 13),
                                    datum_konce=datetime.date(2020, 6, 13)) == True

    with pytest.raises(Exception):
        lhuta._kontrola_po_konci(datum_ukonu=datetime.date(2020, 6, 14), datum_konce=datetime.date(2020, 6, 13))
        assert 'Ukon ze dne 14.6.2020 nemuze nastat po konci behu lhuty dne 13.6.2020.' == str(error.value)

    assert lhuta._kontrola_odst5(konec='1.4.2023',maximalni_delka='1.4.2023') == True
    assert lhuta._kontrola_odst5(konec='31.3.2023', maximalni_delka='1.4.2023') == True


def test_odst2():
    odst2 = Odst2(datum='3.4.2022')
    odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst2._vrat_konec(datum=odst2._konec) == '03.04.2024'

    odst2 = Odst2(datum='2.4.2022')
    odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst2._vrat_konec(datum=odst2._konec) == '03.04.2023'

    with pytest.raises(Exception):
        odst2 = Odst2(datum='31.3.2020')
        odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne 1.4.2020.' == str(error.value)

    with pytest.raises(Exception):
        odst2 = Odst2(datum='4.4.2023')
        odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 4.4.2023 nemuze nastat po konci behu lhuty dne 3.4.2023.' == str(error.value)


def test_odst3():
    odst3 = Odst3(datum='19.9.2022')
    odst3._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst3._vrat_konec(datum=odst3._konec) == '22.09.2025'

    extension = Odst3(datum='11.3.2025')
    extension._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst3._konec, maximalni_delka=odst1._maximalni_delka)
    assert extension._vrat_konec(datum=extension._konec) == '13.03.2028'

    extension2 = Odst3(datum='13.03.2028')
    extension2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=extension._konec, maximalni_delka=odst1._maximalni_delka)
    assert extension2._vrat_konec(datum=extension2._konec) == '01.04.2030'

    with pytest.raises(Exception):
        odst3 = Odst3(datum='31.3.2020')
        odst3._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne 1.4.2020.' == str(error.value)

    with pytest.raises(Exception):
        odst3 = Odst3(datum='4.4.2023')
        odst3._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 4.4.2023 nemuze nastat po konci behu lhuty dne 3.4.2023.' == str(error.value)


def test_odst4():
    odst4 = Odst4(zacatek_staveni='1.5.2021', konec_lhuty=odst1._konec)
    odst4.zadej_konec_staveni(konec_staveni='25.3.2022')
    odst4._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst4._vrat_konec(datum=odst4._konec) == '26.02.2024'

    extension = Odst4(zacatek_staveni='2.1.2024', konec_lhuty=odst4._konec)
    extension.zadej_konec_staveni(konec_staveni='1.7.2024')
    extension._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst4._konec, maximalni_delka=odst1._maximalni_delka)
    assert extension._vrat_konec(datum=extension._konec) == '26.08.2024'

    with pytest.raises(Exception):
        odst4 = Odst4(zacatek_staveni='31.3.2020', konec_lhuty=odst1._konec)
        odst4._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne 1.4.2020.' == str(error.value)

    with pytest.raises(Exception):
        odst4 = Odst4(zacatek_staveni='4.4.2023', konec_lhuty=odst1._konec)
        odst4._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 4.4.2023 nemuze nastat po konci behu lhuty dne 3.4.2023.' == str(error.value)

    with pytest.raises(Exception):
        odst4 = Odst4(zacatek_staveni='14.9.2022', konec_lhuty=odst1._konec)
        odst4._zacatek_staveni(konec_staveni='31.3.2020')
        odst4._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne 1.4.2020.' == str(error.value)

