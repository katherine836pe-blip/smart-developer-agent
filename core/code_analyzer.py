
import ast


def es_cero(node):
    """Comprueba si una expresión representa el número cero."""

    if isinstance(node, ast.Constant):
        return (
            isinstance(node.value, (int, float))
            and not isinstance(node.value, bool)
            and node.value == 0
        )

    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, (ast.USub, ast.UAdd)):
            return es_cero(node.operand)

    return False


def obtener_asignaciones(tree):
    """Obtiene las asignaciones de variables y sus valores."""

    asignaciones = {}

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):
            if es_cero(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        asignaciones.setdefault(target.id, []).append(
                            (node.lineno, True)
                        )
            else:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        asignaciones.setdefault(target.id, []).append(
                            (node.lineno, False)
                        )

        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                asignaciones.setdefault(
                    node.target.id, []
                ).append((node.lineno, es_cero(node.value)))

    return asignaciones


def analyze_code(code: str) -> dict:
    """
    Analiza código Python para detectar:
    - Código vacío.
    - Errores de sintaxis.
    - Divisiones entre cero directas.
    - Divisiones entre variables asignadas a cero.
    """

    if not code.strip():
        return {
            "valid": False,
            "syntax_valid": False,
            "message": "No se proporcionó código.",
            "line": None,
            "column": None,
            "issues": []
        }

    try:
        tree = ast.parse(code)

    except SyntaxError as error:
        return {
            "valid": False,
            "syntax_valid": False,
            "message": error.msg,
            "line": error.lineno,
            "column": error.offset,
            "issues": []
        }

    issues = []
    asignaciones = obtener_asignaciones(tree)

    for node in ast.walk(tree):

        if not isinstance(node, ast.BinOp):
            continue

        if not isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)):
            continue

        divisor = node.right
        es_division_cero = es_cero(divisor)

        # Detectar variables cuyo valor anterior es cero.
        if isinstance(divisor, ast.Name):

            historial = asignaciones.get(divisor.id, [])

            anteriores = [
                valor
                for linea, valor in historial
                if linea < node.lineno
            ]

            if anteriores:
                es_division_cero = anteriores[-1]

        if es_division_cero:
            issues.append({
                "message": "Posible división o módulo entre cero.",
                "line": node.lineno,
                "column": divisor.col_offset + 1
            })

    if issues:
        first_issue = issues[0]

        return {
            "valid": False,
            "syntax_valid": True,
            "message": first_issue["message"],
            "line": first_issue["line"],
            "column": first_issue["column"],
            "issues": issues
        }

    return {
        "valid": True,
        "syntax_valid": True,
        "message": "La sintaxis del código es correcta.",
        "line": None,
        "column": None,
        "issues": []
    }
