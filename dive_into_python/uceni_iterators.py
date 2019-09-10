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
print('fib', fib)
print(fib.__doc__)  # None - nema docstring


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
        self.cache = []  # vyrovnavaci pamet, bude to seznam fci, ktery pretrva i po skonceni hledani na 1 slove

    def __iter__(self):
        """
        metoda se bude volat pokazde, kdyz nekdo zavola iter(rules), tzn. pokazde, kdyz se spusti prevod noveho
        slova do mnozneho cisla
        :return: vraci iterator
        """
        self.cache_index = 0
        # print('volam __iter__()', 'cache index: ', self.cache_index)
        return self

    def __next__(self):  # volana pokazde, kdyz nekdo zavola next(rules); vraci hodnoty behem iterace
        # print('volam __next__()')
        self.cache_index += 1  # de facto pocita iterace pri hledani mnozneho cisla na jednom slove
        # print('self.cache_index: ', self.cache_index)
        if len(self.cache) >= self.cache_index:
            # print('v podmince')
            # print("delka self.cache:", len(self.cache), 'cache_index ', self.cache_index)
            # print('vracim: ', self.cache[self.cache_index - 1])
            return self.cache[self.cache_index - 1]
        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()  # precte z otevreneho souboru presne 1 radek
        # print(line)
        # print('cache index po line: ', self.cache_index)
        if not line:  # dosahlo se konce souboru
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        # print('vytvorena fce, bude vlozena k self.cache')
        self.cache.append(funcs)
        # print('delka cache', len(self.cache))
        return funcs

rules = LazyRules()  # tato instance otevrela soubor, ale necte z nej

r1 = LazyRules()
r2 = LazyRules()
print(r1.rules_filename)
print(r2.rules_filename)
r2.rules_filename = 'override.txt'  # tvorba atributu pro tuto instanci
print(r2.rules_filename, r2.__dict__)
print(r1.rules_filename, r1.__dict__)
print(r1.__class__.rules_filename)
print(r2.__class__.rules_filename)  # hodnota zachovana
r2.__class__.rules_filename = 'papaya.txt'  # prepis pro celou tridu
print(r1.rules_filename)  # na ostatnich instancich se to prepsalo
print(r2.rules_filename)  # tato instance ma jeste ten vlastni atribut
print(r2.__class__.rules_filename)  # ale na tride ten prepsany
print(LazyRules.__dict__)  # opravdu na urovni tridy prepsano

def plural6(noun, rules):
    for matches_rule, apply_rule in rules:
        """
        rules je fce nove vytvorena nebo nactena z cache, pokud byla vytvorena uz predtim
        """
        if matches_rule(noun):
            return apply_rule(noun)
        # else:
            # print('shoda nenalezena, iteruji dal')
    raise ValueError("no matching rule for {0}".format(noun))

print(plural6('haiku', rules))
print('-' * 30)
print(plural6('child', rules))
print('-' * 30)
print(plural6('analysis', rules))
print('-' * 30)

print(plural6('bus', rules))
print('-' * 30)

print(plural6('fish', rules))  # nebylo treba tvorit fci, byla jiz vytvorena
print('-' * 30)
print(plural6('wife', rules))
print('-' * 30)
print(plural6('cheetah', rules))
print('-' * 30)

for i in rules.cache:
    print(i)

print('rules', rules)  # je to instance tridy LazyRules

"""
Princip:
- rules je instance tridy, otevrela soubor s pravidly,ale necetla z nej
- pri uplne prvnim volani fce plural() je self.cache prazdne, cili ze souboru se precte 1 radek, vybuduji se podle
neho fce pro rozhodovani a aplikaci a ulozi se do vyrovnavaci pameti
- nasledne fce plural vyzkousi takto vracene fce na pozadovanem slove. Pokud hned prvni dva fce vyhovuji, zadne dalsi
pravidla ze souboru se nectou.
- pri dalsim volani fce plural na jine slovo cyklus zavola __iter__, tim se vynuluje cache_index, ale nedojde k
resertovani otevreneho souboroveho objektu. Pri prvnim pruchodu zavola for cyklus o hodnotu ze struktury rules, coz
vede k zavolani metody __next__(). Je zjisteno, ze self.cache jiz obsahuje fci, delka self.cache je tedy vetsi nez
cache_index a vrati se tato jiz vytvorena fce. Pokud tentokrat toto pravidlo nevhovuje, for cyklus se zepta na dalsi
hodnotu z rules. Tentokrat je situace v podmince tato:
self.cache = 1 a cache_index = 2, tj. metoda __next__() pokracuje v cinnosti. Z otevreneho souboru precte dalsi radek, 
vytvori rozhodovani a aplikacnifci, tuto vlozi do self.cache. __next__ vrati prave vybudouvanou fci. Pokud ani ona
nevyhovuje, cely proces se opakuje dokud se nenajde shoda nebo dokud nedojdou radky v souboru. Ten se pak zavre a
cyklus skonci.

Vyhody celeho postupu:
- minimalni startovaci cas: pouze se vytvori instance tridy a otevre se soubor
- maximalni vykonnost: hned po vytvoreni fci dojde k jejich ulozeni do vyrovnavaci pameti, v nejhorsim pripade dojde
k precteni celeho souboru najednou. (na rozdil od predchozich pristupu, kdy se fce budovaly pokazde, kdyz se tvorilo
mnozne cislo slova)
- oddeleni kodu a dat: kod je kod a data jsou data a neprolinaji se  
"""