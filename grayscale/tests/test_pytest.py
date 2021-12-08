"""test_pytest.

A module of the tests package containing pytest tests of the
is_gray and to_gray functions.

Imports:
    - import pytest - to implement tests
    - from grayscale.shades import is_gray, to_gray - tested functions

Functions:
    - test_is_gray(color, result) - testing the is_gray function
    - test_is_gray_exceptions(color, exception) - testing the is_gray
        function for exceptions
    - test_to_gray(color, result) - testing the to_gray function
    - test_to_gray_exceptions(color, exception) - testing the to_gray
        function for exceptions

"""
import pytest
from grayscale.shades import is_gray, to_gray


@pytest.mark.parametrize('color, result', [
    ('#101010', True), ('#AAAAAA', True), ('#424242', True),
    ('#000000', False), ('#FFFFFF', False), ('#172486', False)
])
def test_is_gray(color, result):
    """Testing the is_gray function.

    Arguments:
        - color - color code
        - result - expected result

    """
    assert is_gray(color) == result


@pytest.mark.parametrize('color, exception', [
    (123456, TypeError), ('#HHHHHH', ValueError),
    (['#', 'F', '0', 'F', '0', 'F', '0'], TypeError),
    ('808080', ValueError), ('#80808', ValueError)
])
def test_is_gray_exceptions(color, exception):
    """Testing the is_gray function for exceptions.

    Arguments:
        - color - color code
        - exception - expected exception

    """
    with pytest.raises(exception):
        is_gray(color)


@pytest.mark.parametrize('color, result', [
    ('#FFFFFF', (-1, -1, -1)), ('#000000', (1, 1, 1)),
    ('#121416', (2, 0, -2)), ('#808080', (0, 0, 0)),
    ('#CCCCCC', (0, 0, 0))
])
def test_to_gray(color, result):
    """Testing the to_gray function.

    Arguments:
        - color - color code
        - result - expected result

    """
    assert to_gray(color) == result


@pytest.mark.parametrize('color, exception', [
    (235479, TypeError), ('#QWORTY', ValueError),
    (['#', '1', '7', '1', '7', '1', '7'], TypeError),
    ('325427', ValueError), ('#AFF0BC4', ValueError)
])
def test_to_gray_exceptions(color, exception):
    """Testing the to_gray function for exceptions.

    Arguments:
        - color - color code
        - exception - expected exception

    """
    with pytest.raises(exception):
        to_gray(color)
