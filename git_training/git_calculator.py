"""
nacvik odstranovani konfliktu
"""

class StringCalculator:

    def add(self, a):
        if a:
            return 0
        else:
            if a[0] == "/":
                delimiter = a[2]
            else:
                delimiter = "^"
            if "\n" in a:
                a = a.replace("\n", delimiter)
            if delimiter in a:
                a = a.split(delimiter)
                soucet = 0  # komentar
                for i in a:
                    try:
                        if int(i) > 0:
                            soucet += int(i)
                        else:
                            raise Exception("negatives not allowed")
                            continue
                    except ValueError:
                        pass
                return soucet
            else:
                return int(a)

print('hotovo')




