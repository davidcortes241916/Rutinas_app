from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.registrar_usuario, name="login"),
    path("home/", views.home, name="home")
]