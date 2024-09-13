import unittest
from src.string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newlines_as_delimiters(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)

    def test_long_custom_delimiters(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_multiple_long_custom_delimiters(self):
        self.assertEqual(self.calc.add("//[**][%%]\n1**2%%3"), 6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as cm:
            self.calc.add("1,-2,3")
        self.assertEqual(str(cm.exception), "negatives not allowed: [-2]")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as cm:
            self.calc.add("1,-2,-3")
        self.assertEqual(str(cm.exception), "negatives not allowed: [-2, -3]")

    def test_ignore_large_numbers(self):
        self.assertEqual(self.calc.add("2,1001,6"), 8)

    def test_called_count(self):
        self.calc.add("1,2")
        self.calc.add("3,4")
        self.assertEqual(self.calc.get_called_count(), 2)


if __name__ == "__main__":
    unittest.main()
