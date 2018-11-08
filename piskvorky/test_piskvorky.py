import piskvorky
import ai
import pytest


# ta prvni je z tutorialu
def test_tah_na_prazdne_pole():
    pole = ai.tah_pocitace("--------------------", "o")
    assert len(pole) == 20
    assert pole.count("o") == 1
    assert pole.count("-") == 19


def test_vyhodnot():    
    assert piskvorky.vyhodnot("-------xxx----------") == True # poz test    
    assert piskvorky.vyhodnot("--o--xx------oo-----") == False # poz test    
    assert piskvorky.vyhodnot("xoxoxoxoxoxoxoxoxoxo") == True # poz test    
    assert piskvorky.vyhodnot("xoxo----xx----oox--x") == False # poz test


def test_tah():    
    assert ai.tah("----------------K---", 4, "N") == "----N-----------K---"  # poz test  
    assert ai.tah("--------------------", 12, "C") == "------------C-------" # poz test


def test_tah_pocitace():
    symbol = "o"    
    assert ai.tah_pocitace("-xx-----------------", symbol) == "oxx-----------------" # poz test
    assert ai.tah_pocitace("oxx-----------------", symbol) == "oxxo----------------" # poz test
    assert ai.tah_pocitace("oo------------------", symbol) == "ooo-----------------" # poz test
    assert ai.tah_pocitace("------------------oo", symbol) == "-----------------ooo" # poz test
    pole = ai.tah_pocitace("-oox----------------", symbol)
    assert pole.count("o") == 3
    assert pole[:4] == "ooox"
    assert len(pole) == 20
    pole = ai.tah_pocitace("--x-x---------------", symbol)
    assert pole.count("o") == 1
    assert pole[2:5] == "xox"
    pole = ai.tah_pocitace("--------o-o---------", symbol)
    assert pole.count("o") == 3
    assert pole[8:11] == "ooo"
    
    
def test_tah_hrace():
    pole = "----------o---------"
    vstup = "-4"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Cislo uvedeno spatne, vyber 1 - 20.")
    vstup = "55"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Cislo uvedeno spatne, vyber 1 - 20.")
    vstup = "11"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Hrajes na obsazene pole, zkus to znova.")
    vstup = "7"
    assert piskvorky.tah_hrace(pole, vstup) == (6, True, "")
    vstup = "mlp"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    vstup = " " 
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    vstup = "d1"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    vstup = "@#//"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    vstup = ","
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    vstup = "a8"
    assert piskvorky.tah_hrace(pole, vstup) == (0, False, "Zadavas blbosti, zadej cislo!")
    with pytest.raises(ValueError):
        piskvorky.tah_hrace(pole, "::")
