import os


clear = lambda: os.system(['clear','cls'][os.name == 'nt']) # konzultovat na srazu

pole = []
for radek in range(10):
    radek = []
    for prvek in range(10):
        radek.append("-")
    pole.append(radek)
        
    
def tisk_pole(pole):
    clear()
    i = 0
    print(" 0123456789")
    for radek in pole:
        print(i, end= "")
        for prvek in radek:
            print(prvek, end= "")
        print()
        i += 1


def hledej_plichtu(pole):
    pocet_mista = 0
    for cislo_radku in range(10):
        for cislo_prvku in range(10):            
            if pole[cislo_radku][cislo_prvku] == "-":
                pocet_mista += 1
    if pocet_mista == 0:
        return True
        
        
def hledej_vyhru(pole, symbol): # vzdy hodnoti cele pole komplet, nereaguje jen na novy tah
    for cislo_radku in range(10):
        for cislo_prvku in range(10):
            if pole[cislo_radku][cislo_prvku] == symbol: 
                if vedle_sebe(pole, cislo_radku, cislo_prvku, symbol) == True:
                    return True
                elif diagonala(pole, cislo_radku, cislo_prvku, symbol) == True:
                    return True
                elif diagonala_opacne(pole, cislo_radku, cislo_prvku, symbol) == True:
                    return True
                elif sloupec(pole, cislo_radku, cislo_prvku, symbol) == True:
                    return True            
                   

def vedle_sebe(pole, cislo_radku, cislo_prvku, symbol):
    for i in range(5):
        if cislo_prvku + i == 10 or pole[cislo_radku][cislo_prvku + i] != symbol:
            return False
    return True
    
    
def diagonala(pole, cislo_radku, cislo_prvku, symbol):
    for i in range(5):
        if cislo_radku + i == 10 or cislo_prvku + i == 10 or pole[cislo_radku + i][cislo_prvku + i] != symbol:
            return False 
    return True


def diagonala_opacne(pole, cislo_radku, cislo_prvku, symbol):
    for i in range(5):
        if cislo_radku + i == 10 or cislo_prvku - i < 0 or pole[cislo_radku + i][cislo_prvku - i] != symbol:
            return False 
    return True


def sloupec(pole, cislo_radku, cislo_prvku, symbol):
    for i in range(5):
        if cislo_radku + i == 10 or pole[cislo_radku + i][cislo_prvku] != symbol:
            return False
    return True
    
    
def tah_hrace_X_radek(pole):
    print("Na rade je hrac s krizky.")
    while True:
        x = input("Zadej cislo radku, kam chces hrat: (0-9) ")
        try: 
            if int(x) < 0 or int(x) > 9:
                print("Cislo uvedeno mimo pole, vyber 0-9.")
            else:
                cislo_x = int(x)
                return cislo_x                
                break
        except ValueError:
            print("Zadavas blbosti, zadej cislo!")


def tah_hrace_X_sloupec(pole):
    while True:
        y = input("Zadej cislo radku, kam chces hrat: (0-9) ")
        try: 
            if int(y) < 0 or int(y) > 9:
                print("Cislo uvedeno mimo pole, vyber 0-9.")
            else:
                cislo_y = int(y)
                return cislo_y                
                break
        except ValueError:
            print("Zadavas blbosti, zadej cislo!")
            

def tah_X():
    cislo_x = tah_hrace_X_radek(pole)
    cislo_y = tah_hrace_X_sloupec(pole)
    if pole[cislo_x][cislo_y] == "O":
        print("Zahral jsi na obsazene pole, konec hry - prohrals.")
        return False
    else:
        pole[cislo_x][cislo_y] = "X" 
        return pole
        
        
def tah_hrace_O_radek(pole):
    print("Na rade je hrac s kolecky.")
    while True:
        x = input("Zadej cislo radku, kam chces hrat: (0-9) ")
        try: 
            if int(x) < 0 or int(x) > 9:
                print("Cislo uvedeno mimo pole, vyber 0-9.")
            else:
                cislo_x = int(x)
                return cislo_x                
                break
        except ValueError:
            print("Zadavas blbosti, zadej cislo!")


def tah_hrace_O_sloupec(pole):
    while True:
        y = input("Zadej cislo radku, kam chces hrat: (0-9) ")
        try: 
            if int(y) < 0 or int(y) > 9:
                print("Cislo uvedeno mimo pole, vyber 0-9.")
            else:
                cislo_y = int(y)
                return cislo_y                
                break
        except ValueError:
            print("Zadavas blbosti, zadej cislo!")
            
            
def tah_O():
    cislo_x = tah_hrace_O_radek(pole)
    cislo_y = tah_hrace_O_sloupec(pole)
    if pole[cislo_x][cislo_y] == "X":
        print("Zahral jsi na obsazene pole, konec hry - prohrals.")
        return False
    else:
        pole[cislo_x][cislo_y] = "O" 
        return pole
        
        
def piskvorky_2d():
    tisk_pole(pole)
    while True:
        if tah_X() == False:
            break
        tisk_pole(pole)
        if hledej_vyhru(pole, "X") == True:
            print("X vyhrava!")
            break
        if hledej_plichtu(pole) == True:
            print("Plichta - nikdo nevyhral.")
            break
        if tah_O() == False:
            break
        tisk_pole(pole)
        if hledej_vyhru(pole, "O") == True:
            print("O vyhrava!")
            break
        if hledej_plichtu(pole) == True:
            print("Plichta - nikdo nevyhral.")
            break
        
            
piskvorky_2d()
