def formatovani(string):
  if string[:6].isdigit() and string[6] == "/" and string[7:].isdigit():
    return True
  else:
    return False


def delitelnost(string):
  prvni_cast = string[:6]
  druha_cast = string[7:]
  spojene = prvni_cast + druha_cast
  rodne_cislo = int(spojene)
  if rodne_cislo % 11 == 0:
    return True
  else:
    return False


def datum_narozeni(string):
  prvni_cast = string[:6]
  den_string = string[4:6]
  den = int(den_string)
  mesic_string = string[2:4]
  mesic = int(mesic_string)
  if 51 < mesic < 62:
    mesic -= 50
  elif 21 < mesic < 32:
    mesic -= 20
  elif 71 < mesic < 82:
    mesic -= 70
  rok_string = string[:2]
  rok = int(rok_string)
  if rok <= 17:
    rok += 2000
  else:
    rok += 1900
  return den, mesic, rok


def pohlavi(string):
  pohlavi_string = string[2:4]
  pohlavi = int(pohlavi_string)
  if 51 < pohlavi < 62 or 71 < pohlavi < 82:
    return "zena"
  else:
    return "muz"
  

vstup = input("Zadej svoje rodne cislo: ")
zadani_formatu = formatovani(vstup)
urceni_delitelnosti = delitelnost(vstup)
datum = datum_narozeni(vstup)
urceni_pohlavi = pohlavi(vstup)

print("Ze jsi zadala sve rodne cislo spravne je {}".format(zadani_formatu))
print("Je tvoje rodne cislo delitelne 11? {}". format(urceni_delitelnosti))
print("Tve datum na rozeni je: {}".format(datum))
print("Tve pohlavi je {}.".format(urceni_pohlavi))
