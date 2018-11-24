from functools import partial

print("hello world")

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

r = partial(tah(pole))
