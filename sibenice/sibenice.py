import random
import pictures
import os


clear = lambda: os.system(['clear','cls'][os.name == 'nt'])


slovnik = ["antarctica", "denmark", "belgium", "greenland", "germany", "romania", "portugal", "lithuania", "tanzania", "zimbabwe", "ethiopia", "cameroon", "botswana", "swaziland", "pakistan", "kazakhstan", "mongolia", "georgia", "uzbekistan", "thailand", "vietnam", "indonesia", "philippines", "micronesia", "australia", "vanuatu", "argentina", "paraguay", "venezuela", "colombia", "guatemala", "ecuador", "honduras", "nicaragua"]


def volba_slova(seznam):
    random.shuffle(seznam) # je to tu navic, choice by uplne stacilo   
    slovo = random.choice(seznam)
    return slovo


def tvorba_pole(slovo):
    pole = "_" * len(slovo)
    return pole


def prepis_pole(pole, index, pismeno):
    pole = pole[:index] + pismeno + pole[index + 1:]
    return pole


def tah_hrace(slovo, pole, pismeno): # dala by se pridat feature, ze by prvni pismeno bylo capital, jako normalne nazev statu...
    if pismeno in slovo:
        pocet = slovo.count(pismeno)
        delka_slova = len(slovo)        
        for i in range(pocet): # osetreni vice stejnych pismen
            rozdil = delka_slova - len(slovo)                
            index = slovo.index(pismeno)
            slovo = slovo[index + 1:]                
            index += rozdil                                
            pole = prepis_pole(pole, index, pismeno)                
        return 1, pole                
    else:
        return 0, pole


def osetreni_vstupu(vstup):
    vstup = vstup.lower().strip()
    if len(vstup) == 1 and vstup.isalpha():
        return True, vstup 
    else:
        print("Neplatne zadani, zkus to znova.")
        return False, None


def vyhodnot_trefu(pole):    
    if "_" not in pole:
        return False
    else:
        return True


def vyhodnot_netrefu(soubor_obrazku):
    na_tisk = soubor_obrazku[0]
    del soubor_obrazku[0]
    return na_tisk, soubor_obrazku


def sibenice():    
    opakovat = True
    while opakovat:
        obrazky = pictures.pics[:]
        obrazek = None
        slovo = volba_slova(slovnik)        
        pole = tvorba_pole(slovo)
        clear() # vycisteni obrazovky pred hrou
        print(pole)
            
        pokracovat = True
        while pokracovat:
            zadani = False
            while zadani == False:
                vstup = input("Zadej pismeno: ")
                zadani, pismeno = osetreni_vstupu(vstup)
            trefil, pole = tah_hrace(slovo, pole, pismeno)
            clear() # vycisteni obrazovky po tahu
            print(pole)
            
            if trefil == 1:
                pokracovat = vyhodnot_trefu(pole)
                if pokracovat == False:
                    print("Vitezis!")
            elif trefil == 0:
                obrazek, obrazky = vyhodnot_netrefu(obrazky)
            if bool(obrazek) == True:                
                print(obrazek)
            if len(obrazky) == 0:
                print("Konec hry - jsi obesenec!")
                print("Hledane slovo: {}".format(slovo))
                pokracovat = False
                            
        while True:            
            znova = input("Chces hrat znova? a/n ")
            znova = znova.lower().strip()
            if znova == "a":
                clear()
                opakovat = True
                break
            elif znova == "n":
                print("Program konci.")
                opakovat = False
                break
            else:
                print("Neplatne zadani!")
            




        


