
 
#import unittest
#import calc

#class TestCalc(unittest.TestCase):
    
#    def test_add(self):
#        result = calc.add(10, 5)
#        self.assertEqual(result, 15)


#if __name__ == '__main__':
#    unittest.main()

# 1st try   Copyright (C) Microsoft Corporation. All rights reserved.

#Try the new cross-platform PowerShell https://aka.ms/pscore6

#PS S:\BMI6017\week6> conda activate "Basics Packages"
#PS S:\BMI6017\week6> & "C:/Users/Robert/.conda/envs/Basics Packages/python.exe" s:/BMI6017/Week6/exerPythUnitTest/test_calc.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s

#OK
#PS S:\BMI6017\week6>  """

#import unittest
#import calc

#class TestCalc(unittest.TestCase):
    
#    def test_add(self):
#        result = calc.add(10, 5)
#        self.assertEqual(result, 14)


#if __name__ == '__main__':
#    unittest.main()

#Ran 1 test in 0.002s

#FAILED (failures=1)
#PS S:\BMI6017\week6>

""" import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()
    
    
Ran 4 tests in 0.000s

OK  
    """

"""import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2, 2)) #with // in Calc


if __name__ == '__main__':
    unittest.main()

    Ran 4 tests in 0.001s
"""

"""import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        #self.assertEqual(calc.divide(5, 2, 2)) #with // in Calc

        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()

    Ran 4 tests in 0.000s

OK"""

"""import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(1, -1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        #self.assertEqual(calc.divide(5, 2, 2)) #with // in Calc

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
Ran 4 tests in 0.000s

OK"""