"""Punto de entrada para servidores WSGI."""
import os
from django.core.wsgi import get_wsgi_application

# Establecemos la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemplo_django_ui.settings')

# Aplicación WSGI que utilizarán los servidores para lanzar el proyecto
application = get_wsgi_application()
