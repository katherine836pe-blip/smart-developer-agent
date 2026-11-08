
import tempfile
import unittest
from pathlib import Path

from core.skill_loader import load_skills


class TestSkillLoader(unittest.TestCase):

    def test_load_skill_correctly(self):
        with tempfile.TemporaryDirectory() as temp:
            skills_dir = Path(temp)
            skill_folder = skills_dir / "code_review"
            skill_folder.mkdir()

            skill_file = skill_folder / "SKILL.md"
            skill_file.write_text(
                "# Code Review",
                encoding="utf-8"
            )

            result = load_skills(skills_dir)

            self.assertIn("code_review", result)
            self.assertEqual(result["code_review"], "# Code Review")

    def test_missing_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            missing_dir = Path(temp) / "missing"

            result = load_skills(missing_dir)

            self.assertEqual(result, {})

    def test_missing_skill_file(self):
        with tempfile.TemporaryDirectory() as temp:
            skills_dir = Path(temp)
            skill_folder = skills_dir / "code_review"
            skill_folder.mkdir()

            result = load_skills(skills_dir)

            self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
