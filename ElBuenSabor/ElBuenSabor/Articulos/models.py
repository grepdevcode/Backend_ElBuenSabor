from django.db import models
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import text
import json
"""
engine = create_engine(
    'postgresql+pygresql://postgres:123@localhost:5432/elbuensabor', echo=True)
"""


class RubroArticulo(models.Model):
    def __iter__(self):
        return iter([self.id, self.denominacion])
    id = models.AutoField(primary_key=True)
    denominacion = models.TextField()

    #def __str__(self):
        #return '%d, %s' % (self.id, self.denominacion)
    # denominacion = models.CharField(max_length=50)


class Articulo(models.Model):

    #def __iter__(self):
        #return iter([self.id, self.denominacion, self.precioCompra, self.stockActual, self.rubroArticulo])
    id = models.AutoField(primary_key=True)
    denominacion = models.TextField()
    precioCompra = models.FloatField(default=0.00)
    precioVenta = models.FloatField(default=0.00)
    stockActual = models.PositiveSmallIntegerField(default=False)
    unidadDeMedida = models.CharField(max_length=40)
    esInsumo = models.BooleanField()
    rubroArticulo = models.ForeignKey(
        RubroArticulo, related_name='arts', on_delete=models.CASCADE, null=True)
#    #a = rubroArticulo
    """
    def greeting(self):

        meta = MetaData()
        meta.bind = engine
        conn = engine.connect()
        artt = Table("Articulos_articulo", meta, autoload=True)
        s = artt.select()
        t = text('select "Articulos_articulo".denominacion, "Articulos_rubroarticulo".denominacion from "Articulos_articulo" inner join "Articulos_rubroarticulo" on "Articulos_articulo"."rubroArticulo_id" = "Articulos_rubroarticulo".id where "Articulo_rubroarticulo".id = %s',)
        result = conn.execute(t)
        return result

    saludo = greeting
    """
    #def __str__(self):
        #return '%d: %s' % (self.id, self.rubroArticulo)



class ArticuloManufacturado(models.Model):
    id = models.AutoField(primary_key=True)
    tiempoEstimadoCocina = models.PositiveIntegerField(default=False)
    denominacion = models.TextField()
    precioVenta = models.FloatField(default=0.00)


class ArticuloManufacturadoDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField(default=False)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
    articuloManufacturado = models.ForeignKey(
        ArticuloManufacturado, on_delete=models.CASCADE, null=True)


class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField(default=False)
    subtotal = models.FloatField(default=0.00)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
    articuloManufacturado = models.ForeignKey(
        ArticuloManufacturado, on_delete=models.CASCADE, null=True)
