Aquí tienes el texto adaptado en formato de texto plano (con emojis) para que puedas copiarlo y pegarlo directamente en Facebook (ya que Facebook no soporta el formato Markdown con # ni bloques de código con fondos grises):

📌 SISTEMA EMPRESARIAL - CATÁLOGO DE ÍTEMS EN DJANGO

Proyecto de laboratorio desarrollado para el curso de Desarrollo de Aplicaciones Empresariales. Consiste en la construcción e implementación de un sistema empresarial a gran escala para la gestión y visualización de un catálogo de ítems, utilizando arquitectura MVT, interfaz optimizada, filtro dinámico en tiempo real y consumo de API REST.

🛠️ TECNOLOGÍAS Y PRERREQUISITOS

Prerrequisitos:
• Python 3.10+ (Marcar "Add Python to PATH" durante la instalación).
• Git (Para clonar el repositorio).
• Visual Studio Code.

Tecnologías Utilizadas:
• Framework Web: Django 5.x
• Frontend: HTML5, CSS3 & JavaScript (Vanilla)
• Base de Datos: SQLite3

📁 EXPLICACIÓN DE LA ESTRUCTURA DEL PROYECTO

django_project/
│
├── .gitignore (Filtro para ignorar el entorno virtual .venv y archivos temporales)
├── README.md (Documentación oficial con instrucciones)
│
└── src/ (Carpeta raíz con el código fuente del proyecto)
├── manage.py (Script principal para administrar el servidor y migraciones)
├── requirements.txt (Lista de paquetes y dependencias del proyecto)
│
├── config/ (Módulo de configuración global de Django)
│   ├── settings.py (Ajustes principales: Apps, BD, archivos estáticos)
│   ├── urls.py (Enrutador principal de URLs del sitio)
│   └── wsgi.py (Configuración de despliegue para el servidor web)
│
└── core/ (Aplicación principal donde vive el catálogo)
├── models.py (Definición del modelo de datos para los ítems)
├── views.py (Lógica de negocio de la web y endpoints de la API REST)
├── urls.py (Rutas específicas del módulo de catálogo y API)
└── templates/ (Plantillas de renderizado visual HTML)
└── core/
├── base.html (Estructura base, navegación y pie de página)
└── item_list.html (Vista interactiva del catálogo con buscador)

⚙️ INSTALACIÓN DEL PROYECTO

Sigue exactamente estas instrucciones en la terminal de Visual Studio Code para descargar e instalar todas las herramientas necesarias:

Clonar el Repositorio de GitHub:
Abre la terminal (Ctrl + ~) y ejecuta:
git clone https://github.com/yoselin55/django-sistema-empresarial01.git
cd django_project

Crear y Activar el Entorno Virtual:
Crea el entorno e inícialo para aislar las librerías:

• En Windows:
python -m venv .venv
.venv\Scripts\activate

• En Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate

Instalar las Dependencias:
Descarga e instala Django y los paquetes necesarios indicados en requirements.txt:
pip install --upgrade pip
pip install -r src/requirements.txt

🚀 EJECUCIÓN DEL PROYECTO

Una vez completada la instalación, realiza los siguientes pasos para poner en marcha la aplicación web en tu computadora:

Aplicar Migraciones de la Base de Datos:
Entra a la carpeta del código fuente y prepara la base de datos:
cd src
python manage.py migrate

Iniciar el Servidor de Desarrollo:
Ejecuta el siguiente comando para encender el servidor web:
python manage.py runserver

Abrir la Aplicación en el Navegador:
Abre tu navegador e ingresa a cualquiera de los enlaces de acceso:
• Entorno Local: http://130.0.0.1:8000/
• Servidor de Producción / Despliegue: https://sistema-catalogo-empresa.dev.net/app/catalog
