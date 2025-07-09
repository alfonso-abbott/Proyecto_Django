#!/usr/bin/env python3
"""
Archivo de gestión principal para el proyecto Django ejemplo_django_ui.
Permite ejecutar tareas administrativas como arrancar el servidor,
crear migraciones, entre otras.

Se reproduce la funcionalidad estándar del manage.py generado por
``django-admin startproject`` pero escrito manualmente para este ejemplo.
"""
import os
import sys

# Establece la configuración predeterminada del proyecto para Django
# indicándole en qué módulo se encuentran los ajustes.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemplo_django_ui.settings')


def main() -> None:
    """Punto de entrada para la utilidad de línea de comandos de Django."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado, se informa al usuario con claridad.
        raise ImportError(
            "No se pudo importar Django. Asegúrate de que esté instalado y "
            "disponible en tu PYTHONPATH y de haber activado un entorno virtual."
        ) from exc

    # Llama a la utilidad de Django pasándole los argumentos recibidos.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Ejecuta la función principal cuando el archivo se invoca directamente
    main()
