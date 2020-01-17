from main import spocitej_lhutu
from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import pytest

def test1():  # prestalo fungovat pozadani odst4
    ukony = []
    ukon1 = Odst1(datum='1.4.2020')
    ukony.append(ukon1)
    ukon2 = Odst2(datum='14.8.2021')
    ukony.append(ukon2)
    ukon3 = Odst3(datum='3.7.2022')
    ukony.append(ukon3)
    ukon4 = Odst4(datum='14.10.2023')
    ukony.append(ukon4)
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)

    with pytest.raises(Exception) as error:
        spocitej_lhutu(ukony_sorted)
    assert 'Lhutu nelze spocitat, dokud neskoncilo staveni.' == str(error.value)

    ukon4.zadej_konec_staveni(konec_staveni='3.6.2024')
    a = spocitej_lhutu(ukony_sorted)
    assert a == datetime.date(2026, 2, 23)


ukony = []
ukon1 = Odst1(datum='1.4.2020')
ukony.append(ukon1)
ukon2 = Odst2(datum='14.8.2021')
ukony.append(ukon2)
ukon3 = Odst3(datum='3.7.2022')
ukony.append(ukon3)
ukon4 = Odst4(datum='14.10.2023')
ukony.append(ukon4)
ukon4.zadej_konec_staveni(konec_staveni='3.6.2024')
ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
for i in ukony_sorted:
    print(i._ukon)
print('*' * 45)

ukony_sorted[0]._konec_lhuty()
ukony_sorted[0]._maximalni_delka()
print(ukony_sorted[0]._konec)
print(ukony_sorted[0]._maximalni_delka)
