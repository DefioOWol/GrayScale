"""Summary."""
import pytest
from grayscale.shades import is_gray, to_gray


@pytest.mark.parametrize('color, result', [
    ('#101010', True), ('#AAAAAA', True), ('#424242', True),
    ('#000000', False), ('#FFFFFF', False), ('#172486', False)
])
def test_is_gray(color, result):
    """Summary."""
    assert is_gray(color) == result


@pytest.mark.parametrize('color, exception', [
    (123456, TypeError), ('#HHHHHH', ValueError),
    (['#', 'F', '0', 'F', '0', 'F', '0'], TypeError),
    ('808080', ValueError), ('#80808', ValueError)
])
def test_is_gray_exceptions(color, exception):
    """Summary."""
    with pytest.raises(exception):
        is_gray(color)


@pytest.mark.parametrize('color, result', [
    ('#FFFFFF', (-1, -1, -1)), ('#000000', (1, 1, 1)),
    ('#121416', (2, 0, -2)), ('#808080', (0, 0, 0)),
    ('#CCCCCC', (0, 0, 0))
])
def test_to_gray(color, result):
    """Summary."""
    assert to_gray(color) == result


@pytest.mark.parametrize('color, exception', [
    (235479, TypeError), ('#QWORTY', ValueError),
    (['#', '1', '7', '1', '7', '1', '7'], TypeError),
    ('325427', ValueError), ('#AFF0BC4', ValueError)
])
def test_to_gray_exceptions(color, exception):
    """Summary."""
    with pytest.raises(exception):
        to_gray(color)
