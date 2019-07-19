import string_calculator
import pytest

cal = string_calculator.String_calculator()

def test_ex1():
    inputs = ['', '2', '4,18', '2, 50']
    outputs = [0, 2, 22, 52]
    for input, output in zip(inputs, outputs):
        assert cal.add(input) == output



@pytest.mark.parametrize('test_input, expected', [('', 0), ('2', 2), ('4,18', 22), ('2, 50', 52)])
def test_ex1(test_input, expected):
    assert cal.add(test_input) == expected
