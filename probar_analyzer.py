
from core.code_analyzer import analyze_code

codigo_prueba = """
def calcular_promedio():
    total = 100
    cantidad = 0
    resultado = total / cantidad
    return resultado

print(calcular_promedio())
"""

resultado = analyze_code(codigo_prueba)

print("\n===== PRUEBA DIRECTA DEL ANALIZADOR =====")
print("Válido:", resultado["valid"])
print("Sintaxis:", resultado["syntax_valid"])
print("Mensaje:", resultado["message"])
print("Problemas encontrados:", resultado["issues"])
