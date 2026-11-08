
from pathlib import Path

# Importar los módulos del proyecto
from core.skill_loader import load_skills
from core.code_analyzer import analyze_code
from core.code_quality import analyze_quality


class CodeReviewAgent:
    """Agente encargado de revisar código Python."""

    def __init__(self):

        # 1. Identificar la carpeta principal del proyecto
        self.project_dir = Path(__file__).resolve().parent.parent

        # 2. Localizar la carpeta de Skills
        self.skills_dir = self.project_dir / "skills"

        # 3. Cargar las Skills disponibles
        self.skills = load_skills(self.skills_dir)

        # 4. Obtener la Skill de revisión
        self.skill = self.skills.get("code_review")

    def review_code(self, code: str) -> dict:
        """
        Analiza el código utilizando Code Analyzer
        y Code Quality.
        """

        # 5. Comprobar que exista la Skill
        if not self.skill:
            raise ValueError(
                "No se encontró la Skill code_review."
            )

        # 6. Ejecutar el análisis de sintaxis y lógica
        analysis = analyze_code(code)

        # 7. Ejecutar el análisis de calidad
        quality = analyze_quality(code)

        # 8. Devolver todos los resultados
        return {
            "skill": self.skill,
            "analysis": analysis,
            "quality": quality,
            "code": code
        }
