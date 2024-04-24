from django.shortcuts import render
from django.http import HttpResponse
from .models import Registro

def index(request):
    return render(request, "./login.html", {})

def registrar_usuario(request):
    pass