from django.urls import path, include
from . import views
from rutina_app import urls 

urlpatterns = [
    path("", views.index, name="index"),
    #login
    path("login/", views.registrar_usuario, name="registrar_usuario"),

    #inicio
    path("home/", views.home, name="home"),

    #prueba
    path("ajax/", views.jsonTesting, name="jsonTesting"),
    path("prueba/", views.pruebaJson, name="prueba"),
]