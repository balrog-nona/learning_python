velikost_pole = 20

def over_cislo(cislo):
    if 0 <= cislo < velikost_pole:
        print("OK")
    else:
        raise ValueError("Cislo {n} neni v poli.".format(n=cislo))
        
over_cislo(8)
over_cislo(111)
over_cislo(3)
over_cislo(-96)
        

        
