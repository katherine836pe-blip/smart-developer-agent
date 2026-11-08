
import ast


def analyze_code(code: str) -> dict:
    """
    Analiza código Python para detectar:
    - Código vacío.
    - Errores de sintaxis.
    - Posibles divisiones entre cero.
    """

    # 1. Comprobar que exista código
    if not code.strip():
        return {
            "valid": False,
            "syntax_valid": False,
            "message": "No se proporcionó código.",
            "line": None,
            "column": None,
            "issues": []
        }

    # 2. Comprobar la sintaxis
    try:
        tree = ast.parse(code)

    except SyntaxError as error:
        return {
            "valid": False,
            "syntax_valid": False,
            "message": error.msg,
            "line": error.lineno,
            "column": error.offset,
            "issues": [
                f"Error de sintaxis: {error.msg}"
            ]
        }

    # 3. Buscar posibles errores de lógica
    issues = []

    for node in ast.walk(tree):

        if isinstance(node, ast.BinOp):

            # Revisar divisiones, divisiones enteras y módulos
            if isinstance(
                node.op,
                (ast.Div, ast.FloorDiv, ast.Mod)
            ):

                divisor = node.right

                # Detectar cero directo: 10 / 0
                es_cero = (
                    isinstance(divisor, ast.Constant)
                    and isinstance(divisor.value, (int, float))
                    and not isinstance(divisor.value, bool)
                    and divisor.value == 0
                )

                # Detectar cero negativo: 10 / -0
                if (
                    isinstance(divisor, ast.UnaryOp)
                    and isinstance(divisor.op, (ast.USub, ast.UAdd))
                    and isinstance(divisor.operand, ast.Constant)
                    and isinstance(divisor.operand.value, (int, float))
                    and not isinstance(divisor.operand.value, bool)
                    and divisor.operand.value == 0
                ):
                    es_cero = True

                if es_cero:
                    issues.append({
                        "message": "Posible división o módulo entre cero.",
                        "line": node.lineno,
                        "column": node.col_offset + 1
                    })

    # 4. Si se encontraron problemas
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

    # 5. Si no se encontraron problemas
    return {
        "valid": True,
        "syntax_valid": True,
        "message": "La sintaxis del código es correcta.",        "line": None,
        "column": None,
        "issues": []
    }
