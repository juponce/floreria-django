# Generated by Django 4.0.1 on 2022-06-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, default='Aqui va la descripcion', max_length=254, null=True, verbose_name='Descripción'),
        ),
    ]
