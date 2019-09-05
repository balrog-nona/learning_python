import inspect
from inspect import Parameter, Signature
import re
from collections import OrderedDict
from xml.etree.ElementTree import parse
import sys
import os
import imp  # wow, tak toto jsem jeste nevidela...

# podle prednasky https://www.youtube.com/watch?v=sPiWg5jSoZI&list=WL&index=7&t=0s

# navrh dalsiho zpusobu - video 1:44:22
class Descriptor:  # osetreni JEDNOHO atributu
    def __init__(self, name=None):
        self.name = name  # jde se zvenci dostat k tomu, ze bych si overila, ze tento atribut se jmenuje name?

    @staticmethod
    def set_code():  # returning string code fragments!
        return [
            'instance.__dict__[self.name] = value'
        ]
    def __delete__(self, instance):
        print('Delete', self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object  # expected type

    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.ty):',
            '   raise TypeError("Expected {}".format(self.ty))'
        ]

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '   raise ValueError("Must be > 0")'
        ]

class PositiveInteger(Integer, Positive):  # dedeni ze dvou trid!
    pass

class PositiveFloat(Float, Positive):  # kombinuje funkcionality obou trid, tj. type i value checking
    pass

class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if len(value) > self.maxlen:',
            '   raise ValueError("Too big")'
            ]

class SizedString(String, Sized):
    pass

class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)  # to nevadi, ze trida Descriptor s argumenty nepocita?

    @staticmethod
    def set_code():
        return [
            'if not self.pat.match(value):',
            ' raise ValueError("Invalid string")'
            ]

class SizedRegexString(SizedString, Regex):
    pass

def make_signature(names):
    return Signature(Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)

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

print(Descriptor.set_code())  # vsechny produkuji kod
print(Integer.set_code())
print(Positive.set_code())
print(PositiveInteger.__mro__)

"""
co s tim: - ono to nefunguje...
code = ["def __set__(self, instance, value):"]
for cls in PositiveInteger.__mro__:  nefunguje kvuli teto radce
    for line in cls.set_code():
        code.append("   " + line)

print(code)
print('\n'.join(code))  # tohle vytiskne pekne __set__(), jak ma byt
"""

# generation of setter - video 1:51:17
def _make_setter(dcls):  # input - Descriptor class
    code = 'def __set__(self, instance, value):\n'
    for d in dcls.__mro__:  # walks through MRO and collects output of set_code()
        if 'set_code' in d.__dict__:
            for line in d.set_code():
                code += '   ' + line + '\n'  # concatenate to make a __set__() method
    return code

print(_make_setter(Descriptor))  # opravdu tvori kod __set__()
print(_make_setter(PositiveInteger))
print(_make_setter(SizedRegexString))

# ted se potrebuje metaclass pro Descriptor
class DescriptorMeta(type):
    def __init__(self, clsname, bases, clsdict):
        """
        Tvorba koduse musi provadet v __init__ a ne v __new__, protoze pri tvorbe kodu uz musi existovat __mro__,
        coz pri __new__ jeste neexistuje.
        """
        super().__init__(clsname, bases, clsdict)
        code = _make_setter(self)  # making the set code
        exec(code, globals(), clsdict)
        setattr(self, '__set__', clsdict['__set__'])  # tohle je nejaka technikalie, video 1:53:30

