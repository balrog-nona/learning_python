"""
tridni promenna: promenna sdilena vsema instancema, tj. data, ktere chcu, aby mely vsechny instance k nim pristup
instancni promenna: promenna unikatni pro urcitou instanci
"""

# zadani: vsichni zamestnanci maji dostat po roce pridano
# reseni 1: reseni v ramci instance
class Employee:

    def __init__(self, first, last, pay):
        self.firts = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp1 = Employee('john', 'snow', 60000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
"""
dava to ten predpokladany vysledek, ale co kdyz budu chtit zmenit ten koeficient platu? nejlepsi je mit na to tridni
promennou
"""

# reseni 2: tridni promenna + chceme i pocet zamestnancu
class Employee:

    raise_amount = 1.04  # tridni promenne
    no_emp = 0

    def __init__(self, first, last, pay):
        self.firts = first  # instancni atributy
        self.last = last
        self.pay = pay
        Employee.no_emp += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp2 = Employee('sansa', 'stark', 50000)
emp3 = Employee('rob', 'stark', 30000)
print(Employee.raise_amount)  # pristup tridy k promenne
print(emp2.raise_amount)  # instance ma pristup k tridni promenne - syntax jakoby byla jeji
print(emp3.raise_amount)
"""
kdyz pristupuju k atributu na instanci, tak python ho nejdriv hleda na te instanci. pokud ho ale nenajde (jako u emp2),
tak zacne hledat na tride a dalsich tridach, ze kterych se dedilo
"""
emp2.apply_raise()
emp3.apply_raise()
print(emp2.pay, emp3.pay)
print(Employee.no_emp)  # opet pristup tridy k promenne
print(emp3.no_emp)  # a ke stejne promenne na pristup i instance
print(emp2.no_emp)  # a v jine instanci ma tridni promenna stejnou hodnotu
print(emp3.__dict__)
print(Employee.__dict__)


class A:

    a = 'I am a class atribute!'


x = A()
y = A()
print(x.a)  # pristup bud pres instanci
print(y.a)
print(A.a)  # nebo pres tridu

# zmenu tridniho atributu je treba delat pres tridu, jinak se neprojevi, resp. zmeni se jen instance
x.a = 'This creates a new instance atribute for x'
print(y.a)
print(A.a)
print(x.a)
A.a = 'This is changing the class atribute a'
print(A.a, y.a, x.a)
print(x.__dict__)  # ma vlastni atribut a
print(y.__dict__)  # slovnik je prazdny, bo instance y nema zadny atribut
print(A.__dict__)  # zde ulozen tridni atribut


# static methods
class Robot:

    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def Robot_instances():
        return Robot.__counter


print(Robot.Robot_instances())
x = Robot()
print((x.Robot_instances()))
y = Robot()
print(y.Robot_instances(), x.Robot_instances(), Robot.Robot_instances())
"""
vyhoda static methods spociva v tom, ze jsou pristupne jak z tridy tak z jakekoli instance
vsechny jine reseni vedou jen k jednomu moznemu pristupu:
1. kdyby ta metoda byla
def Robot_instances(self):
    return Robot.__counter
- jednotliva instance robota nema nic spolecneho s celkovym poctem robotu
- nemuzu zpristupnit pocet robotu, dokud nejaka instance opravdu neexistuje
- nelze pristoupit pomoci Robot.Robot_instances() - TypeError, protoze to je navazane na self

2. kdyby ta metoda byla:
def Robot_intances():
    return Robot.__counter
- nyni je mozne pristoupit pres tridu Robot.Robot_instances(), ale ne pres instanci, napr.
x.Robot_instances(), protoze zase vyvola TypeError, ze ji byl dan necekany argument self,
protoze x.Robot_instances() je vyhodnocen jako instance method call a takova metoda potrebuje referenci na instanci
jako prvni parametr
"""


class Pet:

    _class_info = 'pet animals'

    def about(self):
        print('This class is about ' + self._class_info)

class Dog(Pet):

    _class_info = "man's best friend"

class Cat(Pet):

    _class_info = 'all kinds of cat'

p = Pet()
d = Dog()
c = Cat()
print(p.about(), d.about(), c.about())  # toto dela, co delat ma, ale je to desny design. Nelze tvorit instance jen
# proto, aby bylo mozne zjistit to _class_info


# prechod na class method
class Pet:

    _class_info = 'pet animals'

    @classmethod
    def about(cls):
        # kdyby ty bylo Pet._class_info, tak to ve vsech instancich vraci pet animals
        print('This class is about ' + cls._class_info)

class Dog(Pet):

    _class_info = "man's best friend"

class Cat(Pet):

    _class_info = 'all kinds of cat'


Pet.about()  # vsechny tridy maji k metode pristup + predavaji ji vlastni hodnotu + nemusim tvorit instance
Dog.about()
Cat.about()