import inspect
from inspect import Parameter, Signature
import re
from collections import OrderedDict


# podle prednasky https://www.youtube.com/watch?v=sPiWg5jSoZI&list=WL&index=7&t=0s


# STRUCTURE
# ZABRANENI OPAKOVANI __INIT__ V KAZDE NOVE TRIDE - video 39:20
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Host:

    def __init__(self, address, port):
        self.address = address
        self.port = port

# too repetitive
# varianta 1:
class Structure:
    _fields = []

    def __init__(self, *args):  # generalizace initu
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Host(Structure):
    _fields = ['address','port']

s = Stock('GOOG', 100, 490.1)
"""
funguje - normalne vytvori potrebne atributy i s hodnotama

Nevyhody:
- ztrati se spousta dat uzitecnych pro debugging, napr. pri help(classname) tam skoro nic neni
- kdyz se zada nespravny pocet argumentu, tak se instance vytvori, ale nebude mit ty spravne atributy
- ztrata moznosti zadavat argumenty jako keywords
- missing calling signature (z modulu inspect)
"""

# SIGNATURE - video 45:10
# build function signature object
fields = ['names', 'shares', 'price']
parms = [Parameter(fname, Parameter.POSITIONAL_OR_KEYWORD) for fname in fields]  # list comprehension
print(parms)  # function parameters
sig = Signature(parms)
print(type(sig), sig)  # Signature object

# sig.bind() binds positional/keyword args to signature
def foo(*args, **kwargs):
    bound = sig.bind(*args, **kwargs)
    for name, val in bound.arguments.items():
        print(name, val)

foo(1, 2, 3)
foo(2, price=50.6, shares=40)  # supports keyword args
# foo(1, 2) does argument checking
# foo(1, 2, 3, 4)

# usage - video 48:40
def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

class Structure:
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])

class Point(Structure):
    __signature__ = make_signature(['x', 'y'])

class Host(Structure):
    __signature__ = make_signature(['address', 'port'])

s = Stock('GOOG', 560, 410.3)
print(s.shares, s.name, s.price)
s = Stock(name='GOOG', shares=600, price=8)  # podpora keyword args
print(s.shares)
# s = Stock('GOOG', 3) error checking for not enough args
print(inspect.signature(Stock))  # pristup k seznamu atributu
print(inspect.signature(Point), inspect.signature(Host))

"""
O hodne jednodussi, nicmene definice tridy je stale repetitivni - ten 1 radek se opakuje ve vsech 3 tridach.
Solutions:

1. class decorators - video 51:40
def add_signature(*names):
    def decorate(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorate
    
@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass
    
2. metaclass - video 52:00
class StructMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        sig = make_signature(clsobj._fields)  automaticky tvori signature, basically doing code
        setattr(clsobj, '__signature__', sig)
        return clsobj
        
class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)
            
class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    
class Point(Structure):
    _fields = ['x', 'y']
    
Back to original simple solution. Signatures are made behind the scenes.

Advice regarding usage - video 55:00
"""

print(help(Stock))


# TYPE CHECKING - video 1:00:50
# especially tricky when checking both type and value
# DESCRIPTORS - video 1:02:10
"""
class Descriptor:   customized processing of attribute access
    def __get__(self, instance, cls):   nepotrubuje se, pokud jen vraci normalne hodnotu z __dict__
        ...
    def __set__(self, instance, value):
        ...
    def __delete__(self, instance):
        ...
"""
class Descriptor:  # osetreni JEDNOHO atributu
    def __init__(self, name=None):
        self.name = name  # jde se zvenci dostat k tomu, ze bych si overila, ze tento atribut se jmenuje name?
    def __get__(self, instance, cls):
        # instance: is the instance being manipulated, e. g. Stock instance
        print('Get', self.name)
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print('Set', self.name, value)
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        print('Delete', self.name)
        del instance.__dict__[self.name]

class StructMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    name = Descriptor('name')
    shares = Descriptor('shares')
    price = Descriptor('price')

s = Stock('GOOG', 450, 200.6)
print(s. shares)  # tady mi to tiskne i nejake None - odkud se bere??
del s.shares
s.shares = 1
print(s.shares)  # tady taky po get je None (jeste pred tim, nez metody v Descriptoru mely return)


# struktura zakladniho descriptoru - video 1:07:09

class Typed(Descriptor):
    ty = object  # expected type
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected {}'.format(self.ty))
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str


