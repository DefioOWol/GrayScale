"""Summary."""
import unittest

from grayscale.shades import is_gray, to_gray


class ShadesTest(unittest.TestCase):
    """Summary."""

    def test_is_gray(self):
        """Summary."""
        self.assertTrue(is_gray('#AFAFAF'))
        self.assertTrue(is_gray('#090909'))
        self.assertFalse(is_gray('#FFFFFF'))
        self.assertFalse(is_gray('#B4C1E2'))

    def test_is_gray_exception(self):
        """Summary."""
        with self.assertRaises(ValueError):
            is_gray('%5698AC')
        with self.assertRaises(ValueError):
            is_gray('#5698AC01')
        with self.assertRaises(TypeError):
            is_gray(105232)

    def test_to_gray(self):
        """Summary."""
        self.assertTupleEqual(to_gray('#FFFFFF'), (-1, -1, -1))
        self.assertTupleEqual(to_gray('#000000'), (1, 1, 1))
        self.assertTupleEqual(to_gray('#667889'), (18, 0, -17))
        self.assertTupleEqual(to_gray('#AACA9A'), (0, -32, 16))

    def test_to_gray_exception(self):
        """Summary."""
        with self.assertRaises(ValueError):
            to_gray('BF348C')
        with self.assertRaises(ValueError):
            to_gray('#ABCD')
        with self.assertRaises(TypeError):
            to_gray(('#', '5', '5', '5', '5', '5', '5'))
