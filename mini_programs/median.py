seznam = []
print("Zadavej cisla a nakonec stiskni jen ENTER pro ukonceni zadavani.")

while True:
  cislo = input("Zadej cislo: ")
  if cislo == "":
    break
  cislo = int(cislo)
  seznam.append(cislo)
  
index = int(len(seznam) / 2)
seznam_2 = sorted(seznam)

for i in seznam:
  median = i - seznam_2[index]
  print(i, " se od medianu odlisuje o ", median)
  




