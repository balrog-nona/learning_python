class Student:

    def __init__(self, jmeno, pohlavi, vek):
        self.jmeno = jmeno
        self.muz = pohlavi
        self.vek = vek
        self.plnolety = (vek > 18)

    def __str__(self):
        jsem_plnolety = "jsem" if self.plnolety else "nejsem"  # takto se da napsat podminka, kdyz je kratka
        pohlavi = "muz" if self.muz else "zena"
        return "Jsem {}, {}. Je mi {} let a {} plnolety.".format(self.jmeno, pohlavi, self.vek, jsem_plnolety)

s = Student(jmeno='Pavel Hora', pohlavi=True, vek=20)
print(s)

s.vek = 15
s.muz = False
print(s)
"""
Kdyz byla trida napsana bez osetreni proti zapisu do atributu, se ta logika rozbila, kdyz se prepsal vek na 15:
__init__ uz neprobehne, nic se neprenastavi a promennou jsem_plnolety to nijak neovlivni.
tzv. nekonzistentni vnitrni stav
Proto to hazelo uplne rozhozeny vysledek: Jsem Pavel hora, zena. Je mi 15 let a jsem plnolety.
"""

# trida s private atributy
class StudentPrivate:

    """
    Tady jsou vsechny atributy pod kontrolou a zvenci to nemuze nikdo rozbit.
    """

    def __init__(self, jmeno, pohlavi, vek):
        self.__jmeno = jmeno
        self.__muz = pohlavi
        self.__vek = vek
        self.__plnolety = (vek >= 18)

    def __str__(self):
        jsem_plnolety = "jsem" if self.__plnolety else "nejsem"
        pohlavi = "muz" if self.__muz else "zena"
        return "Jsem {}, {}. Je mi {} let a {} plnolety.".format(self.__jmeno, pohlavi, self.__vek, jsem_plnolety)

    def vrat_jmeno(self):  # atributy jsou private, takze je musi vracet metody
        return self.__jmeno

    def vrat_plnoletost(self):  # metody, co to vraci jsou gettery, nastavovaci metody jsou settery
        return self.__plnolety

    def vrat_vek(self):
        return self.__vek

    def muz(self):
        return self.__muz

    def nastav_vek(self, hodnota):
        self.__vek = hodnota
        self.__plnolety = True if self.__vek >= 18 else False
        return self.__plnolety


student = StudentPrivate(jmeno='Roman Dostal', pohlavi=True, vek=33)
print(student)
student.nastav_vek(hodnota=12)
print(student)
student.__jmeno = 'nasta'  # toto je jiny atribut nez ten z iniciace
print('a', student.__jmeno)
print(student)


# trida s vlastnostma
class StudentVlastnosti:

    def __init__(self, jmeno, pohlavi, vek):
        self.__jmeno = jmeno
        self.__muz = pohlavi
        self.__vek = vek
        self.__plnolety = (vek >= 18)

    def __str__(self):
        jsem_plnolety = "jsem" if self.__plnolety else "nejsem"
        pohlavi = "muz" if self.__muz else "zena"
        return "Jsem {}, {}. Je mi {} let a {} plnolety.".format(self.__jmeno, pohlavi, self.__vek, jsem_plnolety)

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, hodnota):
        self.__vek = hodnota
        self.__plnolety = (hodnota >= 18)

"""
Dekoratory jsou objekty podporujici volani (fce, metody nebo objektu s metodou __call__() ), ktere vraci upravenou
(dekorovanou) verzi metody nebo fce.
"""
studak = StudentVlastnosti(jmeno='Marek Novotny',pohlavi=True, vek=22)
print(studak)
studak.vek = 15
print(studak)
print(studak.vek)  # vlastnost se pouziva jako normalni atribut

# vsechny atributy objektu se uchovavaji ve slovniku spojenem s objektem + da se tak i prirazovat
print(studak.__dict__)


# trida podle tutorialu Coreyho Schafera
# https://www.youtube.com/watch?v=jCzT9XFZ5bw
class Employee:

    def __init__(self, first, last):
        """
        Pozdejsi zmeny jmena se nepromitnou do emailu, protoze __init__ se provede jen pri tvorbe instance.
        Ale bylo by celkove fajn, kdyby se email updatoval automaticky, pokud se jmeno zmeni. Z teto pozice neni moc
        vhodne udelat z email atributu emailovou metodu, protoze to by vsichni, kdo uz tento kod uzivaji museli
        svuj kod zmenit, coz nechceme! Reseni: prevedeni email atributu na dekorator.
        """
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com' vynato po tvorve dekoratoru

    @property
    def email(self):  # definovano jako metoda, ale pristup jako k atributu
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # nazev vlastnosti.setter - nic nevraci, jen nastavuje
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee(first='John', last='Smith')
emp_1.first = 'Jim'
emp_1.fullname = 'Corey Schafer' # k teto akci se vytvoril setter

print(emp_1.first)
print(emp_1.email)  # kdyby to nebyl dekorator, ale metoda, tak by se vsude pristup k nemu musel prepsat na email()
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first)








cislo = 15
d = cislo > 18
print(d,type(d))


class Kostka:
    """
    Trida reprezentuje hraci kostku.
    """

    def __init__(self, pocet_sten):  # metoda konstruktoru
        self.__pocet_sten = pocet_sten


kostka = Kostka(pocet_sten=5)
kostka.__pocet_sten = 8
print(kostka.__pocet_sten)
print(kostka._Kostka__pocet_sten)
# tady je videt, ze zadani atributu kostka.__pocet_sten neni to stejne jako atribut __pocet_sten vytvoreni pri
# iniciaci
