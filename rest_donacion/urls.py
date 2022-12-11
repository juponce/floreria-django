from django.urls import path
from .views import lista_donaciones, detalle_donaciones

urlpatterns = [
    path('lista_donaciones/', lista_donaciones, name='lista_donaciones'),
    path('detalle_donaciones/<id>', detalle_donaciones, name='detalle_donaciones')
]