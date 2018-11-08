import sibenice
import pytest


def test_tvorba_pole():
    pole = sibenice.tvorba_pole("slepice")
    assert len(pole) == 7
    pole = sibenice.tvorba_pole("norsko")
    assert len(pole) == 6
    pole = sibenice.tvorba_pole("svedsko")
    assert pole == "_______"


def test_prepis_pole():
    pole = sibenice.prepis_pole("______", 2, "d")
    assert pole[2] == "d"
    assert len(pole) == 6
    pole = sibenice.prepis_pole("___", 0, "q")
    assert pole[0] == "q"
    assert pole == "q__"

def test_tah_hrace():    
    zasah, pole = sibenice.tah_hrace("pes", "___", "s")
    assert zasah == 1
    assert pole[2] == "s"
    assert pole == "__s"
    zasah, pole = sibenice.tah_hrace("opice", "_____", "p")
    assert zasah == 1
    assert pole[1] == "p"
    assert pole == "_p___"
    zasah, pole = sibenice.tah_hrace("motyka", "______", "c")
    assert zasah == 0
    assert pole.count("c") == 0
    zasah, pole = sibenice.tah_hrace("pacific", "_______", "i")
    assert zasah == 1
    assert pole.count("i") == 2
    assert pole[3] == "i"
    assert pole[5] == "i"
    assert pole == "___i_i_"
    zasah, pole = sibenice.tah_hrace("kiribati", "________", "i")
    assert zasah == 1
    assert pole.count("i") == 3
    assert pole[1] == "i"
    assert pole[3] == "i"
    assert pole[7] == "i"
    assert len(pole) == 8
    zasah, pole = sibenice.tah_hrace("tahiti", "t__i_i", "j")
    assert zasah == 0
    assert "j" not in pole

def test_osetreni_vstupu():
    zadani, pismeno = sibenice.osetreni_vstupu("D ")
    assert zadani == True
    assert pismeno == "d"
    zadani, pismeno = sibenice.osetreni_vstupu("hu")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu(" ")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu("5")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu("! ")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu("//")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu("=")
    assert zadani == False
    assert pismeno == None
    zadani, pismeno = sibenice.osetreni_vstupu("\n")
    assert zadani == False
    assert pismeno == None


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
