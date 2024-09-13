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

    def test_multiple_numbers(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1,2,3,4"), 10)

    def test_newlines_as_delimiters(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        calc = StringCalculator()
        self.assertEqual(calc.add("//;\n1;2"), 3)
