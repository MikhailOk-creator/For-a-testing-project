import unittest

from main import determ, minus


class MyTestCase(unittest.TestCase):
    def test_determ(self):
        self.assertEqual(determ([[1, 2], [4, 5]]), -3)

    def test_determ1(self):
        self.assertEqual(determ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)

    def test_minus(self):
        self.assertEqual(minus([[1, -2], [-3, -4]]), [[-1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
