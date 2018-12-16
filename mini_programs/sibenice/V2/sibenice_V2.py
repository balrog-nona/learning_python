import random
import os


clear = lambda: os.system(['clear', 'cls'][os.name == 'nt'])


slovnik = ["antarctica", "denmark", "belgium", "greenland", "germany", "romania", "portugal", "lithuania", "tanzania",
           "zimbabwe", "ethiopia", "cameroon", "botswana", "swaziland", "pakistan", "kazakhstan", "mongolia", "georgia",
           "uzbekistan", "thailand", "vietnam", "indonesia", "philippines", "micronesia", "australia", "vanuatu",
           "argentina", "paraguay", "venezuela", "colombia", "guatemala", "ecuador", "honduras", "nicaragua"]


def volba_slova(seznam):
    random.shuffle(seznam)  # je to tu navic, choice by uplne stacilo
    slovo = random.choice(seznam)
    return slovo


def tvorba_pole(slovo):
    pole = "_" * len(slovo)
    return pole


def prepis_pole(pole, index, pismeno):
    pole = pole[:index] + pismeno + pole[index + 1:]
    return pole


def tah_hrace(slovo, pole, pismeno):
    if pismeno in slovo:
        pocet = slovo.count(pismeno)
        delka_slova = len(slovo)        
        for i in range(pocet):  # osetreni vice stejnych pismen
            rozdil = delka_slova - len(slovo)                
            index = slovo.index(pismeno)
            slovo = slovo[index + 1:]                
            index += rozdil                                
            pole = prepis_pole(pole, index, pismeno)
        if pole[0].isalpha():
            pole = pole.capitalize()  # velke pismeno pro staty
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


def nacti_soubor(i):
    with open('sibenice{}.txt'.format(i), encoding="utf-8") as soubor:
        obsah = soubor.read()
        return obsah


def sibenice():    
    opakovat = True
    while opakovat:
        slovo = volba_slova(slovnik)        
        pole = tvorba_pole(slovo)
        netrefeno = -1
        obrazek = None
        clear()  # vycisteni obrazovky pred hrou
        print(pole)
            
        pokracovat = True
        while pokracovat:
            zadani = False
            while not zadani:
                vstup = input("Zadej pismeno: ")
                zadani, pismeno = osetreni_vstupu(vstup)
            trefil, pole = tah_hrace(slovo, pole, pismeno)

            clear()  # vycisteni obrazovky po tahu
            print(pole)

            if trefil == 1:
                pokracovat = vyhodnot_trefu(pole)
                if not pokracovat:
                    print("Vitezis!")
            elif trefil == 0:
                netrefeno += 1
                obrazek = nacti_soubor(netrefeno)
            if obrazek:
                print(obrazek)
            if netrefeno == 9:
                print("Konec hry - jsi obesenec! \nHledane slovo: {}".format(slovo.capitalize()))
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
