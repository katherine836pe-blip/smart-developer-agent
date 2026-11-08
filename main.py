
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

    codigo = "\n".join(lineas_codigo)

    return codigo


def revisar_codigo(agent):

    codigo = ingresar_codigo()

    if not codigo.strip():
        print("\n[ERROR] No ingresaste codigo para revisar.")
        return

    print("\nAnalizando codigo...")

    try:
        resultado = agent.review_code(codigo)

        analisis = resultado["analysis"]

        print("\n======================================")
        print("         RESULTADO DE REVISION")
        print("======================================")

        if analisis["valid"]:
            print("\n[OK] Codigo valido.")
            print(analisis["message"])

        else:
            print("\n[ERROR] Se encontraron problemas.")
            print("Mensaje:", analisis["message"])
            print("Linea:", analisis["line"])
            print("Columna:", analisis["column"])

        print("\n======================================")
        print("           SKILL UTILIZADA")
        print("======================================")

        print(resultado["skill"])

        print("\n======================================")
        print("        FIN DE LA REVISION")
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
