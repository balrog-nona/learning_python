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


def tah(pole, cislo_indexu, symbol):
  pole = pole[:cislo_indexu] + symbol + pole[cislo_indexu + 1:]
  return pole


def tah_hrace(pole):
  while True:
    pozice = input("Na kterou pozici chces hrat? Vyber 1 - 20. ")
    try:
      if int(pozice) < 1 or int(pozice) > 20:
        print("Cislo uvedeno spatne, vyber 1 - 20.")
      elif pole[int(pozice) - 1] != "-":
        print("Hrajes na obsazene pole, zkus to znova.")
      else:
        cislo_indexu = int(pozice) - 1
        return tah(pole, cislo_indexu, "x")
        break
    except ValueError:
      print("Zadavas blbosti, zadej cislo!")
      
    
def tah_pocitace(pole):
  while True:
    if "-xx" in pole:
      pole = pole.replace("-xx", "oxx")
      return pole
      break
    elif "xx-" in pole:
      pole = pole.replace("xx-", "xxo")
      return pole
      break
    elif "x-x" in pole:
      pole = pole.replace("x-x", "xox")
      return pole
      break
    elif "oo-" in pole:
      pole = pole.replace("oo-", "ooo")
      return pole
      break
    elif "-oo" in pole:
      pole = pole.replace("-oo", "ooo")
      return pole
      break
    elif "o-o" in pole:
      pole = pole.replace("o-o", "ooo")
      return pole
      break
    else:
      pozice = randrange(1, 21)
      if pole[pozice - 1] == "-":
        cislo_indexu = pozice - 1
        return tah(pole, cislo_indexu, "o")
        break


def piskvorky1d():
  pole = "--------------------" # je jich 20
  print(pole)
  while True:
    pole = tah_hrace(pole)
    pole = tah_pocitace(pole)
    print(pole)
    if vyhodnot(pole) == True: #call fce v podmince
      break


piskvorky1d()

  
  



  


  




