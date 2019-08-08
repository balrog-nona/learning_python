import string_calculator
import pytest

cal = string_calculator.String_calculator()

def test_String_calculator():  # komentar
    assert cal.add("") == 0
    assert cal.add("5") == 5
    assert cal.add("1, 5") == 6
    assert cal.add("4") == 4
    assert cal.add("4,8") == 12
    assert cal.add("2, 8") == 10
    assert cal.add("1,2, 6, 8") == 17
    assert cal.add("1\n2,3") == 6
    assert cal.add("1\n2, 30") == 33
    assert cal.add("1\n 2,3") == 6
    assert cal.add("1 \n 2 \n 3") == 6
    assert cal.add("//;\n1;2") == 3
    assert cal.add("//:\n 1: 6") == 7
    assert cal.add("//&\n4 &66") == 70  # komentar
    assert cal.add("//,\n2, 3, -2, 1") == 6
