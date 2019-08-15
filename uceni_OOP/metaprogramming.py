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