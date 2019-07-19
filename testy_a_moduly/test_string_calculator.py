import string_calculator
import pytest

cal = string_calculator.StringCalculator()


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


list = [('//[;]\n1; 4\n 50', 55), ('//[~]\n5~200', 205)]  #nevyhodou je, ze to je gloalni promenna
@pytest.mark.parametrize('test_input, expected', list)
def test_ex4(test_input, expected):
    assert cal.add(test_input) == expected


def test_ex5():
    with pytest.raises(Exception) as error:
        cal.add('//[:]\n3: 8:-6: 2')
        assert "-6" in str(error.value)
    with pytest.raises(Exception) as error:
        cal.add('//[&]\n9& -1&68& 23')
        assert "-1" in str(error.value)


def test_ex6():
    with pytest.raises(Exception) as error:
        cal.add('//[.]\n3. -77.-6. 2')
        assert "-77, -6" in str(error.value)
    with pytest.raises(Exception) as error:
        cal.add('//[!]\n-9!1!6008! -235!-55')
        assert "-9, -235, -55" in str(error.value)


def test_get_called_count():
    assert cal.get_called_count() == 24


@pytest.mark.parametrize('test_input, expected', [('//[=]\n6= 55= 1001\n4', 65), ('4,4\n4, 9000', 12)])
def test_ex9(test_input, expected):
    assert cal.add(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [('//[***]\n1***1000*** 45', 1046), ('//[^^]\n3^^ 9 ^^ 100', 112)])
def test_ex10(test_input, expected):
    assert cal.add(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [('//[*][%]\n11* 32%100 % 4 * 1001', 147), \
                                                  ('//[+][-]\n22\n5+ 50-4\n 110-0+1\n1', 193)])
def test_ex11(test_input, expected):
    assert cal.add(test_input) == expected


@pytest.mark.parametrize('test_input, expected', [('//[***][.....]\n11*** 32.....100 ..... 4 *** 1001.....0', 147), \
                                                  ('//[+][---]\n22\n5+ 50---4\n 110---0+1\n1+1 --- 1004', 194)])
def test_ex12(test_input, expected):
    assert cal.add(test_input) == expected