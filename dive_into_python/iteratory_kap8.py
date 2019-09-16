import re
import itertools
import math
import subprocess

"""
algebrogram - nahradit kazde pismeno cislici 0-9 tak, aby pri nahrazeni ve slovech vytvorily artimetickou rovnici
vsechny vyskyty stejneho pismene se musidat nahradit stejnou cislici, zadna cislice se nesmi opakovat a slovo nesmi
zacinat 0
"""

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())  # najde vsechny vyskyty vzorku + prevede na velke pismena, vraci list
    unique_characters = set(''.join(words))  # spoji dohromady a vylouci duplicity prevedenim na set
    assert len(unique_characters) <= 10, 'Too many letters'  # zkracena forma zapisu na vyvolani vyjimky

    first_letters = {word[0] for word in words}  # set prvnich pismen z words
    n = len(first_letters)  # pocet prvnich pismen v retezci (aby nezacinaly nulou)
    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)  # prehledne serazeno

    characters = tuple(ord(c) for c in sorted_characters)  # generatorovy vyraz
    digits = tuple(ord(c) for c in '0123456789')  # generatorovy vyraz
    zero = digits[0]  # ulozena ord hodnota nuly

    for guess in itertools.permutations(digits, len(characters)):  # permutace tvori vsechny mozne varianty
        # permutace vytvori z digits ntice o delce poctu pismen
        if zero not in guess[:n]:  # vyrazeny ntice, kde byla na pozici prvniho pismene slova nula
            equation = puzzle.translate(dict(zip(characters, guess)))  # vysledkem je Pythonni vyraz v textove podobe
            if eval(equation):  # vyhodnoti kazdou rovnici
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

groups = itertools.groupby(names, len)  # names zde musi jit uz serazeny podle te sdruzovaci fce len
"""
groupby prebira posloupnost a fci klice. Vraci iterator, ktery vytvari dvojice, tj. vysledek fce klic a dalsi iterator,
ktery prochazi vsema polozkama se stejnym vysledkem fce klice
groupby je obecna, muze seskupovat podle jakekoli myslitelne fce klice - podle prvniho pismene atp.
"""
print(groups)
print(list(groups))  # volanim fce list se iterator vycerpal; pokud chceme hodnoty znovu, musime ho vytvorit znovu
groups = itertools.groupby(names, len)
# vsem jmenum o delce 4 prideli jeden iterator, pro jmena s delkou 5 prideli jiny iterator atd.
for name_length, name_iter in groups:
    print('Names with {} letters.'.format(name_length))
    for name in name_iter:
        print(name)


print(list(range(0, 3)))
print(list(range(10, 13)))
print(list(itertools.chain(range(0, 3), range(10, 13))))
# chain prebira dva nebo vice iteratoru a vraci iterator, ktery prebira prvky vsech
print(list(zip(range(0, 3), range(10, 13))))  # zip vraci iterator, ktery tvori tuple z prvnich prvku, druhych...
print(list(zip(range(0, 3), range(10, 14))))  # zip zastavi na konci nejkratsi posloupnosti
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))  # tato si sama doplni None

word = re.findall('[A-Z]+', 'SEND + MORE = MONEY')
word = tuple(set(''.join(word)))
print(word)
numbers = 10234567
guess = tuple(str(numbers))
print(guess)
print(tuple(zip(word, guess)))  # sparuje pismena a cislice
print(dict(zip(word, guess)))  # pismena jsou klice a cisla jsou hodnoty
sl = {key:value for key, value in zip(word, guess)} # stejny slovnik se dal vytvorit pomoci dict comprehension
print(sl)

# 6. translate
translation_table = {ord('A'): ord('O')}  # prekladova tabulka; preklada bajty na jine bajty
print(translation_table)  # fce ord vraci ASCII hodnotu znaku
print('MARK'.translate(translation_table))  # translate prepasiruje string pres prekladovou tabulku

characters = tuple(ord(c) for c in 'SMEDONRY')
print(characters)
guess = tuple(ord(c) for c in '91570682')  # tohle je spravna kombinace
print(guess)
translation_table = dict(zip(characters, guess))  # klic je ord pismena, value je ord cisla
print('translation table:', translation_table)
print('SEND + MORE = MONEY'.translate(translation_table))  # obdoba zapisu puzzle.translate(dict(zip(characters,guess)))
# transtale rovnou i prevede ord cisla zpet na cislo

# 7. eval()
print(eval('1 + 1 == 2'))
print(eval('1 + 1 == 4'))
# fce eval vyhodnoti libovolny Pythonovsky vyraz a vraci libovolny datovy typ
print(eval('"A" + "B"'))
print(eval('"MARK".translate({65:79})'))
print(eval('"AAAA".count("A")'))
print(eval('["*"] * 5'))
x = 5
print(eval('x * 5'))  # vyraz predavany eval muze odkazovat na glovalni i lokalni promenne
print(eval('pow(x, 2)')) # taky na fce
print(eval('math.sqrt(x)'))  # i na moduly
print(eval('subprocess.getoutput("ls ~")'))
# modul subprocess dovoli spustit libovolny shellovsky prikaz a ziskat vysledek v podobe retezce!
# dovoli spustit i mocne a nevratne shelloveske prikazy, napr. mazani souboru apod.
"""
Pouziti fce eval() vyzaduje opatrnost, protoze ona vyhdnoti i vyrazy z neduveryhodnych zdroju.
"""
x = 5
# print(eval("x + 5", {}, {}))  # haze NameError ze name x is not defined
"""
{} a {} jsou globalni prostor jmen. Jsou oba prazdne, pri vyhodnocovani retezce neexistuje zadny odkaz na x ani v 
globalnim ani v lokalnim prostoru jmen, takze eval() vyvola vyjimku
"""
print(eval('x + 5', {'x': x}, {}))
# do globalniho prostoru hodnot se vlozila promenna x, takze na a pouze ona bude k dispozici
# print(eval('math.sqrt(x)', {'x': x}, {}))
# haze NameError ze name math is not defined, protoze modul math nebyl vlozen do prostoru jmen
print(eval('pow(5, 2)', {}, {}))
"""
Funguje spravne, prestoze se do globalniho ani lokalniho prostoru nic nevlozilo, a to protoze jsou stale dostupne
vsechny zabudovane fce, coz pow() je.
"""
print(eval('__import__("math").sqrt(5)', {}, {}))
"""
funguje, protoze __import__() je taky zabudovana fce (import prebira jmeno importovaneho modulu v podobe stringu)
Coz znamena, ze ani definice prazdnych slovniku {} a {} nezabrani tomuto:
eval('__import__("subprocess").getoutput("rm /some/random/file")', {}, {})  - bude fungvat, importuje a smaze file
"""
# print(eval("__import__('math').sqrt(5)", {"__builtins__":None}, {}))
# haze to TypeError NoneType is not subscriptable
"""
zabudovane fce jsou vnitrne uzavreny do pseudomodulu __builtins__ Ten je vyhodnocovanym vyrazum normalne zpristupnen,
ale da se to potlacit nastavenim slovniku __builtins__ na None.
"""
print(eval('2 ** 213', {'__builtins__': None}, {}))
# i pres nastaveni __builtins__ je vyraz vyhodnocen, tzn. mocnenim na nejake mega cislo by se dal zablokovat server

