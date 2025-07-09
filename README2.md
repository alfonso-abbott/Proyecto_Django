# Recorrido guiado del proyecto

Este documento complementa el `README.md` tradicional. La idea es
que puedas explorar los archivos poco a poco para entender la
estructura.

1. **`manage.py`**
   - Punto de entrada para comandos de Django. Lee los comentarios
     de este archivo para saber cómo se configura la utilidad.
2. **`ejemplo_django_ui/settings.py`**
   - Explica cómo está configurado Django: base de datos, rutas de
     plantillas y archivos estáticos.
3. **`ejemplo_django_ui/urls.py`**
   - Aquí verás cómo se enrutan las peticiones a la app `pagina`.
4. **`pagina/views.py`** y **`pagina/urls.py`**
   - Muestran la función de vista principal y la URL asociada.
5. **`templates/base.html`**
   - Plantilla principal. Observa los comentarios para entender la
     estructura HTML y el botón de modo oscuro.
6. **`templates/index.html`**
   - Página de inicio que hereda de `base.html` y define las secciones
     hero, servicios y contacto.
7. **`static/css/styles.css`** y **`static/js/scripts.js`**
   - Archivos de estilos y scripts. Revisa los comentarios para conocer
     cómo se implementan los colores y el modo oscuro.

Cuando termines de revisar un archivo vuelve a esta guía para continuar
con el siguiente. ¡Disfruta el aprendizaje!
