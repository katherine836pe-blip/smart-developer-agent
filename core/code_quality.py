
import ast
import builtins


class NameUsageVisitor(ast.NodeVisitor):
    """Identifica variables declaradas y utilizadas."""

    def __init__(self):
        self.assigned = {}
        self.used = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigned.setdefault(node.id, node.lineno)

        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)

    def visit_FunctionDef(self, node):
        # No entrar en funciones internas.
        return

    def visit_AsyncFunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname or alias.name.split(".")[0]
            self.assigned.setdefault(name, node.lineno)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            if alias.name != "*":
                name = alias.asname or alias.name
                self.assigned.setdefault(name, node.lineno)


def analyze_quality(code: str, max_function_lines: int = 20) -> dict:
    """
    Analiza la calidad del código Python.

    Detecta:
    - Variables sin utilizar.
    - Variables no definidas.
    - Funciones demasiado largas.
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
    builtins_names = set(dir(builtins))

    # Obtener las variables y nombres definidos en el módulo.
    module_visitor = NameUsageVisitor()

    for statement in tree.body:
        if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef,
                                  ast.ClassDef)):
            module_visitor.assigned.setdefault(
                statement.name, statement.lineno
            )
        else:
            module_visitor.visit(statement)

    global_names = set(module_visitor.assigned)

    # Detectar nombres utilizados pero no definidos en el módulo.
    for name in module_visitor.used:
        if name not in global_names and name not in builtins_names:
            issues.append({
                "type": "undefined_variable",
                "line": 1,
                "column": None,
                "message": (
                    f"El nombre '{name}' se utiliza "
                    "pero no está definido."
                )
            })

    # Analizar cada función.
    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            function_lines = node.end_lineno - node.lineno + 1

            if function_lines > max_function_lines:
                issues.append({
                    "type": "long_function",
                    "line": node.lineno,
                    "column": None,
                    "message": (
                        f"La función '{node.name}' tiene "
                        f"{function_lines} líneas. "
                        f"El máximo recomendado es "
                        f"{max_function_lines}."
                    )
                })

            visitor = NameUsageVisitor()

            # Las funciones no deben considerar sus parámetros
            # como variables sin utilizar.
            arguments = (
                node.args.posonlyargs
                + node.args.args
                + node.args.kwonlyargs
            )

            parameter_names = {
                argument.arg for argument in arguments
            }

            if node.args.vararg:
                parameter_names.add(node.args.vararg.arg)

            if node.args.kwarg:
                parameter_names.add(node.args.kwarg.arg)

            for statement in node.body:
                visitor.visit(statement)

            local_names = set(visitor.assigned) | parameter_names

            # Detectar variables locales sin utilizar.
            for name, line in visitor.assigned.items():

                if (
                    name not in visitor.used
                    and name not in parameter_names
                    and not name.startswith("_")
                ):
                    issues.append({
                        "type": "unused_variable",
                        "line": line,
                        "column": None,
                        "message": (
                            f"La variable '{name}' "
                            "está declarada pero no se utiliza."
                        )
                    })

            # Detectar variables utilizadas pero no definidas.
            for name in visitor.used:

                if (
                    name not in local_names
                    and name not in global_names
                    and name not in builtins_names
                ):
                    issues.append({
                        "type": "undefined_variable",
                        "line": node.lineno,
                        "column": None,
                        "message": (
                            f"El nombre '{name}' se utiliza "
                            "pero no está definido."
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
