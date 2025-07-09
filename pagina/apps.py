"""Configuración de la aplicación pagina."""
from django.apps import AppConfig


class PaginaConfig(AppConfig):
    """Configuración general de la app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagina'
