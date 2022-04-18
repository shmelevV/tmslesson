import unittest
from main import calculator


class TestCalculation(unittest.TestCase):

    def SetUp(self):
        self.calculator = calculator()

    def test_addiction(self):
        self.assertEqual(self.calculator.addition(5, 5), 10)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 7), 21)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 1)

        if __name__ == "__main__":
            unittest.main()
