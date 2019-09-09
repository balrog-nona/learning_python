import re

"""
dle tutorialu Dive into Python3 lekce 7
iterator je trida, ktera definuje metodu __iter__()
zde se vytvari svuj vlastni iterator
"""

class Fib:

    def __init__(self, max):  # v dobe volani metody uz je objekt zkonstuovan a na novou instanci uz existuje odkaz
        self.max = max

    def __iter__(self):
        """
        Vola se, kdyz nekdo zavola iter(fib) - cyklus for ji vola automaticky
        Na zacatku iterace se provede inicializace, tj. nastaveni stavu self.a a self.b
        :return: muze vratit libovolny objekt, ktery implementuje metodu __next__()
        """
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration  # nevyvolava chybu, je to bezny signal, ze iterace skoncila
        self.a, self.b = self.b, self.a + self.b
        return fib  # nedavat yield, ten ma vyznam jen u generatoru, toto je vlastni iterator


for n in Fib(max=1000):
    print(n, end=" ")

"""
cyklus for vola Fib(1000) - vracise instance tridy Fib (zde alias fib_inst)
cyklus for vola fci iter(fib_inst),ktera vraci objekt iteratoru (zde alias fib_iter). V nasem pripade plati
fib_iter == fib_inst, protoze __iter__() vraci self (ale for cyklu je to jedno)
za ucelem pruchodu hodnotama vola cyklus for fci next(fib_iter), kyera vola metodu __next__() objektu fib_iter. Ta
provede vypocet dalsiho cisla a vraci hodnotu. For cyklus ji prevezme, priradi ji do promenne n a s touto hodnotou
provede telo cyklu.
Kdyz next(fib_iter) vyvola vyjimku StopIteration, cyklus ji psolkne a v poradku se ukonci.
"""
print()
fib = Fib(max=23)
print(fib.__class__)
print(fib)
print(fib.__doc__)


"""
nize je generator pravidel mnozneho cisla, ktery se ve forme ruznych funkci nachazi v souboru uzavery_generatory.py
nyni tedu forma iteratoru
"""

def build_match_and_apply_functions(pattern, search, replace):  # vytvari fce dynamicky; tato fce je closure
    def matches_rule(word):  # fce bude mit prostup k vnejsim hodnotam pattern, search, replace
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)


class LazyRules:

    rules_filename = '../../../diveintopython3/examples/plural6-rules.txt'  # tridni promenna

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')  # soubor se otevre, ale nic se z nej necte
        self.cache = []  # vyrovnavaci pamet, bude to seznam fci

    def __iter__(self):  # metoda se bude volat pokazde, kdyz nekdo zavola iter(rules)
        self.cache_index = 0
        return self

    def __next__(self):  # volana pokazde, kdyz nekdo zavola next(rules); vraci hodnoty behem iterace
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            print("delka cashe:", len(self.cache), 'index ', self.cache_index)
            return self.cache[self.cache_index - 1]
        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()  # precte z otevreneho souboru presne 1 radek
        print(line)
        print('cash index ', self.cache_index)
        if not line:  # dosahlo se konce souboru
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        print('delka cache', len(self.cache))
        return funcs

rules = LazyRules()

"""
r1 = LazyRules()
r2 = LazyRules()
print(r1.rules_filename)
print(r2.rules_filename)
r2.rules_filename = 'override.txt'  # tvorba atributu pro tuto instanci
print(r2.rules_filename, r2.__dict__)
print(r1.rules_filename, r1.__dict__)
print(r1.__class__.rules_filename)
print(r2.__class__.rules_filename)  # hodnota zachovana
r2.__class__.rules_filename = 'papaya.txt'
print(r1.rules_filename)  # na ostatnich instancich se to prepsalo
print(r2.rules_filename)  # tato instance ma jeste ten vlastni atribut
print(r2.__class__.rules_filename)  # ale na tride ten prepsany
print(LazyRules.__dict__)  # opravdu na urovni tridy prepsano
"""
def plural6(noun, rules):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError("no matching rule for {0}".format(noun))

print(plural6('haiku', rules))
print('-' * 30)
print(plural6('child', rules))
print('-' * 30)
print(plural6('analysis', rules))
print('-' * 30)

print(plural6('bus', rules))
print('-' * 30)

print(plural6('fish', rules))
print('-' * 30)
print(plural6('wife', rules))
print('-' * 30)
print(plural6('cheetah', rules))
print('-' * 30)

for i in rules.cache:
    print(i)

print(rules)  # je to instance tridy LazyRules