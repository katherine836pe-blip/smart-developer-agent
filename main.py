
from agents.code_review_agent import CodeReviewAgent


def mostrar_menu():
    print("\n======================================")
    print("       SMART DEVELOPER AGENT")
    print("======================================")
    print("1. Revisar codigo")
    print("2. Salir")
    print("======================================")


def ingresar_codigo():
    print("\nIngresa el codigo Python que deseas revisar.")
    print("Puedes ingresar tantas lineas como necesites.")
    print("Cuando termines, escribe FIN en una linea nueva.")
    print("--------------------------------------")

    lineas_codigo = []

    while True:
        try:
            linea = input()

            if linea.strip().upper() == "FIN":
                break

            lineas_codigo.append(linea)

        except EOFError:
            break

    return "\n".join(lineas_codigo)


def mostrar_analisis(analisis):

    print("\n======================================")
    print("       ANALISIS DE SINTAXIS Y LOGICA")
    print("======================================")

    if analisis.get("valid", False):
        print("\n[OK] Codigo valido.")
        print(analisis.get("message", ""))

    else:
        print("\n[ERROR] Se encontraron problemas.")
        print("Mensaje:", analisis.get("message"))
        print("Linea:", analisis.get("line"))
        print("Columna:", analisis.get("column"))

    issues = analisis.get("issues", [])

    if issues:
        print("\nDetalles de los problemas:")

        for issue in issues:
            print("- Mensaje:", issue.get("message"))
            print("- Linea:", issue.get("line"))
            print("- Columna:", issue.get("column"))
            print("--------------------------------------")


def mostrar_calidad(calidad):

    print("\n======================================")
    print("          ANALISIS DE CALIDAD")
    print("======================================")

    if not calidad.get("valid", False):
        print("[ERROR]", calidad.get("message"))
        return

    print(calidad.get("message", ""))

    issues = calidad.get("issues", [])

    if issues:
        print("\nProblemas de calidad encontrados:")

        for issue in issues:
            print("\nTipo:", issue.get("type"))
            print("Linea:", issue.get("line"))
            print("Detalle:", issue.get("message"))

    else:
        print("\n[OK] No se encontraron problemas de calidad.")


def revisar_codigo(agent):

    codigo = ingresar_codigo()

    if not codigo.strip():
        print("\n[ERROR] No ingresaste codigo para revisar.")
        return

    print("\nAnalizando codigo...")

    try:
        resultado = agent.review_code(codigo)

        analisis = resultado.get("analysis", {})
        calidad = resultado.get("quality", {})

        print("\n======================================")
        print("          RESULTADO DE REVISION")
        print("======================================")

        mostrar_analisis(analisis)

        mostrar_calidad(calidad)

        print("\n======================================")
        print("            SKILL UTILIZADA")
        print("======================================")

        print(resultado.get("skill", "No se encontro una Skill."))

        print("\n======================================")
        print("         FIN DE LA REVISION")
        print("======================================")

    except Exception as error:
        print("\n[ERROR] No se pudo completar la revision.")
        print("Detalle:", error)


def main():

    agent = CodeReviewAgent()

    while True:

        mostrar_menu()

        opcion = input("\nSelecciona una opcion: ").strip()

        if opcion == "1":
            revisar_codigo(agent)

        elif opcion == "2":
            print("\nCerrando Smart Developer Agent...")
            break

        else:
            print("\nOpcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
