from random import randrange

def tah(pole, cislo_indexu, symbol):
  pole = pole[:cislo_indexu] + symbol + pole[cislo_indexu + 1:]
  return pole


def tah_pocitace(pole, symbol):
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
        return tah(pole, cislo_indexu, symbol)
        break


