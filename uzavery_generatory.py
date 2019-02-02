import re
import time

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
def build_match_and_apply_functions(pattern, search, replace):  # vytvari fce dynamicky
    def matches_rule(word):  # fce prebira vnejsi hodnoty - tzv. uzaver
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


patterns = \
    (
        ('[sxz]$',            '$',   'es'),
        ('[^aeioudgkprt]h$', '$',   'es'),
        ('(qu|[^aeiou])y$',    'y$', 'ies'),
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
        if matches_rule(noun):
            return apply_rule(noun)
"""
plural3 a plural2 vypadaji a funguji stejne. Obe berou seznam fci a a volaji je v uvedenem poradi. Nestara se o to, jak
jsou pravidla vytvareni techto fci definovana - u plural 2 to byla proste tuple obsahujici pojmenovane fce, u plural3
je to dynamicky vytvoreny seznam techto fci v rules3 
"""

# a ted se samotne podminky pro tvorbu pluralu ulozi do vlastniho souboru a zde zustane jen kod
rules4 = []

with open('../../diveintopython3/examples/plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)  # None - rozdel v miste bilych znaku, 3 - rozdel 3x
        rules4.append(build_match_and_apply_functions(pattern, search, replace))

# nasledne by se zase dala pouzit fce plural3, akorat tentokrat s rules4
def plural4(noun):
    for matches_rule, apply_rule in rules4:
        if matches_rule(noun):
            return apply_rule(noun)



# uzavery - viz taky soubor filter_list_comprehensions
# 1. priklad
def makeInc(x):
    def inc(y):
        return x + y
    return inc

inc5 = makeInc(7)
print(type(inc5))
print(inc5(5))

inc10 = makeInc(10)
print(inc10(4))


