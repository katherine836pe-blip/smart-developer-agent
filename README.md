# smart-developer-agent
Sistema de agentes inteligentes personalizados con Python
# Smart Developer Agent

## 1. Descripción del proyecto

Smart Developer Agent es un proyecto desarrollado en Python que busca implementar un agente inteligente capaz de utilizar diferentes Skills (habilidades) para apoyar tareas de desarrollo de software, comenzando con la revisión de código.

## 2. Objetivos

- Implementar un sistema modular basado en Skills.
- Identificar y cargar habilidades desde archivos `SKILL.md`.
- Desarrollar un agente encargado de preparar revisiones de código.
- Detectar posibles errores y malas prácticas mediante futuras capacidades de análisis.
- Implementar pruebas automatizadas para verificar el funcionamiento del sistema.

## 3. Tecnologías utilizadas

- Python 3.
- Git y GitHub.
- Visual Studio Code.
- pathlib: gestión de rutas y archivos.
- unittest: ejecución de pruebas automatizadas.

## 4. Estructura del proyecto

```text
smart-developer-agent/
│
├── agents/
│   └── code_review_agent.py
│
├── config/
│
├── core/
│   └── skill_loader.py
│
├── data/
│
├── skills/
│   └── code_review/
│       └── SKILL.md
│
├── tests/
│   ├── test_skill_loader.py
│   └── test_code_review_agent.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto:

```bash
cd smart-developer-agent
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 6. Pruebas automatizadas

Ejecutar las pruebas del cargador de Skills:

```bash
python -m unittest tests.test_skill_loader -v
```

Ejecutar las pruebas del agente:

```bash
python -m unittest tests.test_code_review_agent -v
```

Ejecutar todas las pruebas:

```bash
python -m unittest discover -s tests -v
```

## 7. Estado actual del proyecto

- [x] Estructura inicial del proyecto.
- [x] Implementación del cargador de Skills.
- [x] Creación de la Skill de revisión de código.
- [x] Pruebas automatizadas del cargador.
- [x] Implementación inicial del agente de revisión.
- [ ] Pruebas automatizadas del agente.
- [ ] Implementación de interfaz interactiva CLI.
- [ ] Integración de capacidades de análisis mediante IA.
- [ ] Documentación completa y validación final.

---

**Proyecto:** Smart Developer Agent  
**Lenguaje:** Python  
**Control de versiones:** Git y GitHub