class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = String('name')  # funguje, protoze String dedi od Typed a ten od Descriptor
    shares = Integer('shares')
    price = Float('price')

s = Stock('banana', 450, 2.6)
s.name = 'OTO'
print(s.__dict__)
# s.name = 8  type checking funguje

class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be > 0')
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive):  # dedeni ze dvou trid!
    pass

class PositiveFloat(Float, Positive):  # kombinuje funkcionality obou trid, tj. type i value checking
    pass

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = String('name')  # funguje, protoze String dedi od Typed a ten od Descriptor
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

s = Stock('koxo', 41, 7.6)
# s.shares = 'a lot' funguje, vyvola TypeError
# s.shares = -96  funguje, vyvola ValueError

"""
Poradi dedeni tech dvou trid, ze kterych se dedi 
class PositiveInteger(Integer, Positive)
je dulezite - nejdriv potrebuju type check, aby se nestalo, ze se porovnava nenumericka hodnota, coz vyhodi zcela jiny
error.
Method resolution order:
"""
print(PositiveInteger.__mro__)  # order in which the value is checked by different __set__() methods
# po Integer se zastavi na Typed a nejde dal na Descriptor kvuli fci super()

# length checking - video 1:22:32
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Too big')
        super().__set__(instance, value)

class SizedString(String, Sized):
    pass

# pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)  # to nevadi, ze trida Descriptor s argumenty nepocita?

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError('Invalid string')
        super().__set__(instance, value)

class SizedRegexString(SizedString, Regex):
    pass

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    name = SizedRegexString('name', pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

s = Stock('KOLO', 250, 78.6)
# s.name = 'aaaaaaaaaaaaaaa' funguje, vyhodi ValueError Too big
# s.name = '1234'  funguje, vyhodi ValueError Invalid string
# s.name = 66   funguje, vyhodi TypeError, protoze ocekava string
"""
Muze se dedit i ze 3 trid:
class SizedRegexString(String, Sized, Regex):
    pass
    
Cela ta manipulace s __init__ je umoznena tema keyword only argumenty, tj. name, maxlen, pat - video 1:27:00
"""

# novy level METACLASSES - video 1:29:11
class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):  # returns the dict which will be used during cls creation
        return OrderedDict()  # dict that keeps things in order

    def __new__(cls, name, bases, clsdict):
        fields = [key for key, val in clsdict.items() if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name # tady mi to pripada nejasne

        clsobj = super().__new__(cls, name, bases, dict(clsdict))
        # for class content must be proper dict, not Ordered ot something

        sig = make_signature(fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    """
    Vsechny tz tridy, ktere vznikly dedenim, jsou nejakym zpusobem navazane na Descriptor. Ted se pro kazdy atribut
    vybere ta konkterni trida, do ktere ma spadat - jestli SizedString,PositiveInteger apod.
    """
    name = SizedRegexString(pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger()
    price = PositiveFloat()

s = Stock('UHURU', 77, 22.6)
print(s.name, s.price, s.shares)

"""
Velka nevyhoda celeho toho postupu se signature, metaclass hard core - video 1:37:42
proti proste
class Stock:
    def__init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

POMALOST
"""
# CODE GENERATION - video 1:39:49
# fce, ktera vytvori __init__, aby to cele bylo zase rychle
def _make_init(fields):
    """
    Give a list of field names, make an__init__ method
    """
    code = 'def __init__(self, {}):\n'.format(", ".join(fields))
    for name in fields:
        code += '   self.{} = {}\n'.format(name, name)
    return code

print(_make_init(['name','shares', 'price']))

class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):  # returns the dict which will be used during cls creation
        return OrderedDict()  # dict that keeps things in order

    def __new__(cls, name, bases, clsdict):
        fields = [key for key, val in clsdict.items() if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name

        if fields:
            init_code = _make_init(fields)
            exec(init_code, globals(), clsdict)

        clsobj = super().__new__(cls, name, bases, dict(clsdict))
        # for class content must be proper dict, not Ordered ot something

        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []

class Stock(Structure):
    name = SizedRegexString(pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger()
    price = PositiveFloat()

s = Stock('TUKAN', 55, 230.8)
print(s.name, s.price, s.shares)
# s.name = 33 checking stale funguje

# je to podstatne rychlejsi nez ty srandy s metaclass, ale stale ne tak rychle jako prosta definice class
