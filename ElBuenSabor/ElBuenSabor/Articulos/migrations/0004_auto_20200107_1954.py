# Generated by Django 2.2.1 on 2020-01-07 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0003_auto_20191223_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='precioCompra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precioVenta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='rubroArticulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arts', to='Articulos.RubroArticulo'),
        ),
        migrations.AlterField(
            model_name='articulomanufacturado',
            name='tiempoEstimadoCocina',
            field=models.PositiveIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='articulomanufacturadodetalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='subtotal',
            field=models.FloatField(),
        ),
    ]