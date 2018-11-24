import pytest

abeceda = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]

vstup = input("Zadej rimske cislo: ")
vstup = vstup.upper()
vstup = vstup.strip()

slovo = []
pokracovat = True

if vstup:
    for pismeno in vstup:
        for prvek in abeceda:  
            if pismeno in prvek:        
                slovo.append(pismeno)
    if len(slovo) < len(vstup):
        print("Tve rimske cislo obsahuje nezname znaky.")
        pokracovat = False        
else:
    print("Neplatne zadani.")
    pokracovat = False

# print(slovo)
    
def index_nejvetsiho(slovo, abeceda):    
    nejvetsi_cislo = 0    
    for pismeno in slovo:
        for prvek in abeceda:
            if pismeno in prvek and prvek[1] > nejvetsi_cislo:
                nejvetsi_cislo = prvek[1]
                identifikace_pismena = pismeno
    index = slovo.index(identifikace_pismena)
    if index == 0:
        index_nejvetsiho = index            
    elif index == 1:
        znak_0 = slovo[0]
        znak_1 = slovo[1]
        for prvek in abeceda:
            if znak_0 in prvek:
                cislo_0 = prvek[1]
            if znak_1 in prvek:
                cislo_1 = prvek[1]
        if cislo_0 >= cislo_1:
            index_nejvetsiho = 0
        else:
            index_nejvetsiho = 1
    elif index > 1:
            index_nejvetsiho = index            
    return index_nejvetsiho

# print(index_nejvetsiho(slovo, abeceda))



def arab_cislo(slovo, abeceda): # hleda cislo k pripocteni
    cislo = 0
    index = index_nejvetsiho(slovo, abeceda)    
    if index == 0:
        znak = slovo[0]
        for prvek in abeceda:
            if znak in prvek:        
                cislo += prvek[1]
                return cislo, index        
    elif index == 1: # budu odecitat doleva
        znak_1 = slovo[1]
        for prvek in abeceda:
            if znak_1 in prvek:        
                cislo += prvek[1]        
        znak_0 = slovo[0]
        for prvek in abeceda:
            if znak_0 in prvek:        
                cislo -= prvek[1]                
        return cislo, index
    else:
        return cislo, index


# print(arab_cislo(slovo, abeceda))


cislo_komplet = 0
if pokracovat:
    while True:
        cislo, index = arab_cislo(slovo, abeceda)
        if index <= 1:
            cislo_komplet += cislo
            del slovo[:index + 1]
            if len(slovo) == 0:
                print(cislo_komplet)
                break
            else:
                pass
        elif index > 1:
            print("Rimske cislo zadano v neplatnem formatu.")
            break


def test_index_nejvetsiho():
    assert index_nejvetsiho(["I", "M"], abeceda) == 1
    assert index_nejvetsiho(["X", "X", "V"], abeceda) == 0
    assert index_nejvetsiho(["I", "I", "X"], abeceda) == 2

def test_arab_cislo():
    assert arab_cislo(["I", "M"], abeceda) == (1999, 1)
    assert arab_cislo(["X", "X", "V"], abeceda) == (10, 0)
    assert arab_cislo(["I", "I", "X"], abeceda) == (0, 2)


