from main import spocitej_lhutu
from lhuta_komplet import Lhuta148, Odst1, Odst2, Odst3, Odst4
import datetime
import pytest


# test na odst. 1
def test1():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukony.extend([ukon1, ukon2])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2023, 4, 3)


# test na odst. 2
def test2():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon2a = Odst2(datum='14.12.2022')
    ukony.extend([ukon1,ukon2,ukon2a])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2024, 4, 3)


# test na odst. 3
def test3():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon2a = Odst2(datum='14.12.2022')
    ukon3 = Odst3(datum='1.2.2024')
    ukony.extend([ukon1, ukon2, ukon2a, ukon3])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2027, 2, 2)


# test na odst. 4 samotny
def test4():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon2a = Odst2(datum='14.12.2022')
    ukon3 = Odst3(datum='1.2.2024')
    ukon4 = Odst4(datum='15.9.2026')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2027')
    ukony.extend([ukon1, ukon2, ukon2a, ukon3, ukon4])

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2027, 12, 23)


# test maximalni delky lhuty
def test6():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon3 = Odst3(datum='1.3.2023')
    ukon3a = Odst3(datum='1.2.2026')
    ukon3b = Odst3(datum='3.1.2029')
    ukony.extend([ukon1, ukon3, ukon3a, ukon3b])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2030, 4, 1)


# test ukonu pred zacatkem behu lhuty
def test7():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon3 = Odst3(datum='1.3.2023')
    ukon3a = Odst3(datum='1.2.2020')
    ukony.extend([ukon1, ukon3, ukon3a])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)

    with pytest.raises(Exception) as error:
        spocitej_lhutu(ukony_sorted)
    assert 'Prvnim ukonem musi byt zahajeni behu lhuty dle § 148 odst.1.' == str(error.value)


# test na ukon az po skonceni behu lhuty
def test8():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon2a = Odst2(datum='14.12.2022')
    ukon3 = Odst3(datum='4.4.2024')
    ukony.extend([ukon1, ukon2, ukon2a, ukon3])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    with pytest.raises(Exception) as error:
        spocitej_lhutu(ukony_sorted)
    assert 'Ukon ze dne 04.04.2024 nemuze nastat po konci behu lhuty dne 03.04.2024.' == str(error.value)


# testovani soubehu odst.4 s dalsima udalostma
# soubeh s odst. 2 bez vlivu na delku lhuty
def test9():
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon4 = Odst4(datum='15.3.2022')
    ukon2 = Odst2(datum='12.1.2023')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2023')
    ukony.extend([ukon1, ukon2, ukon4])
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2024, 8, 23)

    
"""    
def test10():  # soubeh s odst. 2 s vlivem na delku lhuty
    ukony = []
    ukon1 = Odst1(datum='1.4.2020')
    ukony.append(ukon1)
    ukon2 = Odst2(datum='14.8.2021')
    ukony.append(ukon2)
    ukon4 = Odst4(datum='15.10.2022')
    ukon2a = Odst2(datum='12.1.2023')
    ukony.append(ukon2a)
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2023')
    ukony.append(ukon4)

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2025, 1, 22)
"""
"""
def test11():  # soubeh s odst. 3
    ukony = list
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon3 = Odst3(datum='1.2.2023')
    ukon4 = Odst4(datum='1.2.2023')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2024')
    ukony.extend([ukon1, ukon2, ukon3, ukon4])

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2027, 8, 5)
    
"""
"""
def test12():  # soubeh s odst. 3 i odst. 2
    ukony = []
    ukon1 = Odst1(datum='1.4.2020')
    ukony.append(ukon1)
    ukon2 = Odst2(datum='14.8.2021')
    ukony.append(ukon2)
    ukon3 = Odst3(datum='1.2.2023')
    ukony.append(ukon3)
    ukon4 = Odst4(datum='1.2.2023')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2024')
    ukony.append(ukon4)
    odst2a = Odst2(datum='11.7.2023')
    ukony.append(odst2a)

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2027, 8, 5)
"""
"""   
def test13():  # soubeh s odst. 4
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon4 = Odst4(datum='1.2.2023')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2024')
    ukon4a = Odst4(datum='12.10.2023')
    ukon4a.zadej_konec_staveni(konec_staveni='30.8.2024')
    ukon4b = Odst4(datum='11.9.2024')
    ukon4b.zadej_konec_staveni(konec_staveni='1.5.2025')
    ukony.extend([ukon1, ukon2, ukon4, ukon4a, ukon4b])

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2025, 6, 23)
    

def test14():  # soubeh s odst.4 i odst. 3
    ukony = list()
    ukon1 = Odst1(datum='1.4.2020')
    ukon2 = Odst2(datum='14.8.2021')
    ukon4 = Odst4(datum='1.2.2023')
    ukon4.zadej_konec_staveni(konec_staveni='4.8.2024')
    ukon4a = Odst4(datum='12.10.2023')
    ukon4a.zadej_konec_staveni(konec_staveni='30.8.2024')
    odst3 = Odst3(datum='15.8.2024')
    ukony.extend([ukon1, ukon2, ukon4, ukon4a, odst3])

    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert spocitej_lhutu(ukony_sorted) == datetime.date(2027, 8, 31)
"""

"""
def test_ukazat():
    ukony = []
    ukon1 = Odst1(datum='1.4.2020')
    ukony.append(ukon1)
    assert datetime.date(2023, 4, 3) == spocitej_lhutu(ukony)

    ukon2 = Odst2(datum='14.8.2021')
    ukony.append(ukon2)
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert datetime.date(2023, 4, 3) == spocitej_lhutu(ukony_sorted) tady vyvolava chybu

    ukon3 = Odst3(datum='3.7.2022')
    ukony.append(ukon3)
    ukony_sorted = sorted(ukony, key=lambda i: i._ukon)
    assert datetime.date(2025, 7, 4) == spocitej_lhutu(ukony_sorted)

Nemuzu mit metodu a atribut stejneho jmena! Na objektu odst1 je v druhem assertu uz nastavany atribut maximalni_delka
a proto se nevola metoda, ale vyvola se ten atribut - proto mi pise, ze datetime.date is not callable

Normalni je mit ve fci 1x assert - 1 vec, kterou testuju ma vlastni fci. Zacnu s testy pro jednotlivosti a pak nasledne
v kazde nove testovaci fci pridam neco, co chci otestovat a testuju az tento konecny stav, neni treba testovat i mezi-
kroky, protoze ty uz jsou testovane samostatnyma fcema.  
"""


