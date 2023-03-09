#Nos permite crear una base de datos.
from django.db import models  
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):

    def __str__(self):
        return f"Producto: {self.elemento} ----- Precio: {self.precio}"
    
    elemento = models.CharField(max_length=60) # Lo que hace es permitir que el nombre no tenga mas de 60 caracteres
    precio = models.FloatField(max_length=60) #Se espera que el usuario ingrese un precio, que puede ser decimal.

class Busqueda(models.Model):

    def __str__(self):
        return f"Producto: {self.elemento} ----- Precio: {self.precio}"

    elemento = models.CharField(max_length=60)
    precio = models.FloatField(max_length=60)
    

class Registro(models.Model):

    def __str__(self):
        return f"nombre: {self.nombre} ----- apellido: {self.apellido}------ correo: {self.correo} "

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    

class Tienda(models.Model): # No tiene atributos porque no hay datos que buscar, solo es informativo

    pass
    

class Nosotros(models.Model): # No tiene atributos porque no hay datos que buscar, solo es informativo
    
    pass

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField (upload_to = "avatares", null=True, blank=True)





