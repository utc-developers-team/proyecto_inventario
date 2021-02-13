# Generated by Django 2.2.3 on 2021-02-13 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='venta',
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='compra',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='compras.Compra', verbose_name='compra'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_compra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio_compra'),
        ),
    ]
