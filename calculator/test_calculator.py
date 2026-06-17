
import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("1 + 2"), 3)
        self.assertEqual(self.calculator.evaluate("10 + -5"), 5)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("5 - 2"), 3)
        self.assertEqual(self.calculator.evaluate("2 - 5"), -3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("2 * 3"), 6)
        self.assertEqual(self.calculator.evaluate("-2 * 3"), -6)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("6 / 3"), 2)
        self.assertEqual(self.calculator.evaluate("7 / 2"), 3.5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("5 / 0")

    def test_precedence(self):
        self.assertEqual(self.calculator.evaluate("1 + 2 * 3"), 7)
        self.assertEqual(self.calculator.evaluate("(1 + 2) * 3"), 9)
        self.assertEqual(self.calculator.evaluate("10 - 4 / 2"), 8)

    def test_parentheses(self):
        self.assertEqual(self.calculator.evaluate("(1 + 2) * (3 + 4)"), 21)
        self.assertEqual(self.calculator.evaluate("((1 + 2) * 3) + 4"), 13)
        with self.assertRaises(ValueError):
            self.calculator.evaluate("((1 + 2)")
        with self.assertRaises(ValueError):
            self.calculator.evaluate("(1 + 2))")

    def test_empty_expression(self):
        self.assertIsNone(self.calculator.evaluate(""))
        self.assertIsNone(self.calculator.evaluate("   "))

    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("1 $ 2")

    def test_invalid_tokens(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("1 two 3")

    def test_negative_numbers(self):
        self.assertEqual(self.calculator.evaluate("-1 + 2"), 1)
        self.assertEqual(self.calculator.evaluate("3 * -4"), -12)
        self.assertEqual(self.calculator.evaluate("1 - -2"), 3)

    def test_floating_point_numbers(self):
        self.assertEqual(self.calculator.evaluate("1.5 + 2.5"), 4.0)
        self.assertEqual(self.calculator.evaluate("4.5 / 1.5"), 3.0)

    def test_multiple_digit_numbers(self):
        self.assertEqual(self.calculator.evaluate("10 + 20"), 30)
        self.assertEqual(self.calculator.evaluate("123 - 45"), 78)

    def test_complex_expressions(self):
        self.assertEqual(self.calculator.evaluate("1 + 2 * 3 - 4 / 2 + (5 - 1)"), 1 + 6 - 2 + 4)
        self.assertEqual(self.calculator.evaluate("10 / 2 + 3 * (6 - 4)"), 5 + 3 * 2)

if __name__ == "__main__":
    unittest.main()
