abeceda = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

vstup = input("Zadej rimske cislo: ")
vstup = vstup.upper()
vstup = vstup.strip()

slovo = []
pokracovat = True

"""
vstup se da osetrit i pomoci bloku try - except. Try by bylo po pristupu do hodnoty po pouziti klice, except by bylo KeyError.
"""
if vstup:
    for pismeno in vstup:  
        if pismeno in abeceda:        
            slovo.append(pismeno)
        else:
            print("Tve rimske cislo obsahuje nezname znaky.")
            pokracovat = False
            break
else:
    print("Neplatne zadani.")
    pokracovat = False

    
def index_nejvetsiho(slovo, abeceda):    
    nejvetsi_cislo = 0
    identifikace_pismena = None
    for pismeno in slovo:
        if abeceda[pismeno] > nejvetsi_cislo:
            nejvetsi_cislo = abeceda[pismeno]
            identifikace_pismena = pismeno
    index = slovo.index(identifikace_pismena)
    if index == 0:
        index_nejvetsiho = index            
    elif index == 1:
        key_0 = slovo[0]
        key_1 = slovo[1]
        if abeceda[key_0] >= abeceda[key_1]:
            index_nejvetsiho = 0
        else:
            index_nejvetsiho = 1
    elif index > 1:
            index_nejvetsiho = index            
    return index_nejvetsiho

# print(index_nejvetsiho(slovo, abeceda))



def arab_cislo(slovo, abeceda): # hleda cislo k pripocteni
    cislo = 0
    index = index_nejvetsiho(slovo, abeceda)    
    if index == 0:
        key = slovo[0]        
        cislo += abeceda[key]
        return cislo, index        
    elif index == 1: # budu odecitat doleva
        key_1 = slovo[1]
        cislo += abeceda[key_1]
        key_0 = slovo[0]
        cislo -= abeceda[key_0]        
        return cislo, index
    else:
        return cislo, index


# print(arab_cislo(slovo, abeceda))


cislo_komplet = 0
if pokracovat == True:
    while True:
        cislo, index = arab_cislo(slovo, abeceda)
        if index <= 1:
            cislo_komplet += cislo
            del slovo[:index + 1]
            if len(slovo) == 0:
                print(cislo_komplet)
                break
            else:
                pass
        elif index > 1:
            print("Rimske cislo zadano v neplatnem formatu.")
            break

