# Generated by Django 2.2.3 on 2020-12-20 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0003_auto_20201219_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre del Producto')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('precio', models.FloatField(verbose_name='Precio de venta')),
                ('stock', models.IntegerField(verbose_name='Cantidad existente')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]