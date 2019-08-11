from functools import wraps

# podle prednasky https://www.youtube.com/watch?v=sPiWg5jSoZI&list=WL&index=7&t=0s


"""
metraprogramming - code that manipulates code
DRY - don't repeat yourself

func(*args, **kwargs)   - *args stands for tuple of positional args, **kwargs stands for dictionary of key word args
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

