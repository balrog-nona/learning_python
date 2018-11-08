from random import randrange

pocty = []

for i in range(1, 5):
  print("Hra hrace c. {}:".format(i))
  hod = 0
  iterace = 0
  while hod < 6:
    print("Pada... ", end=" ")
    hod = randrange(1, 7)
    print(hod)
    iterace += 1
  pocty.append(iterace)

vitez = max(pocty)
index = pocty.index(vitez) # pozor na tvar zavorek!!
  
print("Vitezem se stava hrac c. ", index + 1)
  
  



  


  




