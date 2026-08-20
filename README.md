# Sistema Empresarial - Catálogo de Ítems en Django

Proyecto de laboratorio desarrollado para el curso de **Desarrollo de Aplicaciones Empresariales**. Consiste en la construcción e implementación de un sistema empresarial a gran escala para la gestión y visualización de un catálogo de ítems, utilizando arquitectura MVT, interfaz optimizada, filtro dinámico en tiempo real y consumo de API REST.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework Web:** Django
* **Frontend:** HTML5, CSS3 & JavaScript (Vanilla)
* **Base de Datos:** SQLite3

---

## 📁 Estructura del Proyecto

```text
django_project/
│
├── .gitignore               # Archivo para ignorar la carpeta .venv y archivos temporales
├── README.md                # Documentación oficial del repositorio
│
└── src/                     # Carpeta raíz del código fuente
    ├── manage.py            # Script principal de administración de Django
    ├── requirements.txt     # Lista de librerías y dependencias necesarias
    │
    ├── config/              # Configuración global del proyecto
    │   ├── settings.py      # Ajustes de Django, apps instaladas y base de datos
    │   ├── urls.py          # Enrutamiento principal de la aplicación
    │   └── wsgi.py          # Configuración para el despliegue del servidor
    │
    └── core/                # Aplicación principal del catálogo
        ├── models.py        # Definición de la estructura de datos (Ítems)
        ├── views.py         # Lógica de negocio y endpoints de la API REST
        ├── urls.py          # Rutas específicas del catálogo y la API
        └── templates/       # Plantillas HTML
            └── core/
                ├── base.html       # Estructura y diseño base del sistema
                └── item_list.html  # Vista del catálogo con filtro en tiempo real
