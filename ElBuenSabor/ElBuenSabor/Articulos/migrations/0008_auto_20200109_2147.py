# Generated by Django 2.2.1 on 2020-01-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0007_auto_20200109_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='precioCompra',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precioVenta',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulo',
            name='stockActual',
            field=models.PositiveSmallIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='articulomanufacturado',
            name='precioVenta',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='articulomanufacturado',
            name='tiempoEstimadoCocina',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='articulomanufacturadodetalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='cantidad',
            field=models.PositiveIntegerField(default=False),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='subtotal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='articulomanufacturado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='articulomanufacturadodetalle',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rubroarticulo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
