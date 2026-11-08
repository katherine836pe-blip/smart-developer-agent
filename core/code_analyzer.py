
import ast


def analyze_code(code: str) -> dict:
    """
    Analiza el código Python e identifica errores de sintaxis.
    """

    # Verificar que el usuario haya ingresado código
    if not code.strip():
        return {
            "valid": False,
            "message": "No se proporcionó código.",
            "line": None,
            "column": None
        }

    try:
        # Analizar la estructura del código Python
        ast.parse(code)

        return {
            "valid": True,
            "message": "La sintaxis del código es correcta.",
            "line": None,
            "column": None
        }

    except SyntaxError as error:
        return {
            "valid": False,
            "message": error.msg,
            "line": error.lineno,
            "column": error.offset
        }
