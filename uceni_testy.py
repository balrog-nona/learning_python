import pytest


VELIKOST_POLE = 20

def over_cislo(cislo):
    if 0 <= cislo < VELIKOST_POLE:
        print('OK!')
    else:
        raise ValueError('Čislo {n} není v poli!'.format(n=cislo))
        

        
       
def test_over_cislo():      # tohle zkontroluje vzdy jen prvni moznost, pak fce konci a neprovadi se dalsi dve, proc?? 
    with pytest.raises(ValueError):
        over_cislo(55)
    with pytest.raises(ValueError):   
        over_cislo(-9)
    with pytest.raises(ValueError):
        over_cislo(12)

