import math

class Matematika:

    def scitani(self, a, b):
        # komentar
        """
        Komentar do commitu 1
        """
        return a + b

    def odcitani(self, a, b):
        return a - b

    def nasobeni_deleni(self, a, b):  
        return (a * b, a / b)

    def deleni(self, a, b):
        if b > 0:
            return a / b
        else:
            return 'error'

    def mocnina(self, a, b):  # komentar
        return a ** b

    def odmocnina(self, a):
        return math.sqrt(a)

    def obvod_ctverce(self, a):
        # komentar
        return 4 * a

    def obvod_obdelnika(self, a, b):
        return 2 * (a + b)
