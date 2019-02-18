import re
import os

"""
kap. 6 z Dive into Python 3
vytvari se knihovna, ktera bude prevadet podstatna jmena do pluralu
pravidla tvorby anglickeho pluralu jsou v knize vysvetlene
"""


def plural1(noun):
    if re.search('[sxz]$', noun):  # presne 1 moznost, tj. s nebo x nebo z
        return re.sub('$', 'es', noun)  # nahradi konec retezce pismeny es. stejny ucinek by mela i konkatenace
    elif re.search('[^aeioudgkprt]h$', noun):  # negace - znaky krome uvedenych v []
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):  # slova koncici y kde predhozi znak neni aeiou
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'


print(re.search('[^aeiou]y$', 'vacancy'))  # funguje - predposledni pismeno je c
print(re.search('[^aeiou]y$', 'boy'))  # nefunguje, predposledni je o
print(re.search('[^aeiou]y$', 'day'))  # v day je predposledni a
print(re.search('[^aeiou]y$', 'pita'))  # nekonci na y
print(re.sub('y$', 'ies', 'vacancy'))
print(re.sub('y$', 'ies', 'agency'))
print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy'))  # zapamatuje si znak, ktery je pred y
"""
tento vyraz dela dve veci naraz: 1. zkontroluje, jestli sedi podminka, ze slovo pred koncovym y nema aeiou
2. pokud nema, zapamatuje si pismeno pred koncovym y
nasledne zapamatovanou skupinu (v tomto pripade to predposledni pismeno) vlozi pred ies a toto pak nahradi cy ve slove
vacancy
vyhoda toho celeho je, ze se nemusi nejdrive pouzit fce search na overeni podminky predposledniho pismena
vyraz tedy rika: retezec cy zmeni na cies ve slove vacancy
"""
print(re.sub('([szx])$', r'\1es', 'asterix'))  # prvni dva radky fce plural1 by se daly napsat i takto


# docasne se zkomplikuje jedna cast programu, aby se mohla jina zjednodusit
def match_sxz(noun):  # kazda match fce vraci vysledek volani fce search - tj. objekt nebo None
    return re.search('[sxz]$', noun)


def apply_sxz(noun):  # kazda aplikacni fce vraci po pouziti fce sub vysledek tvorby mnozneho cisla
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'


# misto fce plural1 se vytvori datova struktura s posloupnosti dvojic fci
rules2 = ((match_sxz, apply_sxz),  # neobsahuje jmena fci, ale jejich skutecne objekty!
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
         )

def plural2(noun):
    for matches_rule, apply_rule in rules2:
        if matches_rule(noun):  # jestlize vraci objekt, cili najde shodu, prejde na aplikacni fci a prepise slovo
            return apply_rule(noun)

"""
nevyhoda postupu u plural2 je, ze ted by se pro kazde nove pravidlo musely definovat dve nove fce a zaradit je 
do rules2, zatimco v plural1 stacilo napsat dalsi if podminku
fce plural2 a vsechny fce, ktere pouziva pres strukturu rules2 maji stejny vzorec - je tu match fce, ktera vola search
a apply fce, ktera vola sub. To je dulezite pro uvedomeni, jake vsechny moznosti lze pri sledovani tohoto cile vyuzit 
- viz nize fce build_match_and_apply_functions
"""


# fce plural 2 je ekvivalentem tohoto zapisu
def plural2a(noun):
    if match_sxz(noun):
        return apply_sxz(noun)
    if match_h(noun):
        return apply_h(noun)
    if match_y(noun):
        return apply_y(noun)
    if match_default(noun):
        return apply_default(noun)

# dalsi moznost, jak to vyresit:
def build_match_and_apply_functions(pattern, search, replace):  # vytvari fce dynamicky; tato fce je closure
    def matches_rule(word):  # fce bude mit prostup k vnejsim hodnotam pattern, search, replace
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

