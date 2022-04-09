from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre= models.CharField('nombre',max_length=50)
    color=models.CharField('color',max_length=50)
    talla=models.IntegerField('talla')

    def __str__(self) -> str:
        return f'{self.nombre}-{self.talla}'


class Donantes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)


class Sedes(models.Model):
    nombre=models.CharField(max_length=50)
    lugar=models.CharField(max_length=70)

class Entregas(models.Model):
    nombre=models.CharField(max_length=50)
    fechaEntrega=models.DateField()

