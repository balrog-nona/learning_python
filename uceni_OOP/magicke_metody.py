from numbers import Real
from collections.abc import Sequence
from weakref import WeakKeyDictionary

# magicke jsou ty, ktere zacinaji a konci __

# 1. __new__(cls, *args, **kwargs)
"""
__new__ se vola, kdyz je treba mit kontrolu nad vytvarenim objektu
vraci bud vytvoreny obejekt nebo nic. Pokud vrati objekt, zavola se metoda __init__
Pokud objekt nevraci, __init__ se nevola.
"""
class Test:

    def __new__(cls, fail=False):
        print('Zavolana metoda __new__')
        if not fail:
            return super().__new__(cls)

    def __init__(self):
        print('Zavolana metoda __init__')

test_1 = Test()
test_2 = Test(fail=True)

# v __new__ uz lze prirazovat atributy k objektu
class Point:

    def __new__(cls, x, y):
        self = super().__new__(cls)
        self.x = x
        self.y = y
        return self

point = Point(x=10, y=5)
print(point.x, point.y)


# 2. __init__(self, *args, *kwargs)
"""
Vola se pri inicializaci objektu. Parametr self je predan automaticky.
__init__ by mela vracet pouze None, coz Python sam vraci, pokud metoda nema specifikovany navratovy typ.
Pokud __init__ vraci neco jineho nez None, tak se vyvola TypeError
"""
class Testovaci:

    def __init__(self):
        return 1

# test_A = Testovaci() tady je ten TypeError


# 3. __repr__(self)
"""
Metoda by mela vracet reprezentaci zdrojoveho kodu objektu jako text tak, aby platilo:
x = eval(repr(x))
"""

# 4. __str__(self) - ma vracet lidsky citelnou reprezentaci obejktu
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """
        vola se pri print() nebo str(). Pokud neni naimplementovana tato metoda, tak se vola __repr__
        """
        return 'x: {0.x}, y: {0.y}'.format(self)  # musi vracet string object

    def __repr__(self):
        """
        vraci reprezentaci,coz muze byt any valid expression - tuple, dict, string...
        kdyz tuto metodu vola fce repr(), pak ale i tato metoda musi vracet string, jinak to hodi chybu
        kdyz tato metoda vraci string, tak je mozne vynechat __str__()
        """
        return '{x:self.x, y:self.y}'

point = Point(x=20, y=3)
# __str__() example
print(point)
print(point.__str__())
s = str(point)
print(s)

# __repr__() example
print(point.__repr__())
print(type(point.__repr__()))
print(repr(point))  # hazelo TypeError, dokud __repr__() vracelo dict


# klonovani
class Bod:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return self.__class__(self.x, self.y)  # metoda __class__() obsahuje odkaz na tridu

    # metoda __bool__()
    def __bool__(self):
        return bool(self.x < self.y)

bod = Bod(x=10, y=2)
bod_clone = bod.clone()
print(id(bod), id(bod_clone))  # jsou to ruzne objekty
print(bod.__bool__())


# metody souvisejici s matematikou
class Vector:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({0.x}, {0.y})'.format(self)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y)  # toto vraci novy objekt? id tomu neodpovida...
        elif issubclass(type(other), Sequence):  # kontrola, jestli je to podtrida Sequence z modulu collections.abc
            if len(other) == 2:
                return Vector(self.x+other[0], self.y+other[1])  # tady taky
        raise NotImplemented  # vyvola TypeError

    def __mul__(self, other):
        if issubclass(type(other), Real):
            return Vector(self.x * other, self.y * other)  # tady taky
        raise NotImplemented

    __radd__ = __add__
    __rmul__ = __mul__


vector = Vector(x=1, y=2)
print('id vector: ', id(vector))
vector = [3, 4] + vector
vector *= 2.5
print(vector)  # probehly obe ty operace vyse
print('id vector: ', id(vector))
# print(vector + 3) zde TypeError
"""
Z toho kodu mi to pripada, jakoby se mel vracet novy objekt, ale vraci se ten puvodni, na kterem byly volane ty metody
akorat ma ted zmenene atributy.
"""


# magicke metody kolekci
class Foo:

    def __setattr__(self, name, value):
        """
        Vola se pri nastaveni atributu misto prirazovani promennych do __dict__
        Pokud chce trida atribut ulozit, mela by zavolat __setattr__() nadtridy
        """
        print('Setting')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        """
        Tato metoda se vola, pokud selze hledani atributu pres obvykle metody
        vraci nejakou hodnotu nebo vyvola AttributeError
        """
        print('Getting')
        return 1

foo = Foo()
print(foo.x)  # vola se __getattr__() bo tento atribut neexistuje
print(foo.__dict__)
foo.x = 2
print(foo.x)  # __getattr__() se nevola, bo atribut existuje
print(foo.__dict__)  # doslo i k prirazeni do slovniku
foo.x = 23
print(foo.x)
foo.y = 45
print(foo.__dict__)


