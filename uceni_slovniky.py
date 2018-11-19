import pytest

slovnik = dict()
print(slovnik)

def vytvor_slovnik(n):
    slovnik = {}
    for i in range(1, n + 1):
        slovnik[i] = i ** 2        
    return slovnik
    

slov = vytvor_slovnik(5)
print(slov)
klice = slov.keys() # zbrusu novy data type
print(klice)
print(type(klice))
hodnoty = slov.values() # tady taky
print(hodnoty)


   
def test_vytvor_slovnik():
    slovnik = vytvor_slovnik(3)
    assert len(slovnik) == 3
    assert slovnik[2] == 4
    slovnik2 = vytvor_slovnik(8)
    assert len(slovnik2) == 8
    klice = list(slovnik2.keys())
    assert klice == [1, 2, 3, 4, 5, 6, 7, 8]
    hodnoty = list(slovnik2.values())
    assert hodnoty == [1, 4, 9, 16, 25, 36, 49, 64]
    
    
def scitani(d):
    klice = 0
    hodnoty = 0
    for key in d.keys():   
        klice += key
    for value in d.values():
        hodnoty += value
    return klice, hodnoty
    
    
dvojice = list(scitani(slov))    
print("Soucet klicu je {} a soucet hodnot je {}.".format(*dvojice))


def test_scitani():
    slovnik = {1:2, 2:4, 10:10}
    assert scitani(slovnik) == (13, 16)
    slovnik2 = {20:10, 30:50, 100:1000}
    assert scitani(slovnik2) == (150, 1060)
    
    
def slovnik_slov(slovo):
     slovnik = {}
     for pismeno in slovo:
        slovnik[pismeno] = slovo.count(pismeno)
     return slovnik
     
print(slovnik_slov("Alhambra"))


def test_slovnik_slov():
    slovnik = slovnik_slov("autogramiada")
    assert slovnik["a"] == 4
    assert len(slovnik) == 9
    assert slovnik["d"] == 1
    
    
def vypis_slovnik(d):
    for klic, hodnota in d.items():
        print("{}:{}".format(klic, hodnota))
        
vypis_slovnik(slov)

