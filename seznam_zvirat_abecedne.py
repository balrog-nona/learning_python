zvirata = ["pes", "kocka", "andulka", "kralik", "had"]


def podle_abecedy(list):
  hodnoty = []
  vysledny_seznam = []
  for i in range(len(list)):
    hodnota = ord(list[i][1])
    hodnoty.append((hodnota, list[i]))
  hodnoty.sort()
  for hodnota in hodnoty:
    vysledny_seznam.append(hodnota[1])
  return vysledny_seznam


print(podle_abecedy(zvirata))
