# Ejemplo Django UI

Este repositorio contiene un proyecto **Django** minimalista pensado como base para desarrollar aplicaciones con una interfaz moderna y profesional. Se ha creado manualmente siguiendo las indicaciones del archivo `comentarios.txt` y todas las carpetas se encuentran directamente en la raíz del repositorio para facilitar el acceso.

## Características principales

- Proyecto Django llamado `ejemplo_django_ui`.
- Una aplicación incluida: `pagina`.
- Uso de **Bootstrap 5** y FontAwesome mediante CDN para dotar de un estilo atractivo sin necesidad de instalaciones adicionales.
- Plantilla base con navegación responsive, sección hero animada, tarjetas de servicios y un sencillo formulario de contacto con validación básica en JavaScript.
- Archivos estáticos separados en la carpeta `static/`.

## Requisitos previos

Para ejecutar este proyecto necesitas contar con **Python 3.12** o compatible y tener instalado Django. Puedes crear un entorno virtual para aislar las dependencias.

```bash
python3 -m venv venv
source venv/bin/activate
pip install django
```

## Estructura del proyecto

```
manage.py
comentarios.txt
README.md
/ejemplo_django_ui
    __init__.py
    settings.py
    urls.py
    wsgi.py
    asgi.py
/pagina
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    urls.py
    /migrations
        __init__.py
/templates
    base.html
    index.html
/static
    /css
        styles.css
    /js
        scripts.js
```

### ¿Qué contiene cada archivo?

- **manage.py**: script para ejecutar comandos de Django.
- **ejemplo_django_ui/settings.py**: configuración principal del proyecto (base de datos SQLite, rutas de `templates` y `static`, etc.).
- **ejemplo_django_ui/urls.py**: rutas globales que incluyen las de la app `pagina`.
- **pagina/**: aquí vive la lógica de nuestra aplicación. En `views.py` se renderiza la página principal y en `urls.py` se define la ruta raíz.
- **templates/**: archivos HTML. `base.html` define la estructura con navegación, contenido y footer, mientras que `index.html` hereda de esta base e incluye las secciones solicitadas.
- **static/**: hoja de estilos CSS con efectos hover y archivo JS para manejar el formulario de contacto.

## Cómo ejecutar el proyecto

1. Activa tu entorno virtual y asegúrate de tener Django instalado.
2. Sitúate en la raíz del repositorio (donde se encuentra `manage.py`).
3. Ejecuta las migraciones y luego inicia el servidor de desarrollo:

```bash
python manage.py migrate
python manage.py runserver
```

4. Abre `http://localhost:8000/` en tu navegador para ver la página de inicio.

## Capturas de pantalla sugeridas

Se recomienda añadir capturas de la sección hero, las tarjetas de servicios y la vista móvil para mostrar la adaptabilidad. Colócalas dentro de una carpeta `screenshots/` en el repositorio (no incluida inicialmente).

## Tecnologías utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/) para estilos y componentes.
- [FontAwesome](https://fontawesome.com/) para iconos.

## Créditos y licencia

El proyecto es de uso libre bajo la licencia MIT. Fue generado como ejemplo para otros desarrolladores que deseen una base sencilla pero con una interfaz moderna.
