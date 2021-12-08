"""test_unittest.

A module of the tests package containing unittest tests of the
is_gray and to_gray functions.

Imports:
    - import unittest - to implement tests
    - from grayscale.shades import is_gray, to_gray - tested functions

Classes:
    - ShadesTest - unittest class of tests

"""
import unittest

from grayscale.shades import is_gray, to_gray


class ShadesTest(unittest.TestCase):
    """Unittest class of tests.

    Methods:
        - test_is_gray() - testing the is_gray function
        - test_is_gray_exception() - testing the is_gray function
            for exceptions
        - test_to_gray() - testing the to_gray function
        - test_to_gray_exception() - testing the to_gray function
            for exceptions

    """

    def test_is_gray(self):
        """Testing the is_gray function."""
        self.assertTrue(is_gray('#AFAFAF'))
        self.assertTrue(is_gray('#090909'))
        self.assertFalse(is_gray('#FFFFFF'))
        self.assertFalse(is_gray('#B4C1E2'))

    def test_is_gray_exception(self):
        """Testing the is_gray function for exceptions."""
        with self.assertRaises(ValueError):
            is_gray('%5698AC')
        with self.assertRaises(ValueError):
            is_gray('#5698AC01')
        with self.assertRaises(TypeError):
            is_gray(105232)

    def test_to_gray(self):
        """Testing the to_gray function."""
        self.assertTupleEqual(to_gray('#FFFFFF'), (-1, -1, -1))
        self.assertTupleEqual(to_gray('#000000'), (1, 1, 1))
        self.assertTupleEqual(to_gray('#667889'), (18, 0, -17))
        self.assertTupleEqual(to_gray('#AACA9A'), (0, -32, 16))

    def test_to_gray_exception(self):
        """Testing the to_gray function for exceptions."""
        with self.assertRaises(ValueError):
            to_gray('BF348C')
        with self.assertRaises(ValueError):
            to_gray('#ABCD')
        with self.assertRaises(TypeError):
            to_gray(('#', '5', '5', '5', '5', '5', '5'))
