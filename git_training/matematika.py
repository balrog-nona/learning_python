import math

class Matematika:

    def scitani(self, a, b):
        """
        Nejlepsi komentar k fungovani metody dopise nekdo v budoucnu
        """
        return a + b

    def odcitani(self, a, b):
        return a - b

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

# coment do konfliktu
