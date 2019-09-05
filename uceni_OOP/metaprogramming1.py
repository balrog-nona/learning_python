from functools import wraps, partial

# podle prednasky https://www.youtube.com/watch?v=sPiWg5jSoZI&list=WL&index=7&t=0s


"""
metraprogramming - code that manipulates code
DRY - don't repeat yourself

func(*args, **kwargs)   - *args stands for tuple of positional args, **kwargs stands for dictionary of keyword args
args = (4, 5)
kwargs = {'x': 66, 'y': 100}
func(*args, **kwargs) je to same jako func(4, 5, x=66, y=100)
"""

"""
Video zahrnuje:
- descriptory
- hiding of annoying details (signatures apod.)
- dynamic code generation
- customizing import
"""

# DEBUGGING USING DECORATORS
"""
decorator is a function that creates a wrapper around another function. That wrapper functions exactly the same as
the original fce but there is some extra processing carried out
"""
def debug(func):
    # func if function to be wrapped
    @wraps(func)  # bez tohoto decoratoru se ztrati spousta informaci pri help; kopiruje metadata
    def wrapper(*args, **kwargs):
        print(func.__name__)  # lze pouzit i func.__qualname__ ma vyznam u trid
        return func(*args, **kwargs)
    return wrapper

@debug
def adding(a, b):
    return a + b

@debug
def multi(a, b):
    return a * b

print(adding(2, 6))

# DECORATORS WITH ARGUMENTS - 2 levels of nested functions, video 16:30
def debug(prefix=''):
    def decorate(func):
        msg = prefix + func.__name__
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# usage
@debug(prefix='***')
def add(x, y):
    return x + y

# reformulation
def debug(func=None,prefix=''):
    if func is None:  # function wasn't passed
        return partial(debug, prefix=prefix)

    msg = prefix + func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


# DEBUGGING ALL OF THE METHODS OF THE CLASS AT ONCE - video 20:21
class Spam:  # can I decorate all methods at once? - YES

    @debug
    def grok(self):
        pass

    @debug
    def bar(self):
        pass

    @debug
    def foo(self):
        pass


def debugmethods(cls):
    for key, value in vars(cls).items():
        if callable(value):  # decorates every method
            setattr(cls, key, debug(value))
    return cls

@debugmethods  # takhle se to dela, covers all definitions within the class
class Spam:
    def grok(self):
        pass
    def bar(self):
        pass
    def foo(self):
        pass

"""
Limitations: doesn't work with classmethods and staticmethods, only instance methods get wrapped
"""

# variation - DEBUG ACCESS - video 25:00
def debugattr(cls):  # rewriting part of the class itself, debugging attribute access
    orig_getattribute = cls.__getattribute__  # pristup k tridnim atributum

    def __getattribute__(self, name):
        print('Get: ', name)  # vypise zpravu pred pristupem
        return orig_getattribute(self, name)
    cls.__getattribute__ = __getattribute__  # vrati vsechno do puvodniho stavu

    return cls

@debugattr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)  # vypise zpravu a pak hodnotu atributu
print(p.y)


# DEBUG ALL THE CLASSES - video 25:50
# solution A - DEFINING A METACLASS
class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)  # vytvori tridu
        clsobj = debugmethods(clsobj)  # a pak na ni nabali class decorator - wraps it
        return clsobj

"""
Every type in defined by class: the class is the type of instances created.
The class is a callable that creates instances.
Classes are instances of types: !!
type(int)  - class type
type(list)  - class type
type(Point)  - class type
isinstance(Point, type)  - True

So type must be a class!
type(type)  - class type
Makes instances of types. Used when defining classes.
"""

class Spam(Base):

    """
    Name: Spam
    Base classes: Base,
    Functions: __init__, bar
    """

    def __init__(self, name):
        self.name = name

    def bar(self):
        print('I am Spam.bar')

# What happens during class definition
# step 1: Body of class is isolated
body = """
    def __init__(self, name):
        self.name = name
    def bar(self):
        print('I am Spam.bar')
"""
# step 2: the class dictionary is created
clsdict = type.__prepare__('Spam', (Base,))  # this dictionary serves as local namespace for statements in the cls body
# step 3: body is executed in returned dict
exec(body, globals(), clsdict)
# afterwards cls dict is populated
# step 4: class is constructed from its name,base classes, and the dictionary
Spam2 = type('Spam2', (Base,), clsdict)  # cili takhle to muzu naplnit i rucne mimo normalni definici?

# Changing the METACLASS - video 30:55
# by metaclass keyword argument; sets the class used for creating the type; bydefault it's set to type
# class Spam(metaclass=type)
"""
normally while creating a class I inherit from type and redefine __new__ or __init__
"""
class mytype(type):
    def __new__(cls, name, bases, clsdict):
        """
        tady si fakt muzu dat, co chci, napr. podminku o poctu bases, vyvolavat vyjimky apod.
        """
        clsobj = super().__new__(cls, name, bases, clsdict)
        return clsobj

# usage: class Spam(metaclass=mytype):

"""
Mataclasses get information about class definitions at the time of definition - I can inspect or modify this data.
Essentially similar to a class decorator.

Metaclasses propagate down hierarchies:
class Base(metaclass=mytype):
...
class Spam(Base):   -metaclass Base
...
class Grok(Spam):   -metaclass Base!
...
It's like genetic mutation.
"""
class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)  # vytvori tridu
        clsobj = debugmethods(clsobj)  # a pak na ni nabali class decorator - wraps it
        return clsobj  # class gets created normally + immediately wrapped by class decorator

# debug the universe:
class Base(metaclass=debugmeta):
    pass
class Spam(Base):  # debugging gets applied across entire hierarchy - implicitly applied in subclasses
    pass
class Grok(Spam):
    pass
class Mondo(Grok):
    pass

"""
Wrapping/rewriting:
decorators: functions
class decorators: classes
metaclasses: class hierarchies

With metaclass, there is a way how to make changes before the class creation X class decorators come in play
after the class has already been created. 
"""
