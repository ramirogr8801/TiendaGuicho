from django.db import models

# Create your models here.

class Calzado(models.Model):
    tipo = models.CharField(max_length = 30)
    marca = models.CharField(max_length = 30)
    color = models.CharField(max_length = 15)
    talla = models.FloatField()
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
    # def __str__(self):
    #     return self.tipo
    
class Ropa(models.Model):
    tipo = models.CharField(max_length = 30)
    color = models.CharField(max_length = 15)
    TALLAS_ROPA = (
        ('XS', 'ExtraSmall'),
        ('S','Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
    )
    talla = models.CharField(max_length =2, choices=TALLAS_ROPA)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    
class Accesorios(models.Model):
    nombre = models.CharField(max_length = 30)
    cantidad = models.IntegerField()
    precio = models.IntegerField()