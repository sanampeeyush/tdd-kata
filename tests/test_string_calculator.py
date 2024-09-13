import unittest
from src.string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calc = StringCalculator()
        self.assertEqual(calc.add(""), 0)

    def test_single_number(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1"), 1)

    def test_two_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2"), 3)
