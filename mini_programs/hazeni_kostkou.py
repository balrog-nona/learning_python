from random import randrange

hrac = 0
nejvetsi = 0

for i in range(4):
  print("Hra hrace c. {}:".format(i + 1))
  hod = 0
  iterace = 0
  while hod < 6:
    print("Pada... ", end=" ")
    hod = randrange(1, 7)
    print(hod)
    iterace += 1
  if iterace > nejvetsi:
    nejvetsi = iterace
    hrac = i + 1
  
print("Vitezem se stava hrac c. ", hrac)
  
  



  


  




