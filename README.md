# 📌 Sistema Empresarial — Catálogo de Ítems en Django

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/uso-académico-lightgrey)

Proyecto de laboratorio desarrollado para el curso de **Desarrollo de Aplicaciones Empresariales**. Implementa un sistema empresarial para la gestión y visualización de un catálogo de ítems, utilizando arquitectura **MVT**, interfaz optimizada, filtro dinámico en tiempo real y consumo de **API REST**.

## Índice

- [Tecnologías y prerrequisitos](#️-tecnologías-y-prerrequisitos)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación](#️-instalación)
- [Ejecución](#-ejecución)
- [API](#-api)

## 🛠️ Tecnologías y prerrequisitos

**Prerrequisitos**

| Herramienta | Notas |
|---|---|
| Python 3.10+ | Marcar **"Add Python to PATH"** durante la instalación |
| Git | Para clonar el repositorio |
| Visual Studio Code | Editor recomendado |

**Stack utilizado**

| Capa | Tecnología |
|---|---|
| Framework web | Django 6.1 |
| Frontend | HTML5, CSS3 & JavaScript (Vanilla) |
| Base de datos | SQLite3 |

## 📁 Estructura del proyecto

```text
django_project/
├── .gitignore              # Ignora el entorno virtual .venv y archivos temporales
├── README.md                # Documentación oficial
│
└── src/                      # Código fuente del proyecto
    ├── manage.py              # Script principal (servidor y migraciones)
    ├── requirements.txt       # Dependencias del proyecto
    │
    ├── config/                 # Configuración global de Django
    │   ├── settings.py          # Apps, base de datos, archivos estáticos
    │   ├── urls.py               # Enrutador principal de URLs
    │   └── wsgi.py                # Configuración de despliegue
    │
    └── core/                    # Aplicación principal del catálogo
        ├── models.py             # Modelo de datos de los ítems
        ├── views.py               # Lógica de negocio y endpoints de la API
        ├── urls.py                 # Rutas del catálogo y de la API
        └── templates/core/          # Plantillas HTML
            ├── base.html            # Estructura base, navegación y footer
            └── item_list.html        # Catálogo interactivo con buscador
```

## ⚙️ Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/yoselin55/django-sistema-empresarial01.git
cd django_project
```

**2. Crear y activar el entorno virtual**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instalar las dependencias**

```bash
pip install --upgrade pip
pip install -r src/requirements.txt
```

## 🚀 Ejecución

**1. Aplicar las migraciones de la base de datos**

```bash
cd src
python manage.py migrate
```

**2. Iniciar el servidor de desarrollo**

```bash
python manage.py runserver
```

**3. Abrir la aplicación en el navegador**

Abre tu navegador e ingresa a las rutas locales del proyecto:

| Ruta | URL |
|---|---|
| Catálogo Principal (Inicio) | http://128.0.0.1:8000/ |
| Panel Administrativo | http://128.0.0.1:8000/admin/ |

## 📡 API
| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Vista del catálogo con buscador |
| `GET` | `/api/items/` | Lista de ítems en JSON, ordenados por fecha de creación |
| `GET` | `/api-demo/` | Página de demostración de consumo de la API |
