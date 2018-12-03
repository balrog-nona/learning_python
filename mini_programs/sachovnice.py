sachovnice = [] # moje reseni

for index in range(8):
  radek = []
  if index == 0 or index % 2 == 0:
    radek.append("█ " * 4)
  else:
    radek.append(" █" * 4)
  sachovnice.append(radek)
  
for radek in sachovnice:
  for prvek in radek:
    print(prvek, end= "")
  print()

print("O" * 20)

for i in range(8):
    for j in range(8):
        if i + j == 0 or (i + j) % 2 == 0:
            print("O", end= "")
        else:
            print("I", end= "")
    print()
