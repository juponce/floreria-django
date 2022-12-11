# Generated by Django 4.0.1 on 2022-06-21 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=60, verbose_name='Nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('idDescuento', models.AutoField(primary_key=True, serialize=False)),
                ('nombreDescuento', models.CharField(max_length=60, verbose_name='Nombre descuento')),
                ('porcentaje', models.FloatField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=100, verbose_name='Nombre producto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='venta', verbose_name='Imagen')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock disponible')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.categoriaproducto')),
                ('descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.descuento')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('carrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.carrito')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venta.producto')),
            ],
        ),
    ]
