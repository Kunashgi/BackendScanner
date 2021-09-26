from rest_framework import serializers
from ScannerApp.models import Reserva, Trabajador

class ReservaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reserva
    fields = ('ReservaId', 'Correo', 'Nombre', 'Comuna', 'Direccion', 'Vehiculo', 'Año', 'Modelo', 'Fecha', 'Mensaje')

class TrabajadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trabajador
    fields = ('TrabajadorId', 'Nombre', 'Correo', 'Telefono', 'Direccion', 'Contraseña', 'Codigo')