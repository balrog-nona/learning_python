from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import pytest


def test_lhuta148():
    lhuta = Lhuta148()
    assert lhuta._na_americke_datum(datum='13.6.2021') == datetime.date(2021, 6, 13)
    assert lhuta._na_ceske_datum(datum=datetime.date(2021, 11, 2)) == '02.11.2021'
    assert lhuta._prevod_data(datum=datetime.datetime(2009, 10, 23)) == datetime.date(2009, 10, 23)
    assert lhuta._kontrola_vikendu(datum=datetime.date(2020, 1, 18)) == datetime.date(2020, 1, 20)
    assert lhuta._kontrola_vikendu(datum=datetime.date(2020, 1, 17)) == datetime.date(2020, 1, 17)
    assert lhuta._kontrola_pred_zacatkem(datum_ukonu=datetime.date(2019, 7, 23),
                                         datum_zacatku=datetime.date(2019, 7, 23)) == True
    with pytest.raises(Exception, match='Ukon ze dne 22.07.2019 nemuze nastat pred zapocetim behu lhuty dne 23.07.2019.'):
        lhuta._kontrola_pred_zacatkem(datum_ukonu=datetime.date(2019, 7, 22), datum_zacatku=datetime.date(2019, 7, 23))

    assert lhuta._kontrola_po_konci(datum_ukonu=datetime.date(2020, 6, 13),
                                    datum_konce=datetime.date(2020, 6, 13)) == True

    with pytest.raises(Exception, match='Ukon ze dne 14.06.2020 nemuze nastat po konci behu lhuty dne 13.06.2020.'):
        lhuta._kontrola_po_konci(datum_ukonu=datetime.date(2020, 6, 14), datum_konce=datetime.date(2020, 6, 13))

    assert lhuta._kontrola_odst5(konec=datetime.date(2019, 4, 1), maximalni_delka=datetime.date(2019, 4, 1)) == True
    assert lhuta._kontrola_odst5(konec=datetime.date(2019, 3, 31), maximalni_delka=datetime.date(2019, 4, 1)) == True
    assert lhuta._kontrola_odst5(konec=datetime.date(2019, 4, 2), maximalni_delka=datetime.date(2019, 4, 1)) == False
    assert lhuta._vrat_konec(datum=datetime.date(2021, 8, 30)) == '30.08.2021'


def test_odst1():
    odst1 = Odst1(datum='1.4.2019')
    odst1.konec_lhuty()
    odst1.maximalni_delka()
    assert odst1._vrat_konec(datum=odst1.konec) == '01.04.2022'
    assert odst1.maximalni == datetime.date(2029, 4, 2)
    assert odst1._vrat_konec(datum=odst1.maximalni) == '02.04.2029'

    odst1 = Odst1(datum='1.4.2020')
    odst1.konec_lhuty()
    odst1.maximalni_delka()
    assert odst1._vrat_konec(datum=odst1.konec) == '03.04.2023'
    assert odst1.maximalni == datetime.date(2030, 4, 1)
    assert odst1._vrat_konec(datum=odst1.maximalni) == '01.04.2030'


def test_odst2():
    odst1 = Odst1(datum='1.4.2020')
    odst1.konec_lhuty()
    odst1.maximalni_delka()

    odst2 = Odst2(datum='3.4.2022')
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2._vrat_konec(datum=odst2.konec) == '03.04.2024'

    odst2 = Odst2(datum='2.4.2022')
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2._vrat_konec(datum=odst2.konec) == '03.04.2023'

    with pytest.raises(Exception, match='Ukon ze dne 31.03.2020 nemuze nastat pred zapocetim behu lhuty dne 01.04.2020.'):
        odst2 = Odst2(datum='31.3.2020')
        odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)

    with pytest.raises(Exception, match='Ukon ze dne 04.04.2023 nemuze nastat po konci behu lhuty dne 03.04.2023.'):
        odst2 = Odst2(datum='4.4.2023')
        odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)


def test_odst3():
    odst1 = Odst1(datum='1.4.2020')
    odst1.konec_lhuty()
    odst1.maximalni_delka()

    odst3 = Odst3(datum='19.9.2022')
    odst3.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst3._vrat_konec(datum=odst3.konec) == '22.09.2025'

    extension = Odst3(datum='11.3.2025')
    extension.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst3.konec, maximalni_delka=odst1.maximalni)
    assert extension._vrat_konec(datum=extension.konec) == '13.03.2028'

    extension2 = Odst3(datum='13.03.2028')
    extension2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=extension.konec, maximalni_delka=odst1.maximalni)
    assert extension2._vrat_konec(datum=extension2.konec) == '01.04.2030'

    with pytest.raises(Exception, match='Ukon ze dne 31.03.2020 nemuze nastat pred zapocetim behu lhuty dne 01.04.2020.'):
        odst3 = Odst3(datum='31.3.2020')
        odst3.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)

    with pytest.raises(Exception, match='Ukon ze dne 04.04.2023 nemuze nastat po konci behu lhuty dne 03.04.2023.'):
        odst3 = Odst3(datum='4.4.2023')
        odst3.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)


