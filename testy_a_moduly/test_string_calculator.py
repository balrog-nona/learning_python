import string_calculator
import pytest

cal = string_calculator.String_calculator()
print(cal.add("1\n2,3"))

def test_String_calculator():
    assert cal.add("") == 0
    assert cal.add("2") == 2
    assert cal.add("4,8") == 12
    assert cal.add("2, 5") == 7
    assert cal.add("1,2, 6, 8") == 17
    assert cal.add("1\n2,3") == 6
    assert cal.add("1\n2, 3") == 6
    assert cal.add("1\n 2,3") == 6
    assert cal.add("1 \n 2 \n 3") == 6
    assert cal.add("//;\n1;2") == 3
    assert cal.add("//:\n 1: 6") == 7
    assert cal.add("//&\n4 &6") == 10
