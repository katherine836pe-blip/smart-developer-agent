
import unittest

from core.code_analyzer import analyze_code


class TestCodeAnalyzer(unittest.TestCase):

    def test_valid_code(self):
        result = analyze_code('print("Hello World")')

        self.assertTrue(result["valid"])

    def test_invalid_code(self):
        result = analyze_code('print("Hello World"')

        self.assertFalse(result["valid"])
        self.assertIsNotNone(result["line"])

    def test_empty_code(self):
        result = analyze_code("")

        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
