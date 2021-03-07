import random

def nezmeni_volbu(vyhra=0):
    auta = [False, False, True]
    random.shuffle(auta)
    guess = random.choice(auta)
    auta.remove(False)
    guess2 = guess  # nezmeni volbu
    if guess2:
        vyhra += 1
    return vyhra


def zmeni_volbu(vyhra=0):
    auta = [False, False, True]
    random.shuffle(auta)
    guess = random.choice(auta)
    auta.remove(False)
    index_hadani = auta.index(guess)
    if index_hadani == 0:
        guess2 = auta[1]
    elif index_hadani == 1:
        guess2 = auta[0]
    if guess2:
        vyhra += 1
    return vyhra

vyhra_pri_zachovani = 0
vyhra_pri_zmene = 0
for i in range(1000000):
    vyhra_pri_zachovani += nezmeni_volbu(vyhra=0)

for i in range(1000000):
    vyhra_pri_zmene += zmeni_volbu(vyhra=0)

print("vyhra pri zachovani: ", vyhra_pri_zachovani)
print("vyhra pri zmene: ",vyhra_pri_zmene)