def test_odst4():
    odst1 = Odst1(datum='1.4.2020')
    odst1.konec_lhuty()
    odst1.maximalni_delka()

    odst4 = Odst4(datum='1.5.2021')
    odst4.zadej_konec_staveni(konec_staveni='25.3.2022')
    odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst4._vrat_konec(datum=odst4.konec) == '26.02.2024'

    extension = Odst4(datum='2.1.2024')
    extension.zadej_konec_staveni(konec_staveni='1.7.2024')
    extension.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst4.konec, maximalni_delka=odst1.maximalni)
    assert extension._vrat_konec(datum=extension.konec) == '26.08.2024'

    with pytest.raises(Exception, match='Ukon ze dne 31.03.2020 nemuze nastat pred zapocetim behu lhuty dne 01.04.2020.'):
        odst4 = Odst4(datum='31.3.2020')
        odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)

    with pytest.raises(Exception, match='Ukon ze dne 04.04.2023 nemuze nastat po konci behu lhuty dne 03.04.2023.'):
        odst4 = Odst4(datum='4.4.2023')
        odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)

    with pytest.raises(Exception, match='Ukon ze dne 31.03.2020 nemuze nastat pred zapocetim behu lhuty dne 01.04.2020.'):
        odst4 = Odst4(datum='14.9.2022')
        odst4.zadej_konec_staveni(konec_staveni='31.3.2020')
        odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)


def test_kompletni1():
    odst1 = Odst1(datum='1.4.2020')  # podano DAP
    odst1.konec_lhuty()
    odst1.maximalni_delka()
    assert odst1.konec == datetime.date(2023, 4, 3)
    assert odst1.maximalni == datetime.date(2030, 4, 1)

    odst2 = Odst2(datum='1.7.2020')  # podano DODAP
    odst2.konec_lhuty(datum_zacatku=odst1.ukon,datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2023, 4, 3)

    odst2 = Odst2(datum='1.9.2020')  # DOPLVY
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2023, 4, 3)

    odst2 = Odst2(datum='13.12.2020')  # rozhodnuti o odvolani
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2023, 4, 3)

    odst2 = Odst2(datum='1.8.2022')  # DODAP
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2024, 4, 3)

    odst3 = Odst3(datum='5.9.2022')  # DK
    odst3.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst3.konec == datetime.date(2025, 9, 8)

    odst2 = Odst2(datum='17.2.2023')  # DOPLVY
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst3.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2025, 9, 8)

    odst2 = Odst2(datum='10.10.2023')  # rozhodnuti o odvolani
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst3.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2025, 9, 8)  # 8.9.2025

    odst4 = Odst4(datum='10.11.2023')  # soud
    odst4.zadej_konec_staveni(konec_staveni='19.11.2024')
    odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst2.konec, maximalni_delka=odst1.maximalni)
    assert odst4.konec == datetime.date(2026, 9, 21)


def test_kompetni2():
    odst1 = Odst1(datum='1.4.2020')  # podano DAP
    odst1.konec_lhuty()
    odst1.maximalni_delka()
    assert odst1.konec == datetime.date(2023, 4, 3)
    assert odst1.maximalni == datetime.date(2030, 4, 1)

    odst3 = Odst3(datum='8.10.2022')  # DK
    odst3.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst1.konec, maximalni_delka=odst1.maximalni)
    assert odst3.konec == datetime.date(2025, 10, 9)

    odst2 = Odst2(datum='4.7.2023')  # DOPLVY
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst3.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2025, 10, 9)
    konec = odst2.konec

    odst2 = Odst2(datum='1.3.2024')  # R o odvolani
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2025, 10, 9)
    assert odst2.konec == konec

    odst4 = Odst4(datum='1.4.2024')  # soud
    odst4.zadej_konec_staveni(konec_staveni='19.1.2025')
    odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=konec, maximalni_delka=odst1.maximalni)
    assert odst4.konec == datetime.date(2026, 7, 30)

    odst2 = Odst2(datum='22.5.2025')  # R o odvolani
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst4.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2026, 7, 30)
    konec = odst2.konec

    odst4 = Odst4(datum='3.6.2025')  # soud
    odst4.zadej_konec_staveni(konec_staveni='18.2.2027')
    odst4.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=konec, maximalni_delka=odst1.maximalni)
    assert odst4.konec == datetime.date(2028, 4, 17)

    odst2 = Odst2(datum='17.4.2027')  # R o odvolani
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=odst4.konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2029, 4, 17)
    konec = odst2.konec

    with pytest.raises(Exception) as error:
        odst2 = Odst2(datum='18.5.2029')  # DODAP
        odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=konec, maximalni_delka=odst1.maximalni)
    assert 'Ukon ze dne 18.05.2029 nemuze nastat po konci behu lhuty dne 17.04.2029.' == str(error.value)

    odst2 = Odst2(datum='10.6.2028')  # DODAP
    odst2.konec_lhuty(datum_zacatku=odst1.ukon, datum_konce=konec, maximalni_delka=odst1.maximalni)
    assert odst2.konec == datetime.date(2030, 4, 1)

