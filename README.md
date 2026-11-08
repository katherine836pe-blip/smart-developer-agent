# Smart Developer Agent

**Sistema de agentes inteligentes personalizados desarrollado con Python.**

Smart Developer Agent es un proyecto que implementa un sistema modular de agentes inteligentes capaces de utilizar habilidades (*Skills*) para apoyar tareas relacionadas con el desarrollo de software.

El proyecto incorpora un agente especializado en la revisión de código Python, que permite identificar errores, analizar la calidad del código y proporcionar información sobre los problemas encontrados.

---

## 1. Objetivos del proyecto

- Implementar un sistema modular basado en agentes inteligentes.
- Incorporar habilidades mediante archivos `SKILL.md`.
- Desarrollar un agente especializado en revisión de código.
- Detectar errores de sintaxis y posibles errores lógicos.
- Identificar variables sin utilizar.
- Detectar funciones que superen una longitud recomendada.
- Implementar pruebas automatizadas para validar el funcionamiento.
- Facilitar la incorporación de nuevas funcionalidades.

## 2. Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python 3 | Lenguaje principal |
| Visual Studio Code | Entorno de desarrollo |
| Git | Control de versiones |
| GitHub | Repositorio del proyecto |
| AST | Análisis sintáctico del código Python |
| unittest | Ejecución de pruebas automatizadas |
| pathlib | Gestión de rutas y archivos |
| PowerShell | Ejecución de comandos |

## 3. Estructura del proyecto

```text
smart-developer-agent/
│
├── agents/
│   ├── __init__.py
│   └── code_review_agent.py
│
├── config/
│
├── core/
│   ├── __init__.py
│   ├── code_analyzer.py
│   ├── code_quality.py
│   └── skill_loader.py
│
├── data/
│
├── skills/
│   └── code_review/
│       └── SKILL.md
│
├── tests/
│   ├── __init__.py
│   ├── test_code_analyzer.py
│   ├── test_code_review_agent.py
│   └── test_skill_loader.py
│
├── .gitignore
├── main.py
├── probar_analyzer.py
├── requirements.txt
└── README.md
```

**Nota:** El entorno virtual `.venv` se crea localmente y no debe subirse al repositorio.

## 4. Arquitectura del sistema

El proyecto utiliza una arquitectura modular en la que cada componente tiene una responsabilidad específica.

### 4.1. Agente de revisión de código

Archivo: `agents/code_review_agent.py`

Es el componente principal encargado de coordinar el proceso de revisión.

Sus responsabilidades son:

- Cargar la Skill de revisión.
- Recibir el código Python ingresado por el usuario.
- Ejecutar el análisis de sintaxis y lógica.
- Ejecutar el análisis de calidad.
- Devolver los resultados obtenidos.

### 4.2. Cargador de Skills

Archivo: `core/skill_loader.py`

Permite localizar y cargar las habilidades del agente mediante archivos `SKILL.md`.

Sus responsabilidades son:

- Localizar el directorio de Skills.
- Identificar los archivos de habilidades.
- Leer sus instrucciones.
- Gestionar archivos o directorios inexistentes.

### 4.3. Skill Code Review

Archivo: `skills/code_review/SKILL.md`

Contiene las instrucciones que utiliza el agente para realizar la revisión del código.

Su objetivo es orientar el análisis, identificar problemas y proporcionar recomendaciones de mejora.

## 5. Analizadores implementados

### 5.1. Analizador de código

Archivo: `core/code_analyzer.py`

Utiliza el módulo estándar `ast` de Python para analizar el código.

Funcionalidades:

- Detectar código vacío.
- Identificar errores de sintaxis.
- Obtener la línea donde se encuentra el error.
- Obtener la columna correspondiente.
- Detectar divisiones o módulos entre cero cuando el divisor es un cero literal.
- Mostrar los problemas encontrados.

### 5.2. Analizador de calidad

Archivo: `core/code_quality.py`

Evalúa aspectos de calidad del código Python.

Funcionalidades:

- Identificar variables declaradas que no se utilizan.
- Detectar funciones demasiado largas.
- Indicar la línea donde se encuentra el problema.
- Generar mensajes descriptivos.
- Recomendar mejoras en la organización del código.

El analizador utiliza el módulo `ast` para recorrer la estructura del código.

El límite predeterminado para considerar una función demasiado larga es de 20 líneas.

## 6. Interfaz de usuario

Archivo: `main.py`

