from django.contrib import admin
from .models import *

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario', 'total', 'direccion', 'fechaCreacion')

admin.site.register(Producto)
admin.site.register(CategoriaProducto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Donacion)
admin.site.register(Pedido, PedidoAdmin)
