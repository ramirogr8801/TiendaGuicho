from django.db import models

# Create your models here.

class Calzado(models.Model):
    tipo = models.CharField(max_length = 30)
    marca = models.CharField(max_length = 30)
    color = models.CharField(max_length = 15)
    talla = models.IntegerField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
class Ropa(models.Model):
    tipo = models.CharField(max_length = 30)
    color = models.CharField(max_length = 15)
    talla = models.CharField(max_length = 15)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
class Accesorios(models.Model):
    nombre = models.CharField(max_length = 30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()