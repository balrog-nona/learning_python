import lhuta
import pytest
import datetime

lhuta = lhuta.Lhuta('1.4.2020')


def test_odst1():
    assert lhuta.zacatek == datetime.date(2020, 4, 1)
    assert lhuta.konec == datetime.date(2023, 4, 1)
    assert lhuta.vrat_konec() == "01.04.2023"
    assert lhuta.maximalni_delka == datetime.date(2030, 4, 1)


def test_odst2():
    lhuta.odst2("31.3.2022")
    assert lhuta.konec == datetime.date(2023, 4, 1)
    assert lhuta.vrat_konec() == "01.04.2023"
    lhuta.odst2("1.4.2022")
    assert lhuta.konec == datetime.date(2024, 4, 1)
    assert lhuta.vrat_konec() == "01.04.2024"
    with pytest.raises(Exception) as error:
        lhuta.odst2("2.4.2024")
        assert "Ukon ze dne 2.4.2024 nemuze nastat po konci behu lhuty dne {}".format\
            (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst2("31.3.2020")
        assert "Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.".format\
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)


def test_odst3():
    lhuta.odst3("1. 4. 2024")
    assert lhuta.konec == datetime.date(2027, 4, 1)
    assert lhuta.vrat_konec() == "01.04.2027"
    lhuta.konec = datetime.date(2023, 4, 1)
    with pytest.raises(Exception) as error:
        lhuta.odst3("2.4.2023")
        assert 'Ukon ze dne 2.4.2023 nemuze nastat po konci behu lhuty dne {}.'.format\
                   (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst2("31.3.2020")
        assert "Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.".format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)


def test_odst4():
    lhuta.odst4(ode_dne='1.5.2021', do_dne='25.3.2022')
    assert lhuta.konec == datetime.date(2024, 2, 24)
    lhuta.odst4(ode_dne='2.1.2024', do_dne='1.7.2024')
    assert lhuta.konec == datetime.date(2024, 8, 24)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne="31.3.2020", do_dne=None)
        assert "Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.".format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne="25.8.2024", do_dne=None)
        assert "Ukon ze dne 25.8.2024 nemuze nastat po konci behu lhuty dne {}.".format \
                   (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne=None, do_dne="31.3.2020")
        assert "Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.".format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)


def test_odst5():
    lhuta.odst3('3.5.2023')
    lhuta.odst3('30.4.2026')
    lhuta.odst3('1.2.2029')
    assert lhuta.konec == datetime.date(2030, 4, 1)
    lhuta.odst2('1.11.2029')
    assert lhuta.konec == datetime.date(2030, 4, 1)
    lhuta.odst4(ode_dne='1.12.2029', do_dne='25.3.2030')
    assert lhuta.konec == datetime.date(2030, 4, 1)