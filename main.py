
from agents.code_review_agent import CodeReviewAgent


def main():
    print("==============================")
    print("    SMART DEVELOPER AGENT")
    print("==============================")

    agent = CodeReviewAgent()

    while True:
        print("\n1. Revisar codigo")
        print("2. Salir")

        option = input("\nSelecciona una opcion: ")

        if option == "1":
            code = input("\nIngresa el codigo que deseas revisar:\n")

            if not code.strip():
                print("Error: debes ingresar codigo.")
                continue

            result = agent.review_code(code)

            print("\n===== INSTRUCCIONES DE REVISION =====")
            print(result)

        elif option == "2":
            print("Cerrando Smart Developer Agent...")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
    