El sistema incorpora una interfaz de línea de comandos (CLI) que permite interactuar con el agente.

Opciones disponibles:

1. Revisar código.
2. Salir del sistema.

El usuario puede ingresar varias líneas de código Python y finalizar la entrada escribiendo `FIN` en una línea independiente.

Posteriormente, el sistema ejecuta los analizadores y presenta:

- Resultado de la revisión.
- Mensajes de errores detectados.
- Número de línea y columna.
- Resultado del análisis de calidad.
- Skill utilizada.

## 7. Instalación y configuración

### Requisitos previos

- Python 3 instalado.
- Visual Studio Code.
- Git instalado.
- Cuenta de GitHub para consultar el repositorio.

### Paso 1. Clonar el repositorio

```bash
git clone https://github.com/katherine836pe-blip/smart-developer-agent.git
```

### Paso 2. Entrar al proyecto

```bash
cd smart-developer-agent
```

### Paso 3. Crear el entorno virtual

```bash
python -m venv .venv
```

### Paso 4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Paso 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 6. Ejecutar el proyecto

```bash
python main.py
```

## 8. Pruebas del sistema

El proyecto incorpora pruebas automatizadas mediante el módulo `unittest`.

Para ejecutar las pruebas:

```bash
python -m unittest discover -s tests -v
```

Durante la validación realizada se obtuvo el siguiente resultado:

- 15 pruebas ejecutadas.
- 15 pruebas aprobadas.
- 0 pruebas fallidas.

### 8.1. Pruebas funcionales manuales

También se realizaron pruebas mediante la interfaz principal.

| Prueba | Descripción | Resultado esperado |
|---|---|---|
| 1 | Código Python correcto | Código válido |
| 2 | División entre cero | Problema lógico detectado |
| 3 | Variable sin utilizar | Advertencia de calidad |
| 4 | Error de sintaxis | Error identificado |

### 8.2. Ejemplos utilizados

**Prueba 1: Código correcto**

```python
def calcular_promedio():
    numeros = [10, 20, 30, 40, 50]
    promedio = sum(numeros) / len(numeros)
    return promedio

print(calcular_promedio())
```

**Prueba 2: División entre cero**

```python
def calcular_promedio():
    total = 100
    resultado = total / 0
    return resultado

print(calcular_promedio())
```

**Prueba 3: Variable sin utilizar**

```python
def calcular_total():
    precio = 100
    descuento = 20
    impuesto = 15

    resultado = precio - descuento

    return resultado

print(calcular_total())
```

**Prueba 4: Error de sintaxis**

```python
def saludar():
    nombre = "Kath"
    print("Hola", nombre

saludar()
```

## 9. Resultados obtenidos

Durante el desarrollo y validación del proyecto se comprobó:

- La carga de la Skill de revisión de código.
- La integración del agente con los analizadores.
- La detección de errores de sintaxis.
- La identificación de posibles divisiones entre cero.
- La identificación de problemas de calidad.
- La ejecución de pruebas automatizadas.
- La interacción mediante una interfaz CLI.
- La publicación del proyecto en GitHub.

## 10. Limitaciones actuales

El proyecto tiene algunas limitaciones que pueden mejorarse en futuras versiones:

- La detección de división entre cero se centra en divisores literales, no en todas las variables que podrían contener cero durante la ejecución.
- El análisis de variables sin utilizar es estático y puede tener limitaciones en estructuras anidadas.
- Las recomendaciones de calidad se basan en reglas predefinidas.
- Actualmente el sistema está orientado al análisis de código Python.

## 11. Mejoras futuras

- Incorporar nuevas Skills especializadas.
- Ampliar la detección de errores lógicos.
- Incorporar análisis de código en otros lenguajes.
- Implementar una interfaz web.
- Agregar generación automática de reportes.
- Incorporar recomendaciones más avanzadas.

## 12. Conclusión

Smart Developer Agent demuestra cómo desarrollar un sistema modular basado en agentes inteligentes utilizando Python.

La implementación permitió integrar un agente de revisión de código, un cargador de habilidades, analizadores de sintaxis y calidad, y pruebas automatizadas.

El proyecto representa una base para continuar desarrollando herramientas inteligentes que faciliten la revisión y mejora del código durante el proceso de desarrollo de software.

---

**Repositorio:** [Smart Developer Agent en GitHub](https://github.com/katherine836pe-blip/smart-developer-agent)

**Lenguaje principal:** Python 3

**Control de versiones:** Git y GitHub