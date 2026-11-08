
import unittest

from core.code_quality import analyze_quality


class TestCodeQuality(unittest.TestCase):

    def test_unused_variable(self):
        code = """
def ejemplo():
    nombre = "Kath"
    return 10
"""
        result = analyze_quality(code)

        self.assertTrue(result["valid"])
        self.assertTrue(
            any(
                issue["type"] == "unused_variable"
                for issue in result["issues"]
            )
        )

    def test_long_function(self):
        code = """
def ejemplo():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
"""
        result = analyze_quality(
            code,
            max_function_lines=3
        )

        self.assertTrue(
            any(
                issue["type"] == "long_function"
                for issue in result["issues"]
            )
        )

    def test_valid_quality_code(self):
        code = """
def sumar():
    resultado = 10 + 5
    return resultado
"""
        result = analyze_quality(code)

        self.assertTrue(result["valid"])
        self.assertEqual(len(result["issues"]), 0)

    def test_invalid_syntax(self):
        code = "def ejemplo(:"

        result = analyze_quality(code)

        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()
