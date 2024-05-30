from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
#para las excepciones (se puede borrar despues)
from django.core.exceptions import ValidationError
from django.contrib import messages

#para autenticar usuario
from django.contrib.auth import authenticate, login, logout
from .models import Registro
#librerias json de javascript
from django.http import JsonResponse
import json
import threading

def index(request):
    return render(request, "./login.html")

def home(request):
    return render(request, "./home.html")

#por si acaso
def jsonTesting(request):
    return render(request, "./pruebaJson.html")

def pruebaJson(request):
    #esto despues se quita
    data= {'message': 'ojala funcione :,v'}
    return JsonResponse(data)

  
#registrar usuario
def registrar_usuario(request):
    if request.method != "POST":
        print("quedo aqui")
        return render(request, "./login.html")
    else:
        try:
            # Check if email already exists
            email_usuario = request.POST["email_usuario"]
            print("Checking email:", email_usuario)  # Debugging statement
            usuario_existe = Registro.objects.filter(email_usuario=email_usuario)
            if usuario_existe:
                print(f"el correo {email_usuario} ya existe")
                return JsonResponse({"valide": False})
            #Crear usuario
            print("creando usuario")
            user = Registro.objects.create(
                nombre_usuario=request.POST["nombre_usuario"],
                fecha_nacimiento=request.POST["fecha_nacimiento"],
                password=request.POST["password1"],
                email_usuario=email_usuario,
            )
            user.is_active = True
            user.save()      
            return JsonResponse({"valide": True})    
                     
        except ValidationError as e:
            return HttpResponseBadRequest(e.message)
            #para saber mejor que error ocurre en caso de que sea diferente al esperado
                    
        except Exception as e:
            print(f"Error al registrar el usuario: {e}") 
            return HttpResponse("Ocurrió un error durante el registro.")
