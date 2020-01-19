from main import spocitej_lhutu
from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import pytest

def test1():
    ukony = []
    ukon1 = Odst1(datum='1.4.2020')
    ukony.append(ukon1)
    assert spocitej_lhutu(ukony) == datetime.date(2023, 4, 3)

    ukon2 = Odst2(datum='14.8.2021')
    ukony.append(ukon2)
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    #print(ukony_sorted)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2023, 4, 3)


ukony = []
ukon1 = Odst1(datum='1.4.2020')
ukony.append(ukon1)
#print(datetime.date(2023, 4, 3) == spocitej_lhutu(ukony))

ukon2 = Odst2(datum='14.8.2021')
ukony.append(ukon2)
ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
print(datetime.date(2023, 4, 3) == spocitej_lhutu(ukony_sorted))

ukon3 = Odst3(datum='3.7.2022')
ukony.append(ukon3)
ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
print('4', datetime.date(2025, 7, 4) == spocitej_lhutu(ukony_sorted))
"""
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

print(ukony_sorted)
a = spocitej_lhutu(ukony_sorted)
print(a == datetime.date(2025, 7, 4))
"""
print('*' * 45)
test1()