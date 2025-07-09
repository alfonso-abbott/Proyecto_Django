"""Vistas de la aplicación pagina."""
from django.shortcuts import render


def index(request):
    """Renderiza la página de inicio."""
    return render(request, 'index.html')
