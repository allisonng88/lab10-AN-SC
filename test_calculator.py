import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1,0),-1)
        self.assertNotEqual(add(7,6),14)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 3), 1)
        self.assertEqual(subtract(-1, 0), 1)
        self.assertNotEqual(subtract(7, 6), 1)
    ##########################

    # Partner 1: Allison Ng
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-7, -7), 49)
        self.assertNotEqual(mul(0,7), 7)
        self.assertEqual(mul(1,-1), -1)

    def test_divide(self): # 3 assertions
        self.assertNotEqual(div(2,8), 0)
        self.assertEqual(div(1,8), 8)
        self.assertEqual(div(-1,8), -8)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        self.assertRaises(ZeroDivisionError, div, 0,6)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,32),5)
        self.assertEqual(logarithm(3,9),2)
        self.assertNotEqual(logarithm(2,32),4)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertRaises(ValueError, logarithm, 0, 22)
    ##########################
    
    # Partner 1: Allison Ng
    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm, 0, 5)
        self.assertEqual(logarithm(10,10), 1)
        self.assertEqual(logarithm(10,1), 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertNotEqual(hypotenuse(0,2), 0)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertRaises(ValueError, square_root, -4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()