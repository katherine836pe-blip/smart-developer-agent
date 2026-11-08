import unittest

from agents.code_review_agent import CodeReviewAgent


class TestCodeReviewAgent(unittest.TestCase):

    def setUp(self):
        self.agent = CodeReviewAgent()

    def test_skill_loaded(self):
        self.assertIsNotNone(self.agent.skill)

    def test_review_code_returns_text(self):
        result = self.agent.review_code("print('Hello World')")
        self.assertIsInstance(result, str)

    def test_review_code_includes_source_code(self):
        code = "print('Hello World')"
        result = self.agent.review_code(code)
        self.assertIn(code, result)


if __name__ == "__main__":
    unittest.main()