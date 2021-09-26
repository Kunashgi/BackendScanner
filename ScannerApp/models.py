from django.db import models

# Create your models here.
class Trabajador(models.Model):
  TrabajadorId = models.AutoField(primary_key=True)
  Nombre = models.CharField(max_length=50)
  Correo = models.EmailField()
  Telefono=models.IntegerField()
  Direccion = models.CharField(max_length=100)
  Contraseña = models.CharField(max_length=16)
  Codigo = models.CharField(max_length=20)

class Reserva(models.Model):
  ReservaId = models.AutoField(primary_key=True)
  Correo = models.EmailField()
  Nombre = models.CharField(max_length = 50)
  Comuna = models.CharField(max_length = 30)
  Direccion = models.CharField(max_length=100)
  Vehiculo = models.CharField(max_length=20)
  Año = models.IntegerField()
  Modelo = models.CharField(max_length=20)
  Fecha = models.DateField()
  Mensaje = models.CharField(max_length=500)