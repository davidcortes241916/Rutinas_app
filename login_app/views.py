from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Registro

def index(request):
    return render(request, "./login.html")

def home(request):
    return render(request, "./home.html")

def registrar_usuario(request):
    if request.method != "POST":
        return render(request, "./login.html") 

    else:  
        try:
            if request.POST["password"] == request.POST["password2"]:
                user = Registro.objects.create(
                    email_usuario= request.POST["email_usuario"],
                    nombre_usuario= request.POST["nombre_usuario"],
                    fecha_nacimiento= request.POST["fecha_nacimiento"],
                    password= request.POST["password"]
                )
                user.save()
                return redirect("home")  
            else:
                return HttpResponse("Las contraseñas no coinciden")
        except Exception as e:
            print(f"Error registering user: {e}") 
            return HttpResponse("Ocurrió un error durante el registro.")
            
            