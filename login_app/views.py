from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
#para las excepciones (se puede borrar despues)
from django.core.exceptions import ValidationError
from django.contrib import messages
#para autenticar usuario
from django.contrib.auth import authenticate, login, logout
from .models import Registro


def index(request):
    return render(request, "./login.html")

def home(request):
    return render(request, "./home.html")

def registrar_usuario(request):
    if request.method != "POST":
        return render(request, "./login.html") 

    else:  
        if "cancelar" in request.POST:
            #no hace nada de momento
            return print("aca se pondra la animacion para que vuelva a login")

        try:
            #datos requeridos, haciendolos obligatorios
            required_fields= ["email_usuario", "nombre_usuario", "fecha_nacimiento", "password"]
            #despues de esto hay que generar un mensaje de error en caso de que falten campos, pero se debe hacer con javascript
            for field in required_fields:  
                if not request.POST.get(field):
                    print("todos los campos son necesarios")
                    return redirect("./login.html")
            #cuando se configure javascript este mensaje puede ser borrado ya que javascript debe hacer el mensaje, sin embargo debe ir de la mano con este fragmento de codigo django

            #verifica que el usuario no este creado
            email_usuario= request.POST["email_usuario"]
            if Registro.objects.filter(email_usuario=email_usuario).exists():
                #aca tambien debe ir un codigo javascript de la mano con django
                print(f"El email {email_usuario} ya existe!")
                return redirect("./login.html")   

            if request.POST["password"] == request.POST["password2"]:
                user = Registro.objects.create(
                    nombre_usuario= request.POST["nombre_usuario"],
                    fecha_nacimiento= request.POST["fecha_nacimiento"],
                    password= request.POST["password"],
                    email_usuario=email_usuario
                )
                user.is_active = True
                user.save()

                print(f"usuario creado con exito!")
                return redirect("home")  
            else:
                return HttpResponse("Las contraseñas no coinciden")
            
        except ValidationError as e:
            return HttpResponseBadRequest(e.message)
            #para saber mejor que error ocurre en caso de que sea diferente al esperado
            
        except Exception as e:
            print(f"Error al registrar el usuario: {e}") 
            return HttpResponse("Ocurrió un error durante el registro.")
            
            