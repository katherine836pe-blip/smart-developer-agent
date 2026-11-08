# Smart Developer Agent

**Sistema de agentes inteligentes personalizados desarrollado con Python.**

## 1. Descripción del proyecto

Smart Developer Agent es un proyecto desarrollado en Python que implementa un sistema modular de agentes inteligentes capaces de utilizar diferentes Skills (habilidades) para apoyar tareas relacionadas con el desarrollo de software.

El proyecto comienza con un agente especializado en la revisión de código Python, capaz de analizar la sintaxis, identificar errores y preparar recomendaciones para mejorar la calidad del código.

Su arquitectura permite incorporar nuevas habilidades y funcionalidades de manera independiente.

## 2. Objetivos del proyecto

- Implementar un sistema modular basado en agentes inteligentes y Skills.
- Identificar y cargar habilidades desde archivos `SKILL.md`.
- Desarrollar un agente especializado en revisión de código.
- Analizar código Python mediante herramientas de análisis sintáctico.
- Detectar errores de sintaxis y proporcionar información sobre su ubicación.
- Proponer mejoras y recomendaciones de programación.
- Implementar pruebas automatizadas para validar el funcionamiento del sistema.
- Facilitar la incorporación de nuevas funcionalidades.

## 3. Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python 3 | Lenguaje principal |
| Visual Studio Code | Entorno de desarrollo |
| Git | Control de versiones |
| GitHub | Almacenamiento y colaboración |
| pathlib | Gestión de rutas y archivos |
| ast | Análisis sintáctico de código Python |
| unittest | Pruebas automatizadas |
| PowerShell | Ejecución de comandos |

## 4. Estructura del proyecto

```text
smart-developer-agent/
│
├── .venv/
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
├── requirements.txt
└── README.md
```

## 5. Funcionalidades implementadas

### 5.1. Sistema modular de Skills

Permite organizar las habilidades del agente mediante archivos `SKILL.md`.

Cada Skill contiene instrucciones específicas para realizar una tarea determinada.

### 5.2. Cargador de Skills

Implementado en `core/skill_loader.py`.

Responsabilidades:

- Localizar el directorio de Skills.
- Identificar los archivos `SKILL.md`.
- Leer y cargar las instrucciones.
- Gestionar directorios o archivos inexistentes.

### 5.3. Agente de revisión de código

Implementado en `agents/code_review_agent.py`.

Responsabilidades:

- Cargar la Skill de revisión de código.
- Recibir código Python para su revisión.
- Preparar instrucciones de análisis.
- Incorporar las instrucciones de la habilidad correspondiente.

### 5.4. Analizador de código Python

Implementado en `core/code_analyzer.py`.

Funcionalidades actuales:

- Analizar la sintaxis del código Python.
- Identificar errores sintácticos.
- Obtener el número de línea del error.
- Obtener la posición de la columna.
- Informar cuando el código tiene una sintaxis correcta.

El análisis se realiza mediante el módulo estándar `ast` de Python.

### 5.5