from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ScannerApp.models import Reserva, Trabajador
from ScannerApp.serializers import ReservaSerializer, TrabajadorSerializer

# Create your views here.

@csrf_exempt
def reservaApi(request, id=0):
  if request.method == 'GET':
    reserva = Reserva.objects.all()
    reserva_serializer = ReservaSerializer(reserva, many=True)
    return JsonResponse(reserva_serializer.data, safe=False)

  elif request.method=='POST':
    reserva_data=JSONParser().parse(request)
    reserva_serializer = ReservaSerializer(data=reserva_data)
    if reserva_serializer.is_valid():
      reserva_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)

  elif request.method=='PUT':
    reserva_data = JSONParser().parse(request)
    reserva = Reserva.objects.get(ReservaId=reserva_data['ReservaId'])
    reserva_serializer = ReservaSerializer(reserva,data=reserva_data)
    if reserva_serializer.is_valid():
      reserva_serializer.save()
      return JsonResponse("Update succesfull", safe=False)
    return JsonResponse ("failed update," ,safe=False)

  elif request.method=='DELETE':
    reserva=Reserva.objects.get(ReservaId=id)
    reserva.delete()
    return JsonResponse("delete sucessfull", safe=False)

@csrf_exempt
def trabajadorApi(request, id=0):
  if request.method == 'GET':
    trabajador = Trabajador.objects.all()
    trabajador_serializer = TrabajadorSerializer(trabajador, many=True)
    return JsonResponse(trabajador_serializer.data, safe=False)

  elif request.method=='POST':
    trabajador_data=JSONParser().parse(request)
    trabajador_serializer = TrabajadorSerializer(data=trabajador_data)
    if trabajador_serializer.is_valid():
      trabajador_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)

  elif request.method=='PUT':
    trabajador_data = JSONParser().parse(request)
    trabajador = Trabajador.objects.get(TrabajadorId=trabajador_data['TrabajadorId'])
    trabajador_serializer = TrabajadorSerializer(trabajador,data=trabajador_data)
    if trabajador_serializer.is_valid():
      trabajador_serializer.save()
      return JsonResponse("Update succesfull", safe=False)
    return JsonResponse ("failed update," ,safe=False)

  elif request.method=='DELETE':
    trabajador=Trabajador.objects.get(TrabajadorId=id)
    trabajador.delete()
    return JsonResponse("delete sucessfull", safe=False)
