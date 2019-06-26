import string_calculator
import pytest

cal = string_calculator.String_calculator()

def test_String_calculator():
    assert cal.add("") == 0
    assert cal.add("2") == 2
    assert cal.add("4,8") == 12
    assert cal.add("2, 5") == 7
    assert cal.add("1,2, 6, 8") == 17