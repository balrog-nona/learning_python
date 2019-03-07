"""
dle tutorialu Dive into Python3 lekce 7
iterator je trida, ktera definuje metodu __iter__()
zde se vytvari svuj vlastni iterator
"""

class Fib:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for n in Fib(max=1000):  # kompletni vysvetleni je v knizce
    print(n, end=" ")


"""
nize je generator pravidel mnozneho cisla, ktery se ve forme ruznych funkci nachazi v souboru uzavery_generatory.py
nyni tedu forma iteratoru
"""


