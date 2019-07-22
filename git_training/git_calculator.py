"""
Nacvik prace s Gitem - hlavne zmeny v souboru, ktery se v mezidobi vyvinul
Metoda: prevazne pokus-omyl
"""

class StringCalculator:

    def add(self, a):
<<<<<<< HEAD
        if bool(a) == False:
=======
        if a:
>>>>>>> 368a269... Condition changed
            return 0
        else:
            if a[0] == "/":
                delimiter = a[2]
            else:
                delimiter = ","
            if "\n" in a:
                a = a.replace("\n", delimiter)
            if delimiter in a:
                a = a.split(delimiter)
                summary = 0
                for i in a:
                    try:
                        if int(i) > 0:
                            summary += int(i)
                        else:
                            raise ValueError("negatives not allowed")
                            continue
                    except ValueError:
                        pass
                return summary
            else:
                return int(a)




