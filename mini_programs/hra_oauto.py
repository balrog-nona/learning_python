import random

auta = [False, False, True]
random.shuffle(auta)
guess = random.choice(auta)
"""
nesedi ta uprava aut
"""
auta.remove(False)
index_hadani = auta.index(guess)
print(auta, index_hadani)

vyhra_pri_zmene = 0
vyhra_pri_zachovani = 0

for i in range(1000000):
    guess2 = guess  # nezmeni volbu
    if guess2:
        vyhra_pri_zachovani += 1

for i in range(1000000):
    if index_hadani == 0:
        guess2 = auta[1]
    elif index_hadani == 1:
        guess2 = auta[0]
    if guess2:
        vyhra_pri_zmene += 1

print("vyhra pri zachovani: ", vyhra_pri_zachovani)
print("vyhra pri zmene: ",vyhra_pri_zmene)

