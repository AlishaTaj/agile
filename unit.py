import unittest
import math

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def squareroot(self, a):
        return math.sqrt(a)
    def multiply(self, a, b):
        return a * b

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition(self):
        result = self.calculator.add(2, 2)
        self.assertEqual(result, 4)
    def test_subtraction(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
    def test_squareroot(self):
        result = self.calculator.squareroot(16)
        self.assertEqual(result, 4)
    def test_multiplication(self):
        result = self.calculator.multiply(3, 4)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()