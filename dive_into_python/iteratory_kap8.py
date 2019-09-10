import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())  # najde vsechny vyskyty vzorku + prevede na velke pismena, vraci list
    unique_characters = set(''.join(words))  # spoji dohromady a vylouci duplicity prevedenim na set
    assert len(unique_characters) <= 10, 'Too many letters'  # zkracena forma zapisu na vyvolani vyjimky
    firts_letters = {word[0] for word in words}  # set prvnich pismen z words
    n = len(firts_letters)
    sorted_characters = ''.join(firts_letters) + ''.join(unique_characters - firts_letters)
    characters = tuple(ord(c) for c in sorted_characters)  # generatorovy vyraz
    digits = tuple(ord(c) for c in '0123456789')  # generatorovy vyraz
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation


if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)


# co se deje:
# 1. nalezeni vsech vyskytu vzorku
print(re.findall('[0-9]+', '16 2-by-4s inrows of 8'))  # fce findall najde vsechny vyskyty vzorku, vraci seznam
print(re.findall('[A-Z]+', 'SEND + MORE == MONEY'))  # regex definovan tak, aby to naslo cele slova

print(re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick."))
# .*? jakykoli znak 0 nebo vicekrat, ale nepovinny
# tady se misto 5 shod vraci 3, protoze se nevraci prekryvajici se shody (prekryva se prvni shoda s druhou a treti se
# ctvrtou

# 2. nalezeni jedinecnych prvku
a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
print(set(a_list))
a_string = 'EAST IS EAST'
print(set(a_string))
words = ['send', 'more','money']
print(''.join(words))  # spoji dohromady
print(set(''.join(words)))  # spoji dohromady, vyradi duplicity, protoze tak funguji sety, a prevede na set

# 3. prikaz assert - da se za nej libovolny vyraz, vyhodnocuje na True nebo False (vyvola vyjimku)
assert 1 + 1 == 2  # vyhodnoti jako True, takze nedela nic
# assert 1 + 1 == 3 vyvola AssertionError
# assert 2 + 2 == 5, 'Only for very large values of 2.' zkracena forma zapisu na vyvolani vyjimky
"""
assert len(unique_characters) <= 10, 'Too many letters'
je ekvivalentem
if len(unique_characters) <= 10:
    raise AssertionError('Too many letters')

Program pouziva assert k predcasnemu ukonceni cinnosti, kdyby bylo pismen vic nez cislic - nema reseni.
"""

# 4. generatorove vyrazy
unique = set(''.join(words))
gen = (ord(c) for c in unique)  # generatorovy vyraz, uzavren v kulatych zavorkach, i kdyz se podoba list comprehension
print('gen', gen)  # vraci iterator
print(next(gen))  # vraci dalsi hodnotu iteratoru
print(next(gen))
a = tuple(ord(c) for c in unique)  # v teto souvislosti staci jedny zavorky, Python pozna, ze je to generatorovy vyraz
# timto se oteruje pres vsechny hodnoty a rovnou se prevadi na jiny datovy typ
print(a)
b = list(ord(c) for c in unique)
print(b)
c = set(ord(c) for c in unique)
print(c)
"""
Pouziti generatoroveho vyrazu misto generatorove notace seznamu (list comprehension) setri CPU i RAM.
Generatorovy vyraz se hodi zvlast tam, kde se ten seznam zase vyhodi (treba predanim do tuple() nebo set() ).
"""
def ord_map(a_string):  # stejneho efektu se dosahne pomoci generatorove fce
    for c in a_string:
        yield ord(c)

gen = ord_map(unique)
for i in gen:
    print(i, end=' ')

print()
# 5.vypocet permutaci - mozne ntice bez opakovani
perms = itertools.permutations([1, 2, 3], 2)  # chci najit vsechny mozne usporadane dvojice
print(next(perms))  # permutace jsou usporadane (1, 2) je neco jineho nez (2, 1)
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
# print(next(perms))   tady se konci, dalsi dvojice nejsou

perms = itertools.permutations('ABC', 3)  # lze predat cokoli, cim lze iterovat
for i in perms:  # fce permutations vraci iterator
    print(i, end=' ')
print()
print(list(itertools.permutations('ABC', 3)))  # iterator se predal fci list()

print(list(itertools.product('ABC', '123')))  # vraci iterator a vytvari kartezsky soucin dvou posloupnosti
print(list(itertools.combinations('ABC', 2)))  # posloupnost, delka
# vraci iterator, ktery vytvari kombinace dane delky. Kombinace nezahrnuje bysledky vznikle jen zmenou usporadani

file = '../../../diveintopython3/examples/favorite-people.txt'
names = list(open(file, encoding='utf-8'))  # vraci seznam vsech radku v souboru
print(names)
names = [name.rstrip() for name in names]
print(names)
names = sorted(names)  # seradi abecedne
print(names)
names = sorted(names, key=len)  # seradim dle delky
print(names)
