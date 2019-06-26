import pytest

class String_calculator:

    def add(self, a):
        if bool(a) == False:
            return 0
        else:
            if "," in a:
                a = a.split(",")
                summary = 0
                for i in a:
                    summary += int(i)
                return summary
            else:
                return int(a)




