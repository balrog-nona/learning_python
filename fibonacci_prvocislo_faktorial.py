n = int(input("Zadej cislo: "))

faktorial = 1
for cislo in range(1, n + 1): 
    faktorial *= cislo

print("Faktorial cisla je: ", faktorial) 

#prvocislo
prvocislo = 0
for cislo in range(2, n): 
    if n % cislo == 0:
        prvocislo += 1

if prvocislo >= 1:
    print("Cislo neni prvocislo.")
else:
    print("Cislo je prvocislo.")


#fibonacci
list = [1, 1]
if n > len(list):
    for i in range(n):
        prvek = list[len(list) - 1] + list[len(list) - 2]
        list.append(prvek)
        if len(list) == n:
            break

print(list)
    
 

    
