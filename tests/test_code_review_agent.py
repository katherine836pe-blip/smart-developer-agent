
import unittest

from agents.code_review_agent import CodeReviewAgent


class TestCodeReviewAgent(unittest.TestCase):

    def setUp(self):
        """Inicializa el agente antes de cada prueba."""
        self.agent = CodeReviewAgent()

    def test_skill_loaded(self):
        """Comprueba que la Skill de revisión se haya cargado."""
        self.assertIsNotNone(self.agent.skill)

    def test_review_code_includes_source_code(self):
        """Comprueba que el resultado conserve el código original."""
        code = "print('Hello World')"

        result = self.agent.review_code(code)

        self.assertIsInstance(result, dict)
        self.assertIn("code", result)
        self.assertEqual(result["code"], code)

    def test_review_code_returns_text(self):
        """Comprueba que el agente devuelva un resultado estructurado."""
        code = "print('Hello World')"

        result = self.agent.review_code(code)

        self.assertIsInstance(result, dict)

        self.assertIn("skill", result)
        self.assertIn("analysis", result)
        self.assertIn("code", result)

        self.assertIsInstance(result["skill"], str)
        self.assertIsInstance(result["analysis"], dict)
        self.assertIsInstance(result["code"], str)

    def test_review_code_analysis_structure(self):
        """Comprueba que el análisis tenga los campos necesarios."""
        code = "print('Hello World')"

        result = self.agent.review_code(code)
        analysis = result["analysis"]

        self.assertIn("valid", analysis)
        self.assertIn("message", analysis)

        self.assertIsInstance(analysis["valid"], bool)
        self.assertIsInstance(analysis["message"], str)


if __name__ == "__main__":
    unittest.main()
