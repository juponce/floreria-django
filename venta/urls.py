from django.urls import path
from .views import *

urlpatterns = [
    path('', productos, name='productos'),
    path('carrito/', carrito, name='carrito'),
    path('pedido/', pedido, name='pedido'),
    path('checkout/', checkout, name='checkout'),
    path('direccion/', direccion, name='direccion'),
    path('comprar/', comprar, name='comprar'),
    path('donacion/', donacion, name='donacion'),
    path('agregar_producto/', agregarProducto, name='agregar_producto'),
]