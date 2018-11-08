import ai
from random import randrange

def vyhodnot(pole):
  if "xxx" in pole:
    print("x - vitezi")
    return True
  elif "ooo" in pole:
    print("o - vitezi")
    return True
  elif "-" not in pole:
    print("! - plichta")
    return True
  else:
    return False


def tah_hrace(pole, pozice):  
    try:
      if int(pozice) < 1 or int(pozice) > 20:        
        return 0, False, "Cislo uvedeno spatne, vyber 1 - 20."
      elif pole[int(pozice) - 1] != "-":        
        return 0, False, "Hrajes na obsazene pole, zkus to znova."
      else:
        cislo_indexu = int(pozice) - 1        
        return cislo_indexu, True, ""       
    except ValueError: 
      return 0, False, "Zadavas blbosti, zadej cislo!"

    
def piskvorky1d():
  pole = "--------------------" # je jich 20
  print(pole)
  while True:
    zadani = False
    while zadani == False:
        vstup = input("Zadej cislo 1 - 20, kam chces hrat. ")
        cislo_indexu, zadani, hlaska = tah_hrace(pole, vstup)
        if len(hlaska) > 1:
            print(hlaska)
    pole = ai.tah(pole, cislo_indexu, "x")
    pole = ai.tah_pocitace(pole, "o")
    print(pole)
    if vyhodnot(pole) == True: #call fce v podmince
      break




  
  



  


  




