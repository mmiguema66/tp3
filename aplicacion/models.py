from django.db import models

# Create your models here.
class Cliente(models.Model): 
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField() 

    def __str__(self):
        return f"{self.nombre}"


class Marca(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca}"

class Patente(models.Model):
    patente = models.CharField(max_length=8)
    numero_motor = models.IntegerField()
 
    #class Meta:
        #verbose_name = "Profesor"
        #verbose_name_plural = "Profesores"
       

    def __str__(self):
        return f"{self.patente}"

class Problema(models.Model):
    reparar = models.CharField(max_length=50)  
    ingreso = models.DateField()
    entregado = models.BooleanField()   

    def __str__(self):
        return f"{self.reparar}"     
