from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriaProducto(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=60, verbose_name='Nombre categoria')

    def __str__(self):
        return self.nombreCategoria


class Descuento(models.Model):
    idDescuento = models.AutoField(primary_key=True)
    nombreDescuento = models.CharField(max_length=60, verbose_name='Nombre descuento')
    porcentaje = models.FloatField(verbose_name='')
    def __str__(self):
        return self.nombreDescuento


class Donacion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.usuario


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre producto')
    imagen = models.ImageField(upload_to='venta', null=True, blank=True, verbose_name='Imagen')
    descripcion = models.CharField(max_length=254, verbose_name='Descripción',  null=True, blank=True)
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock disponible')
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuento, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nombreProducto

    @property
    def get_discount_price(self):
        if self.descuento is none:
            final = precio
        else:
            final = precio * (1-(descuento/100))
        return final

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return str(self.id)

    def get_total_cart(self, i):
        # if Donacion.objects.get(usuario=self.usuario) != none:
        #     itemscarrito = self.itemcarrito_set.all()
        #     total = (0.95*(sum([item.get_total for item in itemscarrito])))
        #     return total

        itemscarrito = self.itemcarrito_set.all()
        total = round(sum([item.get_total for item in itemscarrito]) * i)
        return total


    def get_sub_total(self):
        itemscarrito = self.itemcarrito_set.all()
        sub_total = sum([item.get_total for item in itemscarrito])
        return sub_total

class ItemCarrito(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total
    
    @property
    def get_stock(self):
        number_list = list(range(1, self.producto.stock+1))
        return number_list





class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calle = models.CharField(max_length=254)
    numero = models.CharField(max_length=254)
    dpto = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class EstadoEnvio(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, verbose_name='Estado del envio')

    def __str__(self):
        return self.estado


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.ForeignKey(EstadoEnvio, on_delete=models.SET_NULL, null=True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return str(self.id)


class ItemsPedido(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)

