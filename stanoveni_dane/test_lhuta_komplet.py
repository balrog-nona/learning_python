from lhuta_komplet import Lhuta148, Odst1
import datetime
import pytest

def test_odst1():
    odst1 = Odst1(datum='1.4.2019')
    odst1._konec_lhuty()
    odst1._maximalni_delka()
    assert odst1._vrat_konec() == '01.04.2022'
    assert odst1._maximalni_delka == '02.04.2029'

    odst1 = Odst1(datum='1.4.2020')
    odst1._konec_lhuty()
    odst1._maximalni_delka()
    assert odst1._vrat_konec() == '03.04.2023'
    assert odst1._maximalni_delka == '01.04.2030'
