import string_calculator
import pytest

cal = string_calculator.String_calculator()

def test_ex1v1(): #v1 stands for version 1
    inputs = ['', '2', '4,18', '2, 50']
    outputs = [0, 2, 22, 52]
    for input, output in zip(inputs, outputs):
        assert cal.add(input) == output

def test_ex2v1():
    inputs = ['6, 7, 2', '4, 4, 4,9', '0,0, 1, 1, 1']
    outputs = [15, 21, 3]
    for input, output in zip(inputs, outputs):
        assert cal.add(input) == output

def test_ex3v1():
    inputs = ['60\n3, 8\n1', '1\n0,6\n30, 4']
    outputs = [72, 41]
    for input, output in zip(inputs, outputs):
        assert cal.add(input) == output



@pytest.mark.parametrize('test_input, expected', [('', 0), ('2', 2), ('4,18', 22), ('2, 50', 52)])
def test_ex1(test_input, expected):
    assert cal.add(test_input) == expected

@pytest.mark.parametrize('test_input, expected', [('6, 7, 2', 15), ('4,4,4, 9', 21), ('0,0, 1, 1, 1', 3)])
def test_ex2(test_input, expected):
    assert cal.add(test_input) == expected

@pytest.mark.parametrize('test_input, expected', [('6\n70\n2', 78), ('4,4\n4, 9', 21)])
def test_ex3(test_input, expected):
    assert cal.add(test_input) == expected