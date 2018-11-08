slovnik = {}

def tvorba_slovniku(n):    
    for cislo in range(1, n + 1):
        slovnik[cislo] = cislo ** 2
    return slovnik

a = 4


def scitani(d):
    klice = 0
    hodnoty = 0
    for key in d:
        klice += key
    for hodnota in d.values():
        hodnoty += hodnota
    return klice, hodnoty

print(tvorba_slovniku(a))
print(scitani(slovnik))


slovnik_2 = {}
def slovnikovy_retezec(slovo):    
    for pismeno in slovo:
        slovnik_2[pismeno] = slovo.count(pismeno)
    return slovnik_2

print(slovnikovy_retezec("Noninka"))


def vypis_slovnik(d):
    for klic, hodnota in d.items():
        print("{}: {}".format(klic, hodnota))

vypis_slovnik(slovnik_2)
    


