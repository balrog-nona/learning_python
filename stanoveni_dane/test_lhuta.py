from lhuta import Lhuta
import pytest
import datetime


def test_odst1():
    lhuta = Lhuta(zacatek='1.4.2020')
    assert lhuta.zacatek == datetime.date(2020, 4, 1)
    assert lhuta.konec == datetime.date(2023, 4, 1)
    assert lhuta.vrat_konec() == '01.04.2023'
    assert lhuta.maximalni_delka == datetime.date(2030, 4, 1)


def test_odst2():
    lhuta = Lhuta(zacatek='1.4.2020')
    lhuta.odst2('31.3.2022')
    assert lhuta.konec == datetime.date(2023, 4, 1)
    assert lhuta.vrat_konec() == '01.04.2023'
    lhuta.odst2('1.4.2022')
    assert lhuta.konec == datetime.date(2024, 4, 1)
    assert lhuta.vrat_konec() == '01.04.2024'
    lhuta.odst2('19.9.2023')
    assert lhuta.vrat_konec() == '01.04.2025'
    with pytest.raises(Exception) as error:
        lhuta.odst2('2.4.2025')
        assert 'Ukon ze dne 2.4.2025 nemuze nastat po konci behu lhuty dne {}.'.format\
            (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst2('31.3.2020')
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.'.format\
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)


def test_odst3():
    lhuta = Lhuta(zacatek='1.4.2020')
    lhuta.odst3('23.9.2021')
    assert lhuta.konec == datetime.date(2024, 9, 24)
    assert lhuta.vrat_konec() == '24.09.2024'
    lhuta.odst3('24.9.2024')
    assert lhuta.vrat_konec() == '25.09.2027'
    with pytest.raises(Exception) as error:
        lhuta.odst3('26.9.2027')
        assert 'Ukon ze dne 26.9.2027 nemuze nastat po konci behu lhuty dne {}.'.format\
                   (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst2('31.3.2020')
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.'.format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)
    lhuta.odst3('30.4.2023')
    assert lhuta.konec == datetime.date(2026, 5, 1)


def test_odst4():
    lhuta = Lhuta(zacatek='1.4.2020')
    lhuta.odst4(ode_dne='1.5.2021', do_dne='25.3.2022')
    assert lhuta.konec == datetime.date(2024, 2, 24)
    lhuta.odst4(ode_dne='2.1.2024', do_dne='1.7.2024')
    assert lhuta.konec == datetime.date(2024, 8, 24)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne='31.3.2020', do_dne=None)
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.'.format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne='25.8.2024', do_dne=None)
        assert 'Ukon ze dne 25.8.2024 nemuze nastat po konci behu lhuty dne {}.'.format \
                   (lhuta.na_ceske_datum(lhuta.konec)) == str(error.value)
    with pytest.raises(Exception) as error:
        lhuta.odst4(ode_dne=None, do_dne='31.3.2020')
        assert 'Ukon ze dne 31.3.2020 nemuze nastat pred zapocetim behu lhuty dne {}.'.format \
                   (lhuta.na_ceske_datum(lhuta.zacatek)) == str(error.value)


def test_odst5():
    lhuta = Lhuta(zacatek='1.4.2020')
    lhuta.odst3('3.5.2022')
    lhuta.odst3('13.4.2025')
    lhuta.odst3('1.2.2028')
    assert lhuta.konec == datetime.date(2030, 4, 1)
    lhuta.odst2('1.11.2029')
    assert lhuta.konec == datetime.date(2030, 4, 1)
    lhuta.odst4(ode_dne='1.12.2029', do_dne='25.3.2030')
    assert lhuta.konec == datetime.date(2030, 4, 1)


def test_komplexni1():
    lhuta = Lhuta(zacatek='1.4.2019')
    assert lhuta.vrat_konec() == '01.04.2022'
    lhuta.odst2(datum='1.9.2019')
    assert lhuta.vrat_konec() == '01.04.2022'
    lhuta.odst3(datum='1.11.2019')
    assert lhuta.vrat_konec() == '02.11.2022'
    lhuta.odst2(datum='1.3.2021')
    assert lhuta.vrat_konec() == '02.11.2022'
    lhuta.odst4(ode_dne='1.5.2021', do_dne='1.2.2023')
    assert lhuta.vrat_konec() == '05.08.2024'
    lhuta.odst2(datum='1.4.2023')
    assert lhuta.vrat_konec() == '05.08.2024'
    lhuta.odst2(datum='1.7.2023')
    assert lhuta.vrat_konec() == '05.08.2024'
    lhuta.odst3(datum='1.9.2023')
    assert lhuta.vrat_konec() == '02.09.2026'
    lhuta.odst2(datum='1.10.2025')
    assert lhuta.vrat_konec() == '02.09.2027'
    lhuta.odst2(datum='1.2.2026')
    assert lhuta.vrat_konec() == '02.09.2027'
