"""Definición de URLs principales del proyecto."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para el administrador de Django
    path('admin/', admin.site.urls),
    # Incluimos las URLs de la aplicación 'pagina'
    path('', include('pagina.urls')),
]
