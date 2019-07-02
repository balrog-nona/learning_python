import string_calculator
import pytest

cal = string_calculator.StringCalculator()
#print(cal.add("//,5,6,-4,-2"))

def test_StringCalculator():
    assert cal.add("") == 0
    assert cal.add("2") == 2
    assert cal.add("4,8") == 12
    assert cal.add("2, 5") == 7
    assert cal.add("1,2, 6, 8") == 17
    assert cal.add("1\n2,3") == 6
    assert cal.add("1\n2, 3") == 6
    assert cal.add("1\n 2,3") == 6
    assert cal.add("1 \n 2 \n 3") == 6
    assert cal.add("//[;]\n1;2") == 3
    assert cal.add("//[::]\n 1:: 6") == 7
    assert cal.add("//[&&&]\n4 &&&6") == 10
    with pytest.raises(Exception) as error:
        cal.add("//[,]\n2, 3, -2, 1")
        assert "-2" in str(error.value)
    with pytest.raises(Exception) as error:
        cal.add("//[:]\n 1:4:-6:-7:3:-1")
        assert "-6 -7 -1" in str(error.value)
    assert cal.add("//[:]\n 2:6:10:1001") == 18
    assert cal.add("//[;]\n2; 7; 50; 1001") == 59
    assert cal.add("//[*****]\n1*****2 *****3") == 6
    assert cal.add("//[*][.]\n 2.55.6 * 520*11* 3 . 1") == 598



"""
def test_get_called_count():
    cal.add("2, 6, 4")
    cal.add("1, 2, 5")
    assert cal.get_called_count() == 2
"""