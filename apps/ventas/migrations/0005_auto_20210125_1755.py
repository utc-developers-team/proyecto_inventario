# Generated by Django 2.2.3 on 2021-01-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20201220_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]