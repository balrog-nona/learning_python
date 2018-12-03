n = int(input("Zadej cislo: "))

faktorial = 1
for cislo in range(1, n + 1): 
    faktorial *= cislo

print("Faktorial cisla je: ", faktorial) 

# prvocislo
prvocislo = 0
for cislo in range(2, n): 
    if n % cislo == 0:
        prvocislo += 1

if prvocislo >= 1:
    print("Cislo neni prvocislo.")
else:
    print("Cislo je prvocislo.")


# fibonacci
lst = [1, 1]
if n > len(lst):
    for i in range(n):
        prvek = lst[len(lst) - 1] + lst[len(lst) - 2]  # to jsem jeste neznala zaporne indexy
        lst.append(prvek)
        if len(lst) == n:
            break

print(lst)


# verze fibonacciho z netu, kde se nic netvori a neni to narocne na pamet:
x, y = 0, 1
for i in range(n):
    print(x)
    x, y = y, x + y
