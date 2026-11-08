
import ast


class NameUsageVisitor(ast.NodeVisitor):
    """Identifica variables asignadas y utilizadas."""

    def __init__(self):
        self.assigned = {}
        self.used = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigned.setdefault(node.id, node.lineno)

        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)

    def visit_FunctionDef(self, node):
        # No analizar funciones internas en este recorrido.
        return

    def visit_AsyncFunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return


def analyze_quality(code: str, max_function_lines: int = 20) -> dict:
    """
    Analiza la calidad del código Python.

    Detecta variables sin utilizar y funciones demasiado largas.
    """

    if not code.strip():
        return {
            "valid": False,
            "message": "No se proporcionó código.",
            "issues": []
        }

    try:
        tree = ast.parse(code)

    except SyntaxError as error:
        return {
            "valid": False,
            "message": error.msg,
            "issues": []
        }

    issues = []

    # Analizar las funciones
    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            # Calcular la longitud de la función
            function_lines = (
                node.end_lineno - node.lineno + 1
            )

            if function_lines > max_function_lines:
                issues.append({
                    "type": "long_function",
                    "line": node.lineno,
                    "message": (
                        f"La función '{node.name}' tiene "
                        f"{function_lines} líneas. "
                        f"El máximo recomendado es "
                        f"{max_function_lines}."
                    )
                })

            # Revisar variables locales
            visitor = NameUsageVisitor()

            for statement in node.body:
                visitor.visit(statement)

            for name, line in visitor.assigned.items():

                if name not in visitor.used and not name.startswith("_"):
                    issues.append({
                        "type": "unused_variable",
                        "line": line,
                        "message": (
                            f"La variable '{name}' "
                            "está declarada pero no se utiliza."
                        )
                    })

    return {
        "valid": True,
        "message": (
            "Análisis de calidad completado."
            if issues else
            "No se encontraron problemas de calidad."
        ),
        "issues": issues
    }
