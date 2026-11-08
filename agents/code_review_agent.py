
from pathlib import Path

from core.skill_loader import load_skills
from core.code_analyzer import analyze_code


class CodeReviewAgent:
    """Agente encargado de revisar código Python."""

    def __init__(self):
        # Identificar la carpeta principal del proyecto
        project_dir = Path(__file__).resolve().parent.parent

        # Cargar las Skills disponibles
        skills_dir = project_dir / "skills"
        self.skills = load_skills(skills_dir)

        # Obtener la Skill de revisión
        self.skill = self.skills.get("code_review")

    def review_code(self, code: str) -> dict:
        """Analiza código y prepara una revisión."""

        if not self.skill:
            raise ValueError(
                "No se encontró la Skill code_review."
            )

        # Ejecutar el analizador de código
        analysis = analyze_code(code)

        return {
            "skill": self.skill,
            "analysis": analysis,
            "code": code
        }
