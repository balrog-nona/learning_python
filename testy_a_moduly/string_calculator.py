import pytest

class String_calculator:

    def add(self, a):
        if bool(a) == False:
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
                        summary += int(i)
                    except ValueError:
                        pass
                return summary
            else:
                return int(a)




