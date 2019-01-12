slovo = str(input("Zadej slovo k sifrovani: "))
heslo = str(input("Zadej heslo: "))

#protahnuti hesla na delku slova
if len(slovo) > len(heslo): 
  slice = len(slovo) // len(heslo)
  zbytek = len(slovo) % len(heslo)
  heslo *= slice
  heslo += heslo[:zbytek]
  
#zjisteni pozice noveho znaku
sifra = ""
for i in range(len(slovo)):
  index = ord(slovo[i]) + ord(heslo[i]) - 96
  if index > 122:
    index -= 26
  sifra += chr(index)

print("Vysledek: ", sifra)
