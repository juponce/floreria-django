from rest_framework import serializers
from venta.models import Donacion

class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = ['id', 'usuario', 'nombre']