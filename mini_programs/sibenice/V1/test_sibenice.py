import sibenice
import pytest


def test_tvorba_pole():
    assert sibenice.tvorba_pole("slepice") == "_______"  # lepsi takove vypsani, bo je to bohatsi
    assert sibenice.tvorba_pole("norsko") == "______"
    assert sibenice.tvorba_pole("svedsko") == "_______"


def test_prepis_pole():
    pole = sibenice.prepis_pole("______", 2, "d")
    assert pole[2] == "d"
    assert len(pole) == 6
    assert sibenice.prepis_pole("___", 0, "q") == "q__"


def test_tah_hrace():  # lepsi assert sibenice.tah_hrace("pes", "___", "s") == (1, "__s") - zjednoduseni prace  
    assert sibenice.tah_hrace("pes", "___", "s") == (1, "__s")
    assert sibenice.tah_hrace("opice", "_____", "p") == (1, "_p___")
    assert sibenice.tah_hrace("motyka", "______", "c") == (0, "______")
    assert sibenice.tah_hrace("pacific", "_______", "i") == (1, "___i_i_")
    assert sibenice.tah_hrace("kiribati", "________", "i") == (1, "_i_i___i")
    assert sibenice.tah_hrace("tahiti", "t__i_i", "j") == (0, "t__i_i")


def test_osetreni_vstupu():
     assert sibenice.osetreni_vstupu("D ") == (True, "d")
     assert sibenice.osetreni_vstupu("hu") == (False, None)
     assert sibenice.osetreni_vstupu(" ") == (False, None)
     assert sibenice.osetreni_vstupu("5") == (False, None)
     assert sibenice.osetreni_vstupu("! ") == (False, None)
     assert sibenice.osetreni_vstupu("//") == (False, None)
     assert sibenice.osetreni_vstupu("=") == (False, None)
     assert sibenice.osetreni_vstupu("\n") == (False, None)


def test_vyhodnot_trefu():
    assert sibenice.vyhodnot_trefu("___") == True
    assert sibenice.vyhodnot_trefu("kocka") == False
    assert sibenice.vyhodnot_trefu("__k") == True
    assert sibenice.vyhodnot_trefu("p_s") == True


def test_vyhodnot_netrefu():
    obrazek, seznam = sibenice.vyhodnot_netrefu([100, 101, 102, 103])
    assert obrazek == 100
    assert 100 not in seznam
    assert len(seznam) == 3
    assert seznam[0] == 101       
