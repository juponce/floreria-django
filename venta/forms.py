from django import forms
from django.forms import ModelForm
from .models import *

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['usuario', 'calle', 'numero', 'dpto']

    def __init__(self, *args, **kwargs):
        super(DireccionForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control radius'

class DonacionForm(ModelForm):
    class Meta:
        model = Donacion
        fields = ['usuario', 'nombre']

    def __init__(self, *args, **kwargs):
        super(DonacionForm, self).__init__(*args, **kwargs)


        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control radius'
