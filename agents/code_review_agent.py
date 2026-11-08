
from pathlib import Path

from core.skill_loader import load_skills


class CodeReviewAgent:
    """Agente encargado de preparar revisiones de código."""

    def __init__(self):
        # Identificar la carpeta principal del proyecto
        project_dir = Path(__file__).resolve().parent.parent

        # Cargar las Skills disponibles
        skills_dir = project_dir / "skills"
        self.skills = load_skills(skills_dir)

        # Obtener la Skill de revisión de código
        self.skill = self.skills.get("code_review")

    def review_code(self, code: str) -> str:
        """Prepara las instrucciones para revisar un código."""

        if not self.skill:
            raise ValueError("No se encontró la Skill code_review.")

        return f"""
{self.skill}

## Código que se debe revisar:

{code}
"""
