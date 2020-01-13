from django.db import models
from ElBuenSabor.usuarios.models import Cliente


# Create your models here.
class TipoEnvio(models.Model):

    idTipoEnvio = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=25)


class Pedido(models.Model):

    idPedido = models.AutoField(primary_key=True)
    fk_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fk_idTipoEnvio = models.ForeignKey(TipoEnvio, on_delete=models.CASCADE)
    fecha = models.DateField()
#    #hora: Toma la hora en que se hizo el pedido
    hora = models.TimeField()
    horaEstimadaFin = models.TimeField()


class Estado(models.Model):

    idEstado = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30)


class EstadoPedido(models.Model):

    idEstadoPedido = models.AutoField(primary_key=True)
    fk_idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fk_idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#    #hora: Se registra la hora en que se modifica el estado
    hora = models.TimeField()
    descripcion = models.CharField(max_length=70)
