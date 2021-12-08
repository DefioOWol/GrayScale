"""doctests.

Tests package module containing doctest tests.

Imports:
    - from doctest import testmod - to run tests

>>> from grayscale.shades import is_gray
>>> is_gray('#F0F0F0')
True
>>> is_gray('#808080')
True
>>> is_gray('#171717')
True
>>> is_gray('#231223')
False
>>> is_gray('#444444')
True
>>> is_gray('#FFFFFF')
False
>>> is_gray('#000000')
False

>>> from grayscale.shades import to_gray
>>> to_gray('#F0F0F0')
(0, 0, 0)
>>> to_gray('#231223')
(0, 17, 0)
>>> to_gray('#424536')
(0, -3, 12)
>>> to_gray('#FFFFFF')
(-1, -1, -1)
>>> to_gray('#000000')
(1, 1, 1)
>>> to_gray('#00FF00')
(1, -254, 1)
>>> to_gray('#09FBEC')
(227, -15, 0)

"""
from doctest import testmod

if __name__ == '__main__':
    testmod(verbose=True)
