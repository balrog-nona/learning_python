import random

d = {"Kdo?": [], "S kym?": [], "Co delali?": [], "Jak?": [], "Kdy?": [], "Kde?": [], "Proc?": []}


for key in d: 
    zadani_klice = True   
    while zadani_klice:
        pokracovat = True
        while pokracovat:
            vstup = input(key)
            vstup = vstup.strip()
            if bool(vstup) == True:
                d[key].append(vstup)
                pokracovat = False
            else:
                print("Neplatne zadani, zkus to znovu.")
        dalsi = True
        while dalsi:             
            opakovat = input("Chces opet zadat {} Napis a/n.".format(key))
            opakovat = opakovat.lower()
            opakovat = opakovat.strip()            
            if opakovat == "n":                
                dalsi = False
                zadani_klice = False
            elif opakovat == "a":
                dalsi = False
                zadani_klice = True                
            else:
                print("Neplatne zadani, zkus to znovu a/n.")



for key in d:
    random.shuffle(d[key])

for key in d:
    slovo = random.choice(d[key])
    print(slovo, end=" ")