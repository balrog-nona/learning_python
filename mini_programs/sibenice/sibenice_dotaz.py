import random

slovnik = ["gruzie", "rusko", "equador", "honduras", "turecko", "denmark", "belgium"]

obrazky = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]


def volba_slova(seznam):
    random.shuffle(seznam)    
    slovo = random.choice(seznam)
    return slovo


def tvorba_pole(slovo):
    pole = "_ " * len(slovo)
    return pole


def prepis_pole(pole, index, pismeno):
    pole = pole[:index] + pismeno + pole[index + 1:]
    return pole


def tah_hrace(slovo, pole, pismeno):
    if pismeno in slovo:
        index = slovo.index(pismeno)
        pole = prepis_pole(pole, index, pismeno)
        return 1, pole
    else:
        return 0, pole


def osetreni_vstupu(vstup):
    vstup = vstup.lower().strip()
    if len(vstup) == 1 and vstup.isalpha():
        return True, vstup 
    else:
        raise ValueError("Nepovedlo se, zkus to znova.")
        return False, None


def vyhodnot_trefu(pole):    
    if "_ " not in pole:
        return False
    else:
        return True

def vyhodnot_netrefu(soubor_obrazku):
    na_tisk = soubor_obrazku[0]
    del soubor_obrazku[0]
    return na_tisk, soubor_obrazku


def sibenice():
    slovo = volba_slova(slovnik) # bere si globalni promennou
    print(slovo)
    pole = tvorba_pole(slovo)
    print(pole)    
    mimo = 0
    pokracovat = True
    while pokracovat:
        zadani = False
        while zadani == False:
            vstup = input("Zadej pismeno: ")
            zadani, pismeno = osetreni_vstupu(vstup)
        trefil, pole = tah_hrace(slovo, pole, pismeno)
        print(pole)
        if trefil == 1:
            pokracovat = vyhodnot_trefu(pole)
            if pokracovat == False:
                print("Vitezis!")
        if trefil == 0:
            dvojice = vyhodnot_netrefu(obrazky)
            obrazek = dvojice[0]
            obrazky = dvojice[1] # ta fce kolabuje na techto obrazcich, ne na tech ve volani fce. Program se podival na tuto fci globalne a nasel az tady tyto.
            print(obrazek)
            if len(obrazky) == 0:
                print("Konec hry - jsi obesenec!")
                pokracovat = False


sibenice()
        


