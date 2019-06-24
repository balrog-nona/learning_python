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


cal = String_calculator()

def test_String_calculator():
    assert cal.add("") == 0
    assert cal.add("2") == 2
    assert cal.add("4,8") == 12
    assert cal.add("2, 5") == 7


