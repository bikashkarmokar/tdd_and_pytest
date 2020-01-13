from arithmatic_function import *


def test_is_multiple_of_five():
    assert is_multiple_of_five(5) == True
    assert is_multiple_of_five(50) == True
    assert is_multiple_of_five(0) == False
    assert is_multiple_of_five(-10) == False


def test_inc():
    assert inc(3) == 4