class Descriptor(metaclass=DescriptorMeta):
    def __init__(self, name=None):
        self.name = name  # jde se zvenci dostat k tomu, ze bych si overila, ze tento atribut se jmenuje name?

    @staticmethod
    def set_code():  # returning string code fragments!
        return [
            'instance.__dict__[self.name] = value'
        ]
    def __delete__(self, instance):
        print('Delete', self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object  # expected type

    @staticmethod
    def set_code():
        return [
            'if not isinstance(value, self.ty):',
            '   raise TypeError("Expected {}".format(self.ty))'
        ]

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

class Positive(Descriptor):
    @staticmethod
    def set_code():
        return [
            'if value < 0:',
            '   raise ValueError("Must be > 0")'
        ]

class PositiveInteger(Integer, Positive):  # dedeni ze dvou trid!
    pass

class PositiveFloat(Float, Positive):  # kombinuje funkcionality obou trid, tj. type i value checking
    pass

class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    @staticmethod
    def set_code():
        return [
            'if len(value) > self.maxlen:',
            '   raise ValueError("Too big")'
            ]

class SizedString(String, Sized):
    pass

class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)  # to nevadi, ze trida Descriptor s argumenty nepocita?

    @staticmethod
    def set_code():
        return [
            'if not self.pat.match(value):',
            ' raise ValueError("Invalid string")'
            ]

class SizedRegexString(SizedString, Regex):
    pass

def _make_init(fields):
    """
    Give a list of field names, make an__init__ method
    """
    code = 'def __init__(self, {}):\n'.format(", ".join(fields))
    for name in fields:
        code += '   self.{} = {}\n'.format(name, name)
    return code

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

s = Stock('GOOG', 33, 22.8)
print(s.name, s.price)  # funguje
# user has no idea about the code generation
# je to rychlejsi nez metaclasses

# XML to CLASSES - video 2:03:45
# jak predelat XLM na Python code
class Structure(metaclass=StructMeta):
    _fields = []
# XML parsing - na videu ten xml soubor byl pripraveny
def _xml_to_code(filename):  # vytvari class definice
    doc = parse(filename)
    code = ""
    for structure in doc.findall('structure'):
        clscode = _struct_to_class(structure)
        code += clscode
    return code

def _struct_to_class(structure): # toto je poplatne xml souboru, ktery nemam
    name = structure.get('name')
    code = 'class {}(Structure):\n'.format(name)
    for field in structure.findall('field'):
        dtype = field.get('type')
    options = ['{} = {}'.format(key, val) for key, val in field.items() if key != 'type'] # tady je to asi divne...
    name = field.text.strip()
    code += '   {} = {}({})'.format(name, dtype, ','.join(options))
    return code

class Stock(Structure):
    name = SizedRegexString(pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger()
    price = PositiveFloat()


# import statement upraven na importovani xml - video 2:14:51
print(sys.path)
print(sys.meta_path)  # list of classes that trigger the import statement

class Finder:
    def find_module(self, fullname,path):
        # fullname is name of what's being imported
        # path is path setting (for packages)
        print(fullname, path)
        return None

# sys.meta_path.insert(0, Finder())  tohle zacne u kazdeho importu hazet None

class StructFinder:
    def find_module(self, fullname,path):
        # will look for a matching XML file and make it import somehow
        for dirname in sys.path:
            filename = os.path.join(dirname, fullname + '.xml')
            if os.path.exists(filename):
                print('Loadind XML:', filename)
                return StructXMLLoader(filename)
        return None

class StructXMLLoader:
    def __init__(self, filename):
        self.filename = filename
    def load_module(self, fullname):
        # carry out the import steps
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = imp.new_module(fullname)  # modul vytvoren
            # vlozit modul mezi module cache
            sys.modules[fullname] = mod
        mod.__file__ = self.filename
        mod.__loader__ = self
        code = _xml_to_code(self.filename)
        exec(code, mod.__dict__, mod.__dict__)
        return mod


"""
Moduly jsou v Pythonu objekty, tzn.clovek si je muze i sam vytvorit:
import  imp
mod = imp.new_module('foo')
"""

def install_importer():
    sys.meta_path.append(StructFinder())

class Stock(Structure):
    name = SizedRegexString(pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger()
    price = PositiveFloat()

# tyhle srandy se nedaji delat v test-driven developing style

"""
Nic z toho, co se ve videu delalo, vlastne neohybalo Python jako takovy nebo neslouzilo k tomu, aby ho nejak obchazelo.
"""