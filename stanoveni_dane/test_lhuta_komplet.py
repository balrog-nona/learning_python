from lhuta_komplet import Lhuta148, Odst1, Odst2
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

def test_odst2():
    odst2 = Odst2(datum='3.4.2022')
    odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst2._vrat_konec(datum=odst2._konec) == '03.04.2024'

    odst2 = Odst2(datum='2.4.2022')
    odst2._konec_lhuty(datum_zacatku=odst1._ukon, datum_konce=odst1._konec, maximalni_delka=odst1._maximalni_delka)
    assert odst2._vrat_konec(datum=odst2._konec) == '03.04.2023'

