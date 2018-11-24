from collections import defaultdict  # nejak nefunguji importy


# creating a dictionary using list function and two lists
names = ["girl", "boy"]
hobbies = ["fitness", "reading"]
d = dict(zip(names, hobbies))
print(d)


# counting with dictionaries
colors = ["red", "green", "red", "blue", "green", "red"]
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

print(d)


# grouping with dictionaries
names = ["charlie", "will", "stephen", "roxanne", "yoko", "ted", "raymond"]
s = {}
for name in names:  # logicky spravne, ale neidiomaticke + nejpomalejsi
    key = len(name)
    if key not in s:
        s[key] = []
    s[key].append(name)

print(s)

r = {}
for name in names:
    key = len(name)
    r.setdefault(key, []).append(name)  # ne az tak moderni verze + o neco pomalejsi nez defaultdict

print(r)
"""
Setdefault returns a value of a key if the key is in the dictionary. If not, it inserts key with a default value to the 
dictionary.
setdefault method returns: 
- the value of the key, if the key is in dictionary
- None, if key is not in the dictionary and the default value is not specified
- default value if key is not in the dictionary and default value is specified (second parameter)
"""

"""
dict_q = defaultdict(list)  # nejmodernejsi a nejrychlejsi verze, NEFUNGUJE
for name in names:
    key = len(name)
    dict_q[key].append(name)

print(dict_q)
"""

"""
Poznamky ruzne:
1. Ve fcich je dobre pro vetsi citelnost psat do argumentu keywords, aby tam nebyly jen nejake hausnumera nebo slova,
ktere budou s postupem casu neprehledne.
2. Vyuzivej moznosti updatovat vice promennych naraz, viz updating multiple state variables - eliminuje to chyby typu
hodnota promenne se zmenila + umoznuje to high level thinking - chunking.
3. pure function - returns the same value every time you call it
4. caching - dela asi neco s funkcema, asi je stabilizije?
"""


# unpacking sequences
k = "bill", "gates", 54, "bill@microsoft.com"
fname, sname, age, email = k  # nepsat 4 liny se 4 promennyma a indexovat k

letters = "abc"
first, second, third = letters

seznam = ["ovoce", "lusteniny", "drogerie"]
polozka1, polozka2, polozka3 = seznam

print(fname, sname, age, email, first, second, third, polozka1, polozka2, polozka3)


# updating multiple state variables
x, y = 0, 1  # finonacciho posloupnost
for i in range(4):
    print(x)
    x, y = y, x + y
"""
wow, toto prestane fungovat, kdyz je to na dvou radcich! promenne se zde musi menit zaroven! Kdyz se to napise na dva
radky, tak to nefunguje, bo hodnota x se zmeni a je pak brana do vypoctu.
"""

# unpacking a list of strings
v = names[:]
v = ", ".join(v)
print(v, type(v))


"""
zajimava knihovna collections - deque kolekce napr.
variable_name = deque(iterable) - provides methods like del, append, pop, but it is much more quick!
besides, there are special methods: popleft(), appendleft()
video pana 39:21 + dokumentace
"""


# factor-out temporary contexts
"""
idiom pro:
try:
    os.remove("somefile.tmp")
except OSError:
    pass
    
je:
with ignored(OSError):
    os.remove("somefile.tmp")
"""

# list comprehensions and generator expressions
print(sum([i ** 2 for i in range(10)]))
# funguje i verze bez [] a je to rychlejsi a nezere tolik pameti tvourbou listu
"""
rozdil se da chapat tak, ze pokud je to rozepsane na hafo radku a postupne apendovane do seznamu, tak to rika spis
JAK se to ma udelat, zatimco ve verzi comprehension to rika, CO to ma udelat.
"""

