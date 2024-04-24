from django.db import models

# Create your models here.
class Registro(models.Model):
    email_usuario= models.CharField(max_length=100, null= False, default="")
    nombre_usuario= models.CharField(max_length= 80, null= False)
    fecha_nacimiento= models.DateField(null= False)
    contraseña= models.CharField(max_length=100, null= False)
    imagen_perfil= models.ImageField(null= True)

    def __str__(self):
        return self.nombre_usuario