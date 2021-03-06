# Generated by Django 2.2.1 on 2019-06-06 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEnvio',
            fields=[
                ('idTipoEnvio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('horaEstimadaFin', models.TimeField()),
                ('fk_idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente')),
                ('fk_idTipoEnvio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedido.TipoEnvio')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('idEstadoPedido', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
                ('descripcion', models.CharField(max_length=70)),
                ('fk_idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedido.Estado')),
                ('fk_idPedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPedido.Pedido')),
            ],
        ),
    ]
