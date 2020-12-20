# Generated by Django 2.2.3 on 2020-12-20 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dias_visita',
            field=models.CharField(default='', max_length=300, verbose_name='Dias de visita'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre del Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(default='', max_length=10, verbose_name='Teléfono'),
            preserve_default=False,
        ),
    ]
