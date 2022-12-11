from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from venta.models import Donacion
from .serializers import DonacionSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def lista_donaciones(request):

    if request.method == 'GET':
        donacion = Donacion.objects.all()
        serializer = DonacionSerializer(donacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DonacionSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST', 'DELETE'])
def detalle_donaciones(request, id):

    try:
        donacion = Donacion.objects.get(id=id)
    except Donacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DonacionSerializer(donacion)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DonacionSerializer(donacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        donacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)