"""Definición de rutas para la aplicación pagina."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
