from random import randrange 
import os


clear = lambda: os.system(['clear','cls'][os.name == 'nt'])

def tvorba_mapy(pocet_radku, pocet_sloupcu):
    mapa = []
    for radek in range(pocet_radku):
        radek = []
        for prvek in range(pocet_sloupcu):
            radek.append(".")
        mapa.append(radek)
    return mapa
    

def nakresli_mapu(seznam_souradnic, souradnice_ovoce, iterace, pocet_radku, pocet_sloupcu):         
    novy_tah = seznam_souradnic[-1]   
    snezene_ovoce = 0 
    if novy_tah in souradnice_ovoce: # kontrola, jestli zral            
        snezene_ovoce += 1
        souradnice_ovoce.remove(novy_tah)
    # print("snezene_ovoce = ", snezene_ovoce, "iterace: ", iterace, "souradnice ovoce1: ", souradnice_ovoce)
    if snezene_ovoce == 0 and iterace > 1:
        del seznam_souradnic[0] # zkraceni hada, kdyz nezral
    # print("seznam_souradnic z nakresli_mapu: ", seznam_souradnic)                
    if snezene_ovoce > 0 and bool(souradnice_ovoce) == False: # tvorba ovoce po sezrani ovoce
        souradnice_ovoce = tvorba_ovoce(seznam_souradnic, souradnice_ovoce, pocet_radku, pocet_sloupcu)
        # print("tvorim ovoce 1: ", souradnice_ovoce)
    if bool(souradnice_ovoce) == False: # tvorba ovoce na zacatku hry
        souradnice_ovoce = tvorba_ovoce(seznam_souradnic, souradnice_ovoce, pocet_radku, pocet_sloupcu)       
    if iterace % 30 == 0: # tvorba ovoce po 30 tazich
        souradnice_ovoce = tvorba_ovoce(seznam_souradnic, souradnice_ovoce, pocet_radku, pocet_sloupcu)
        # print("tvorim ovoce 2:", souradnice_ovoce)
    pole = tvorba_mapy(pocet_radku, pocet_sloupcu)       
    for dvojice in seznam_souradnic:
        sloupec, radek = dvojice
        pole[radek][sloupec] = "X"
    for dvojice in souradnice_ovoce:
        sloupec, radek = dvojice
        pole[radek][sloupec] = "?"    
    clear()   
    for radek in pole:
        for prvek in radek:
            print(prvek, end= "")
        print()
       

def tvorba_ovoce(seznam_souradnic, souradnice_ovoce, pocet_radku, pocet_sloupcu):
    while True:        
        radek = randrange(pocet_radku)
        sloupec = randrange(pocet_sloupcu)
        ovoce = (sloupec, radek)
        if ovoce not in seznam_souradnic and ovoce not in souradnice_ovoce:
            souradnice_ovoce.append(ovoce)
        return souradnice_ovoce


def pohyb(seznam_souradnic, souradnice_ovoce, strana, iterace, pocet_radku, pocet_sloupcu):     
    prvek = seznam_souradnic[-1]
    sloupec = prvek[0]
    radek = prvek[1]
    novy_prvek = ()

    if strana == "s":
        radek -= 1 
        if radek < 0:
            print("Hrajes mimo pole - game over.")
            return False
        else:
            novy_prvek = (sloupec, radek)
    elif strana == "j":
        radek += 1
        if radek >= pocet_radku:
            print("Hrajes mimo pole - game over.")
            return False
        else:
            novy_prvek = (sloupec, radek)
    elif strana == "v":
        sloupec += 1
        if sloupec >= pocet_sloupcu:
            print("Hrajes mimo pole - game over.")
            return False
        else:
            novy_prvek = (sloupec, radek)
    elif strana == "z":
        sloupec -= 1
        if sloupec < 0:
            print("Hrajes mimo pole - game over.")
            return False
        else:
            novy_prvek = (sloupec, radek)

    if novy_prvek in seznam_souradnic: 
        print("Hrajes na obsazene pole - game over.")
        return False
    else:
        seznam_souradnic.append(novy_prvek)
        
    # print("seznam_souradnic z fce pohyb: ", seznam_souradnic)            
    nakresli_mapu(seznam_souradnic, souradnice_ovoce, iterace, pocet_radku, pocet_sloupcu)

    
souradnice = [(0, 0), (1, 0), (2, 0)]
souradnice_ovoce = [] 
iterace = 1

while True:
    try:
        pocet_radku =  int(input("Kolik chces radku v poli? "))
        pocet_sloupcu = int(input("Kolik chces sloupcu v poli? "))
        break
    except ValueError:
        print("Zadej cislo. ")
        
nakresli_mapu(souradnice, souradnice_ovoce, iterace, pocet_radku, pocet_sloupcu)        


while True:
    zadani = False
    while zadani == False:            
        strana = input("Zadej prvni pismeno svetove strany, kam chces jet: ")
        strana = strana.lower()
        strana = strana.strip()
        if strana == "s" or strana == "j" or strana == "v" or strana == "z":            
            zadani = True
        else:
            zadani = False
    iterace += 1
    if pohyb(souradnice, souradnice_ovoce, strana, iterace, pocet_radku, pocet_sloupcu) == False:
        break
    
               
            
                     


        
