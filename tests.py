import math
import unittest

from lib import *


class Test(unittest.TestCase):
    def test__mul__matrix(self):
        A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
        x = Vector([1, 2, 3])
        self.assertEqual("(14,32,50)", (A * x).__str__())
        self.assertEqual("|2,4,6|\n|8,10,12|\n|14,16,18|\n", (A * 2).__str__())

    def test__add__matrix(self):
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        B = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        self.assertEqual("|2,4,10|\n|4,8,10|\n|12,14,18|\n", (A + B).__str__())

    def test__sub__matrix(self):
        A = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        B = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        self.assertEqual("|0,0,-4|\n|0,0,0|\n|0,0,-2|\n", (A - B).__str__())


if __name__ == "__main__":
    unittest.main()
