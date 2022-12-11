from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .forms import *
from rest_donacion.serializers import DonacionSerializer

# Create your views here.


# Productos
def productos(request):

    if request.user.is_authenticated:
        user = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=user)
        items = carrito.itemcarrito_set.all()
    else:
        items = []

    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'venta/productos.html', data)


# Pedidos
def pedido(request):
    if request.user.is_authenticated:
        user = request.user
        pedido = Pedido.objects.filter(usuario=user)
        data = {
            'pedido': pedido
        }

    return render(request, 'venta/pedido.html', data)


# Checkout
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=user)
        items = carrito.itemcarrito_set.all()
        dona = Donacion.objects.filter(usuario=user).count()
        if dona != 0:
            carrito = {'get_total_cart': Carrito.get_total_cart(carrito, 0.95)}
        else:
            carrito = {'get_total_cart': Carrito.get_total_cart(carrito, 1)}
    else:
        items = []
        carrito = {'get_total_cart': 0}

    data = {'items': items, 'carrito':carrito}

    return render(request, 'venta/checkout.html', data)


# Carrito
def carrito(request):
    if request.user.is_authenticated:
        user = request.user
        carrito, created = Carrito.objects.get_or_create(usuario=user)
        items = carrito.itemcarrito_set.all()
        dona = Donacion.objects.filter(usuario=user).count()
        if dona != 0:
            carrito = {'get_total_cart': Carrito.get_total_cart(carrito, 0.95)}
        else:
            carrito = {'get_total_cart': Carrito.get_total_cart(carrito, 1)}
    else:
        dona = 0
        items = []
        carrito = {'get_total_cart': 0}

    # if Donacion.objects.get(usuario=user) != null:
    #     total = 

    data = {'items': items, 'carrito': carrito, 'dona': dona}
    return render(request, 'venta/carrito.html', data)



def direccion(request):
    data = {
        'form' : DireccionForm(),
    }
    if request.method == 'POST':
        formulario = DireccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'venta/direccion.html', data)



def agregarProducto(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:', id)
    print('Action:', action)

    user = request.user.id
    product = Producto.objects.get(id=productId)

    pedido, created = Carrito.objects.get_or_create(usuario=user)

    itemCarrito, created = ItemCarrito.objects.get_or_create(carrito=pedido, producto=product)

    if action == 'add' and itemCarrito.producto.stock > itemCarrito.cantidad:
        itemCarrito.cantidad = (itemCarrito.cantidad + 1)
    elif action == 'remove':
        itemCarrito.cantidad = (itemCarrito.cantidad - 1)
    elif action == 'delete':
        itemCarrito.cantidad = 0

    itemCarrito.save()

    if itemCarrito.cantidad <= 0:
        itemCarrito.delete()
    return JsonResponse('Producto añadido', safe=False)


def comprar(request):
    data = json.loads(request.body)

    carritoId = data['carritoId']
    action = data['action']
    total = data['total']

    print('carritoId:', id)
    print('Action:', action)

    user = request.user.id
    usuario = request.user
    carrito = Carrito.objects.get(id=carritoId)
    direccion = Direccion.objects.get(usuario=user)
    itemCarrito = ItemCarrito.objects.get_queryset()
    estadoEnvio = EstadoEnvio.objects.get(id=1)
    pedido, created = Pedido.objects.get_or_create(usuario=usuario, direccion=direccion, estado=estadoEnvio, total=total)

    for i in itemCarrito:
        instancia = Producto.objects.get(id= i.producto.id)
        itemsPedido, created = ItemsPedido.objects.get_or_create(pedido=pedido, producto=instancia)

        instancia.stock = instancia.stock - i.cantidad

        instancia.save()

        i.cantidad = 0

        if i.cantidad == 0:
            i.delete()

    return JsonResponse('Pedido completado', safe=False)

def donacion(request):
    form = DonacionForm(initial={'usuario': request.user})

    data = {
        'form': form
    }


    if request.method == 'POST':
        formulario = DonacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'venta/donacion.html', data)