# deskriptory - umoznuji prepsani pristupu k atributum pomoci jine tridy
class Typed:

    """
    Deskriptor Typed zajistuje, aby byl atribut urciteho typu.
    Mela to byt evidentne obecna trida pouzitelna na jakykoli atribut.
    Petr mi potvrdil, ze to nefunguje kvuli tomu slovniku
    """

    dictionary = WeakKeyDictionary()

    def __init__(self, ty=int):
        print('tvorba descriptoru')
        self.ty = ty

    def __get__(self, instance, owner=None):
        if instance is None:  # zpristupnuje se pres tridu
            return self
        print('Getting instance')
        return self.dictionary[instance]

    def __set__(self, instance, value):  # bere jako parametr instanci a hodnotu, na kterou ma byt atribut nastaveny
        print('Setting instance', instance, 'to', value)
        if not isinstance(value, self.ty):  # kontrola, jestli je hodnota spravneho typu
            raise TypeError('Value must be type {}'.format(self.ty))
        self.dictionary[instance] = value  # nemelo byt tu byt spis self.dictionary[atribute] = value??

"""
WeakKeyDictionary funguje jako normalni slovnik, ale pokud pro dany objekt (klic) ve slovniku neexistuje vic referenci,
snaze objekt ze slovniku, coz by bezny slovnik neudelal, bo on sam by ho pouzival. Timto se zamezi memory leakum
v pameti.
neni resene jak zaridit, aby tam byly ulozene atributy a jejich hodnoty
"""

class Person:

    # tridni promenne
    name = Typed(ty=str)  # jmeno musi byt string. to se vytvari pri tvorbe teto tridy person.name je vlastne singleton
    age = Typed()  # vek bude int
    weight = Typed(ty=float)  # vaha bude float

    def __init__(self, name, age, weight):
        self.name = name  # pri volani atributu Python pozna, ze jde o deskriptory a zavola __get__(), __set__()
        self.age = age
        self.weight = weight  # navazane na weight a tim padem na typed
"""
kdyz neco nema instance ve slovniku tak se diva na to same do slovniku tridy
"""

# funguje i na podtridy
class CleverPerson(Person):

    iq = Typed(ty=int)

    def __init__(self, name, age, weight, iq):
        super().__init__(name, age, weight)
        self.iq = iq


# lze vytvaret i podtridy deskriptoru
class Ranged(Typed):

    def __init__(self, ty=int, min=0, max=100):
        super().__init__(ty)
        self.min = min
        self.max = max

    def __set__(self, instance, value):
        if value < self.min:
            raise TypeError('Value must be greater than {}'.format(self.min))
        elif value > self.max:
            raise TypeError('Value must be lower than {}'.format(self.max))
        super().__set__(instance, value)


bob = CleverPerson(name='Bob', age=33, weight=88.7,iq=120)  # toto nefunguje
print('bob name: ', bob.name)  # pokazde se prepise zrejme cela instance, az zustane ta posledni hodnota...
print(bob.__dict__)  # slovnik je prazdny - neobsahuje zadne atributy
del bob  # snizi se pocet referenci na objekt
# print(bob.age) vyvola NameError - bob uz neexistuje
print('clever person name:', CleverPerson.name)


# descriptory podle netu https://www.youtube.com/watch?v=HUtLnn5MBGk
class MyDescriptor:

    def __init__(self):
        self.__age = 0

    def __get__(self, instance, owner):  # instance je sam, owner je class, ktere ta instance nalezi, tj. zde Person
        return self.__age

    def __set__(self, instance, value):  # instance opet sam, value je ta pozadovana hodnota atributu
        if not isinstance(value, int):
            raise TypeError('Age must be integer value.')
        if value < 0 or value > 120:
            raise ValueError('Age must be between 0 and 120.')
        self.__age = value

    def __delete__(self, instance):
        del self.__age


class Person:

    age = MyDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{} is {} years old.'.format(self.name, self.age)

sam = Person(name='Sam', age=44)
print(sam)
# sam.age = -88  vyhodi spravne ValueError
# sam.age = 'twenty' tady taky
"""
Descriptory jsou navazane na tridu, ne na instanci - kdyz se zmeni hodnota descriptoru, tak se prepise na vsech
instancich.
Aby se tomu zamezilo, descriptor musi mit slovnik, ktery udrzuje hodnoty pro kazdou instanci.
"""
peter = Person(name='Peter', age=11)
print(peter)
print(sam)  # tady haze, ze Samovi je 11

