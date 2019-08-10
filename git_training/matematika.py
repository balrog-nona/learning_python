import math

class Matematika:  # koment k tride

    def scitani(self, a, b):
        """
        Nejlepsi komentar k fungovani metody dopise nekdo v budoucnu
        """
        return (a + b, b + a)

    def nasobeni_deleni(self, a, b):  
        return (a * b, a / b)

    def deleni(self, a, b):  # operace deleni vzdycky vraci float
        if b > 0:
            return a / b
        else:
            return 'error'

    def mocnina(self, a, b):  # komentar
        return a ** b

    def odmocnina(self, a):  # jde odmocnovat nulou??
        return math.sqrt(a)

    def obvod_obdelnika(self, a, b):
        return 2 * (a + b)

# comment 1
# coment do konfliktu
