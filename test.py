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

    class Test(unittest.TestCase):
        def test_discharged_matrix(self):
            self.assertEqual(discharged_matrix([[1, 2], [3, 4]]), [[0, 2], [3, 0]])

        def test_is_discharged_matrix(self):
            self.assertEqual(is_discharged_matrix([[0, 0], [3, 0]]), True)

        def test_is_discharged_matrix1(self):
            self.assertEqual(is_discharged_matrix([[1, 2], [3, 4]]), False)


if __name__ == '__main__':
    unittest.main()