# lomitko dole za patterns zajisti, aby to mohl vyraz pokracovat na dalsim radku; lomitko musi byt posledni znak
patterns = \
    (
        ('[sxz]$',           '$',   'es'),
        ('[^aeioudgkprt]h$', '$',   'es'),
        ('(qu|[^aeiou])y$',  'y$', 'ies'),
        ('$',                '$',   's')  # zbytkova fce se musela trochu prepsat - proste se na konci retezce prida s
    )

rules3 = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]  # stacilo by for pattern in patterns
"""
rules3 vytvari posloupnost fci. bere vzorec z patterns a pouzitim fce build_match_and_apply_functions vytvori pro kazdy
pattern fci na match a fci na apply. Match fce zavola search a apply zavola sub.
zde struktura rules3 na stejnou funkcni podobu jako u rules2 - seznam dvojic fci 
"""


def plural3(noun):
    for matches_rule, apply_rule in rules3:
        if matches_rule(noun):  # dodana hodnota do parametru word
            return apply_rule(noun)  # tady taky
"""
plural3 a plural2 vypadaji a funguji stejne. Obe berou seznam fci a a volaji je v uvedenem poradi. Nestara se o to, jak
jsou pravidla vytvareni techto fci definovana - u plural 2 to byla proste tuple obsahujici pojmenovane fce, u plural3
je to dynamicky vytvoreny seznam techto fci v rules3 
"""

# a ted se samotne podminky pro tvorbu pluralu ulozi do vlastniho souboru a zde zustane jen kod
rules4 = []  # bude to seznam z tuple - dvojic fci

with open('../../diveintopython3/examples/plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)  # None - rozdel v miste bilych znaku, 3 - rozdel 3x
        rules4.append(build_match_and_apply_functions(pattern, search, replace))


# nasledne by se zase dala pouzit fce plural3, akorat tentokrat s rules4
def plural4(noun):
    for matches_rule, apply_rule in rules4:  # stacilo by for dvojice in rules4
        if matches_rule(noun):
            return apply_rule(noun)



# CLOSURES - viz taky soubor filter_list_comprehensions
# 1. priklad
def makeInc(x):  # tato fce je closure
    def inc(y):
        return x + y
    return inc  # tato fce pak bude mit pristup k hodnote x

inc5 = makeInc(7)  # dosadila se hodnota do x
print(type(inc5))
print(inc5(5))  # dosadila se hodnota do y

inc10 = makeInc(10)
print(inc10(4))
"""
closure fce je obvykle ulozi to vlastni promenne, coz bude type fce, bo closure fce vraci fci
VYHODA pouziti closure - 
1 muze to byt citelnejsi
2. je to rychlejsi nez pouziti jinych struktur
3. avoiding global variables since closure provides data hiding
4. implementing a class with a public method
5. decorators use closures
"""

# 2. priklad
def outer_fce(name):
    print("Hello, sweet little", name)

    def inner_fce():  # fce bude mit pristup k hodnote paranetru name
        print(name, "you are very small.")

    return inner_fce

r_fce = outer_fce("Nona")  # vytiskne vetu + vraci fci
print("-" * 30)  # pomaha podchytit chronologii behu programu
r_fce()  # ma pristup k name, proto vytiskne, co ma
"""
To have a closure:
1. a nested function
2. nested function refers to variable/s from enclosing scope
3. nested function is returned from the enclosing scope
"""

# 3. ukazka
def func1():
    name = "Nona"
    num1 = 5
    num2 = 6

    def func2():
        print(name + str(num1) + str(num2))

    return func2

c = func1()
print(c.__closure__)  # vrati tuple se vsemi objekty, ktere jsou schovane v closure
print(c.__closure__[0].cell_contents)  # pristup k jednotlivym hodnotam objektu
print(c.__closure__[1].cell_contents)  # cell_contents je atribut
print(c.__closure__[2].cell_contents)


# GENERATORS
"""
fce plural by totiz mela delat nasledujici:1. ziskat soubor s pravidly, 2. zkontrolovat, ktera se maji pouzit, 
3. provest prislusne tranformace, 4. prejit k dalsimu pravidlu
"""

# 1. priklad
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i * i

mygenerator = create_generator()  # creates a generator
print(mygenerator)
for i in mygenerator:
    print(i)

"""
Pri volani fce kod z tela fce neprobehne - fce pouze vrati generator object. Ten kod probehne pokazde, kdyz for cyklus
pouzije ten generator object.
Poprve, kdyz for cyklus zavola generator object, probehne kod v tele fce od zacatku, az dokud neprijde k yield a pak 
vrati prvni hodnotu z cyklu. Pak pokazde pri volani fce probehne for cyklus z te fce a vrati dalsi hodnotu, az neni uz
zadna hodnota k vraceni.
Generator je povazovan za prazdny, kdyz uz kod nedosahne na yield - napr. kdyz cyklus dojde ke konci nebo uz se
nenaplnuje podminka.
Fce, ktere maji yield jsou generator functions.
modul itertools - manipulates iterables
"""

# 2. priklad
def make_counter(x):
    print("entering make counter")
    while True:
        yield x  # specialni druh fce, ktera generuje hodnoty jednu po druhe
        print("incrementing x")
        x += 1


counter = make_counter(2)  # pri zavolani vraci generator, nedojde k provedeni kodu fce
print(counter)
print(next(counter))  # bez print tiskne jen to, co tiskne primo fce, tedy netiskne hodnotu x
print(next(counter))
print(next(counter))
"""
yield fci zastavi - next() pokracuje od poslednih ozastaveni
fce next() bere objekt generatoru a vraci jeho dalsi hodnotu. Pri prvnim volani se kod z make_counter provede az do 
prvniho yield a vrati se hodnota x. 
Pri dalsim volani fce next() se zacina od mista, kde se minule skoncilo a pokracuje se do mista dalsiho yield a 
zase se vrati hodnota x.
Pri provedeni yield jsou totiz vsechny promenne, lokalni stav a dalsi veci ulozeny a pri dalsim volani next() jsou
obnoveny.
Pri prvnim volani next() se tedy provede prikaz print("entering make counter"), pak se vleze do cyklu, hned se narazi
na yield a hodnota x je 2.
Pri dalsim volani next() se vytiskne "incerementing x", provede se prikaz x += 1 a pak se jde znovu na yield,
x ma ted hodnotu 3. Pri dalsim volani next() se zacne zase tiskem incrementing x a hodnota x se zvedne na 4, pak se zase
skonci na yield.
"""

# 3. priklad
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a  # generator function
        a, b = b, a + b

for n in fib(1000):  # for cyklus automaticky dostava dalsi hodnoty volanim fce next()!!
    print(n, end=" ")

print(list(fib(1000)))  # fce list() iteruje pres hodnoty generatoru a vraci jejich seznam


# opet k fci plural
def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)


