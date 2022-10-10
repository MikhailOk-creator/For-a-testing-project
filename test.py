import unittest

from main import *


class MyTestCase(unittest.TestCase):
    def test_determ(self):
        self.assertEqual(determ([[1, 2], [4, 5]]), -3)

    def test_determ1(self):
        self.assertEqual(determ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)

    def test_minus(self):
        self.assertEqual(minus([[1, -2], [-3, -4]]), [[-1, 2], [3, 4]])

    def test_increase(self):
        self.assertEqual(increase([[1, -1], [-4, -8]], 5), [[5, -5], [-20, -40]])

    def test_transpose(self):
        self.assertEqual(transpose([[2, 1, 3], [3, 1, 5]]), [[2, 3], [1, 1], [3, 5]])

if __name__ == '__main__':
    unittest.main()
