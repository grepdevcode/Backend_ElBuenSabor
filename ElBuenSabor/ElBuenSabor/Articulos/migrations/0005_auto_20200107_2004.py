# Generated by Django 2.2.1 on 2020-01-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0004_auto_20200107_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='cantidad',
            field=models.PositiveIntegerField(default=True),
        ),
    ]