directory, name = os.path.split('../../diveintopython3/examples/plural5-rules.txt')

def plural5(noun, rules_filename=name):
    for matches_rule, apply_rule in rules(rules_filename):
        """Pri druhe obratce se dostaneme tam, kde generator rules posledne skoncil, cili pri druhe obratce zde ve 
        for cyklu se dostaneme do rules do druheho radku for cyklu, coz vygeneruje dalsi dve fce a vrati se pres yield.
        A tak to pujde porad dokola, dokud se zde nenajde shoda a neprovede se i apply funkce nebo dokud to cele 
        neskonci vyjimkou. 
        """
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError("no matching rule for {0}".format(noun))

"""
Proti plural4() vyhody: ziskal se startovaci cas, bo v plural4() se musel importovat modul plural4 a vytvorit se seznam
pravidel, nez se mohlo zacit neco delat. Pri pouziti generatoru se da vsechno delat na posledni chvili - naste se
pravidlo, vytvori se fce, vyzkousi se. Pokud to funguje, nemusi se nacitat zbytek ani tvorit dalsi fce.

Nevyhody: ztrata vykonnosti - generator rules() startuje vzdycky od pokazde, kdyz se vola fce plural5(), tj. soubor se
vzorky se musi znova otevrit a musi se cist jeden radek po druhem.
"""

print(plural5("vacancy", rules_filename=name))  # tak toto mi nefunguje...
