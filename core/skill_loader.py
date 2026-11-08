
from pathlib import Path


def load_skills(skills_dir: Path) -> dict[str, str]:
    """
    Busca y carga las Skills disponibles.

    Cada Skill debe estar dentro de una carpeta
    y contener un archivo llamado SKILL.md.
    """

    loaded_skills = {}

    if not skills_dir.exists():
        return loaded_skills

    for skill_folder in skills_dir.iterdir():

        if skill_folder.is_dir():

            skill_file = skill_folder / "SKILL.md"

            if skill_file.exists():

                content = skill_file.read_text(
                    encoding="utf-8"
                )

                loaded_skills[skill_folder.name] = content

    return loaded_skills