# verze se slovnikem
class MyDescriptor2:

    def __init__(self):
        self.__age = WeakKeyDictionary()

    def __get__(self, instance, owner):  # instance je sam, owner je class, ktere ta instance nalezi, tj. zde Person
        return self.__age.get(instance)

    def __set__(self, instance, value):  # instance opet sam, value je ta pozadovana hodnota atributu
        if not isinstance(value, int):
            raise TypeError('Age must be integer value.')
        if value < 0 or value > 120:
            raise ValueError('Age must be between 0 and 120.')
        self.__age[instance] = value

    def __delete__(self, instance):
        del self.__age[instance]

"""
Tato trida ovsem umi osetrit jen 1 atribut, a to age - kdyby tam byly dalsi, jako vaha, vyska apod., nedalo by se to
pouzit. Ta trida Typed() z ITNetwork mela predstavovat obecne osetreni pro vstupy.
"""

class Person:

    age = MyDescriptor2()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{} is {} years old.'.format(self.name, self.age)


john = Person(name='John', age=33)
print(john)
print('john age:', john.age)  # ale vypise se spravne
print(type(john.age))
print('john dict: ', john.__dict__)  # jak to,ze age neni v __dict__ jako atribut? on se eviduje v tride MyDescriptor2?
eric = Person(name='Eric',age=77)
print('eric ', eric)  # tady nedoslo k prepisu drivejsi instance
print('eric age', eric.age)
print('eric dict', eric.__dict__)  # ani tady neni age
"""
Tohle teda funguje, ale osetruje to jen 1 konkretni atribut, neni to obecna kontrola typu.
Totiz asi obecne descriptory by mely evidovat 3 veci - instanci, atribut, hodnotu, ne??
"""

"""
poradne video k tomuto ve watch later! 
"""
print('==================================================================================================')
# muj vytvor
class Descriptor:

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value  # tento key se jmenuje self.name nebo name?

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected {}'.format(self.ty))
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class String(Typed):
    ty = str

class Float(Typed):
    ty = float

class Ranged(Descriptor):
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Must be greater than 0')
        super().__set__(instance, value)

class RangedInteger(Integer, Ranged):
    pass

class RangedFloat(Float, Ranged):
    pass

class Person:  # jak to, ze to funguje?

    name = String('name')
    age = RangedInteger('age')
    weight = RangedFloat('weight')

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

bobby = Person('bobby', 44, 55.8)
print(bobby.name)
print(id(bobby))
print(bobby.age)
# bobby.age = -5 funguje

ron = Person('ron', 77, 96.4)
print(ron.name, ron.weight, ron.age)
ron.name = 'betty'
print(ron.name)
# ron.weight = -33.7 funguje
print(id(ron))

print(bobby.name)
print(bobby.__dict__)
print(ron.__dict__)

class CleverPerson(Person):
    iq = RangedInteger('iq')

    def __init__(self, name, age, weight, iq):
        super().__init__(name, age, weight)
        self.iq = iq

paula = CleverPerson('paula', 22, 55.7, 145)
print(paula.iq, paula.age, paula.weight, paula.name)
# paula.iq = -6 funguje
paula.age = 18
print(paula.age, bobby.age, ron.age)
print(paula.__dict__)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
# 2. verze s kontrolou vseho mozneho
class Descriptor:

    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected {}'.format(self.ty))
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class String(Typed):
    ty = str

class Float(Typed):
    ty = float

class NameString(String, Descriptor):
    def __set__(self, instance, value):
        if value[0].islower():
            raise ValueError('Names start with capital letter.')
        super().__set__(instance, value)

class Ranged(Descriptor):
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Must be greater than 0')
        super().__set__(instance, value)

class RangedInteger(Integer, Ranged):
    def __set__(self, instance, value):
        if value > 120:
            raise ValueError('Max. 120')
        super().__set__(instance, value)

class RangedFloat(Float, Ranged):
    pass

class Person:  # jak to, ze to funguje?

    name = NameString('name')
    age = RangedInteger('age')
    weight = RangedFloat('weight')

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

miguel = Person('Miguel', 50, 87.5)  # opravdu kontroluje velka pismena
print(miguel.name, miguel.weight)
# miguel.age = -66 funguje
miguel.age = 12
print(miguel.age)
print(miguel.__dict__)

class Max_iq(Integer, Ranged):
    def __set__(self, instance, value):
        if value > 190:
            raise ValueError('Max. 190')
        super().__set__(instance, value)

class CleverPerson(Person):
    iq = Max_iq('iq')

    def __init__(self, name, age, weight, iq):
        super().__init__(name, age, weight)
        self.iq = iq

joe = CleverPerson(name='Joe', age=24, weight=67.2, iq=165)  # podporuje keywords
print(joe.name, joe.iq)
# joe.iq = 210 funguje
joe.name = 'Peter'
print(joe.name, joe.weight)
print(joe.__dict__)