
import unittest

from core.code_analyzer import analyze_code


class TestCodeAnalyzer(unittest.TestCase):

    # Prueba 1: Código correcto
    def test_valid_code(self):
        result = analyze_code('print("Hello World")')

        self.assertTrue(result["valid"])
        self.assertEqual(
            result["message"],
            "La sintaxis del código es correcta."
        )

    # Prueba 2: Código con errores
    def test_invalid_code(self):
        result = analyze_code('print("Hello World"')

        self.assertFalse(result["valid"])
        self.assertIsNotNone(result["line"])
        self.assertIsNotNone(result["column"])

    # Prueba 3: Código vacío
    def test_empty_code(self):
        result = analyze_code("")

        self.assertFalse(result["valid"])
        self.assertEqual(
            result["message"],
            "No se proporcionó código."
        )

    # Prueba 4: Código con espacios
    def test_whitespace_code(self):
        result = analyze_code("   ")

        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()

